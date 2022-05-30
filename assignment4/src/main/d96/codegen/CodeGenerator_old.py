'''
 *   @author Vo Nguyen Thien Nhan
'''
## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##
from main.d96.utils.AST import *
from main.d96.checker.StaticCheck import *
from main.d96.checker.StaticError import *
## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##

from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
        
    def __str__(self):
        return "MType(" + str(self.partype) + ", " + str(self.rettype) + ")"

class Symbol:
    def __init__(self, name, mtype, value=None, sKind=None, kind=None):
        self.name = name
        self.sKind = sKind
        self.kind = kind
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol("+self.name+", "+str(self.mtype)+", "+str(self.value.value)+")"

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        self.value = value

class CName(Val):
    def __init__(self, value):
        self.value = value

class Const(Val):
    def __init__(self, value):
        self.value = value

class SubBody():
    def __init__(self, frame: Frame, sym: List[Symbol]):
        self.frame = frame
        self.sym = sym

class ClassComponent:
    def __init__(self, cname, pname, mem):
        self.cname = cname
        self.pname = pname
        self.mem = mem
        
    def __str__(self):
        return "ClassComponent(" + str(self.cname) + ", " + str(self.pname) + ", " + "[" + ','.join(str(x) for x in self.mem) + "]" + ")"

class VisitorGlobal(BaseVisitor):
    def visitProgram(self, ast, c):
        env = []
        for decl in ast.decl: env = env + [self.visit(decl, c)]
        return env

    def visitClassDecl(self, ast, c):
        self.class_name = ast.classname.name
        parent_name = ast.parentname.name if ast.parentname else ""
        mem_list = []
        for mem in ast.memlist: 
            mem_list = mem_list + [self.visit(mem, c)]
        return ClassComponent(ast.classname.name, parent_name, mem_list)

    def visitAttributeDecl(self, ast, c):
        decl = ast.decl
        kind = ast.kind
        sKind = "Static" if isinstance(kind, Static) else "Instance"
        
        if isinstance(decl, VarDecl):
            value = Index(decl.varInit) if decl.varInit else None
            return Symbol(decl.variable.name, decl.varType, value, sKind, "Attribute")

        if isinstance(decl, ConstDecl):
            return Symbol(decl.constant.name, decl.constType, Const(decl.value), sKind, "Attribute")

    def visitMethodDecl(self, ast, c):
        kind = ast.kind
        name = ast.name.name
        params = ast.param
        sKind = "Instance" if isinstance(kind, Instance) else "Static"
        return Symbol(name, MType([para.varType for para in params], VoidType()), CName(self.class_name), sKind, "Method")

class CodeGenerator():
    def __init__(self):
        self.lib_name = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.lib_name)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.lib_name)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.lib_name)),
                    Symbol("writeInt", MType([IntType()],
                        VoidType()), CName(self.lib_name), "Static", "Method"),
                    Symbol("writeIntLn", MType([IntType()],
                        VoidType()), CName(self.lib_name), "Static", "Method"),
                    Symbol("writeStr",  MType([StringType()], VoidType()), CName(
                        self.lib_name), "Static", "Method"),
                    Symbol("writeStrLn",  MType([StringType()], VoidType()), CName(
                        self.lib_name), "Static", "Method"),
                    Symbol("writeFloat", MType([FloatType()], VoidType()), CName(
                        self.lib_name), "Static", "Method"),
                    Symbol("writeFloatLn", MType([FloatType()], VoidType()), CName(
                        self.lib_name), "Static", "Method"),
                    Symbol("writeBool", MType([BoolType()], VoidType()), CName(
                        self.lib_name), "Static", "Method"),
                    Symbol("writeBoolLn", MType([BoolType()], VoidType()), CName(
                        self.lib_name), "Static", "Method")
                    ]

    def gen(self, ast, dir_):
        global_env = VisitorGlobal().visit(ast, None)            # return List[ClassComponent]
        gl = [ClassComponent("io", "", self.init())]
        gc = CodeGenVisitor(ast, gl + global_env, dir_)        # gl + globalEnv is List[ClassComponent]
        gc.visit(ast, None)

class CodeGenVisitor(BaseVisitor):
        
    def __init__(self, astTree, env, dir_):
        self.astTree = astTree
        self.env = env
        self.class_name = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.class_name + ".j")
        
        self.current_class = None
        self.current_method = None
        self.classes_list = {}
        self.method_list = []
        self.attribute_list = []

    def visitProgram(self, ast, o):
        for each_class in ast.decl:
            self.visit(each_class, o)
        return o

    def visitAttributeDecl(self, ast, c):
        pass
        
    def visitClassDecl(self, ast, o):
        classname = ast.classname.name
        memList = ast.memlist
        parentname = ast.parentname.name if ast.parentname else "java.lang.Object"
        
        self.class_name = ast.classname.name
        self.current_class = classname
        self.classes_list[classname] = {}
        
        self.emit = Emitter(self.path + "/" + self.class_name + ".j")
        self.emit.printout(self.emit.emitPROLOG(classname, parentname))

        for mem in memList:
            if isinstance(mem, MethodDecl):
                self.visit(mem, SubBody(None, []))

        self.generate_method(MethodDecl(Instance(), Id("<init>"), list(), Block([])), o, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return o
        
    def generate_method(self, method, o, frame):
        check_init = True if method.name.name == "<init>" else False
        check_main = method.name.name == "main"
        return_type = VoidType()
        method_name = "<init>" if check_init else method.name.name
        in_type = [ArrayType(0, StringType())] if check_main else list(map(lambda x: x.varType, method.param))
        mtype = MType(in_type, return_type)

        # generate for begin method
        self.emit.printout(self.emit.emitMETHOD(method_name, mtype, not check_init, frame))

        frame.enterScope(True)

        global_env = o
        
        # generate label var
        if check_init:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(Id(self.class_name)), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif check_main:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            # append local variable of method (params)
            local_env = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)] + env.sym), method.param, SubBody(frame, []))
            global_env = local_env.sym + global_env
        
        # generate for statements in method
        body = method.body
        if len(body.inst) > 0:
            variable = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)] + env.sym) if (isinstance(ele, VarDecl) or isinstance(ele, ConstDecl)) else SubBody(frame, env.sym), body.inst, SubBody(frame, []))
            global_env = variable.sym + global_env
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        if check_init:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.current_class)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        
        # for initialization of variable
        for stmt in body.inst:
            if isinstance(stmt, VarDecl) and stmt.varInit is not None:
                self.visit(Assign(stmt.variable, stmt.varInit), SubBody(frame, global_env))  
        
        # other statements except VarDecl and ConstDecl
        for stmt in body.inst:
            if not isinstance(stmt, VarDecl) and not isinstance(stmt, ConstDecl):
                self.visit(stmt, SubBody(frame, global_env))
        
        # generate for end method
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if isinstance(return_type, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        
    def visitMethodDecl(self,ast,o):
        kind = ast.kind
        name = ast.name.name
        params = ast.param
        frame = Frame(name, VoidType())
        self.generate_method(ast, o.sym, frame)
        sKind = "Instance" if isinstance(kind, Instance) else "Static"
        return Symbol(ast.name, MType([para.varType for para in params], VoidType()), CName(self.class_name), sKind, "Method")
        
    def visitVarDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, ast.variable.name, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        return Symbol(ast.variable.name, ast.varType, Index(idx), None, None)

    def visitConstDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, ast.constant.name, ast.constType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        return Symbol(ast.constant.name, ast.constType, Const(ast.value), None, None)
    
    def visitUnaryOp(self, ast, o):
        op = ast.op
        body_code, body_type = self.visit(ast.body, o)
        if op == '-':
            return body_code + self.emit.emitNEGOP(body_type, o.frame), body_type
        if op == '!':
            return body_code + self.emit.emitNOT(body_type, o.frame), body_type
              
    def visitBinaryOp(self, ast, o):
        frame = o.frame
        op = str(ast.op)
        left_code, left_type = self.visit(ast.left, o)
        right_code, right_type = self.visit(ast.right, o)
        ret_type = left_type
        
        if left_type == FloatType or right_type == FloatType or op == "/":
            ret_type = FloatType
            if left_type == IntType:    left_code = left_code + self.emit.emitI2F(frame)
            if right_type == IntType:   right_code = right_code + self.emit.emitI2F(frame)
        if op in ['+', '-']:
            return left_code + right_code + self.emit.emitADDOP(op, ret_type, frame), ret_type
        if op in ['*','/']:
            return left_code + right_code + self.emit.emitMULOP(op, ret_type, frame), ret_type
        if op == '%':
            return left_code + right_code + self.emit.emitMOD(frame), ret_type
        if op == '&&':
            return left_code + right_code + self.emit.emitANDOP(frame), ret_type
        if op == '||':
            return left_code + right_code + self.emit.emitOROP(frame), ret_type
        if op in [">", ">=", "<", "<=", "!=", "=="]:
            return left_code + right_code + self.emit.emitREOP(op, ret_type, frame), ret_type
        
    def visitBlock(self, ast, o):
        env = o.sym
        frame = o.frame

        frame.enterScope(False)
        new_env = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)] + env.sym) if (isinstance(ele, VarDecl) or isinstance(ele, ConstDecl)) else SubBody(frame, env.sym), ast.inst, SubBody(frame, []))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        for stmt in ast.inst:
            if not isinstance(stmt, VarDecl) and not isinstance(stmt, ConstDecl):
                self.visit(stmt, SubBody(frame, new_env.sym + env))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        
    def visitFor(self, ast, o):
        exp1, exp1_type = self.visit(ast.expr1, Access(o.frame, o.sym, False, True))
        exp2, exp2_type = self.visit(ast.expr2, Access(o.frame, o.sym, False, True))
        exp3, exp3_type = self.visit(ast.expr3, Access(o.frame, o.sym, False, True)) if ast.expr3 else None
        id_write, id_write_type = self.visit(ast.id, Access(o.frame, o.sym, True, True))
        id_read, id_read_type = self.visit(ast.id, Access(o.frame, o.sym, False, False))
        
        start_label = o.frame.getNewLabel()
        end_label = o.frame.getNewLabel()
        
        # init value
        self.emit.printout(exp1)
        self.emit.printout(id)
        o.frame.enterLoop()
        
        # start label
        self.emit.printout(self.emit.emitLABEL(start_label, o.frame))
        
        # check condition
        self.emit.printout(id_read)
        self.emit.printout(exp2)
        self.emit.printout(self.emit.emitIFICMPGT(end_label, o.frame))
        
        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))
        
        self.emit.printout(id_read)
        self.emit.printout(self.emit.emitPUSHICONST(1, o.frame))
        self.emit.printout(self.emit.emitADDOP('+', IntType(), o.frame))
        self.emit.printout(id_write)
        
        self.emit.printout(self.emit.emitGOTO(start_label, o.frame))
        self.emit.printout(self.emit.emitLABEL(end_label, o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))
        
        o.frame.exitLoop()
        
    def visitReturn(self, ast, o):
        code, return_type = self.visit(ast.expr, Access(o.frame, o.sym, False, True)) if ast.expr else "", VoidType()
        
        if not isinstance(return_type, VoidType):
           self.emit.printout(code)
        self.emit.printout(self.emit.emitRETURN(return_type, o.frame))
        return ""
    
    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
              
    def visitAssign(self, ast, o):
        right_code, right_type = self.visit(ast.exp, Access(o.frame, o.sym, False, True))
        left_code, left_type = self.visit(ast.lhs, Access(o.frame, o.sym, True, True))
        if isinstance(right_type, IntType) and isinstance(left_type, FloatType):
            self.emit.printout(right_code + self.emit.emitI2F(o.frame))
        else:
            self.emit.printout(right_code)
        self.emit.printout(left_code)
        
    def visitNewExpr(self, ast, o):
        code = ""
        code += self.emit.emitNEW(ast.classname.name, ast.param, o.frame)
        code += self.emit.emitDUP(o.frame)
        code += self.emit.emitINVOKESPECIAL(o.frame, ast.classname.name, MType([], VoidType()))
        return (code, MType([], VoidType()))
        
    def visitFieldAccess(self, ast, o):
        if isinstance(ast.obj, SelfLiteral):
            sym = self.access_handler(ast, o, self.class_name)
        else:
            # obj = self.visit(ast.obj, Access(o.frame, o.sym, True, False))
            obj_code, obj_type = self.visit(ast.obj, Access(o.frame, o.sym, True, False))
            sym = self.access_handler(ast, o, obj_code)
        if sym is not None:
            if(o.isLeft == True):
                return (self.emit.emitPUTSTATIC(obj_code + "." + sym.name, sym.mtype, o.frame), sym.mtype)
            if sym.value is not None:
                return (self.emit.emitPUSHCONST(self.emit.emitExpr(sym.value, sym.mtype), sym.mtype, o.frame), sym.mtype)
            return (self.emit.emitGETSTATIC(obj_code + "." + sym.name, sym.mtype, o.frame), sym.mtype)
    
    def visitCallStmt(self, ast, o):
        if isinstance(ast.obj, SelfLiteral):
            sym = self.access_handler(ast, o, self.class_name)
        else:
            obj = self.visit(ast.obj, o)
            sym = self.access_handler(ast, o, obj[0])
        cname = sym.value.value
        ctype = sym.mtype
        code_and_type = ("", [])      # (code, type)
        for para in ast.param:
            code, type_data = self.visit(para, Access(o.frame, o.sym, False, True))
            code_and_type = (code_and_type[0] + code, code_and_type[1].append(type_data))
    
        # print code
        self.emit.printout(code_and_type[0])  
        
        # calling method
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, o.frame))
        
    def access_handler(self, ast, o, name):
        field_name = ast.fieldname.name if isinstance(ast, FieldAccess) else ast.method.name
        current_class = self.lookup(name, self.env, lambda x: x.cname)
        method = self.lookup(field_name, current_class.mem, lambda x: x.name)
        if method is not None:   return method
        if current_class.pname != "":
            return self.access_handler(ast, o, current_class.pname)
        
    def visitId(self, ast, o):
        sym = self.lookup(ast.name, o.sym, lambda x: x.name)
        if sym is None: # io
            currentClass = self.lookup(
                self.class_name, self.env, lambda x: x.cname)        # self.env is List[ClassComponent], return ClassComponent object
            sym = self.lookup(ast.name, currentClass.mem, lambda x: x.name)
        if sym is None:
            # continue find in parent class
            if currentClass.pname != "":
                parentClass = self.lookup(
                    currentClass.pname, self.env, lambda x: x.cname)
                sym = self.lookup(
                    ast.method, parentClass.mem, lambda x: x.name)
        if sym is not None:
            if type(sym.value) is Index or type(sym.value) is Const:
                if o.isLeft == True:
                    if o.isFirst == True:
                        return (self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o.frame), sym.mtype)
                    else:
                        if type(sym.mtype) is ClassType:
                            return (sym.mtype.classname.name, sym.mtype)
                        return (ast.name, sym.mtype)
                else:
                    if o.isFirst == True:
                        if type(sym.value) is Index:
                            return (self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o.frame), sym.mtype)
                        if type(sym.value) is Const:
                            return (self.emit.emitREADCONST(sym.value.value, sym.mtype, o.frame), sym.mtype)
                    else:
                        return (ast.name, sym.mtype)
            else:
                return (ast.name, sym.mtype)
        sym = self.lookup(ast.name, self.env, lambda x: x.cname)
        if sym is not None:
            return (ast.name, ClassType(ast.name))

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST('"' + ast.value + '"', StringType(), o.frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value), o.frame), BoolType()
    
    def visitNullLiteral(self, ast, o):
        return self.emit.emitPUSHNULL(), BoolType()
    
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

    

'''
 *   @author Vo Nguyen Thien Nhan
'''
## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##
# from main.d96.utils.AST import *
# from main.d96.parser.D96Parser import D96Parser
# from main.d96.parser.D96Visitor import D96Visitor
# from StaticError import *
from main.d96.utils.AST import *
from main.d96.checker.StaticCheck import *
from main.d96.checker.StaticError import *
## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##

# from AST import *
# from Utils import *
# from StaticCheck import *
# from StaticError import *
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

# class Symbol:
#     def __init__(self,name,mtype,value = None):
#         self.name = name
#         self.mtype = mtype
#         self.value = value

class Symbol:
    def __init__(self, name, mtype, value=None, sKind=None, kind=None):
        self.name = name
        self.sKind = sKind
        self.kind = kind
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol("+self.name+", "+str(self.mtype)+", "+str(self.value.value)+")"

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

# class ArrayPointerType(Type):
#     def __init__(self, ctype):
#         #cname: String
#         self.eleType = ctype

#     def __str__(self):
#         return "ArrayPointerType({0})".format(str(self.eleType))

#     def accept(self, v, param):
#         return None
    
# class ClassType(Type):
#     def __init__(self,cname):
#         self.cname = cname
#     def __str__(self):
#         return "Class({0})".format(str(self.cname))
#     def accept(self, v, param):
#         return None
        
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
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class Const(Val):
    def __init__(self, value):
        self.value = value

class SubBody():
    def __init__(self, frame: Frame, sym: List[Symbol]):
        #frame: Frame
        #sym: List[Symbol]
        self.frame = frame
        self.sym = sym

class ClassData:
    def __init__(self, cname, pname, mem):
        self.cname = cname
        self.pname = pname
        self.mem = mem
        
    def __str__(self):
        return "ClassData(" + str(self.cname) + ", " + str(self.pname) + ", " + "[" + ','.join(str(x) for x in self.mem) + "]" + ")"

class GlobalEnv(BaseVisitor):
    def visitProgram(self, ast, c):
        env = list(map(lambda i: self.visit(i, c), ast.decl))
        
        # print("env: ")
        # for i in range(len(env)):
        #     print(env[i])
        
        return env

    def visitClassDecl(self, ast, c):
        self.classname = ast.classname.name
        memlist = list(map(lambda i: self.visit(i, c), ast.memlist))
        if ast.parentname is None:
            parentName = ""
        else:
            parentName = ast.parentname.name
        return ClassData(ast.classname.name, parentName, memlist)

    def visitAttributeDecl(self, ast, c):
        decl = ast.decl
        if type(ast.kind) is Static:
            sKind = "Static"
        else:
            sKind = "Instance"
        if type(decl) is VarDecl:
            if decl.varInit is None:
                value = None
            else:
                value = Index(decl.varInit)
            return Symbol(decl.variable.name, decl.varType, value, sKind, "Attribute")
        if type(decl) is ConstDecl:
            return Symbol(decl.constant.name, decl.constType, Const(decl.value), sKind, "Attribute")

    def visitMethodDecl(self, ast, c):
        if type(ast.kind) is Static:
            sKind = "Static"
        else:
            sKind = "Instance"
        return Symbol(ast.name.name, MType([x.varType for x in ast.param], VoidType()), CName(self.classname), sKind, "Method")

class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("writeInt", MType([IntType()],
                        VoidType()), CName(self.libName), "Static", "Method"),
                    Symbol("writeIntLn", MType([IntType()],
                        VoidType()), CName(self.libName), "Static", "Method"),
                    Symbol("writeStr",  MType([StringType()], VoidType()), CName(
                        self.libName), "Static", "Method"),
                    Symbol("writeStrLn",  MType([StringType()], VoidType()), CName(
                        self.libName), "Static", "Method"),
                    Symbol("writeFloat", MType([FloatType()], VoidType()), CName(
                        self.libName), "Static", "Method"),
                    Symbol("writeFloatLn", MType([FloatType()], VoidType()), CName(
                        self.libName), "Static", "Method"),
                    Symbol("writeBool", MType([BoolType()], VoidType()), CName(
                        self.libName), "Static", "Method"),
                    Symbol("writeBoolLn", MType([BoolType()], VoidType()), CName(
                        self.libName), "Static", "Method")
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        # gl = self.init()
        # gc = CodeGenVisitor(ast, gl, dir_)
        # gc.visit(ast, None)
        
        globalEnv = GlobalEnv().visit(ast, None)            # return List[ClassData]
        gl = [ClassData("io", "", self.init())]
        gc = CodeGenVisitor(ast, gl+globalEnv, dir_)        # gl + globalEnv is List[ClassData]
        gc.visit(ast, None)

class CodeGenVisitor(BaseVisitor):
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None
    
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        
        self.current_class = None
        self.current_method = None
        self.classes_list = {}
        self.method_list = []
        self.attribute_list = []
        
    # def visit(self,ast,param):
    #     return ast.accept(self,param)

    def visitProgram(self, ast, o):
        #ast: Program
        #c: Any

        for each_class in ast.decl:
            self.visit(each_class, o)
        return o
    
        # self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # e = SubBody(None, self.env)
        # for x in ast.decl:
        #     e = self.visit(x, e)
        # # generate default constructor
        # self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list(), list())), c, Frame("<init>", VoidType))
        # self.emit.emitEPILOG()
        # return c

    def visitAttributeDecl(self, ast, c):
        pass
        
    def visitClassDecl(self, ast, o):
        classname = ast.classname.name
        memList = ast.memlist
        parentname = ast.parentname.name if ast.parentname else None
        
        self.className = ast.classname.name
        self.current_class = classname
        self.classes_list[classname] = {}
        
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        if parentname is None:
            self.emit.printout(self.emit.emitPROLOG(
                classname, "java.lang.Object"))
        else:
            self.emit.printout(self.emit.emitPROLOG(
                classname, parentname))
        
        for mem in memList:
            if isinstance(mem, MethodDecl):
                self.visit(mem, SubBody(None, []))

        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
        ), Block([])), o, Frame("<init>", VoidType()))
        
        # self.genMETHOD(MethodDecl(Instance(), Id("<clinit>"), list(
        # ), Block([])), o, Frame("<clinit>", VoidType()))
        
        self.emit.emitEPILOG()
        
        return o
        
    def genMETHOD(self, consdecl, o, frame):
        
        isInit = True if consdecl.name.name == '<init>' else False
        isMain = consdecl.name.name == "main"
        returnType = VoidType()
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayType(0, StringType())] if isMain else list(
            map(lambda x: x.varType, consdecl.param))
        mtype = MType(intype, returnType)

        # generate for begin method
        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o
        
        # generate label var
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                Id(self.className)), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            # append local variable of method (params)
            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)] + env.sym), consdecl.param, SubBody(frame, []))
            glenv = local.sym + glenv
        
        # generate for statements in method
        body = consdecl.body
        if len(body.inst) > 0:
            variable = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)] + env.sym) if (isinstance(ele, VarDecl) or isinstance(ele, ConstDecl)) else SubBody(frame, env.sym), body.inst, SubBody(frame, []))
            glenv = variable.sym + glenv
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.current_class)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        
        # for initialization of variable
        for x in body.inst:
            if type(x) is VarDecl and x.varInit is not None:
                self.visit(Assign(x.variable, x.varInit), SubBody(frame, glenv))
        
        # other statements except VarDecl and ConstDecl
        for x in body.inst:
            if not isinstance(x, VarDecl) and not isinstance(x, ConstDecl):
                self.visit(x, SubBody(frame, glenv))
        # list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.inst))
        
        # generate for end method
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        
    def visitMethodDecl(self,ast,o):
        kind = ast.kind
        name = ast.name.name
        param = ast.param

        frame = Frame(name, VoidType())
        self.genMETHOD(ast, o.sym, frame)
        if isinstance(kind, Static):
            sKind = "Static"
        else:
            sKind = "Instance"
        return Symbol(ast.name, MType([x.varType for x in ast.param], VoidType()), CName(self.className), sKind, "Method")
            
        
        # kind = ast.kind
        # name = ast.name.name
        # param = ast.param
        
        # self.method_list.append(Symbol(name, MType([], VoidType()), CName(self.current_class)))
        # self.current_method = self.method_list[-1]
        # is_static = True if '$' in name else False
        
        # in_type = []
        # return_type = VoidType()
        # mtype = MType(in_type, return_type)
        # frame = o
        # self.emit.printout(self.emit.emitMETHOD(name, mtype, not is_static, frame))
        
        # self.emit.printout(self.emit.emitENDMETHOD(frame))
        
    def visitVarDecl(self, ast, o):
        
        frame = o.frame
        env = o.sym
        idx = frame.getNewIndex()
    
        self.emit.printout(self.emit.emitVAR(
            idx, ast.variable.name, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
        # if ast.varInit == None:
        #     return Symbol(ast.variable.name, ast.varType, Index(idx), None, None)
        # return Symbol(ast.variable.name, ast.varType, Index(ast.varInit), None, None)
        return Symbol(ast.variable.name, ast.varType, Index(idx), None, None)

    def visitConstDecl(self, ast, o):
        frame = o.frame
        env = o.sym
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(
            idx, ast.constant.name, ast.constType, frame.getStartLabel(), frame.getEndLabel(), frame))
        return Symbol(ast.constant.name, ast.constType, Const(ast.value), None, None)
    
    def visitUnaryOp(self, ast, o):
        body = self.visit(ast.body, o)
        print("body: ", body)
        frame = o.frame
        if str(ast.op) == '+':
            return body
        if str(ast.op) == '-':
            return body[0] + self.emit.emitNEGOP(body[1], frame), body[1]
        if str(ast.op) == '!':
            return body[0] + self.emit.emitNOT(body[1], frame), body[1]
              
    def visitBinaryOp(self, ast, o):
        frame = o.frame
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        op = str(ast.op)
        typeop = e2t
        if (e1t == FloatType or e2t == FloatType or op == "/"):
            typeop = FloatType
            if e1t == IntType:
                e1c = e1c + self.emit.emitI2F(frame)
            if e2t == IntType:
                e2c = e2c + self.emit.emitI2F(frame)
        if op == '+':
            return e1c + e2c + self.emit.emitADDOP(ast.op, typeop, frame), typeop
        if op == '-':
            return e1c + e2c + self.emit.emitADDOP(ast.op, typeop, frame), typeop
        if op == '*':
            return e1c + e2c + self.emit.emitMULOP(ast.op, typeop, frame), typeop
        # if op == '\\':
        #     return e1c + e2c + self.emit.emitMULOP(ast.op, typeop, frame), typeop
        if op == '/':
            return e1c + e2c + self.emit.emitMULOP(ast.op, typeop, frame), typeop
        if op == '%':
            return e1c + e2c + self.emit.emitMOD(frame), typeop
        # if op == '^':
        #     left_str = e1c
        #     right_str = e2c
        #     return self.emit.emitConcat("\""+left_str[6:len(left_str)-2] +
        #                                 right_str[6:len(right_str)-2]+"\"", frame), StringType
        if op == '&&':
            return e1c + e2c + self.emit.emitANDOP(frame), typeop
        if op == '||':
            return e1c + e2c + self.emit.emitOROP(frame), typeop
        if op in [">", ">=", "<", "<=", "!=", "=="]:
            return e1c + e2c + self.emit.emitREOP(ast.op, typeop, frame), typeop
        
    def visitBlock(self, ast, o):
        env = o.sym
        frame = o.frame

        frame.enterScope(False)

        nenv = reduce(lambda env, ele: SubBody(
            frame, [self.visit(ele, env)] + env.sym) if (isinstance(ele, VarDecl) or isinstance(ele, ConstDecl)) else SubBody(frame, env.sym), ast.inst, SubBody(frame, []))

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        for x in ast.inst:
            if not isinstance(x, VarDecl) and not isinstance(x, ConstDecl):
                self.visit(x, SubBody(frame, nenv.sym + env))
        # map(lambda x: self.visit(x, SubBody(frame, nenv+env)),ast.stmt)
        
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
        
        # ctxt = o
        # frame = ctxt.frame
        # nenv = ctxt.sym
        # exp1Code, _ = self.visit(ast.expr1, Access(frame, nenv, False, True))
        # exp2Code, _ = self.visit(ast.expr2, Access(frame, nenv, False, True))
        # lhsWCode, _ = self.visit(ast.id, Access(frame, nenv, True, True)) # Write code
        # lhsRCode, _ = self.visit(ast.id, Access(frame, nenv, False, False)) # Read code
        
        # labelS = frame.getNewLabel() # label start
        # labelE = frame.getNewLabel() # label end

        # # Init value
        # self.emit.printout(exp1Code)
        # self.emit.printout(lhsWCode)
        # frame.enterLoop()
        # # Loop
        # self.emit.printout(self.emit.emitLABEL(labelS, frame))
        # # 1. Condition
        # self.emit.printout(lhsRCode)
        # self.emit.printout(exp2Code)
        # if ast.up:
        #     self.emit.printout(self.emit.emitIFICMPGT(labelE, frame))
        # else:
        #     self.emit.printout(self.emit.emitIFICMPLT(labelE, frame))
        # # 2. Statements
        # self.visit(ast.loop, o)
        # self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        # # 3. Update index
        # self.emit.printout(lhsRCode)
        # self.emit.printout(self.emit.emitPUSHICONST(1, frame))
        # self.emit.printout(self.emit.emitADDOP('+' if ast.up else '-', IntType(), frame))
        # self.emit.printout(lhsWCode)

        # self.emit.printout(self.emit.emitGOTO(labelS, frame)) # loop
        # self.emit.printout(self.emit.emitLABEL(labelE, frame))
        # self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        # frame.exitLoop()
        
    def visitReturn(self, ast, o):
        return_type, code = None, None
        if ast.expr:
            code, return_type = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
        else:
            return_type = VoidType
        
        if not (type(return_type) is VoidType):
           self.emit.printout(code)
        self.emit.printout(self.emit.emitRETURN(return_type, o.frame))
        return True
    
    def visitContinue(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitBreak(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))
              
    def visitAssign(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        right = self.visit(ast.exp, Access(frame, nenv, False, True))
        left = self.visit(ast.lhs, Access(frame, nenv, True, True))
        if (type(right[1]) is IntType and type(left[1]) is FloatType):
            self.emit.printout(right[0] + self.emit.emitI2F(frame))
        else:
            self.emit.printout(right[0])
        self.emit.printout(left[0])
        
    def visitNewExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        new = self.emit.emitNEW(ast.classname.name, ast.param, frame)
        dup = self.emit.emitDUP(frame)
        invo = self.emit.emitINVOKESPECIAL(
            frame, ast.classname.name, MType(list(), VoidType()))
        return (new+dup+invo, MType(list(), VoidType()))
        
    def visitFieldAccess(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        if type(ast.obj) is SelfLiteral:
            sym = self.handleAccess(ast, o, self.className)
        else:
            obj = self.visit(ast.obj, Access(frame, ctxt.sym, True, False))
            sym = self.handleAccess(ast, o, obj[0])
        if sym is not None:
            if(ctxt.isLeft == True):
                return (self.emit.emitPUTSTATIC(obj[0]+"."+sym.name, sym.mtype, frame), sym.mtype)
            if sym.value is not None:
                return (self.emit.emitPUSHCONST(self.emit.emitExpr(sym.value, sym.mtype), sym.mtype, frame), sym.mtype)
            return (self.emit.emitGETSTATIC(obj[0]+"."+sym.name, sym.mtype, frame), sym.mtype)
    
    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        if type(ast.obj) is SelfLiteral:
            sym = self.handleAccess(ast, o, self.className)
        else:
            obj = self.visit(ast.obj, o)
            sym = self.handleAccess(ast, o, obj[0])
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())      # (code, type)
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
            
        # print code
        self.emit.printout(in_[0])  
        
        # calling method
        self.emit.printout(self.emit.emitINVOKESTATIC(      
            cname + "/" + ast.method.name, ctype, frame))
        
    def handleAccess(self, ast, o, name):
        if type(ast) is FieldAccess:
            nameField = ast.fieldname.name
        else:
            nameField = ast.method.name
        currentClass = self.lookup(name, self.env, lambda x: x.cname)
        method = self.lookup(
            nameField, currentClass.mem, lambda x: x.name)
        if method is not None:
            return method
        if currentClass.pname != "":
            return self.handleAccess(ast, o, currentClass.pname)
        
    def visitId(self, ast, o):

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        # print("ast: ", ast)
        sym = self.lookup(ast.name, nenv, lambda x: x.name)
        # print("sym found: ", sym)
        if sym is None: # io
            currentClass = self.lookup(
                self.className, self.env, lambda x: x.cname)        # self.env is List[ClassData], return ClassData object
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
                if ctxt.isLeft == True:
                    if ctxt.isFirst == True:
                        return (self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype)
                    else:
                        if type(sym.mtype) is ClassType:
                            return (sym.mtype.classname.name, sym.mtype)
                        return (ast.name, sym.mtype)
                else:
                    if ctxt.isFirst == True:
                        if type(sym.value) is Index:
                            # if type(sym.value.value) is int:
                            return (self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype)
                            # return (self.emit.emitREADCONST(sym.value.value, sym.mtype, frame), sym.mtype)
                        if type(sym.value) is Const:
                            return (self.emit.emitREADCONST(sym.value.value, sym.mtype, frame), sym.mtype)
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

    

"""
    @author: Vo Nguyen Thien Nhan
"""

## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##
from ast import expr
from main.d96.utils.AST import *
from main.d96.checker.StaticCheck import *
from main.d96.checker.StaticError import *
## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##

from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from CodeGenError import *

class Attribute:
    def __init__(self, name, type, is_static, init_value=None):
        self.name = name
        self.type = type
        self.is_static = is_static
        self.init_value = init_value

class Method:
    def __init__(self, name, type, is_static):
        self.name = name
        self.type = type
        self.is_static = is_static

class Local:
    def __init__(self, name, type, index):
        self.name = name
        self.type = type
        self.index = index

class Enviroment:
    def __init__(self, global_env={}, local_env=[{}]):
        self.global_env = global_env
        self.local_env = local_env

    def visit_class(self, class_name):
        self.global_env[class_name] = ComponentClass()

    def visit_scope(self):
        self.local_env = [{}] + \
            self.local_env if self.local_env is not None else [{}]

    def exit_scope(self):
        self.local_env.pop(0)

    def add_local(self, local_id, local_type):
        self.local_env[0][local_id] = local_type

    def add_attribute(self, class_name, attribute_name, attribute_type):
        return self.global_env[class_name].add_attribute(
            attribute_name, attribute_type
        )

    def add_method(self, class_name, method_name, method_type):
        return self.global_env[class_name].add_method(method_name, method_type)

    def lookup_local(self, id):
        for local_scope in self.local_env:
            if id in local_scope:
                return local_scope[id]
        return None

    def lookup_attribute(self, class_name, attribute_name):
        return self.global_env[class_name].lookup_attribute(attribute_name)

    def lookup_method(self, class_name, method_name):
        return self.global_env[class_name].lookup_method(method_name)

    def copy(self):
        return Enviroment(self.global_env, self.local_env.copy())


class ComponentClass:
    def __init__(self, attribute={}, method={}):
        self.attribute = attribute
        self.method = method

    def add_attribute(self, attribute_name, attribute_type):
        self.attribute[attribute_name] = attribute_type

    def lookup_attribute(self, attribute_name):
        if attribute_name in self.attribute:
            return self.attribute[attribute_name]
        return None
    
    def add_method(self, method_name, method_type):
        self.method[method_name] = method_type

    def lookup_method(self, method_name):
        if method_name in self.method:
            return self.method[method_name]
        return None

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class SubBody:
    def __init__(self, frame, env):
        self.frame = frame
        self.env = env

class Access:
    def __init__(self, frame, env, is_left, is_first):
        self.frame = frame
        self.env = env
        self.is_left = is_left
        self.is_first = is_first

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        # value: Int
        self.value = value


# class Class_name(Val):
#     def __init__(self, value, si_kind=None):
#         # value: String
#         self.value = value
#         self.si_kind = si_kind


class CodeGenerator:
    
    def __init__(self):
        self.lib_name = "io"

    def init(self):
        global_env = {
            self.lib_name: ComponentClass(
                {},
                {
                    "getInt":       Method("getInt", MType([], IntType()), True),
                    "putInt":       Method("putInt", MType([IntType()], VoidType()), True),
                    "putIntLn":     Method("putIntLn", MType([IntType()], VoidType()), True),
                    "getBool":      Method("getBool", MType([], BoolType()), True),
                    "putBool":      Method("putBool", MType([BoolType()], VoidType()), True),
                    "putBoolLn":    Method("putBoolLn", MType([BoolType()], VoidType()), True),
                    "putString":    Method("putString", MType([StringType()], VoidType()), True),
                    "putStringLn":  Method("putStringLn", MType([StringType()], VoidType()), True),
                    "getFloat":     Method("getFloat", MType([], FloatType()), True),
                    "putFloat":     Method("putFloat", MType([FloatType()], VoidType()), True),
                    "putFloatLn":   Method("putFloatLn", MType([FloatType()], VoidType()), True),
                    "putLn":        Method("putLn", MType([], VoidType()), True),
                },
            )
        }
        return Enviroment(global_env, None)

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String
        env = self.init()
        global_codegen = CodeGenVisitor(ast, env, dir_)
        global_codegen.visit(ast, None)


class CodeGenVisitor(BaseVisitor):
    def __init__(self, ast, env, dir_):
        self.ast = ast
        self.env = env
        self.path = dir_
        self.current_class = None
        self.parent_class = None
        self.instance_attr_list = None
        self.static_attr_list = None
        self.current_method = None      # for return type
        self.emit = None

    def visitProgram(self, ast, o):
        for each_class in ast.decl:
            self.visit(each_class, self.env)

    def visitClassDecl(self, ast, o):
        classname = ast.classname.name
        memList = ast.memlist
        parentname = ast.parentname.name if ast.parentname else "java/lang/Object"
        
        o.visit_class(classname)
        self.current_class = classname
        self.parent_class = parentname
        self.instance_attr_list = []
        self.static_attr_list = []
        self.emit = Emitter(self.path + "/" + self.current_class + ".j")
        
        self.emit.printout(self.emit.emitPROLOG(classname, parentname))
        
        # get attributes and methods
        constructor = None
        check_default_constructor = False
        attr_list = []
        method_list = []
        for mem in memList:
            if isinstance(mem, AttributeDecl):
                attr_list += [mem]
            if isinstance(mem, MethodDecl):
                if mem.name.name == 'Constructor':
                    constructor = mem
                    if len(mem.param) == 0:     check_default_constructor = True
                else:
                    method_list += [mem]
        
        # visit attributes
        for each_attr in attr_list:
            self.visit(each_attr, o)
            
        # visit constructor
        if constructor:
            self.visit(constructor, o)
        if check_default_constructor == False:
            o.visit_scope()
            frame = Frame("<init>", VoidType())
            self.gen_method(
                MethodDecl(Instance(), Id("<init>"), [], Block([])),
                SubBody(frame, o),
                frame,
            )
        o.exit_scope()
        o.visit_scope()
        frame = Frame("<clinit>", VoidType())
        self.gen_method(
            MethodDecl(Static(), Id("<clinit>"), [], Block([])),
            SubBody(frame, o),
            frame,
        )
        o.exit_scope()
        
        # visit methods
        for each_method in method_list:
            self.visit(each_method, o)
            
        self.emit.emitEPILOG()

    def visitAttributeDecl(self, ast, o):
        kind = ast.kind
        decl = ast.decl
        
        name, type_data, init_value = None, None, None
        check_static = True if isinstance(kind, Static) else False
        check_constant = False
        if isinstance(decl, VarDecl):
            name, type_data, init_value = decl.variable.name, decl.varType, decl.varInit if decl.varInit else None
        else:
            name, type_data, init_value = decl.constant.name, decl.constType, decl.value if decl.value else None
            check_constant = True
            
        if check_static:
            self.emit.printout(self.emit.emitSTATIC(name, type_data, check_constant, init_value))
        else:
            self.emit.printout(self.emit.emitINSTANCE(name, type_data, check_constant, init_value))
        
        new_attr = Attribute(name, type_data, check_static, init_value)
        self.static_attr_list.append(new_attr) if check_static else self.instance_attr_list.append(new_attr)
        o.add_attribute(self.current_class, name, new_attr)

    def visitMethodDecl(self, ast, o):
        kind = ast.kind
        name = ast.name.name
        params = ast.param
        
        if name == 'Constructor':
            ast.name.name = '<init>'
            name = '<init>'
        check_static = True if isinstance(kind, Static) else False
        frame = Frame(name, None)
        o.visit_scope()
        self.gen_method(ast, SubBody(frame, o), frame)
        o.add_method(self.current_class, name, Method(name, MType([para.varType for para in params], self.current_method), check_static))
        o.exit_scope()

    def gen_method(self, method_ast, o, frame):
        kind = method_ast.kind
        name = method_ast.name.name
        params = method_ast.param
        body = method_ast.body
        
        self.current_method = None
        code = ""
        check_main = True if (name == 'main' and len(params) == 0) else False
        check_static = True if (isinstance(kind, Static) or check_main) else False
        par_type = [ArrayType(0, StringType())] if check_main else [para.varType for para in params]
        
        frame.enterScope(True)
        # generate variable for method
        if name == '<init>' or not check_static:
            idx = frame.getNewIndex()
            code += self.emit.emitVAR(idx, "this", ClassType(Id(self.current_class)), frame.getStartLabel(), frame.getEndLabel(), frame)
        elif check_main:
            idx = frame.getNewIndex()
            code += self.emit.emitVAR(idx, "args", ArrayType(0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame)
        # visit parameters
        for para in params:
            code += self.visit(para, o)
        # label of method
        code += self.emit.emitLABEL(frame.getStartLabel(), frame)
        if name == '<init>':
            code += self.emit.emitTHIS(frame)
            code += self.emit.emitINVOKESPECIAL(frame, self.parent_class + "/<init>", MType([], VoidType()))
            for each_attr in self.instance_attr_list:
                if each_attr.init_value is None:
                    continue
                code += self.emit.emitTHIS(frame)
                init_code, init_type = self.visit(each_attr.init_value, Access(frame, self.env, False, False))
                if isinstance(each_attr.type, FloatType) and isinstance(init_type, IntType): 
                    init_code += self.emit.emitI2F(o.frame)
                code += init_code
                code += self.emit.emitPUTFIELD(self.current_class + "." + each_attr.name, each_attr.type, frame)
        elif name == "<clinit>":
            for each_attr in self.static_attr_list:
                if each_attr.init_value is None:
                    continue
                init_code, init_type = self.visit(each_attr.init_value, Access(frame, self.env, False, False)) 
                if isinstance(each_attr.type, FloatType) and isinstance(init_type, IntType): 
                    init_code += self.emit.emitI2F(o.frame)
                code += init_code
                code += self.emit.emitPUTSTATIC(self.current_class + "." + each_attr.name, each_attr.type, frame)
        # visit body method
        for inst in body.inst:
            code += self.visit(inst, o)
        if self.current_method is None:
            self.current_method = VoidType()
        # generate label of method after know return type
        mtype = MType(par_type, self.current_method)
        code = self.emit.emitMETHOD(name, mtype, check_static, frame) + code
        code += self.emit.emitLABEL(frame.getEndLabel(), frame)
        # generate end method
        if isinstance(self.current_method, VoidType):
            code += self.emit.emitRETURN(VoidType(), frame)
        code += self.emit.emitENDMETHOD(frame)
        self.emit.printout(code)
        frame.exitScope()
        
    def visitVarDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        o.env.add_local(ast.variable.name, Local(ast.variable.name, ast.varType, idx))
        code = ""
        code += self.emit.emitVAR(idx, ast.variable.name, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        code += self.visit(Assign(ast.variable, ast.varInit), o) if ast.varInit else ""
        return code
        
    def visitConstDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        o.env.add_local(ast.constant.name, Local(ast.constant.name, ast.constType, idx))
        code = ""
        code += self.emit.emitVAR(idx, ast.constant.name, ast.constType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        code += self.visit(Assign(ast.constant, ast.value), o) if ast.value else ""
        return code
        
    def visitUnaryOp(self, ast, o):
        code, type_data = self.visit(ast.body, o)
        if ast.op == "-":   return code + self.emit.emitNEGOP(type_data, o.frame), type_data
        return code + self.emit.emitNOT(type_data, o.frame), type_data

    def visitBinaryOp(self, ast, o):
        op = ast.op
        left_code, left_type = self.visit(ast.left, o)
        right_code, right_type = self.visit(ast.right, o)
        ret_type = left_type
        if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) or op == "/":
            ret_type = FloatType()
            if isinstance(left_type, IntType):      left_code += self.emit.emitI2F(o.frame)
            if isinstance(right_type, IntType):     right_code += self.emit.emitI2F(o.frame)
        if op in ["+", "-"]:
            return left_code + right_code + self.emit.emitADDOP(op, ret_type, o.frame), ret_type
        if op in ["*", "/"]:
            return left_code + right_code + self.emit.emitMULOP(op, ret_type, o.frame), ret_type
        if op == "%":
            return left_code + right_code + self.emit.emitMOD(o.frame), ret_type
        if op == "&&":
            return left_code + right_code + self.emit.emitANDOP(o.frame), ret_type
        if op == "||":
            return left_code + right_code + self.emit.emitOROP(o.frame), ret_type
        if op in [">", ">=", "<", "<=", "!=", "==", "==."]:
            return left_code + right_code + self.emit.emitREOP(op, ret_type, o.frame), BoolType()
        if op == "+.":
            return left_code + right_code + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), o.frame), StringType()

    def visitNewExpr(self, ast, o):
        code = ""
        classname = ast.classname.name
        params = ast.param
        
        code += self.emit.emitNEW(classname, params, o.frame)
        code += self.emit.emitDUP(o.frame)

        # default constructor
        if len(params) == 0:
            code += self.emit.emitINVOKESPECIAL(o.frame, classname + "/<init>", MType([], VoidType()))
            return code, ClassType(classname)
        
        # constructor with params
        init = o.env.lookup_method(classname, "<init>")
        
        if init is None:
            raise IllegalRuntimeException("Cannot find <init>!")
        
        for i in range(len(params)):
            arg_code, arg_type = self.visit(ast.param[i], o)
            code += arg_code
            if isinstance(arg_type, IntType) and isinstance(init.type.partype[i], FloatType):
                code += self.emit.emitI2F(o.frame)
                
        code += self.emit.emitINVOKESPECIAL(o.frame, classname + "/<init>", init.type)
        return code, ClassType(classname)

    def visitAssign(self, ast, o):
        left = ast.lhs
        exp = ast.exp
        
        if isinstance(left, FieldAccess):
            return self.visit(left, (Access(o.frame, o.env, True, True), exp))[0]

        if isinstance(left, ArrayCell):
            return self.visit(left, (Access(o.frame, o.env, True, True), exp))[0]
        
        right_code, right_type = self.visit(exp, Access(o.frame, o.env, False, True))
        left_code, left_type = self.visit(left, Access(o.frame, o.env, True, True))
        code = right_code
        if isinstance(right_type, IntType) and isinstance(left_type, FloatType):
            code += self.emit.emitI2F(o.frame)
        return code + left_code

    def visitFieldAccess(self, ast, o):
        obj = ast.obj
        fieldname = ast.fieldname.name
        
        value = None
        if type(o) is tuple:
            value = o[1]
            o = o[0]
            
        code = ""
        class_name = None
        obj_code, obj_type = self.visit(obj, Access(o.frame, o.env, False, False))
        if obj_code is None or obj_type is None:  
            class_name = ast.obj.name
        else:
            class_name = obj_type.classname.name  
        
        attr = o.env.lookup_attribute(class_name, ast.fieldname.name)

        if attr is None:
            raise IllegalRuntimeException("Cannot find attribute!")

        if o.is_left and o.is_first:  # write
            value_code, value_type = self.visit(value, Access(o.frame, o.env, False, True))
            if attr.is_static:
                code = value_code + self.emit.emitPUTSTATIC(class_name + "/" + fieldname, attr.type, o.frame)
            else:
                code = obj_code + value_code + self.emit.emitPUTFIELD(class_name + "/" + fieldname, attr.type, o.frame)
        else:   # read
            if attr.is_static:
                code = self.emit.emitGETSTATIC(class_name + "/" + fieldname, attr.type, o.frame)
            else:
                code = obj_code + self.emit.emitGETFIELD(class_name + "/" + fieldname, attr.type, o.frame)
        return code, attr.type

    def visitArrayCell(self, ast, o):
        arr = ast.arr
        idx_list = ast.idx
        
        code = ""
        value = None
        if type(o) is tuple:
            value = o[1]
            o = o[0]
            
        code, arr_type = self.visit(arr, Access(o.frame, o.env, False, True))
        arr_type = arr_type.eleType
        for i in range(len(idx_list) - 1):
            idx_code, idx_type = self.visit(idx_list[i], Access(o.frame, o.env, False, True))
            code += idx_code
            code += self.emit.emitALOAD(arr_type, o.frame)
            arr_type = arr_type.eleType
        # last ele
        idx_code, idx_type = self.visit(idx_list[-1], Access(o.frame, o.env, False, True))
        if o.is_left:
            value_code, value_type = self.visit(value, Access(o.frame, o.env, False, True))
            code += idx_code + value_code + self.emit.emitASTORE(arr_type, o.frame)
        else:
            code += idx_code + self.emit.emitALOAD(arr_type, o.frame)
        return code, arr_type
        
    def visitBlock(self, ast, o):
        o.env.visit_scope()
        code = ""
        for inst in ast.inst:
            code += self.visit(inst, o)
        o.env.exit_scope()
        return code

    def visitIf(self, ast, o):
        code = ""
        expr_code, expr_type = self.visit(ast.expr, Access(o.frame, o.env, False, True))
        code += expr_code
        exit_label = o.frame.getNewLabel()
        false_label = o.frame.getNewLabel()
        code += self.emit.emitIFFALSE(false_label, o.frame)
        code += self.visit(ast.thenStmt, o)
        code += self.emit.emitGOTO(exit_label, o)
        code += self.emit.emitLABEL(false_label, o.frame)
        code += (self.visit(ast.elseStmt, o) if ast.elseStmt else "")
        code += self.emit.emitLABEL(exit_label, o.frame)
        return code
        
    def visitFor(self, ast, o):
        code = ""
        if ast.expr3 is None:
            ast.expr3 = IntLiteral(1)
        expr1_code, _ = self.visit(
            ast.expr1, Access(o.frame, o.env, False, True))
        expr2_code, _ = self.visit(
            ast.expr2, Access(o.frame, o.env, False, True))
        expr3_code, _ = self.visit(
            ast.expr3, Access(o.frame, o.env, False, True))
        id_write_code, _ = self.visit(ast.id, Access(
            o.frame, o.env, True, True))  # Write code
        id_read_code, _ = self.visit(ast.id, Access(
            o.frame, o.env, False, True))  # Read code
        # Virtual stack size at here is 3: exp1, exp2, exp3

        label_start_loop = o.frame.getNewLabel()
        label_check_condition_down = o.frame.getNewLabel()
        label_loop_body = o.frame.getNewLabel()
        label_update_down = o.frame.getNewLabel()
        # Assign init value for scalar variable:
        code += expr1_code
        code += id_write_code

        o.frame.enterLoop()
        # Check condition
        # Check down or up
        code += self.emit.emitLABEL(label_start_loop, o.frame)
        code += expr1_code
        code += expr2_code
        code += self.emit.emitREOP(">", IntType(), o.frame)  # Loop down
        code += self.emit.emitIFTRUE(label_check_condition_down, o.frame)

        # Condition for loop up
        code += id_read_code
        code += expr2_code
        code += self.emit.emitREOP(">", IntType(), o.frame)
        o.frame.push()
        code += self.emit.emitIFTRUE(o.frame.getBreakLabel(), o.frame)
        code += self.emit.emitGOTO(label_loop_body, o.frame)

        # Condition for loop down
        code += self.emit.emitLABEL(label_check_condition_down, o.frame)
        code += id_read_code
        code += expr2_code
        o.frame.push()
        o.frame.push()
        code += self.emit.emitREOP("<", IntType(), o.frame)
        code += self.emit.emitIFTRUE(o.frame.getBreakLabel(), o.frame)

        # Loop body
        code += self.emit.emitLABEL(label_loop_body, o.frame)
        code += self.visit(ast.loop, o)

        code += self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame)

        # Update scalar variable
        # Check update is up or down
        code += expr1_code
        code += expr2_code
        o.frame.push()
        o.frame.push()
        code += self.emit.emitREOP(">", IntType(), o.frame)  # Loop down
        code += self.emit.emitIFTRUE(label_update_down, o.frame)

        # Update up
        code += id_read_code
        code += expr3_code
        o.frame.push()
        code += self.emit.emitADDOP("+", IntType(), o.frame)
        code += id_write_code
        code += self.emit.emitGOTO(label_start_loop, o.frame)

        # Update down
        code += self.emit.emitLABEL(label_update_down, o.frame)
        code += id_read_code
        code += expr3_code
        o.frame.push()
        code += self.emit.emitADDOP("-", IntType(), o.frame)
        code += id_write_code
        code += self.emit.emitGOTO(label_start_loop, o.frame)
        code += self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame)
        o.frame.exitLoop()
        return code

    def visitBreak(self, ast, o):
        return self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame)

    def visitContinue(self, ast, o):
        return self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame)

    def visitReturn(self, ast, o):
        code = ""
        expr_code, expr_type = (self.visit(ast.expr, Access(o.frame, o.env, False, True)) if ast.expr else ("", VoidType()))
        code += expr_code
        code += self.emit.emitRETURN(expr_type, o.frame)
        self.current_method = expr_type if self.current_method is None else self.current_method
        return code

    def visitCallExpr(self, ast, o):
        code = ""
        obj = ast.obj
        method_name = ast.method.name
        params = ast.param
        
        class_name = None
        obj_code, obj_type = self.visit(obj, o)

        if obj_code is None or obj_type is None:  
            class_name = obj.name
        else:
            class_name = obj_type.classname.name 

        # Find method
        method = o.env.lookup_method(class_name, method_name)       # type of method is MType
        if method is None:
            raise IllegalRuntimeException("Cannot find method!")

        for i in range(len(params)):
            arg_code, arg_type = self.visit(params[i], Access(o.frame, o.env, False, True))
            code += arg_code
            if isinstance(arg_type, IntType) and isinstance(method.type.partype[i], FloatType):
                code += self.emit.emitI2F(o.frame)
        
        if method.is_static:
            code += self.emit.emitINVOKESTATIC(class_name + "/" + method_name, method.type, o.frame)
        else:
            code = obj_code + code + self.emit.emitINVOKEVIRTUAL(class_name + "/" + method_name, method.type, o.frame)
        return code, method.type.rettype
        
    def visitCallStmt(self, ast, o):
        code = ""
        obj = ast.obj
        method_name = ast.method.name
        params = ast.param
        
        class_name = None
        obj_code, obj_type = self.visit(obj, Access(o.frame, o.env, False, True))
        if obj_code is None or obj_type is None:  
            class_name = obj.name
        else:
            class_name = obj_type.classname.name  

        # Find method
        method = o.env.lookup_method(class_name, method_name)
        if method is None:
            raise IllegalRuntimeException("Cannot find method!")
        
        for i in range(len(params)):
            arg_code, arg_type = self.visit(params[i], Access(o.frame, o.env, False, True))
            code += arg_code
            if isinstance(arg_type, IntType) and isinstance(method.type.partype[i], FloatType):
                code += self.emit.emitI2F(o.frame)
        
        if method.is_static:
            code += self.emit.emitINVOKESTATIC(class_name + "/" + method_name, method.type, o.frame)
        else:
            code = obj_code + code + self.emit.emitINVOKEVIRTUAL(class_name + "/" + method_name, method.type, o.frame)
        if not isinstance(method.type.rettype, VoidType):
            code += self.emit.emitPOP(o.frame)
        return code
        
    def visitId(self, ast, o):  # ID only for local variable, attribute or method use access
        local_found = o.env.lookup_local(ast.name)
        if local_found is None:
            return None, None
        if o.is_left:   # write
            return self.emit.emitWRITEVAR(ast.name, local_found.type, local_found.index, o.frame), local_found.type
        # read
        return self.emit.emitREADVAR(ast.name, local_found.type, local_found.index, o.frame), local_found.type

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(str(ast.value), BoolType(), o.frame), BoolType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST('"' + str(ast.value) + '"', StringType(), o.frame), StringType()
        
    def visitNullLiteral(self, ast, o):
        return self.emit.emitNULL(o.frame), NullLiteral()

    def visitSelfLiteral(self, ast, o):
        return self.emit.emitTHIS(o.frame), ClassType(Id(self.current_class))
    
    def visitArrayLiteral(self, ast, o):
        code = ""
        value_list = ast.value
        ele_type = None
        o.frame.push()  # Virtual emit array, need emit after because we don't know type of element at this line
        for i in range(len(value_list)):
            code += self.emit.emitDUP(o.frame)
            code += self.emit.emitPUSHICONST(i, o.frame)
            ele_code, ele_type = self.visit(value_list[i], o)
            code += ele_code
            code += self.emit.emitASTORE(ele_type, o.frame)
        o.frame.pop()  # Reset frame
        arr_type = ArrayType(len(value_list), ele_type)
        code = self.emit.emitARRAY(arr_type, o.frame) + code
        return code, arr_type
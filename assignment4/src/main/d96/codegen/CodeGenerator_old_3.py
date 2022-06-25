"""
    @author: Vo Nguyen Thien Nhan 1910409
"""

## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##
from main.d96.utils.AST import *
from main.d96.checker.StaticCheck import *
from main.d96.checker.StaticError import *
## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##

from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from CodeGenError import *
from functools import reduce

class ComponentClass:
    def __init__(self, attr_list, method_list):
        self.attr_list = attr_list
        self.method_list = method_list

    def add_attribute(self, name, data_type):
        self.attr_list[name] = data_type

    def lookup_attribute(self, name):
        return self.attr_list[name] if name in self.attr_list else None
    
    def add_method(self, name, ret_type):
        self.method_list[name] = ret_type

    def lookup_method(self, name):
        return self.method_list[name] if name in self.method_list else None

class SymbolMethod:
    def __init__(self, name, data_type, check_static):
        self.name = name
        self.data_type = data_type
        self.check_static = check_static
        
class SymbolAttribute:
    def __init__(self, name, data_type, check_static, value_initialization):
        self.name = name
        self.data_type = data_type
        self.check_static = check_static
        self.value_initialization = value_initialization
        self.index = None   # for VariableInMethod
        
class SymbolVariableInMethod:
    def __init__(self, name, data_type, index):
        self.name = name
        self.data_type = data_type
        self.index = index

class SymbolDemo:
    def __init__(self, name, data_type, check_static, value_initialization=None, index=None):
        self.name = name
        self.data_type = data_type
        self.check_static = check_static
        self.value_initialization = value_initialization
        self.index = index  

class ComponentGlobalLocal:
    def __init__(self, global_sym, local_sym):
        self.global_sym = global_sym
        self.local_sym = local_sym

    def add_attribute(self, class_name, name, data_type):
        return self.global_sym[class_name].add_attribute(name, data_type)
    
    def lookup_attribute(self, class_name, name):
        return self.global_sym[class_name].lookup_attribute(name)

    def add_method(self, class_name, name, ret_type):
        return self.global_sym[class_name].add_method(name, ret_type)
    
    def lookup_method(self, class_name, name):
        return self.global_sym[class_name].lookup_method(name)

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class SubBody:
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Access:
    def __init__(self, frame, sym, isLeft, isFirst):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        # value: Int
        self.value = value

class CodeGenerator:
    
    def __init__(self):
        self.lib_name = "io"

    def init(self):
        global_env = {
            self.lib_name: ComponentClass({},
                {   "getInt": SymbolMethod("getInt", MType([], IntType()), True),
                    "putInt": SymbolMethod("putInt", MType([IntType()], VoidType()), True),
                    "putIntLn": SymbolMethod("putIntLn", MType([IntType()], VoidType()), True),
                    "getBool": SymbolMethod("getBool", MType([], BoolType()), True),
                    "putBool": SymbolMethod("putBool", MType([BoolType()], VoidType()), True),
                    "putBoolLn": SymbolMethod("putBoolLn", MType([BoolType()], VoidType()), True),
                    "putString": SymbolMethod("putString", MType([StringType()], VoidType()), True),
                    "putStringLn": SymbolMethod("putStringLn", MType([StringType()], VoidType()), True),
                    "getFloat": SymbolMethod("getFloat", MType([], FloatType()), True),
                    "putFloat": SymbolMethod("putFloat", MType([FloatType()], VoidType()), True),
                    "putFloatLn": SymbolMethod("putFloatLn", MType([FloatType()], VoidType()), True),
                    "putLn": SymbolMethod("putLn", MType([], VoidType()), True),
                },
            )
        }
        return ComponentGlobalLocal(global_env, None)

    def gen(self, ast, dir_):
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
        self.instance_attr_list = []
        self.static_attr_list = []
        self.current_method = None      # for return type
        self.emit = None

    def visitProgram(self, ast, o):
        [self.visit(each_class, self.env) for each_class in ast.decl]

    def visitClassDecl(self, ast, o):
        classname = ast.classname.name
        memList = ast.memlist
        parentname = ast.parentname.name if ast.parentname else "java/lang/Object"

        # init class to global symbols
        o.global_sym[classname] = ComponentClass({}, {})
        self.current_class = classname
        self.parent_class = parentname
        self.emit = Emitter(self.path + "/" + self.current_class + ".j")
        
        self.emit.printout(self.emit.emitPROLOG(classname, parentname))
        
        # get and methods
        constructor = None
        check_default_constructor = False
        attr_list = reduce(lambda x, y: x + [y] if isinstance(y, AttributeDecl) else x + [], memList, [])
        method_list = []
        for mem in memList:
            if isinstance(mem, MethodDecl):
                if mem.name.name == 'Constructor':
                    constructor = mem
                    if len(mem.param) == 0:     check_default_constructor = True
                else:
                    method_list += [mem]
        
        # visit attributes
        [self.visit(each_attr, o) for each_attr in attr_list]
            
        # visit constructor
        if constructor:
            self.visit(constructor, o)
        if check_default_constructor == False:
            o.local_sym = [{}] + o.local_sym if o.local_sym is not None else [{}]
            self.generate_method(MethodDecl(Instance(), Id('<init>'), [], Block([])), SubBody(Frame('<init>', VoidType()), o), Frame('<init>', VoidType()))
            o.local_sym.pop(0)
        o.local_sym = [{}] + o.local_sym if o.local_sym is not None else [{}]
        self.generate_method(MethodDecl(Static(), Id('<clinit>'), [], Block([])), SubBody(Frame("<clinit>", VoidType()), o), Frame("<clinit>", VoidType()))
        o.local_sym.pop(0)
        
        # visit methods
        [self.visit(method_list, o) for method_list in method_list]
            
        self.emit.emitEPILOG()

    def visitAttributeDecl(self, ast, o):
        kind = ast.kind
        decl = ast.decl
        
        name, type_data, value_initialization = None, None, None
        check_static = True if isinstance(kind, Static) else False
        check_constant = False
        if isinstance(decl, VarDecl):
            name, type_data, value_initialization = decl.variable.name, decl.varType, decl.varInit if decl.varInit else None
        else:
            name, type_data, value_initialization = decl.constant.name, decl.constType, decl.value if decl.value else None
            check_constant = True
        
        new_attr = SymbolAttribute(name, type_data, check_static, value_initialization)
        self.static_attr_list.append(new_attr) if check_static else self.instance_attr_list.append(new_attr)
        o.add_attribute(self.current_class, name, new_attr)
            
        if check_static:
            self.emit.printout(self.emit.emitSTATIC(name, type_data, check_constant, value_initialization))
        else:
            self.emit.printout(self.emit.emitINSTANCE(name, type_data, check_constant, value_initialization))

    def visitMethodDecl(self, ast, o):
        kind = ast.kind
        name = ast.name.name
        params = ast.param
        
        if name == 'Constructor':
            ast.name.name = '<init>'
            name = '<init>'
        check_static = True if isinstance(kind, Static) else False
        frame = Frame(name, None)
        o.local_sym = [{}] + o.local_sym if o.local_sym is not None else [{}]
        self.generate_method(ast, SubBody(frame, o), frame)
        o.add_method(self.current_class, name, SymbolMethod(name, MType([para.varType for para in params], self.current_method), check_static))
        o.local_sym.pop(0)

    def generate_method(self, method_ast, o, frame):
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
            code += self.emit.emitVAR(idx, 'this', ClassType(Id(self.current_class)), frame.getStartLabel(), frame.getEndLabel(), frame)
        elif check_main:
            idx = frame.getNewIndex()
            code += self.emit.emitVAR(idx, 'args', ArrayType(0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame)
        # visit parameters
        for para in params:
            code += self.visit(para, o)
        # label of method
        code += self.emit.emitLABEL(frame.getStartLabel(), frame)
        if name == '<init>':
            code += self.emit.emitTHIS(frame)
            code += self.emit.emitINVOKESPECIAL(frame, self.parent_class + '/<init>', MType([], VoidType()))
            for each_attr in self.instance_attr_list:
                if each_attr.value_initialization is None:
                    continue
                code += self.emit.emitTHIS(frame)
                code_value_init, type_value_init = self.visit(each_attr.value_initialization, Access(frame, self.env, False, False))
                code += code_value_init
                code += self.emit.emitI2F(o.frame) if (isinstance(each_attr.data_type, FloatType) and isinstance(type_value_init, IntType)) else ""
                code += self.emit.emitPUTFIELD(self.current_class + "." + each_attr.name, each_attr.data_type, frame)
        elif name == '<clinit>':
            for each_attr in self.static_attr_list:
                if each_attr.value_initialization is None:
                    continue
                init_code, init_type = self.visit(each_attr.value_initialization, Access(frame, self.env, False, False)) 
                code += init_code
                code += self.emit.emitI2F(o.frame) if (isinstance(each_attr.data_type, FloatType) and isinstance(init_type, IntType)) else ""
                code += self.emit.emitPUTSTATIC(self.current_class + "." + each_attr.name, each_attr.data_type, frame)
        # visit body method
        for inst in body.inst:
            code += self.visit(inst, o)
        if self.current_method is None:
            self.current_method = VoidType()
        # generate label of method after know return type
        code = self.emit.emitMETHOD(name, MType(par_type, self.current_method), check_static, frame) + code
        code += self.emit.emitLABEL(frame.getEndLabel(), frame)
        # generate end method
        if isinstance(self.current_method, VoidType):
            code += self.emit.emitRETURN(VoidType(), frame)
        code += self.emit.emitENDMETHOD(frame)
        self.emit.printout(code)
        frame.exitScope()
        
    def visitVarDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        o.sym.local_sym[0][ast.variable.name] = SymbolVariableInMethod(ast.variable.name, ast.varType, idx)
        code = ""
        code += self.emit.emitVAR(idx, ast.variable.name, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        code += self.visit(Assign(ast.variable, ast.varInit), o) if ast.varInit else ""
        return code
        
    def visitConstDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        o.sym.local_sym[0][ast.constant.name] = SymbolVariableInMethod(ast.constant.name, ast.constType, idx)
        code = ""
        code += self.emit.emitVAR(idx, ast.constant.name, ast.constType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        code += self.visit(Assign(ast.constant, ast.value), o) if ast.value else ""
        return code
        
    def visitUnaryOp(self, ast, o):
        code, type_data = self.visit(ast.body, o)
        op = ast.op
        if op == "!":   return code + self.emit.emitNOT(type_data, o.frame), type_data
        return code + self.emit.emitNEGOP(type_data, o.frame), type_data

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
        if op == "+.":
            return left_code + right_code + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), o.frame), StringType()
        if op == "&&":
            return left_code + right_code + self.emit.emitANDOP(o.frame), ret_type
        if op == "||":
            return left_code + right_code + self.emit.emitOROP(o.frame), ret_type
        if op == "%":
            return left_code + right_code + self.emit.emitMOD(o.frame), ret_type
        if op in [">", "<", ">=", "<=", "==", "!=", "==."]:
            return left_code + right_code + self.emit.emitREOP(op, ret_type, o.frame), BoolType()

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
        contructor_with_params = o.sym.lookup_method(classname, '<init>')
        
        if not contructor_with_params:
            raise IllegalRuntimeException('Cannot find <init>!')
        
        for i in range(len(params)):
            arg_code, arg_type = self.visit(ast.param[i], o)
            code += arg_code
            code += self.emit.emitI2F(o.frame) if isinstance(arg_type, IntType) and isinstance(contructor_with_params.data_type.partype[i], FloatType) else ""
                
        code += self.emit.emitINVOKESPECIAL(o.frame, classname + '/<init>', contructor_with_params.data_type)
        return code, ClassType(classname)

    def visitAssign(self, ast, o):
        code = ""
        left = ast.lhs
        exp = ast.exp

        check_field_access_or_array_cell, data_type = (self.visit(left, (Access(o.frame, o.sym, True, True), exp))) if (isinstance(left, FieldAccess) or isinstance(left, ArrayCell)) else ("", VoidType())
        if check_field_access_or_array_cell != "":  return check_field_access_or_array_cell
                    
        right_code, right_type = self.visit(exp, Access(o.frame, o.sym, False, True))
        left_code, left_type = self.visit(left, Access(o.frame, o.sym, True, True))
        code += right_code 
        code += self.emit.emitI2F(o.frame) if isinstance(right_type, IntType) and isinstance(left_type, FloatType) else ""
        code += left_code
        return code

    def visitFieldAccess(self, ast, o):
        code = ""
        obj = ast.obj
        fieldname = ast.fieldname.name

        o, expr = (o[0], o[1]) if isinstance(o, tuple) else (o, None)

        obj_code, obj_type = self.visit(obj, Access(o.frame, o.sym, False, False))
        class_name = ast.obj.name if (obj_code is None or obj_type is None) else obj_type.classname.name
        attr = o.sym.lookup_attribute(class_name, ast.fieldname.name)

        if not attr:
            raise IllegalRuntimeException("Cannot find attribute!")

        if o.isLeft and o.isFirst:  # write
            expr_code, expr_type = self.visit(expr, Access(o.frame, o.sym, False, True))
            code += (expr_code + self.emit.emitPUTSTATIC(class_name + "/" + fieldname, attr.data_type, o.frame)) \
                    if attr.check_static \
                    else (obj_code + expr_code + self.emit.emitPUTFIELD(class_name + "/" + fieldname, attr.data_type, o.frame))
        else:   # read
            code += (self.emit.emitGETSTATIC(class_name + "/" + fieldname, attr.data_type, o.frame)) \
                    if attr.check_static \
                    else (obj_code + self.emit.emitGETFIELD(class_name + "/" + fieldname, attr.data_type, o.frame))
        return code, attr.data_type

    def visitArrayCell(self, ast, o):
        code = ""
        arr = ast.arr
        idx_list = ast.idx
        
        o, expr = (o[0], o[1]) if isinstance(o, tuple) else (o, None)
            
        code, arr_type = self.visit(arr, Access(o.frame, o.sym, False, True))
        arr_type = arr_type.eleType
        for i in range(len(idx_list) - 1):
            idx_code, idx_type = self.visit(idx_list[i], Access(o.frame, o.sym, False, True))
            code += idx_code
            code += self.emit.emitALOAD(arr_type, o.frame)
            arr_type = arr_type.eleType
        # last element
        idx_code, idx_type = self.visit(idx_list[-1], Access(o.frame, o.sym, False, True))
        code += idx_code + self.visit(expr, Access(o.frame, o.sym, False, True))[0] + self.emit.emitASTORE(arr_type, o.frame) \
                if o.isLeft \
                else idx_code + self.emit.emitALOAD(arr_type, o.frame) 
        return code, arr_type
        
    def visitBlock(self, ast, o):
        o.sym.local_sym = [{}] + o.sym.local_sym if o.sym.local_sym is not None else [{}]
        code = ""
        for inst in ast.inst:
            code += self.visit(inst, o)
        o.sym.local_sym.pop(0)
        return code

    def visitIf(self, ast, o):
        code = ""
        expr_code, expr_type = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
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
            ast.expr1, Access(o.frame, o.sym, False, True))
        expr2_code, _ = self.visit(
            ast.expr2, Access(o.frame, o.sym, False, True))
        expr3_code, _ = self.visit(
            ast.expr3, Access(o.frame, o.sym, False, True))
        id_write_code, _ = self.visit(ast.id, Access(
            o.frame, o.sym, True, True))  # Write code
        id_read_code, _ = self.visit(ast.id, Access(
            o.frame, o.sym, False, True))  # Read code
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
        expr_code, expr_type = (self.visit(ast.expr, Access(o.frame, o.sym, False, True)) if ast.expr else ("", VoidType()))
        code += expr_code
        code += self.emit.emitRETURN(expr_type, o.frame)
        self.current_method = expr_type if self.current_method is None else self.current_method
        return code

    def visitCallExpr(self, ast, o):
        code = ""
        obj = ast.obj
        method_name = ast.method.name
        params = ast.param

        obj_code, obj_type = self.visit(obj, o)
        class_name = obj.name if obj_code is None or obj_type is None else obj_type.classname.name
        # find method
        found_method = o.sym.lookup_method(class_name, method_name)       # type of method is MType
        if found_method is None:
            raise IllegalRuntimeException("Cannot find method!")

        for i in range(len(params)):
            arg_code, arg_type = self.visit(params[i], Access(o.frame, o.sym, False, True))
            code += arg_code
            code += self.emit.emitI2F(o.frame) if isinstance(arg_type, IntType) and isinstance(found_method.data_type.partype[i], FloatType) else ""
        
        code =  code + self.emit.emitINVOKESTATIC(class_name + "/" + method_name, found_method.data_type, o.frame) \
                if found_method.check_static \
                else obj_code + code + self.emit.emitINVOKEVIRTUAL(class_name + "/" + method_name, found_method.data_type, o.frame)
        return code, found_method.data_type.rettype
        
    def visitCallStmt(self, ast, o):
        code = ""
        obj = ast.obj
        method_name = ast.method.name
        params = ast.param
        
        obj_code, obj_type = self.visit(obj, Access(o.frame, o.sym, False, True))
        class_name = obj.name if obj_code is None or obj_type is None else obj_type.classname.name

        # Find method
        method = o.sym.lookup_method(class_name, method_name)
        if method is None:
            raise IllegalRuntimeException("Cannot find method!")
        
        for i in range(len(params)):
            arg_code, arg_type = self.visit(params[i], Access(o.frame, o.sym, False, True))
            code += arg_code
            code += self.emit.emitI2F(o.frame) if isinstance(arg_type, IntType) and isinstance(method.data_type.partype[i], FloatType) else "" 

        code =  code + self.emit.emitINVOKESTATIC(class_name + "/" + method_name, method.data_type, o.frame) \
                if method.check_static \
                else obj_code + code + self.emit.emitINVOKEVIRTUAL(class_name + "/" + method_name, method.data_type, o.frame)
        
        code += self.emit.emitPOP(o.frame) if not isinstance(method.data_type.rettype, VoidType) else ""
        return code
        
    def visitId(self, ast, o):  # ID only for local variable, attribute or method use access
        local_found = None
        for each_local_scope in o.sym.local_sym:
            if ast.name in each_local_scope:
                local_found = each_local_scope[ast.name]

        return (None, None) if not local_found else (
            (self.emit.emitWRITEVAR(ast.name, local_found.data_type, local_found.index, o.frame), local_found.data_type) \
            if o.isLeft \
            else (self.emit.emitREADVAR(ast.name, local_found.data_type, local_found.index, o.frame), local_found.data_type)
        ) 

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
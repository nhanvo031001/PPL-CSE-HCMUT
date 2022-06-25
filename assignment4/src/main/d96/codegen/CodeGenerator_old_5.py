"""
    @author: Vo Nguyen Thien Nhan
"""

## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##
# from main.d96.utils.AST import *
# from main.d96.checker.StaticCheck import *
# from main.d96.checker.StaticError import *
## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##

from functools import reduce
from Frame import Frame
from Emitter import Emitter
from CodeGenError import *
from abc import ABC, abstractmethod
from AST import *
from Visitor import *

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

class APIComponentClass:
    def __init__(self, global_sym, local_sym=None):
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

class Symbol:
    def __init__(self, name, data_type, check_static, value_initialization=None, index=None):
        self.name = name
        self.data_type = data_type
        self.check_static = check_static
        self.value_initialization = value_initialization
        self.index = index 

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
        
class CodeGenerator:
    
    def __init__(self):
        self.lib_name = "io"

    def get_io_sym(self):
        global_sym = {self.lib_name: ComponentClass({}, {   
                            "getInt": Symbol("getInt", MType([], IntType()), True, None, None),
                            "readInt": Symbol("readInt", MType([], IntType()), True, None, None),
                            "$getInt": Symbol("$getInt", MType([], IntType()), True, None, None),
                            "$readInt": Symbol("$readInt", MType([], IntType()), True, None, None),
                            
                            "putInt": Symbol("putInt", MType([IntType()], VoidType()), True, None, None),
                            "putIntLn": Symbol("putIntLn", MType([IntType()], VoidType()), True, None, None),
                            "writeInt": Symbol("writeInt", MType([IntType()], VoidType()), True, None, None),
                            "writeIntLn": Symbol("writeIntLn", MType([IntType()], VoidType()), True, None, None),
                            "printInt": Symbol("printInt", MType([IntType()], VoidType()), True, None, None),
                            "printIntLn": Symbol("printIntLn", MType([IntType()], VoidType()), True, None, None),
                            "$putInt": Symbol("$putInt", MType([IntType()], VoidType()), True, None, None),
                            "$putIntLn": Symbol("$putIntLn", MType([IntType()], VoidType()), True, None, None),
                            "$writeInt": Symbol("$writeInt", MType([IntType()], VoidType()), True, None, None),
                            "$writeIntLn": Symbol("$writeIntLn", MType([IntType()], VoidType()), True, None, None),
                            "$printInt": Symbol("$printInt", MType([IntType()], VoidType()), True, None, None),
                            "$printIntLn": Symbol("$printIntLn", MType([IntType()], VoidType()), True, None, None),
                            
                            
                            "getBool": Symbol("getBool", MType([], BoolType()), True, None, None),
                            "readBool": Symbol("readBool", MType([], BoolType()), True, None, None),
                            "$getBool": Symbol("$getBool", MType([], BoolType()), True, None, None),
                            "$readBool": Symbol("$readBool", MType([], BoolType()), True, None, None),
                            
                            "putBool": Symbol("putBool", MType([BoolType()], VoidType()), True, None, None),
                            "putBoolLn": Symbol("putBoolLn", MType([BoolType()], VoidType()), True, None, None),
                            "writeBool": Symbol("writeBool", MType([BoolType()], VoidType()), True, None, None),
                            "writeBoolLn": Symbol("writeBoolLn", MType([BoolType()], VoidType()), True, None, None),
                            "printBool": Symbol("printBool", MType([BoolType()], VoidType()), True, None, None),
                            "printBoolLn": Symbol("printBoolLn", MType([BoolType()], VoidType()), True, None, None),
                            "$putBool": Symbol("$putBool", MType([BoolType()], VoidType()), True, None, None),
                            "$putBoolLn": Symbol("$putBoolLn", MType([BoolType()], VoidType()), True, None, None),
                            "$writeBool": Symbol("$writeBool", MType([BoolType()], VoidType()), True, None, None),
                            "$writeBoolLn": Symbol("$writeBoolLn", MType([BoolType()], VoidType()), True, None, None),
                            "$printBool": Symbol("$printBool", MType([BoolType()], VoidType()), True, None, None),
                            "$printBoolLn": Symbol("$printBoolLn", MType([BoolType()], VoidType()), True, None, None),
                            
                            
                            "putString": Symbol("putString", MType([StringType()], VoidType()), True, None, None),
                            "putStringLn": Symbol("putStringLn", MType([StringType()], VoidType()), True, None, None),
                            "writeString": Symbol("writeString", MType([StringType()], VoidType()), True, None, None),
                            "writeStringLn": Symbol("writeStringLn", MType([StringType()], VoidType()), True, None, None),
                            "printString": Symbol("printString", MType([StringType()], VoidType()), True, None, None),
                            "printStringLn": Symbol("printStringLn", MType([StringType()], VoidType()), True, None, None),
                            "$putString": Symbol("$putString", MType([StringType()], VoidType()), True, None, None),
                            "$putStringLn": Symbol("$putStringLn", MType([StringType()], VoidType()), True, None, None),
                            "$writeString": Symbol("$writeString", MType([StringType()], VoidType()), True, None, None),
                            "$writeStringLn": Symbol("$writeStringLn", MType([StringType()], VoidType()), True, None, None),
                            "$printString": Symbol("$printString", MType([StringType()], VoidType()), True, None, None),
                            "$printStringLn": Symbol("$printStringLn", MType([StringType()], VoidType()), True, None, None),
                            
                            
                            "putStr": Symbol("putStr", MType([StringType()], VoidType()), True, None, None),
                            "putStrLn": Symbol("putStrLn", MType([StringType()], VoidType()), True, None, None),
                            "writeStr": Symbol("writeStr", MType([StringType()], VoidType()), True, None, None),
                            "writeStrLn": Symbol("writeStrLn", MType([StringType()], VoidType()), True, None, None),
                            "printStr": Symbol("printStr", MType([StringType()], VoidType()), True, None, None),
                            "printStrLn": Symbol("printStrLn", MType([StringType()], VoidType()), True, None, None),
                            "$putStr": Symbol("$putStr", MType([StringType()], VoidType()), True, None, None),
                            "$putStrLn": Symbol("$putStrLn", MType([StringType()], VoidType()), True, None, None),
                            "$writeStr": Symbol("$writeStr", MType([StringType()], VoidType()), True, None, None),
                            "$writeStrLn": Symbol("$writeStrLn", MType([StringType()], VoidType()), True, None, None),
                            "$printStr": Symbol("$printStr", MType([StringType()], VoidType()), True, None, None),
                            "$printStrLn": Symbol("$printStrLn", MType([StringType()], VoidType()), True, None, None),
                            
                            
                            # "getFloat": Symbol("getFloat", MType([], FloatType()), True, None, None),
                            # "putFloat": Symbol("putFloat", MType([FloatType()], VoidType()), True, None, None),
                            # "putFloatLn": Symbol("putFloatLn", MType([FloatType()], VoidType()), True, None, None),
                            "getFloat": Symbol("getFloat", MType([], FloatType()), True, None, None),
                            "readFloat": Symbol("readFloat", MType([], FloatType()), True, None, None),
                            "$getFloat": Symbol("$getFloat", MType([], FloatType()), True, None, None),
                            "$readFloat": Symbol("$readFloat", MType([], FloatType()), True, None, None),
                            
                            "putFloat": Symbol("putFloat", MType([FloatType()], VoidType()), True, None, None),
                            "putFloatLn": Symbol("putFloatLn", MType([FloatType()], VoidType()), True, None, None),
                            "writeFloat": Symbol("writeFloat", MType([FloatType()], VoidType()), True, None, None),
                            "writeFloatLn": Symbol("writeFloatLn", MType([FloatType()], VoidType()), True, None, None),
                            "printFloat": Symbol("printFloat", MType([FloatType()], VoidType()), True, None, None),
                            "printFloatLn": Symbol("printFloatLn", MType([FloatType()], VoidType()), True, None, None),
                            "$putFloat": Symbol("$putFloat", MType([FloatType()], VoidType()), True, None, None),
                            "$putFloatLn": Symbol("$putFloatLn", MType([FloatType()], VoidType()), True, None, None),
                            "$writeFloat": Symbol("$writeFloat", MType([FloatType()], VoidType()), True, None, None),
                            "$writeFloatLn": Symbol("$writeFloatLn", MType([FloatType()], VoidType()), True, None, None),
                            "$printFloat": Symbol("$printFloat", MType([FloatType()], VoidType()), True, None, None),
                            "$printFloatLn": Symbol("$printFloatLn", MType([FloatType()], VoidType()), True, None, None),
                            
                            
                            "putLn": Symbol("putLn", MType([], VoidType()), True, None, None),
                            "$putLn": Symbol("$putLn", MType([], VoidType()), True, None, None),
                            "printLn": Symbol("printLn", MType([], VoidType()), True, None, None),
                            "$printLn": Symbol("$printLn", MType([], VoidType()), True, None, None),
                        })}
        return APIComponentClass(global_sym)

    def gen(self, ast, dir_):
        sym = self.get_io_sym()
        global_codegen = CodeGenVisitor(ast, sym, dir_)
        global_codegen.visit(ast, None)


class CodeGenVisitor(BaseVisitor):
    def __init__(self, ast, sym, dir_):
        self.ast = ast
        self.sym = sym
        self.path = dir_
        self.current_class = None
        self.current_method = None      # for return type
        self.parent_class = None
        self.attr_list = {'instance': [], 'static': []}
        self.emit = None

    def visitProgram(self, ast, o):
        [self.visit(each_class, self.sym) for each_class in ast.decl]

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
                    if len(mem.param) == 0:     check_default_constructor = True
                    constructor = mem
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
        o.add_method(self.current_class, name, Symbol(name, MType([para.varType for para in params], self.current_method), check_static))
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
        code =  self.emit.emitVAR(frame.getNewIndex(), 'this', ClassType(Id(self.current_class)), frame.getStartLabel(), frame.getEndLabel(), frame)  \
                if (not check_static or name == '<init>')   \
                else self.emit.emitVAR(frame.getNewIndex(), 'args', ArrayType(0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame)
        # visit parameters
        for para in params:
            code += self.visit(para, o)
        # label of method
        code += self.emit.emitLABEL(frame.getStartLabel(), frame)
        if name == '<clinit>':
            for each_attr in self.attr_list['static']:
                if each_attr.value_initialization is None:
                    continue
                init_code, init_type = self.visit(each_attr.value_initialization, Access(frame, self.sym, False, False)) 
                code += init_code
                code += self.emit.emitI2F(o.frame) if (isinstance(each_attr.data_type, FloatType) and isinstance(init_type, IntType)) else ""
                code += self.emit.emitPUTSTATIC(self.current_class + "." + each_attr.name, each_attr.data_type, frame)
        elif name == '<init>':
            code += self.emit.emitNONSTATICMETHODTHIS(frame)
            code += self.emit.emitINVOKESPECIAL(frame, self.parent_class + '/<init>', MType([], VoidType()))
            for each_attr in self.attr_list['instance']:  
                if each_attr.value_initialization is None:
                    continue
                code += self.emit.emitNONSTATICMETHODTHIS(frame)
                code_value_init, type_value_init = self.visit(each_attr.value_initialization, Access(frame, self.sym, False, False))
                code += code_value_init
                code += self.emit.emitI2F(o.frame) if (isinstance(each_attr.data_type, FloatType) and isinstance(type_value_init, IntType)) else ""
                code += self.emit.emitPUTFIELD(self.current_class + "." + each_attr.name, each_attr.data_type, frame)
        # visit body method
        for inst in body.inst:
            code += self.visit(inst, o)
        self.current_method = VoidType() if self.current_method is None else self.current_method
        # generate label of method after know return type
        code = self.emit.emitMETHOD(name, MType(par_type, self.current_method), check_static, frame) + code
        code += self.emit.emitLABEL(frame.getEndLabel(), frame)
        # generate end method
        code += self.emit.emitRETURN(VoidType(), frame) if isinstance(self.current_method, VoidType) else ""
        code += self.emit.emitENDMETHOD(frame)
        self.emit.printout(code)
        frame.exitScope()
        
    def visitAttributeDecl(self, ast, o):
        kind = ast.kind
        decl = ast.decl
        
        name, type_data, value_initialization = None, None, None
        check_static = True if isinstance(kind, Static) else False
        name, type_data, value_initialization, check_constant = (decl.variable.name, decl.varType, decl.varInit if decl.varInit else None, False) \
            if isinstance(decl, VarDecl) \
            else (decl.constant.name, decl.constType, decl.value if decl.value else None, True)
        
        new_attr = Symbol(name, type_data, check_static, value_initialization)
        self.attr_list['static'].append(new_attr) if check_static else self.attr_list['instance'].append(new_attr)
        o.add_attribute(self.current_class, name, new_attr)
        
        self.emit.printout(self.emit.emitATTRIBUTE(name, type_data, check_constant, value_initialization, 'static')) \
            if check_static \
            else self.emit.printout(self.emit.emitATTRIBUTE(name, type_data, check_constant, value_initialization, 'instance'))
        
    def visitVarDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        o.sym.local_sym[0][ast.variable.name] = Symbol(ast.variable.name, ast.varType, None, None, idx)
        code = ""
        code += self.emit.emitVAR(idx, ast.variable.name, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        code += self.visit(Assign(ast.variable, ast.varInit), o) if ast.varInit else ""
        return code
        
    def visitConstDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        o.sym.local_sym[0][ast.constant.name] = Symbol(ast.constant.name, ast.constType, None, None, idx)
        code = ""
        code += self.emit.emitVAR(idx, ast.constant.name, ast.constType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        code += self.visit(Assign(ast.constant, ast.value), o) if ast.value else ""
        return code
        
    def visitBlock(self, ast, o):
        o.sym.local_sym = [{}] + o.sym.local_sym if o.sym.local_sym is not None else [{}]
        code = ""
        for inst in ast.inst:
            code += self.visit(inst, o)
        o.sym.local_sym.pop(0)
        return code

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
        for i in range(len(params)):
            arg_code, arg_type = self.visit(ast.param[i], o)
            code += arg_code
            code += self.emit.emitI2F(o.frame) if isinstance(contructor_with_params.data_type.partype[i], FloatType) and isinstance(arg_type, IntType) else ""   
        code += self.emit.emitINVOKESPECIAL(o.frame, classname + '/<init>', contructor_with_params.data_type)
        return code, ClassType(classname)

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
        o.frame.enterLoop()
        expr1_code, exp1_type = self.visit(ast.expr1, Access(o.frame, o.sym, False, True))
        expr2_code, exp2_type = self.visit(ast.expr2, Access(o.frame, o.sym, False, True))
        expr3_code, exp3_type = self.visit(ast.expr3, Access(o.frame, o.sym, False, True)) if ast.expr3 else (IntLiteral(1), None)
        begin_loop_label, body_loop_label, forward_loop_label, forward_update_label, end_loop_label = (o.frame.getNewLabel(), o.frame.getNewLabel(), o.frame.getNewLabel(), o.frame.getNewLabel(), o.frame.getNewLabel())
        continue_label, break_label = (o.frame.getContinueLabel(), o.frame.getBreakLabel())
        store_var, store_var_type = self.visit(ast.id, Access(o.frame, o.sym, True, True))
        load_var, load_var_type = self.visit(ast.id, Access(o.frame, o.sym, False, True))
        # id = exp1
        code += expr1_code
        code += store_var
        # check condition
        code += self.emit.emitLABEL(begin_loop_label, o.frame)
        code += expr1_code
        code += expr2_code
        code += self.emit.emitREOP("<", IntType(), o.frame)
        code += self.emit.emitIFTRUE(forward_loop_label, o.frame)
        # backward
        code += load_var
        code += expr2_code
        code += self.emit.emitREOP("<", IntType(), o.frame)
        o.frame.push()
        code += self.emit.emitIFTRUE(end_loop_label, o.frame)
        code += self.emit.emitGOTO(body_loop_label, o.frame)
        # forward
        code += self.emit.emitLABEL(forward_loop_label, o.frame)
        code += load_var
        code += expr2_code
        o.frame.push()
        o.frame.push()
        code += self.emit.emitREOP(">", IntType(), o.frame)
        code += self.emit.emitIFTRUE(end_loop_label, o.frame)
        # body
        code += self.emit.emitLABEL(body_loop_label, o.frame)
        code += self.visit(ast.loop, o)
        code += self.emit.emitLABEL(continue_label, o.frame)
        # update
        code += expr1_code
        code += expr2_code
        o.frame.push()
        o.frame.push()
        code += self.emit.emitREOP("<", IntType(), o.frame)  # Loop down
        code += self.emit.emitIFTRUE(forward_update_label, o.frame)
        # exp -= exp3
        code += load_var
        code += expr3_code
        o.frame.push()
        code += self.emit.emitADDOP("-", IntType(), o.frame)
        code += store_var
        code += self.emit.emitGOTO(begin_loop_label, o.frame)
        # exp1 += exp3
        code += self.emit.emitLABEL(forward_update_label, o.frame)
        code += load_var
        code += expr3_code
        o.frame.push()
        code += self.emit.emitADDOP("+", IntType(), o.frame)
        code += store_var
        # back to loop
        code += self.emit.emitGOTO(begin_loop_label, o.frame)
        # exit loop
        code += self.emit.emitLABEL(break_label, o.frame)
        code += self.emit.emitLABEL(end_loop_label, o.frame)
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

    def visitCallStmt(self, ast, o):
        code = ""
        obj = ast.obj
        method_name = ast.method.name
        params = ast.param
        
        obj_code, obj_type = self.visit(obj, Access(o.frame, o.sym, False, True))
        class_name = obj.name if obj_code is None or obj_type is None else obj_type.classname.name

        # Find method
        method = o.sym.lookup_method(class_name, method_name)
        for i in range(len(params)):
            arg_code, arg_type = self.visit(params[i], Access(o.frame, o.sym, False, True))
            code += arg_code
            code += self.emit.emitI2F(o.frame) if isinstance(arg_type, IntType) and isinstance(method.data_type.partype[i], FloatType) else "" 

        code =  code + self.emit.emitINVOKESTATIC(class_name + "/" + method_name, method.data_type, o.frame) \
                if method.check_static \
                else obj_code + code + self.emit.emitINVOKEVIRTUAL(class_name + "/" + method_name, method.data_type, o.frame)
        
        code += self.emit.emitPOP(o.frame) if not isinstance(method.data_type.rettype, VoidType) else ""
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
        
    def visitCallExpr(self, ast, o):
        code = ""
        obj = ast.obj
        method_name = ast.method.name
        params = ast.param

        obj_code, obj_type = self.visit(obj, o)
        class_name = obj.name if obj_code is None or obj_type is None else obj_type.classname.name
        # find method
        found_method = o.sym.lookup_method(class_name, method_name)       # type of method is MType
        for i in range(len(params)):
            arg_code, arg_type = self.visit(params[i], Access(o.frame, o.sym, False, True))
            code += arg_code
            code += self.emit.emitI2F(o.frame) if isinstance(arg_type, IntType) and isinstance(found_method.data_type.partype[i], FloatType) else ""
        
        code =  code + self.emit.emitINVOKESTATIC(class_name + "/" + method_name, found_method.data_type, o.frame) \
                if found_method.check_static \
                else obj_code + code + self.emit.emitINVOKEVIRTUAL(class_name + "/" + method_name, found_method.data_type, o.frame)
        return code, found_method.data_type.rettype
        
    def visitId(self, ast, o):
        local_found = None
        for each_local_scope in o.sym.local_sym:
            if ast.name in each_local_scope:
                local_found = each_local_scope[ast.name]

        return (None, None) if not local_found else (
            (self.emit.emitWRITEVAR(ast.name, local_found.data_type, local_found.index, o.frame), local_found.data_type) \
            if o.isLeft \
            else (self.emit.emitREADVAR(ast.name, local_found.data_type, local_found.index, o.frame), local_found.data_type)
        ) 
        
    def visitArrayLiteral(self, ast, o):
        code = ""
        value_list = ast.value
        ele_type = None
        o.frame.push()
        for i in range(len(value_list)):
            code += self.emit.emitDUP(o.frame)
            code += self.emit.emitPUSHICONST(i, o.frame)
            ele_code, ele_type = self.visit(value_list[i], o)
            # if isinstance(ele_type, IntType) and isinstance(o.sym.eleType, FloatType): ele_code += self.emit.emitI2F(o.frame)
            code += ele_code
            code += self.emit.emitASTORE(ele_type, o.frame)
        o.frame.pop()
        code = self.emit.emitARRAYLITERAL(ArrayType(len(value_list), ele_type), o.frame) + code
        return code, ArrayType(len(value_list), ele_type)

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST('"' + str(ast.value) + '"', StringType(), o.frame), StringType()
    
    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(str(ast.value), BoolType(), o.frame), BoolType()
        
    def visitSelfLiteral(self, ast, o):
        return self.emit.emitNONSTATICMETHODTHIS(o.frame), ClassType(Id(self.current_class))
    
    def visitNullLiteral(self, ast, o):
        return self.emit.emitPUSHNULL(o.frame), NullLiteral()
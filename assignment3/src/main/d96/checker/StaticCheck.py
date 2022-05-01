from cgi import FieldStorage
from cgitb import lookup
from pydoc import classname
from sqlite3 import IntegrityError
from xml.dom.minidom import TypeInfo
from matplotlib.pyplot import isinteractive
from numpy import isin
from pyparsing import conditionAsParseAction
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##
from main.d96.utils.AST import *
from main.d96.parser.D96Parser import D96Parser
from main.d96.parser.D96Visitor import D96Visitor
## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##

def lookup_attribute (attri_name, class_name, global_scope, list_inherit):
    current_class = class_name
    while current_class:
        if attri_name in global_scope['global'][current_class]:
            return global_scope['global'][current_class][attri_name]
        current_class = list_inherit[current_class]
    return None

def type_inference (lhs, rhs, list_inherit):
    if isinstance(lhs, FloatType) and isinstance(rhs, IntType): return True
    
    if isinstance(lhs, ClassType) and isinstance(rhs, ClassType):
        parent_class = list_inherit[rhs.classname.name]
        while (parent_class):
            if lhs.classname.name == parent_class: return True
            parent_class = list_inherit[parent_class]
    return False

def type_compare (first, second):
    # print("\nfirst, second: ", first, second)
    # print("\n type first, second: ", type(first), type(second))
    if isinstance(first, ClassType) and isinstance(second, ClassType):
        return first.classname.name == second.classname.name
    if isinstance(first, ArrayType) and isinstance(second, ArrayType):
        return first.size == second.size and type_compare(first.eleType, second.eleType)
    return type(first) == type(second)

def type_params_and_args_list (params, args, list_inherit):
    # print("param, arg: ", params, args)
    if len(params) != len(args): return False
    for i in range(len(params)):
        if type_compare(params[i], args[i]) == False and type_inference(params[i], args[i], list_inherit) == False:
            return False
    return True

class Symbol:
    def __init__(self, name, kind, static_or_instance, type_data, param_type_list = None):
        self.name = name
        self.kind = kind
        self.static_or_instance = static_or_instance
        self.type_data = type_data
        self.param_type_list = param_type_list
    
    def __str__(self):
        return "Symbol" + "("+ str(self.name) + ", " + str(self.kind) + ", " + str(self.static_or_instance) + ", " +str(self.type_data)  + (", " + str(self.param_type_list) if self.param_type_list else "") + ")"

class StaticChecker(BaseVisitor, Utils):

    def __init__(self,ast):
        self.ast = ast
        self.list_inherit = {}
        
    def check(self):
        return self.visit(self.ast, None)
    
    def visitId(self, ast: Id, o):
        # print("\no in visitId: ", o)
        
        const_decl = None
        if len(o) == 2:
            const_decl, o = o
        
        # check local
        for each_local in o['local']:
            if ast.name in each_local:
                if const_decl and (each_local[ast.name].kind == 'mutable' or each_local[ast.name].kind == 'variable'):
                    raise IllegalConstantExpression(ast)
                return each_local[ast.name]     # return Symbol
        
        # lookup_attri = lookup_attribute(ast.name, o['current_class'], o, self.list_inherit)
        # if lookup_attri: 
        #     if const_decl and (lookup_attri.kind == 'mutable' or lookup_attri.kind == 'variable'):
        #         raise IllegalConstantExpression(ast)
        #     return lookup_attri     # return Symbol
        raise Undeclared(Identifier(), ast.name)
    
    def visitBinaryOp(self, ast: BinaryOp, o):
        op = ast.op
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o)
        
        flag_const_init = None
        if len(o) == 2:
            flag_const_init, o = o
            
        if flag_const_init:
            if isinstance(left, Symbol):
                if left.kind == 'mutable' or left.kind == 'variable': raise IllegalConstantExpression(ast)
            if isinstance(right, Symbol):
                if right.kind == 'mutable' or right.kind == 'variable': raise IllegalConstantExpression(ast)
            
        if isinstance(left, Symbol): left = left.type_data
        if isinstance(right, Symbol): right = right.type_data
        
        if op in ['+', '-', '*', '/']:
            if isinstance(left, IntType) and isinstance(right, IntType): return IntType() if ast.op != '/' else FloatType()
            if isinstance(left, FloatType) or isinstance(right, FloatType): return FloatType()
            raise TypeMismatchInExpression(ast)
        
        if op == '%':
            if isinstance(left, IntType) and isinstance(right, IntType): return IntType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['&&', '||']:
            if isinstance(left, BoolType) and isinstance(right, BoolType): return BoolType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['==.']:
            if isinstance(left, StringType) and isinstance(right, StringType): return BoolType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['+.']:
            if isinstance(left, StringType) and isinstance(right, StringType): return StringType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['<', '>', '<=', '>=']:
            if not (isinstance(left, IntType) or isinstance(left, FloatType)) or not (isinstance(right, IntType) or isinstance(right, FloatType)): 
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if op in ['==', '!=']:
            # if not (isinstance(left, IntType) or isinstance(left, BoolType)) or not (isinstance(right, IntType) or isinstance(right, BoolType)): 
            #     raise TypeMismatchInExpression(ast)
            return BoolType()
    
    def visitUnaryOp(self, ast: UnaryOp, o):    # return data type
        flag_const_init = None
        if len(o) == 2:
            flag_const_init, o = o
            
        op = ast.op
        exp_type_data = self.visit(ast.body, o)

        # if isinstance(exp_type_data, Symbol):   # ID
        #     if flag_const_init and (exp_type_data.kind == 'mutable' or exp_type_data.kind == 'variable'):
        #         raise IllegalConstantExpression(ast)
        if isinstance(exp_type_data, Symbol):
            exp_type_data = exp_type_data.type_data
        
        if op == '!':
            if isinstance(exp_type_data, BoolType): return BoolType()
            raise TypeMismatchInExpression(ast)
        if op == '-':
            if isinstance(exp_type_data, IntType): return IntType()
            if isinstance(exp_type_data, FloatType): return FloatType()
            raise TypeMismatchInExpression(ast)
        if op == 'New':
            if isinstance(exp_type_data, ClassType): return ClassType()
            raise TypeMismatchInExpression(ast)
    
    def visitCallExpr(self, ast: CallExpr, o):
        print("\nvisitCallExpr")
        temp = o
        flag_const_init = None
        if len(o) == 2:
            flag_const_init, o = o
        
        
        method = ast.method.name
        args_list = [self.visit(each_param, temp) for each_param in ast.param]

        # static method invocation
        if isinstance(ast.obj, Id) and method[0] == '$':
            print("\nstatic method invoke")
            class_name = ast.obj.name
            if class_name not in o['global']: raise Undeclared(Class(), class_name)
            lookup_method = lookup_attribute(method, class_name, o, self.list_inherit)
            if not lookup_method: raise Undeclared(Method(), method)
            if not isinstance(lookup_method.static_or_instance, Static): raise IllegalMemberAccess(ast)
            if lookup_method.kind != 'method': raise Undeclared(Method(), method)
            if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                raise TypeMismatchInExpression(ast)
            print("\n pass static method invoke")
            return lookup_method.type_data
        
        # instance method invocation
        obj = self.visit(ast.obj, temp)
        if isinstance(obj.type_data, ClassType):
            lookup_method = lookup_attribute(method, obj.type_data.classname.name, o, self.list_inherit)
            if not lookup_method: raise Undeclared(Method(), method)
            if not isinstance(lookup_method.static_or_instance, Instance): raise IllegalMemberAccess(ast)
            if lookup_method.kind != 'method': raise Undeclared(Method(), method)
            if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                raise TypeMismatchInExpression(ast)
            return lookup_method.type_data
        raise TypeMismatchInExpression(ast)
    
    def visitNewExpr(self, ast: NewExpr, o):
        print("\nvisitNewExpr")
        flag_const_init = None
        if len(o) == 2:
            flag_const_init, o = o
        
        class_name = ast.classname.name
        if class_name not in o['global']:
            raise Undeclared(Class(), class_name)
        
        if len(ast.param) != 0:
            if 'Constructor' in o['global'][class_name]:
                print("\n have constructor")
                method_constructor = o['global'][class_name]['Constructor']     # return Symbol
                args = [self.visit(each_arg, o) for each_arg in ast.param]
                if type_params_and_args_list(method_constructor.param_type_list, args, self.list_inherit) == False:
                    raise TypeMismatchInExpression(ast)
            else:
                raise Undeclared(Method(), 'Constructor')
        
        return ClassType(class_name)
    
    def visitArrayCell(self, ast: ArrayCell, o):
        print("\ 1 pass")
        temp = o
        flag_const_init = None
        if len(o) == 2:
            flag_const_init, o = o
        
        arr = self.visit(ast.arr, temp)     # visitID, return Symbol
        idx_list = [self.visit(each_idx, temp) for each_idx in ast.idx]
        
        for each_idx in idx_list:
            # print("\narr, each_idx: ", arr, each_idx)
            if not isinstance(arr.type_data, ArrayType): raise TypeMismatchInExpression(ast)
            if not isinstance(each_idx, IntType): raise TypeMismatchInExpression(ast)
            arr = arr.type_data.eleType
        return arr
    
    def visitFieldAccess(self, ast: FieldAccess, o):
        print("\vvisitFieldAccess")
        temp = o
        flag_const_init = None
        if len(o) == 2:
            flag_const_init, o = o
        
        field_name = ast.fieldname.name
        print("field name: ", field_name)
        # static field access
        if isinstance(ast.obj, Id) and field_name[0] == '$':
            print("\n static field access")
            class_name = ast.obj.name
            if class_name not in o['global']: raise Undeclared(Class(), class_name)
            find_attribute = lookup_attribute(field_name, class_name, o, self.list_inherit)
            if not find_attribute: raise Undeclared(Attribute(), field_name)
            if not isinstance(find_attribute.static_or_instance, Static): raise IllegalMemberAccess(ast)
            if find_attribute.kind == 'method': raise Undeclared(Attribute(), field_name)
            if flag_const_init and find_attribute.kind == 'mutable': raise IllegalConstantExpression(ast)
            print("\n pass static field access")
            return find_attribute.type_data
        
        # instance field access
        obj = self.visit(ast.obj, temp)     # Symbol
        if isinstance(obj.type_data, ClassType):
            print("\n instance field access")
            class_name = obj.type_data.classname.name
            find_attribute = lookup_attribute(field_name, class_name, o, self.list_inherit)
            if not find_attribute: raise Undeclared(Attribute(), field_name)
            if not isinstance(find_attribute.static_or_instance, Instance): raise IllegalMemberAccess(ast)
            if find_attribute.kind == 'method': raise Undeclared(Attribute(), field_name)
            if flag_const_init and find_attribute.kind == 'mutable': raise IllegalConstantExpression(ast)
            print("\n pass instance field access")
            return find_attribute.type_data
        raise TypeMismatchInExpression(ast)

    def visitIntLiteral(self, ast, o):
        return IntType()
    
    def visitFloatLiteral(self, ast, o):
        return FloatType()
    
    def visitStringLiteral(self, ast, o):
        return StringType()
    
    def visitBooleanLiteral(self, ast, o):
        return BoolType()
    
    def visitNullLiteral(self, ast, o):
        return NullLiteral()
    
    def visitSelfLiteral(self, ast, o):
        return SelfLiteral()
    
    def visitArrayLiteral(self, ast: ArrayLiteral, o):
        value_list = [self.visit(each_value, o) for each_value in ast.value]
        print("\nvisitArrayLiteral")
        for each_value in value_list:
            print("type each_value and value[0]: ", type(each_value), type(value_list[0]))
            # if type(each_value) != type(value_list[0]):
            if type_compare(each_value, value_list[0]) == False:
                raise IllegalArrayLiteral(ast)
        print("\nvalue list: ", value_list)
        return ArrayType(len(value_list), value_list[0])
    
    def visitAssign(self, ast: Assign, o):
        print("\nvisitAssign")
        in_loop, o = o
        rhs = self.visit(ast.exp, o)
        lhs = self.visit(ast.lhs, o)
        if isinstance(lhs, Symbol):
            if lhs.kind == 'immutable' or lhs.kind == 'constant': raise CannotAssignToConstant(ast)
            lhs = lhs.type_data
        if isinstance(rhs, Symbol):
            rhs = rhs.type_data
        if type_compare(lhs, rhs) == False and type_inference(lhs, rhs, self.list_inherit) == False:
            raise TypeMismatchInStatement(ast)
        print("\nrhs and lhs: ", rhs, lhs)
        
    def visitIf(self, ast: If, o):
        temp = o    
        if len(o) == 2:
            in_loop, o = o
        
        conditional_expr = self.visit(ast.expr, o)
        if not isinstance(conditional_expr, BoolType): raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, temp)
        if len(temp[1]['local']) != 0:      # after visit thenStmt, pop local
            temp[1]['local'].pop(0) # 
        temp[1]['local'] = [{}] + temp[1]['local']
        if ast.elseStmt:
            self.visit(ast.elseStmt, temp)
    
    def visitFor(self, ast: For, o):
        print("\nvisitFor")
        in_loop, o = o
        in_loop = True
        
        id = self.visit(ast.id, o)
        expr1 = self.visit(ast.expr1, o)
        expr2 = self.visit(ast.expr2, o)
        expr3 = self.visit(ast.expr3, o) if ast.expr3 else None
        
        if id.kind == 'immutable' or id.kind == 'constant':
            raise CannotAssignToConstant(ast.expr1)
        
        if isinstance(expr1, Symbol): expr1 = expr1.type_data
        if isinstance(expr2, Symbol): expr2 = expr2.type_data
        if isinstance(expr3, Symbol): expr2 = expr3.type_data
        
        if not isinstance(id.type_data, IntType) and not isinstance(id.type_data, FloatType):
            raise TypeMismatchInStatement(ast)
        if not isinstance(expr1, IntType) or not isinstance(expr2, IntType):
            raise TypeMismatchInStatement(ast)
        if expr3 and not isinstance(expr3, IntType):
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.loop, (in_loop, o))
        
    
    def visitBreak(self, ast, o):
        in_loop, o = o
        if in_loop == False:
            raise MustInLoop(ast)
    
    def visitContinue(self, ast, o):
        in_loop, o = o
        if in_loop == False:
            raise MustInLoop(ast)
    
    def visitReturn(self, ast: Return, o):
        in_loop, o = o
            
        print("\n visitReturn")
        
        expr = self.visit(ast.expr, o) if ast.expr else None
        current_class = o['current_class']
        current_method = o['current_method']
        if current_method == 'main' and current_class == 'Program' and expr:
            raise TypeMismatchInStatement(ast)
        if current_method == 'Destructor':
            raise TypeMismatchInStatement(ast)
        if expr is None: expr = VoidType()
        if isinstance(expr, Symbol): expr = expr.type_data
        
        method_return_type = o['global'][current_class][current_method].type_data
        if method_return_type is None:
            o['global'][current_class][current_method].type_data =  expr
        else:
            if not type_compare(expr, method_return_type) and not type_inference(method_return_type, expr, self.list_inherit):
                raise TypeMismatchInStatement(ast)
    
    def visitCallStmt(self, ast: CallStmt, o):
        print("\visitCallStmt")
        in_loop, o = o
        
        
        method = ast.method.name
        args_list = [self.visit(each_param, temp) for each_param in ast.param]

        # static method invocation
        if isinstance(ast.obj, Id) and method[0] == '$':
            print("\nstatic method invoke")
            class_name = ast.obj.name
            if class_name not in o['global']: raise Undeclared(Class(), class_name)
            lookup_method = lookup_attribute(method, class_name, o, self.list_inherit)
            if not lookup_method: raise Undeclared(Method(), method)
            if not isinstance(lookup_method.static_or_instance, Static): raise IllegalMemberAccess(ast)
            if lookup_method.kind != 'method': raise Undeclared(Method(), method)
            if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                raise TypeMismatchInStatement(ast)
            print("\n pass static method invoke")
            return
        
        # instance method invocation
        obj = self.visit(ast.obj, temp)
        if isinstance(obj.type_data, ClassType):
            print("\ninstance method invoke")
            lookup_method = lookup_attribute(method, obj.type_data.classname.name, o, self.list_inherit)
            if not lookup_method: raise Undeclared(Method(), method)
            if not isinstance(lookup_method.static_or_instance, Instance): raise IllegalMemberAccess(ast)
            if lookup_method.kind != 'method': raise Undeclared(Method(), method)
            if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                raise TypeMismatchInStatement(ast)
            print("\npassinstance method invoke")
            return
            
        raise TypeMismatchInExpression(ast)
    
    def visitAttributeDecl(self, ast: AttributeDecl, o):
        o['out_or_in_method'] = 'out'
        print("o visitAttributeDecl: ", o)
        self.visit(ast.decl, (ast.kind, o))
        o['out_or_in_method'] = 'none'     # reset after 
    
    def visitMethodDecl(self, ast: MethodDecl, o):
        kind = self.visit(ast.kind, o)  # kind: Static or Instance method
        name = ast.name.name
        
        o['current_method'] = name
        
        # check redeclare method
        current_class = o['current_class']
        if name in o['global'][current_class]:
            raise Redeclared(Method(), name)
        param_type_list = [self.visit(each_param.varType, o) for each_param in ast.param]
        o['global'][current_class][name] = Symbol(name, 'method', kind, None, param_type_list)
        

        o['local'] = [{}] + o['local']
        in_loop = False
        
        # Check param --> inside method
        for each_param in ast.param:
            o['out_or_in_method'] = 'in'
            self.visit(each_param, (Parameter(), o))
        
        # Check block
        self.visit(ast.body, (in_loop, o))
        

        o['local'] = []   # reset after finishing visit 1 method --> local empty
        o['current_method'] = '-1'
    
    def visitVarDecl(self, ast: VarDecl, kind_and_o):
        # kind: Attribute(Static, Instance); Local(Param, Variable)
        kind, o = kind_and_o
        variable = ast.variable.name
        var_type = self.visit(ast.varType, o)
        var_init = self.visit(ast.varInit, o) if ast.varInit else None

        # if var_type != var_init: pass             # should check ???
        
        if o['out_or_in_method'] == 'out':          # check attribute outside method
            current_class = o['current_class']
            if variable in o['global'][current_class]:
                raise Redeclared(Attribute(), variable)
            o['global'][current_class][variable] = Symbol(variable, 'mutable', kind, var_type)  # kind: Static or Instance
            print("\no['global'][current_class][variable]: ", o['global'][current_class][variable])
            o['out_or_in_method'] == 'none'         # reset
            
        if o['out_or_in_method'] == 'in':           # check param and variable inside method
            if variable in o['local'][0]:
                raise Redeclared(kind, variable)    # kind: Param or Variable
            o['local'][0][variable] = Symbol(variable, 'variable', None, var_type)      # 'None' cuz inside method, not check Static or Instance ---> always instance, not dollar ID
            print("\no['local'][0][variable]: ", o['local'][0][variable])
            o['out_or_in_method'] = 'none'          # reset
    
    def visitConstDecl(self, ast: ConstDecl, kind_and_o):
        # constant not initialize
        if ast.value is None: raise IllegalConstantExpression(ast.value)
        
        # kind: Attribute(Static, Instance); Local(Constant)
        kind, o = kind_and_o
        constant = ast.constant.name
        const_type = self.visit(ast.constType, o)
        # value = self.visit(ast.value, o) if ast.value else None
        flag_const_init = True
        value = self.visit(ast.value, (flag_const_init, o)) if ast.value else None

        if o['out_or_in_method'] == 'out':          # check attribute outside method
            current_class = o['current_class']
            if constant in o['global'][current_class]:
                raise Redeclared(Attribute(), constant)
            o['global'][current_class][constant] = Symbol(constant, 'immutable', kind, const_type)      # kind: Static or Instance
            o['out_or_in_method'] == 'none'         # reset
            
        if o['out_or_in_method'] == 'in':           # check constant inside method
            if constant in o['local'][0]:
                raise Redeclared(kind, constant)    # kind: Constant
            o['local'][0][constant] = Symbol(constant, 'constant', None, const_type)    # inside method, not check Static or Instance ---> always instance, not dollar ID
            o['out_or_in_method'] == 'none'         # reset
            
    def visitBlock(self, ast: Block, inloop_scope):
        print("\no BEFORE visitBlock: ", inloop_scope)
        in_loop, o = inloop_scope
        for each_inst in ast.inst:
            o['out_or_in_method'] = 'in'
            if isinstance(each_inst, VarDecl): self.visit(each_inst, (Variable(), o))
            elif isinstance(each_inst, ConstDecl): self.visit(each_inst, (Constant(), o))
            else:
                o['local'] = [{}] + o['local']      # only useful cho IfStmt, BlockStmt,, ForStmt
                self.visit(each_inst, (in_loop, o))
                o['local'].pop(0)   
        print("\no AFTER visitBlock:", o, "\n")

    
    def visitInstance(self, ast: Instance, o):
        return Instance()
    
    def visitStatic(self, ast: Static, o):
        return Static()
    
    def visitIntType(self, ast, o):
        return IntType()
    
    def visitFloatType(self, ast, o):
        return FloatType()
    
    def visitBoolType(self, ast, o):
        return BoolType()
    
    def visitClassDecl(self, ast, o):
        
        class_name = ast.classname.name
        parent_name = ast.parentname.name if ast.parentname else None
        
        print("visitClassDecl: ", class_name, " ", "\t", "parent name: ", parent_name, "\n")
        print("o BEFORE visitClassDecl: ", o, "\n")
        
        if class_name in o['global']:     # check redeclare class
            raise Redeclared(Class(), class_name)
        
        if parent_name:    # check parent name whether has been declared
            if parent_name not in o['global']:
                raise Undeclared(Class(), parent_name)
            self.list_inherit[class_name] = parent_name     # update list inheritance of the class
        else: self.list_inherit[class_name] = None
        
        o['current_class'] = class_name
        o['global'][class_name] = {}        # init scope for current class
        
        
        check_no_entry_point = True if ast.classname.name == 'Program' else False

        for each_mem in ast.memlist:
            self.visit(each_mem, o)

            # meet main() method with params --> break immediately because No Entry Point
            if ast.classname.name == 'Program' and isinstance(each_mem, MethodDecl) and each_mem.name.name == 'main' and len(each_mem.param) != 0:
                break
            
            if ast.classname.name == 'Program' and isinstance(each_mem, MethodDecl) and each_mem.name.name == 'main' and len(each_mem.param) == 0:
                check_no_entry_point = False


        o['current_class'] = '-1'       # reset, finishing visit current class
       
        
        print("o AFTER visitClassDecl", class_name, "AFTER: ", o, "\n")

        return check_no_entry_point
    
    def visitStringType(self, ast, o):
        return StringType()
    
    def visitArrayType(self, ast: ArrayType, o):
        print("\nvisitArrayType")
        return ArrayType(ast.size, ast.eleType)
    
    def visitClassType(self, ast: ClassType, o):
        print("\nvisitClassType")
        if ast.classname.name in o['global']:
            return ClassType(ast.classname)
        raise Undeclared(Class(), ast.classname.name)
    
    def visitVoidType(self, ast: VoidType, o):
        return VoidType()

    def visitProgram(self, ast: Program, o):
        global_env = {}
        global_env['global'] = {}
        global_env['local'] = []
        global_env['current_class'] = '-1'
        global_env['current_method'] = '-1'
        global_env['out_or_in_method'] = 'none' # attribute decl or variable and cons decl (inside method)
        
        check_have_program_class = False
        for each_class in ast.decl:
            check_no_entry_point = self.visit(each_class, global_env)
            if each_class.classname.name == 'Program':
                check_have_program_class = True
            if check_no_entry_point:
                raise NoEntryPoint()
        
        if check_have_program_class == False:       # no program class
            raise NoEntryPoint()


"""
 * @author Vo Nguyen Thien Nhan 1910409
"""
from AST import * 
from Visitor import *
from StaticError import *

## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##
from main.d96.utils.AST import *
from main.d96.parser.D96Parser import D96Parser
from main.d96.parser.D96Visitor import D96Visitor
from StaticError import *
## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##

def lookup_attribute (attri_name, class_name, global_scope, list_inherit):
    current_class = class_name
    while current_class:
        if attri_name in global_scope['global'][current_class]:
            return global_scope['global'][current_class][attri_name]    # return Symbol
        current_class = list_inherit[current_class]
    return None

def type_inference (lhs, rhs, list_inherit):
    if isinstance(lhs, FloatType) and isinstance(rhs, IntType): return True
    
    if isinstance(lhs, ClassType) and isinstance(rhs, ClassType):
        parent_class = list_inherit[rhs.classname.name]
        while (parent_class):
            if lhs.classname.name == parent_class: return True
            parent_class = list_inherit[parent_class]
    
    if isinstance(lhs, ClassType) and isinstance(rhs, NullLiteral): return True
            
    if isinstance(lhs, ArrayType) and isinstance(rhs, ArrayType):
        return lhs.size == rhs.size and type_inference(lhs.eleType, rhs.eleType, list_inherit)
    return False

def type_compare (first, second):
    # print("\nfirst, second: ", first, second)
    if isinstance(first, ClassType) and isinstance(second, ClassType):
        return first.classname.name == second.classname.name
    if isinstance(first, ArrayType) and isinstance(second, ArrayType):
        return first.size == second.size and type_compare(first.eleType, second.eleType)
    return type(first) == type(second)

def type_params_and_args_list (params, args, list_inherit):
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

class StaticChecker(BaseVisitor):
    
    # def __init__(self,ast):
    #     self.ast = ast

    # def check(self):
    #     return self.visit(self.ast,StaticChecker.global_envi)
    
    def __init__(self,ast):
        self.ast = ast
        self.list_inherit = {}
        
    def check(self):
        return self.visit(self.ast, None)
    
    def visitId(self, ast: Id, o):
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
            if (isinstance(left, IntType) and isinstance(right, IntType)) or (isinstance(left, BoolType) and isinstance(right, BoolType)):
                return BoolType()
            raise TypeMismatchInExpression(ast)
    
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
    
    def visitCallExpr(self, ast: CallExpr, o):
        temp = o
        flag_const_init = None
        if len(o) == 2:
            flag_const_init, o = o
        
        if flag_const_init: raise IllegalConstantExpression(ast)
        
        method = ast.method.name
        args_list = [self.visit(each_param, temp) for each_param in ast.param]
        
        # Self call
        if isinstance(ast.obj, SelfLiteral):
            current_class = o['current_class']     
            current_method = o['current_method'] 
            if current_method != '-1' and isinstance(o['global'][current_class][current_method].static_or_instance, Static): 
                raise IllegalMemberAccess(ast)
            lookup_method = lookup_attribute(method, current_class, o, self.list_inherit)
            if not lookup_method: raise Undeclared(Method(), method)
            if not isinstance(lookup_method.static_or_instance, Instance): raise IllegalMemberAccess(ast)
            if lookup_method.kind != 'method': raise Undeclared(Method(), method)
            if isinstance(lookup_method.type_data, VoidType): raise TypeMismatchInExpression(ast)
            if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                raise TypeMismatchInExpression(ast)
            return lookup_method.type_data

        # static method invocation
        # if isinstance(ast.obj, Id) and method[0] == '$':
        #     print("\nstatic method invoke")
        #     class_name = ast.obj.name
        #     if class_name not in o['global']: raise Undeclared(Class(), class_name)
        #     lookup_method = lookup_attribute(method, class_name, o, self.list_inherit)
        #     if not lookup_method: raise Undeclared(Method(), method)
        #     if not isinstance(lookup_method.static_or_instance, Static): raise IllegalMemberAccess(ast)
        #     if lookup_method.kind != 'method': raise Undeclared(Method(), method)
        #     if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
        #         raise TypeMismatchInExpression(ast)
        #     print("\n pass static method invoke")
        #     return lookup_method.type_data
        
        if isinstance(ast.obj, Id):
            if method[0] == '$':
                # example: A is local variable and has class A, A::$func()
                class_name = ast.obj.name
                if class_name not in o['global']:       # not find class
                    # find in local
                    lookup_local = None
                    for each_local in o['local']:
                        if class_name in each_local:
                            lookup_local = each_local[class_name]
                            break
                    if lookup_local: raise IllegalMemberAccess(ast)     # A is local var --> error
                    raise Undeclared(Class(), class_name)       # don't have local var A --> undeclare class
                
                # has class name
                lookup_method = lookup_attribute(method, class_name, o, self.list_inherit)
                if not lookup_method: raise Undeclared(Method(), method)
                if not isinstance(lookup_method.static_or_instance, Static): raise IllegalMemberAccess(ast)
                if lookup_method.kind != 'method': raise Undeclared(Method(), method)
                if isinstance(lookup_method.type_data, VoidType): raise TypeMismatchInStatement(ast)
                if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                    raise TypeMismatchInExpression(ast)
                return lookup_method.type_data

            # example: A is local variable and has class A, A.attri
            lookup_local = None
            obj_name = ast.obj.name
            for each_local in o['local']:
                if obj_name in each_local:
                    lookup_local = each_local[obj_name]     # return Symbol
                    break
            if lookup_local:        # has variable type object
                if isinstance(lookup_local.type_data, ClassType):
                    class_name = lookup_local.type_data.classname.name
                    lookup_method = lookup_attribute(method, class_name, o, self.list_inherit)
                    if not lookup_method: raise Undeclared(Method(), method)
                    if not isinstance(lookup_method.static_or_instance, Instance): raise IllegalMemberAccess(ast)
                    if lookup_method.kind != 'method': raise Undeclared(Method(), method)
                    if isinstance(lookup_method.type_data, VoidType): raise TypeMismatchInStatement(ast)
                    if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                        raise TypeMismatchInExpression(ast)
                    return lookup_method.type_data
                else:
                    raise TypeMismatchInExpression(ast)
            if obj_name in o['global']:     # is class name
                raise IllegalMemberAccess(ast)
            raise Undeclared(Identifier(), obj_name)
        
        # instance method invocation    
        obj = self.visit(ast.obj, temp)     # Symbol
        if isinstance(obj.type_data, ClassType):
            lookup_method = lookup_attribute(method, obj.type_data.classname.name, o, self.list_inherit)
            if not lookup_method: raise Undeclared(Method(), method)
            if not isinstance(lookup_method.static_or_instance, Instance): raise IllegalMemberAccess(ast)
            if lookup_method.kind != 'method': raise Undeclared(Method(), method)
            if isinstance(lookup_method.type_data, VoidType): raise TypeMismatchInStatement(ast)
            if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                raise TypeMismatchInExpression(ast)
            return lookup_method.type_data
        raise TypeMismatchInExpression(ast)
    
    def visitNewExpr(self, ast: NewExpr, o):
        flag_const_init = None
        if len(o) == 2:
            flag_const_init, o = o
        
        class_name = ast.classname.name
        if class_name not in o['global']:
            raise Undeclared(Class(), class_name)
        
        if len(ast.param) != 0:
            if 'Constructor' in o['global'][class_name]:
                method_constructor = o['global'][class_name]['Constructor']     # return Symbol
                args = [self.visit(each_arg, o) for each_arg in ast.param]
                if type_params_and_args_list(method_constructor.param_type_list, args, self.list_inherit) == False:
                    raise TypeMismatchInExpression(ast)
            else:
                raise Undeclared(Method(), 'Constructor')
        
        return ClassType(ast.classname)
    
    def visitArrayCell(self, ast: ArrayCell, o):
        temp = o
        flag_const_init = None
        if len(o) == 2:
            flag_const_init, o = o
            
        arr = self.visit(ast.arr, temp)     # visitID, return Symbol
        
        name, kind = None, None
        if isinstance(arr, Symbol):
            name = arr.name
            kind = arr.kind

        idx_list = [self.visit(each_idx, temp) for each_idx in ast.idx]
        
        for each_idx in idx_list:
            if isinstance(arr, Symbol): arr = arr.type_data
            if isinstance(each_idx, Symbol): each_idx = each_idx.type_data
            if not isinstance(arr, ArrayType): raise TypeMismatchInExpression(ast)
            if not isinstance(each_idx, IntType): raise TypeMismatchInExpression(ast)
            arr = arr.eleType
        return Symbol(name, kind, None, arr)
    
    def visitFieldAccess(self, ast: FieldAccess, o):
        temp = o
        flag_const_init = None
        if len(o) == 2:
            flag_const_init, o = o
        
        field_name = ast.fieldname.name

        # Self access
        if isinstance(ast.obj, SelfLiteral):
            class_name = o['current_class']     
            current_method = o['current_method'] 
            if current_method != '-1' and isinstance(o['global'][class_name][current_method].static_or_instance, Static): 
                raise IllegalMemberAccess(ast)
            find_attribute = lookup_attribute(field_name, class_name, o, self.list_inherit)
            if not find_attribute: raise Undeclared(Attribute(), field_name)
            if not isinstance(find_attribute.static_or_instance, Instance): raise IllegalMemberAccess(ast)      # should add ??
            if find_attribute.kind == 'method': raise Undeclared(Attribute(), field_name)
            if flag_const_init and find_attribute.kind == 'mutable': raise IllegalConstantExpression(ast)
            return find_attribute
        
        # static field access
        # if isinstance(ast.obj, Id) and field_name[0] == '$':
        #     print("\n static field access")
        #     class_name = ast.obj.name
        #     if class_name not in o['global']: raise Undeclared(Class(), class_name)
        #     find_attribute = lookup_attribute(field_name, class_name, o, self.list_inherit)
        #     if not find_attribute: raise Undeclared(Attribute(), field_name)
        #     if not isinstance(find_attribute.static_or_instance, Static): raise IllegalMemberAccess(ast)
        #     if find_attribute.kind == 'method': raise Undeclared(Attribute(), field_name)
        #     if flag_const_init and find_attribute.kind == 'mutable': raise IllegalConstantExpression(ast)
        #     print("\n pass static field access")
        #     # return find_attribute.type_data
        #     return find_attribute
        
        if isinstance(ast.obj, Id):
            if field_name[0] == '$':
                # example: A is local variable and has class A, A::$attri
                class_name = ast.obj.name
                if class_name not in o['global']:       # not find class
                    # find in local
                    lookup_local = None
                    for each_local in o['local']:
                        if class_name in each_local:
                            lookup_local = each_local[class_name]
                            break
                    if lookup_local: raise IllegalMemberAccess(ast)     # A is local var --> error
                    raise Undeclared(Class(), class_name)       # don't have local var A --> undeclare class
                
                # has class name
                find_attribute = lookup_attribute(field_name, class_name, o, self.list_inherit)
                if not find_attribute: raise Undeclared(Attribute(), field_name)
                if not isinstance(find_attribute.static_or_instance, Static): raise IllegalMemberAccess(ast)
                if find_attribute.kind == 'method': raise Undeclared(Attribute(), field_name)
                if flag_const_init and find_attribute.kind == 'mutable': raise IllegalConstantExpression(ast)
                return find_attribute

            # example: A is local variable and has class A, A.attri
            lookup_local = None
            obj_name = ast.obj.name
            for each_local in o['local']:
                if obj_name in each_local:
                    lookup_local = each_local[obj_name]     # return Symbol
                    break
            if lookup_local:        # has variable type object
                if isinstance(lookup_local.type_data, ClassType):
                    class_name = lookup_local.type_data.classname.name
                    find_attribute = lookup_attribute(field_name, class_name, o, self.list_inherit)
                    if not find_attribute: raise Undeclared(Attribute(), field_name)
                    if not isinstance(find_attribute.static_or_instance, Instance): raise IllegalMemberAccess(ast)
                    if find_attribute.kind == 'method': raise Undeclared(Attribute(), field_name)
                    if flag_const_init and find_attribute.kind == 'mutable': raise IllegalConstantExpression(ast)
                    return find_attribute
                else:
                    raise TypeMismatchInExpression(ast)
            if obj_name in o['global']:     # is class name
                raise IllegalMemberAccess(ast)
            raise Undeclared(Identifier(), obj_name)
        
        # instance field access
        obj = self.visit(ast.obj, temp)     # Symbol
        if isinstance(obj.type_data, ClassType):
            class_name = obj.type_data.classname.name
            find_attribute = lookup_attribute(field_name, class_name, o, self.list_inherit)
            if not find_attribute: raise Undeclared(Attribute(), field_name)
            if not isinstance(find_attribute.static_or_instance, Instance): raise IllegalMemberAccess(ast)
            if find_attribute.kind == 'method': raise Undeclared(Attribute(), field_name)
            if flag_const_init and find_attribute.kind == 'mutable': raise IllegalConstantExpression(ast)
            # return find_attribute.type_data
            return find_attribute
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
        for each_value in value_list:
            if type_compare(each_value, value_list[0]) == False:
                raise IllegalArrayLiteral(ast)
        return ArrayType(len(value_list), value_list[0])
    
    def visitAssign(self, ast: Assign, o):
        in_loop, o = o
        rhs = self.visit(ast.exp, o)
        lhs = self.visit(ast.lhs, o)
        if isinstance(lhs, Symbol):
            if lhs.kind == 'immutable' or lhs.kind == 'constant': 
                raise CannotAssignToConstant(ast)
            lhs = lhs.type_data
        if isinstance(rhs, Symbol):
            rhs = rhs.type_data
        if type_compare(lhs, rhs) == False and type_inference(lhs, rhs, self.list_inherit) == False:
            raise TypeMismatchInStatement(ast)
        
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
        in_loop, o = o
        
        method = ast.method.name
        args_list = [self.visit(each_param, o) for each_param in ast.param]
        
        # Self call
        if isinstance(ast.obj, SelfLiteral):
            current_class = o['current_class']     
            current_method = o['current_method'] 
            if current_method != '-1' and isinstance(o['global'][current_class][current_method].static_or_instance, Static): 
                raise IllegalMemberAccess(ast)
            lookup_method = lookup_attribute(method, current_class, o, self.list_inherit)
            if not lookup_method: raise Undeclared(Method(), method)
            if not isinstance(lookup_method.static_or_instance, Instance): raise IllegalMemberAccess(ast)
            if lookup_method.kind != 'method': raise Undeclared(Method(), method)
            if isinstance(lookup_method.type_data, VoidType): raise TypeMismatchInExpression(ast)
            if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                raise TypeMismatchInExpression(ast)
            return

        if isinstance(ast.obj, Id):
            if method[0] == '$':
                # example: A is local variable and has class A, A::$func()
                class_name = ast.obj.name
                if class_name not in o['global']:       # not find class
                    # find in local
                    lookup_local = None
                    for each_local in o['local']:
                        if class_name in each_local:
                            lookup_local = each_local[class_name]
                            break
                    if lookup_local: raise IllegalMemberAccess(ast)     # A is local var --> error
                    raise Undeclared(Class(), class_name)       # don't have local var A --> undeclare class
                
                # has class name
                lookup_method = lookup_attribute(method, class_name, o, self.list_inherit)
                if not lookup_method: raise Undeclared(Method(), method)
                if not isinstance(lookup_method.static_or_instance, Static): raise IllegalMemberAccess(ast)
                if lookup_method.kind != 'method': raise Undeclared(Method(), method)
                if isinstance(lookup_method.type_data, VoidType): raise TypeMismatchInStatement(ast)
                if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                    raise TypeMismatchInExpression(ast)
                return

            # example: A is local variable and has class A, A.attri
            lookup_local = None
            obj_name = ast.obj.name
            for each_local in o['local']:
                if obj_name in each_local:
                    lookup_local = each_local[obj_name]     # return Symbol
                    break
            if lookup_local:        # has variable type object
                if isinstance(lookup_local.type_data, ClassType):
                    class_name = lookup_local.type_data.classname.name
                    lookup_method = lookup_attribute(method, class_name, o, self.list_inherit)
                    if not lookup_method: raise Undeclared(Method(), method)
                    if not isinstance(lookup_method.static_or_instance, Instance): raise IllegalMemberAccess(ast)
                    if lookup_method.kind != 'method': raise Undeclared(Method(), method)
                    if isinstance(lookup_method.type_data, VoidType): raise TypeMismatchInStatement(ast)
                    if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                        raise TypeMismatchInExpression(ast)
                    return
                else:
                    raise TypeMismatchInExpression(ast)
            if obj_name in o['global']:     # is class name
                raise IllegalMemberAccess(ast)
            raise Undeclared(Identifier(), obj_name)
        
        # instance method invocation    
        obj = self.visit(ast.obj, o)     # Symbol
        if isinstance(obj.type_data, ClassType):
            lookup_method = lookup_attribute(method, obj.type_data.classname.name, o, self.list_inherit)
            if not lookup_method: raise Undeclared(Method(), method)
            if not isinstance(lookup_method.static_or_instance, Instance): raise IllegalMemberAccess(ast)
            if lookup_method.kind != 'method': raise Undeclared(Method(), method)
            if isinstance(lookup_method.type_data, VoidType): raise TypeMismatchInStatement(ast)
            if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
                raise TypeMismatchInExpression(ast)
            # return lookup_method.type_data
            return
        raise TypeMismatchInExpression(ast)
    
    

        # # static method invocation
        # if isinstance(ast.obj, Id) and method[0] == '$':
        #     print("\nstatic method invoke")
        #     class_name = ast.obj.name
        #     if class_name not in o['global']: raise Undeclared(Class(), class_name)
        #     lookup_method = lookup_attribute(method, class_name, o, self.list_inherit)
        #     if not lookup_method: raise Undeclared(Method(), method)
        #     if not isinstance(lookup_method.static_or_instance, Static): raise IllegalMemberAccess(ast)
        #     if lookup_method.kind != 'method': raise Undeclared(Method(), method)
        #     if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
        #         raise TypeMismatchInStatement(ast)
        #     print("\n pass static method invoke")
        #     return
        
        # # instance method invocation
        # obj = self.visit(ast.obj, temp)
        # if isinstance(obj.type_data, ClassType):
        #     print("\ninstance method invoke")
        #     lookup_method = lookup_attribute(method, obj.type_data.classname.name, o, self.list_inherit)
        #     if not lookup_method: raise Undeclared(Method(), method)
        #     if not isinstance(lookup_method.static_or_instance, Instance): raise IllegalMemberAccess(ast)
        #     if lookup_method.kind != 'method': raise Undeclared(Method(), method)
        #     if not type_params_and_args_list(lookup_method.param_type_list, args_list, self.list_inherit):
        #         raise TypeMismatchInStatement(ast)
        #     print("\npassinstance method invoke")
        #     return
            
        # raise TypeMismatchInExpression(ast)
    
    def visitAttributeDecl(self, ast: AttributeDecl, o):
        o['out_or_in_method'] = 'out'
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
            o['out_or_in_method'] == 'none'         # reset
            
        if o['out_or_in_method'] == 'in':           # check param and variable inside method
            if variable in o['local'][0]:
                raise Redeclared(kind, variable)    # kind: Param or Variable
            o['local'][0][variable] = Symbol(variable, 'variable', None, var_type)      # 'None' cuz inside method, not check Static or Instance ---> always instance, not dollar ID
            o['out_or_in_method'] = 'none'          # reset
            
        if var_init:    # check data type declared and type of init value
            if isinstance(var_init, Symbol):
                var_init = var_init.type_data
            if not type_compare(var_type, var_init) and not type_inference(var_type, var_init, self.list_inherit):
                raise TypeMismatchInStatement(ast)
    
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
            
        if value:
            if isinstance(value, Symbol):
                value = value.type_data
            if not type_compare(const_type, value) and not type_inference(const_type, value, self.list_inherit):
                raise TypeMismatchInConstant(ast)
            
    def visitBlock(self, ast: Block, inloop_scope):
        in_loop, o = inloop_scope
        for each_inst in ast.inst:
            o['out_or_in_method'] = 'in'
            if isinstance(each_inst, VarDecl): self.visit(each_inst, (Variable(), o))
            elif isinstance(each_inst, ConstDecl): self.visit(each_inst, (Constant(), o))
            else:
                o['local'] = [{}] + o['local']      # only useful cho IfStmt, BlockStmt,, ForStmt
                self.visit(each_inst, (in_loop, o))
                o['local'].pop(0)   

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

        return check_no_entry_point
    
    def visitStringType(self, ast, o):
        return StringType()
    
    def visitArrayType(self, ast: ArrayType, o):
        return ArrayType(ast.size, ast.eleType)
    
    def visitClassType(self, ast: ClassType, o):
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

    
    


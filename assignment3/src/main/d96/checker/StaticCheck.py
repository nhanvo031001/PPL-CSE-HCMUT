from cmath import exp
from xml.dom.minidom import NamedNodeMap
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

class Symbol:
    def __init__(self, name, kind, static_or_instance, type_data, param_type_list = None):
        self.name = name
        self.kind = kind
        self.static_or_instance = static_or_instance
        self.type_data = type_data
        self.param_type_list = param_type_list
    
    def __str__(self):
        return "Symbol" + "("+ str(self.name) + ", " + str(self.kind) + ", " + str(self.static_or_instance) + ", " +str(self.type_data)  + (", " + str(self.paramparam_type_list_type) if self.param_type_list else "") + ")"

class StaticChecker(BaseVisitor,Utils):

    def __init__(self,ast):
        self.ast = ast
        self.list_inherit = {}
        
    def check(self):
        return self.visit(self.ast, None)
    
    def visitId(self, ast: Id, o):
        print("\no in visitId: ", o)
        
        const_decl = None
        if len(o) == 2:
            const_decl, o = o
        
        # check local
        for each_local in o['local']:
            if ast.name in each_local:
                if const_decl and (each_local[ast.name].kind == 'mutable' or each_local[ast.name].kind == 'variable'):
                    raise IllegalConstantExpression(ast)
                return each_local[ast.name]     # return Symbol
        
        lookup_attri = lookup_attribute(ast.name, o['current_class'], o, self.list_inherit)
        # print("lookup_attri: ", lookup_attri)
        if lookup_attri: 
            if const_decl and (lookup_attri.kind == 'mutable' or lookup_attri.kind == 'variable'):
                raise IllegalConstantExpression(ast)
            return lookup_attri     # return Symbol
        raise Undeclared(Identifier(), ast.name)
    
    def visitBinaryOp(self, ast: BinaryOp, o):
        op = ast.op
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o)
        
        if op in ['+', '-', '*', '/']:
            if isinstance(left, IntType) and isinstance(right, IntType): return IntType()
            if isinstance(left, FloatType) or isinstance(right, FloatType): return FloatType()
            raise TypeMismatchInExpression(ast)
        
        if op == '%':
            if isinstance(left, IntType) and isinstance(right, IntType): return IntType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['&&', '||']:
            if isinstance(left, BoolType) and isinstance(right, BoolType): return BoolType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['==.', '+.']:
            if isinstance(left, StringType) and isinstance(right, StringType): return StringType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['<', '>', '<=', '>=']:
            if not (isinstance(left, IntType) or isinstance(left, FloatType)) or not (isinstance(right, IntType) or isinstance(right, FloatType)): 
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if op in ['==', '!=']:
            if not (isinstance(left, IntType) or isinstance(left, BoolType)) or not (isinstance(right, IntType) or isinstance(right, BoolType)): 
                raise TypeMismatchInExpression(ast)
            return BoolType()
    
    def visitUnaryOp(self, ast: UnaryOp, o):    # return data type
        print("2 param: ", o)
        
        flag_const_init = None
        if len(o) == 2:
            flag_const_init, o = o
            
        op = ast.op
        exp_type_data = self.visit(ast.body, o)
        
        print("\n o in visitUnaryOp: ", o)
        print("\n exp_type_data: ", exp_type_data)
        
        if isinstance(exp_type_data, Symbol):   # ID
            
            if flag_const_init and (exp_type_data.kind == 'mutable' or exp_type_data.kind == 'variable'):
                raise IllegalConstantExpression(ast)
        print("\n body type of exp: ", exp_type_data)
        if isinstance(exp_type_data, Symbol):
            exp_type_data = exp_type_data.type_data
        
        print("\n body type of exp: ", exp_type_data)
        
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
        pass
    
    def visitNewExpr(self, ast: NewExpr, o):
        pass
    
    def visitArrayCell(self, ast: ArrayCell, o):
        pass
    
    def visitFieldAccess(self, ast: FieldAccess, o):
        pass

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
        pass
    
    def visitAssign(self, ast: Assign, o):
        pass
    
    def visitIf(self, ast: If, o):
        pass
    
    def visitFor(self, ast: For, o):
        pass
    
    def visitBreak(self, ast, o):
        return
    
    def visitContinue(self, ast, o):
        return
    
    def visitReturn(self, ast: Return, o):
        pass
    
    def visitCallStmt(self, ast: CallStmt, o):
        pass
    
    def visitAttributeDecl(self, ast: AttributeDecl, o):
        o['out_or_in_method'] = 'out'
        print("o visitAttributeDecl: ", o)
        self.visit(ast.decl, (ast.kind, o))
        o['out_or_in_method'] = 'none'     # reset after 
    
    def visitMethodDecl(self, ast: MethodDecl, o):
        kind = self.visit(ast.kind, o)
        name = ast.name.name
        
        # check redeclare method
        current_class = o['current_class']
        if name in o['global'][current_class]:
            raise Redeclared(Method(), name)
        param_type_list = [self.visit(each_param.varType, o) for each_param in ast.param]
        o['global'][current_class][name] = Symbol(name, 'method', kind, None, param_type_list)
        

        o['local'] = [{}] + o['local']
        in_loop = False
        method_name = name
        
        # Check param --> inside method
        for each_param in ast.param:
            o['out_or_in_method'] = 'in'
            self.visit(each_param, (Parameter(), o))
        
        # Check block
        self.visit(ast.body, (in_loop, method_name, o))
        
        o['local'] = []   # reset after finishing visit 1 method --> local empty
    
    def visitVarDecl(self, ast: VarDecl, kind_and_o):

        static_inst_param_var, o = kind_and_o
        variable = ast.variable.name
        var_type = self.visit(ast.varType, o)
        var_init = self.visit(ast.varInit, o) if ast.varInit else None
        
        print("var_type: ", var_type)
        # if var_type != var_init: pass             # should check ???
        
        if o['out_or_in_method'] == 'out':          # check attribute outside method
            current_class = o['current_class']
            if variable in o['global'][current_class]:
                raise Redeclared(Attribute(), variable)
            o['global'][current_class][variable] = Symbol(variable, 'mutable', static_inst_param_var, var_type)
            o['out_or_in_method'] == 'none'         # reset
            
        if o['out_or_in_method'] == 'in':           # check variable and const inside method
            if variable in o['local'][0]:
                raise Redeclared(static_inst_param_var, variable)
            o['local'][0][variable] = Symbol(variable, 'variable', None, var_type)      # inside method, not check Static or Instance ---> always instance, not dollar ID
            o['out_or_in_method'] = 'none'          # reset
    
    def visitConstDecl(self, ast: ConstDecl, kind_and_o):

        # constant not initialize
        if ast.value == None: raise IllegalConstantExpression(ast.value)
        
        static_inst_param_var, o = kind_and_o
        constant = ast.constant.name
        const_type = self.visit(ast.constType, o)
        # value = self.visit(ast.value, o) if ast.value else None
        flag_const_init = True
        value = self.visit(ast.value, (flag_const_init, o)) if ast.value else None
        
        print("const_type: ", const_type)
        if o['out_or_in_method'] == 'out':          # check attribute outside method
            current_class = o['current_class']
            if constant in o['global'][current_class]:
                raise Redeclared(Attribute(), constant)
            o['global'][current_class][constant] = Symbol(constant, 'immutable', static_inst_param_var, const_type)
            o['out_or_in_method'] == 'none'         # reset
            
        if o['out_or_in_method'] == 'in':           # check attribute inside method
            if constant in o['local'][0]:
                raise Redeclared(static_inst_param_var, constant)
            o['local'][0][constant] = Symbol(constant, 'constant', None, const_type)    # inside method, not check Static or Instance ---> always instance, not dollar ID
            o['out_or_in_method'] == 'none'         # reset
            
    def visitBlock(self, ast: Block, loop_name_scope):
        print("\no BEFORE visitBlock: ", loop_name_scope)
        in_loop, method_name, o = loop_name_scope
        for each_inst in ast.inst:
            o['out_or_in_method'] = 'in'
            if isinstance(each_inst, VarDecl): self.visit(each_inst, (Variable(), o))
            elif isinstance(each_inst, ConstDecl): self.visit(each_inst, (Constant(), o))
            else:
                o['local'] = [{}] + o['local']
                self.visit(each_inst, (in_loop, method_name, o))
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
        
        for x in ast.memlist:
            self.visit(x, o)
        
        o['current_class'] = '-1'       # reset, finishing visit current class
       
        
        print("o AFTER visitClassDecl", class_name, "AFTER: ", o, "\n")
        
    
    def visitStringType(self, ast, o):
        return StringType()
    
    def visitArrayType(self, ast: ArrayType, o):
        pass
    
    def visitClassType(self, ast: ClassType, o):
        pass
    
    def visitVoidType(self, ast: VoidType, o):
        return VoidType()

    def visitProgram(self, ast: Program, o):
        global_env = {}
        global_env['global'] = {}
        global_env['local'] = []
        global_env['current_class'] = '-1'
        global_env['out_or_in_method'] = 'none' # attribute decl or variable and cons decl (inside method)
        for each_class in ast.decl:
            self.visit(each_class, global_env)

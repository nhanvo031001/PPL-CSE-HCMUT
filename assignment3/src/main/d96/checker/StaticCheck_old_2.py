
"""
 * @author nhphung
"""
from pydoc import classname
from tracemalloc import StatisticDiff
from matplotlib.pyplot import isinteractive

from numpy import isin, var
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *


## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##
from main.d96.utils.AST import *
from main.d96.parser.D96Parser import D96Parser
from main.d96.parser.D96Visitor import D96Visitor
## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##

class StaticChecker(BaseVisitor,Utils):

    global_envi = {}

    def __init__(self,ast):
        self.ast = ast
        StaticChecker.global_envi['global'] = {}
        StaticChecker.global_envi['local'] = [{}]
        StaticChecker.global_envi['current_class'] = '-1'
        StaticChecker.global_envi['var_or_attri'] = 'none'
        
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)
    
    def visitId(self, ast: Id, o):
        print("o in visitId: ", o)
        # print("id name: ", ast.name, "\n")
        id_name = ast.name
        if StaticChecker.global_envi['var_or_attri'] == 'attri':
            current_class = StaticChecker.global_envi['current_class']
            if id_name in StaticChecker.global_envi['global'][current_class]:
                return StaticChecker.global_envi['global'][current_class][id_name]
            
        if StaticChecker.global_envi['var_or_attri'] == 'var':
            if id_name in StaticChecker.global_envi['local'][0]:
                print("return StaticChecker.global_envi['local'][0][id_name]: ", StaticChecker.global_envi['local'][0][id_name])
                return StaticChecker.global_envi['local'][0][id_name]
        
        raise Undeclared(Identifier, id_name)
    
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
        op = ast.op
        exp = self.visit(ast.body, o)
        
        if op == '!':
            if isinstance(exp, BoolType): return BoolType()
            raise TypeMismatchInExpression(ast)
        
        if op == '-':
            if isinstance(exp, IntType): return IntType()
            if isinstance(exp, FloatType): return FloatType()
            raise TypeMismatchInExpression(ast)
        
        if op == 'New':
            if isinstance(exp, ClassType): return ClassType()
            raise TypeMismatchInExpression(ast)
        
        print("op: ", op)
        print("exp: ", exp, "\n")
    
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
    
    def visitVarDecl(self, ast: VarDecl, o):

        # variable = self.visit(ast.variable, o)
        variable = ast.variable.name
        var_type = self.visit(ast.varType, o)
        var_init = self.visit(ast.varInit, o) if ast.varInit else None
        
        # if var_type != var_init: pass     # check ???
        
        if StaticChecker.global_envi['var_or_attri'] == 'attri':
            current_class = StaticChecker.global_envi['current_class']
            if variable in StaticChecker.global_envi['global'][current_class]:
                raise Redeclared(Variable(), variable)
            StaticChecker.global_envi['global'][current_class][variable] = var_type
            
            StaticChecker.global_envi['var_or_attri'] == 'none' # reset
            
        if StaticChecker.global_envi['var_or_attri'] == 'var':
            if variable in StaticChecker.global_envi['local'][0]:
                raise Redeclared(Variable(), variable)
            StaticChecker.global_envi['local'][0][variable] = var_type
            
            StaticChecker.global_envi['var_or_attri'] = 'none' # reset

    
    def visitBlock(self, ast: Block, o):
        for x in ast.inst:
            StaticChecker.global_envi['var_or_attri'] = 'var'
            self.visit(x, o)
        print("o AFTER visitBlock:", o, "\n")
    
    def visitConstDecl(self, ast: ConstDecl, o):

        # constant = self.visit(ast.constant, o)
        constant = ast.constant.name
        const_type = self.visit(ast.constType, o)
        value = self.visit(ast.value, o) if ast.value else None
        
        if StaticChecker.global_envi['var_or_attri'] == 'attri':
            current_class = StaticChecker.global_envi['current_class']
            if constant in StaticChecker.global_envi['global'][current_class]:
                raise Redeclared(Variable(), constant)
            StaticChecker.global_envi['global'][current_class][constant] = const_type
            
            StaticChecker.global_envi['var_or_attri'] == 'none' # reset
            
        if StaticChecker.global_envi['var_or_attri'] == 'var':
            if constant in StaticChecker.global_envi['local'][0]:
                raise Redeclared(Variable(), constant)
            StaticChecker.global_envi['local'][0][constant] = const_type

            StaticChecker.global_envi['var_or_attri'] == 'none' # reset
    
    def visitInstance(self, ast: Instance, o):
        return Instance()
    
    def visitStatic(self, ast: Static, o):
        return Static()
    
    def visitMethodDecl(self, ast: MethodDecl, o):
        kind = self.visit(ast.kind, o)
        # name = self.visit(ast.name, o)
        name = ast.name.name
        
        current_class = StaticChecker.global_envi['current_class']
        if name in StaticChecker.global_envi['global'][current_class]:
            raise Redeclared(Method, name)
        StaticChecker.global_envi['global'][current_class][name] = ['no return type']
        
        for x in ast.param:
            StaticChecker.global_envi['var_or_attri'] = 'var'
            self.visit(x, o)
        # param = [self.visit(x, o) for x in ast.param]
        
        body = self.visit(ast.body, o)
        
        print("o in visitMethodDecl", name, ":", o, "\n")
        
        StaticChecker.global_envi['local'] = [{}]   # reset
    
    def visitAttributeDecl(self, ast: AttributeDecl, o):
        StaticChecker.global_envi['var_or_attri'] = 'attri'
        print("o visitAttributeDecl: ", o)
        print("ast.SIKIND: ", ast.kind)
        print("ast.decl: ", ast.decl)
        # print("self.visiit: ", self.visit(ast.kind, o))
        self.visit(ast.decl, o)
        
        StaticChecker.global_envi['var_or_attri'] = 'none'     # reset
    
    def visitIntType(self, ast, o):
        return IntType()
    
    def visitFloatType(self, ast, o):
        return FloatType()
    
    def visitBoolType(self, ast, o):
        return BoolType()
    
    def visitClassDecl(self, ast, o):
        print("o visitClassDecl: ", o, "\n")
        class_name = ast.classname.name
        parent_name = ast.parentname.name if ast.parentname else None
        if class_name in StaticChecker.global_envi['global']:     # check redeclare class
            raise Redeclared(Class(), class_name)
        if parent_name and parent_name not in StaticChecker.global_envi['global']:    # check parent name whether has been declared
            raise Undeclared(Class(), parent_name)
        StaticChecker.global_envi['current_class'] = class_name
        StaticChecker.global_envi['global'][class_name] = {}
        
        memList = [self.visit(x, o) for x in ast.memlist]
        
        StaticChecker.global_envi['current_class'] = '-1'
       
        print("visitClassDecl: ", class_name, " ", "\t", "parent name: ", parent_name, "\n")
        print("o visitClassDecl", class_name, "AFTER: ", o, "\n")
        
        
    
    def visitStringType(self, ast, o):
        return StringType()
    
    def visitArrayType(self, ast: ArrayType, o):
        pass
    
    def visitClassType(self, ast: ClassType, o):
        pass
    
    def visitVoidType(self, ast: VoidType, o):
        return VoidType()

        
    def visitProgram(self, ast: Program, o):
        for each_class in ast.decl:
            self.visit(each_class, o)

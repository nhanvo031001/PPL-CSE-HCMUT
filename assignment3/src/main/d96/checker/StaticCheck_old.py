
"""
 * @author nhphung
"""
from pydoc import classname
from matplotlib.pyplot import isinteractive

from numpy import isin
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *


## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##
from main.d96.utils.AST import *
from main.d96.parser.D96Parser import D96Parser
from main.d96.parser.D96Visitor import D96Visitor
## REMEMBER TO COMMENT 3 LINES BEFORE SUBMIT ##

# class MType:
#     def __init__(self,partype,rettype):
#         self.partype = partype
#         self.rettype = rettype

# class Symbol:
#     def __init__(self,name,mtype,value = None):
#         self.name = name
#         self.mtype = mtype
#         self.value = value

class StaticChecker(BaseVisitor,Utils):

    # global_envi = [
    # Symbol("getInt",MType([],IntType())),
    # Symbol("putIntLn",MType([IntType()],VoidType()))
    # ]

    global_envi = [{}]
    
    

    def __init__(self,ast):
        self.ast = ast

    def check(self):
        # print("check function")
        # print("self.ast: ", self.ast)
        return self.visit(self.ast,StaticChecker.global_envi)
    
    def visitId(self, ast: Id, o):
        print("o in visitId: ", o)
        return ast.name
    
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
        # print("visitVarDecl")
        # print("o visitVarDecl: ", o)
        variable = self.visit(ast.variable, o)
        var_type = self.visit(ast.varType, o)
        var_init = self.visit(ast.varInit, o) if ast.varInit else None
        
        # if var_type != var_init: pass     # check ???
        
        if variable in o[0]:
            raise Redeclared(Variable(), variable)
        o[0][variable] = var_type
        print("variable: ", variable)
        # print("varType: ", var_type)
        # print("varInit: ", var_init)
        print("o visitVarDecl AFTER: ", o, "\n")
    
    def visitBlock(self, ast: Block, o):
        pass
    
    def visitConstDecl(self, ast: ConstDecl, o):
        # print("visitConstDecl")
        # print("o visitConstDecl: ", o)
        constant = self.visit(ast.constant, o)
        const_type = self.visit(ast.constType, o)
        value = self.visit(ast.value, o)
        if constant in o[0]:
            raise Redeclared(Variable(), constant)
        o[0][constant] = const_type
        print("constant: ", constant)
        # print("constType: ", const_type)
        # print("value: ", value)
        print("o visitConstDecl AFTER: ", o, "\n")
    
    def visitInstance(self, ast: Instance, o):
        return Instance()
    
    def visitStatic(self, ast: Static, o):
        return Static()
    
    def visitMethodDecl(self, ast: MethodDecl, o):
        pass
    
    def visitAttributeDecl(self, ast: AttributeDecl, o):
        # print("o visitAttributeDecl: ", o)
        print("ast.SIKIND: ", ast.kind)
        print("ast.decl: ", ast.decl)
        print("self.visiit: ", self.visit(ast.kind, o))
        self.visit(ast.decl, o)
    
    def visitIntType(self, ast, o):
        return IntType()
    
    def visitFloatType(self, ast, o):
        return FloatType()
    
    def visitBoolType(self, ast, o):
        return BoolType()
    
    def visitClassDecl(self, ast, o):
        # print("o: ", o, "\n")
        class_name = self.visit(ast.classname, o)
        local_env = [{}]
        memList = [self.visit(x, local_env + o) for x in ast.memlist]
        parent_name = self.visit(ast.parentname, o) if ast.parentname else None
        print("visitClassDecl: ", class_name, " ", "\t", "parent name: ", parent_name, "\n")
        if class_name in StaticChecker.global_envi[0]:     # check redeclare class
            raise Redeclared(Class(), class_name)
        if parent_name and parent_name not in StaticChecker.global_envi[0]:    # check parent name whether has been declared
            raise Undeclared(Class(), parent_name)
        StaticChecker.global_envi[0][class_name] = Class()
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
        # o = [{}]
        # print("visitProgram, ast.decl: ", ast.decl, "\n")
        print("o: ", o, "\n")
        for each_class in ast.decl:
            # print("each_class: ", each_class)
            self.visit(each_class, o)

    # def visitProgram(self,ast, c): 
    #     return [self.visit(x,c) for x in ast.decl]

    # def visitFuncDecl(self,ast, c): 
    #     return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 
    

    # def visitCallExpr(self, ast, c): 
    #     at = [self.visit(x,(c[0],False)) for x in ast.param]
        
    #     res = self.lookup(ast.method.name,c[0],lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType:
    #         raise Undeclared(Function(),ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         if c[1]:
    #             raise TypeMismatchInStatement(ast)
    #         else:
    #             raise TypeMismatchInExpression(ast)
    #     else:
    #         return res.mtype.rettype

    # def visitIntLiteral(self,ast, c): 
    #     return IntType()
    


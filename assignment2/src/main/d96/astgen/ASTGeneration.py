from array import ArrayType
from distutils.command.sdist import sdist
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from main.d96.utils.AST import ArrayCell, ArrayLiteral, Assign, BoolType, CallStmt, ClassDecl, ClassType, ConstDecl, Expr, FieldAccess, FloatType, For, Instance, IntLiteral, IntType, MethodDecl, NewExpr, NullLiteral, SelfLiteral, Static, StringType, VarDecl


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        class_declare_list = []
        for each_declare in ctx.exp():
            class_declare_list.append(self.visit(each_declare))
        return Program(class_declare_list)
        
    def visitClass_declare(self, ctx: D96Parser.Class_declareContext):
        pass
    
    def visitName_class(self, ctx: D96Parser.Name_classContext):
        pass
    
    def visitBody_class(self, ctx: D96Parser.Body_classContext):
        pass
    
    def visitMem_class_declare(self, ctx: D96Parser.Mem_class_declareContext):
        pass
    
    def visitConstructor_declare(self, ctx: D96Parser.Constructor_declareContext):
        pass
    
    def visitParams_list(self, ctx: D96Parser.Params_listContext):
        pass
    
    def visitParams_declare(self, ctx: D96Parser.Params_declareContext):
        pass
    
    def visitId_list(self, ctx: D96Parser.Id_listContext):
        pass
    
    def visitType_data(self, ctx: D96Parser.Type_dataContext):
        pass
            
    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        pass
    
    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        pass
    
    def visitElement_type(self, ctx: D96Parser.Element_typeContext):
        pass
    
    def visitSize(self, ctx: D96Parser.SizeContext):
        pass
    
    def visitClass_type(self, ctx: D96Parser.Class_typeContext):
        pass
    
    def visitDestructor_declare(self, ctx: D96Parser.Destructor_declareContext):
        pass
    
    def visitMethod_declare(self, ctx: D96Parser.Method_declareContext):
        pass
        
    def visitAttribute_declare(self, ctx: D96Parser.Attribute_declareContext):
        pass
    
    def visitVariable_name_list(self, ctx: D96Parser.Variable_name_listContext):
        pass
    
    def visitValue_list(self, ctx: D96Parser.Value_listContext):
        pass
    
    def visitBlock_stmt(self, ctx: D96Parser.Block_stmtContext):
        pass
    
    def visitStmt(self, ctx: D96Parser.StmtContext):
        pass
    
    def visitVariable_and_constant_stmt(self, ctx: D96Parser.Variable_and_constant_stmtContext):
        pass
    
    def visitVariable_name_list_in_method(self, ctx: D96Parser.Variable_name_list_in_methodContext):
        pass
    
    def visitValue_list_stmt(self, ctx: D96Parser.Value_list_stmtContext):
        pass
    
    def visitAssignment_stmt(self, ctx: D96Parser.Assignment_stmtContext):
        pass
    
    def visitScalar_variable(self, ctx: D96Parser.Scalar_variableContext):
        pass
        
    def visitIndex_exp_for_scalar_variable(self, ctx: D96Parser.Index_exp_for_scalar_variableContext):
        pass
            
    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        pass
    
    def visitFor_in_stmt(self, ctx: D96Parser.For_in_stmtContext):
        pass
    
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return Break()
    
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return Continue()
    
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return(None)
    
    def visitMethod_invocation_stmt(self, ctx:D96Parser.Method_invocation_stmtContext):
        pass
    
    def visitStatic_method_invocation(self, ctx:D96Parser.Static_method_invocationContext):
        pass
    
    def visitInstance_method_invocation(self, ctx:D96Parser.Instance_method_invocationContext):
        pass
    
    def visitPre_exp(self, ctx:D96Parser.Pre_expContext):
        pass
        
    def visitExp(self, ctx:D96Parser.ExpContext):
        if ctx.getChildCount() == 1:    # recursive to second case (exp1)
            return self.visit(ctx.exp1(0))
        else:
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)
        
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        if ctx.getChildCount() == 1:    # recursive to second case (exp2)
            return self.visit(ctx.exp2(0))
        else:
            left = self.visit(ctx.exp2(0))
            right = self.visit(ctx.exp2(1))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)
        
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        if ctx.getChildCount() == 1:    # recursive to second case (exp3)
            return self.visit(ctx.exp3())
        else:
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)
        
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        if ctx.getChildCount() == 1:    # recursive to second case (exp4)
            return self.visit(ctx.exp4())
        else:
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitExp4(self, ctx:D96Parser.Exp4Context):
        if ctx.getChildCount() == 1:    # recursive to second case (exp5)
            return self.visit(ctx.exp5())
        else:
            left = self.visit(ctx.exp4())
            right = self.visit(ctx.exp5())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)
        
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        if ctx.exp6():    # recursive to second case (exp6)
            return self.visit(ctx.exp6())
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp5()))

    def visitExp6(self, ctx:D96Parser.Exp6Context):
        if ctx.exp7():    # recursive to second case (exp7)
            return self.visit(ctx.exp7())
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp6()))
    
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        if ctx.exp8():    # recursive to second case (exp8)
            return self.visit(ctx.exp8())
        else:
            exp = self.visit(ctx.exp7())
            list_exp = self.visit(ctx.index_operator())
            return ArrayCell(exp, list_exp)
        
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp9())
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.exp8()), Id(ctx.ID().getText()))
        list_exp = []
        if ctx.exp_list():
            list_exp = self.visit(ctx.exp_list())
        return CallStmt(self.visit(ctx.exp8()), ctx.ID().getText(), list_exp)
    
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp10())
        elif ctx.getChildCount() == 3:
            return FieldAccess(ctx.ID().getText(), ctx.STATIC_ID().getText())
        list_exp = []
        if ctx.exp_list():
            list_exp = self.visit(ctx.exp_list())
        return CallStmt(ctx.ID().getText(), ctx.STATIC_ID().getText(), list_exp)    
    
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands())
        list_exp = []
        if ctx.exp_list():
            list_exp.extend(self.visit(ctx.exp_list()))     # xài extend vì self.visit(ctx.exp_list()) trả về một list rồi
        return NewExpr(Id(ctx.ID().getText()), list_exp)
            
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.literals():
            return self.visit(ctx.literals())
        else:
            return self.visit(ctx.exp())
        
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        if ctx.ZERO_LIT():
            return IntLiteral(int(ctx.ZERO_LIT().getText()))
        elif ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.boolean_literal():
            return self.visitBoolean_literal(ctx.boolean_literal())
        elif ctx.array_literal():
            return self.visitArray_literal(ctx.array_literal())
        
    def visitBoolean_literal(self, ctx:D96Parser.Boolean_literalContext):
        return BooleanLiteral(True) if ctx.TRUE() else BooleanLiteral(False)
    
    def visitArray_literal(self, ctx:D96Parser.Array_literalContext):
        if ctx.multidimensional_array():
            return self.visitMultidimensional_array(ctx.multidimensional_array())
        return self.visitIndexed_array(ctx.indexed_array())
    
    def visitMultidimensional_array(self, ctx: D96Parser.Multidimensional_arrayContext):
        array_list = []
        if ctx.array_list():
            array_list = self.visit(ctx.array_list())
        return ArrayLiteral(array_list)
    
    def visitArray_list(self, ctx: D96Parser.Array_listContext):
        array_literal_list = []
        for each_array_literal in ctx.array_literal():
            array_literal_list.append(self.visit(each_array_literal))
        return array_literal_list
    
    def visitIndexed_array(self, ctx: D96Parser.Indexed_arrayContext):
        literal_list = []
        if ctx.exp_list():
            literal_list.extend(self.visit(ctx.exp_list()))
        return ArrayLiteral(literal_list)
    
    def visitExp_list(self, ctx: D96Parser.Exp_listContext):
        exp_list = []
        for each_exp in ctx.exp():
            exp_list.append(self.visit(each_exp))
        return exp_list
    
    def visitIndex_operator(self, ctx: D96Parser.Index_operatorContext):
        exp_list = []
        exp_list.append(self.visit(ctx.exp()))
        if ctx.getChildCount() == 3:
            return exp_list
        return self.visitIndex_operator(ctx.index_operator())



    
    # def visitProgram(self, ctx: D96Parser.ProgramContext):
    #     return Program([FuncDecl(Id("main"),
    #                              [],
    #                              self.visit(ctx.mptype()),
    #                              Block([], [self.visit(ctx.body())] if ctx.body() else []))])

    # def visitMptype(self, ctx: D96Parser.MptypeContext):
    #     if ctx.INTTYPE():
    #         return IntType()
    #     else:
    #         return VoidType()

    # def visitBody(self, ctx: D96Parser.BodyContext):
    #     return self.visit(ctx.funcall())

    # def visitFuncall(self, ctx: D96Parser.FuncallContext):
    #     return CallExpr(Id(ctx.ID().getText()), [self.visit(ctx.exp())] if ctx.exp() else [])

    # def visitExp(self, ctx: D96Parser.ExpContext):
    #     if (ctx.funcall()):
    #         return self.visit(ctx.funcall())
    #     else:
    #         return IntLiteral(int(ctx.INTLIT().getText()))

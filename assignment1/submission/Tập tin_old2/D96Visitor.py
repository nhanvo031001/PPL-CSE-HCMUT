# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declare.
    def visitClass_declare(self, ctx:D96Parser.Class_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#name_class.
    def visitName_class(self, ctx:D96Parser.Name_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body_class.
    def visitBody_class(self, ctx:D96Parser.Body_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor_declare.
    def visitConstructor_declare(self, ctx:D96Parser.Constructor_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params_list.
    def visitParams_list(self, ctx:D96Parser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params_declare.
    def visitParams_declare(self, ctx:D96Parser.Params_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_list.
    def visitId_list(self, ctx:D96Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#type_data.
    def visitType_data(self, ctx:D96Parser.Type_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_type.
    def visitElement_type(self, ctx:D96Parser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#size.
    def visitSize(self, ctx:D96Parser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor_declare.
    def visitDestructor_declare(self, ctx:D96Parser.Destructor_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declare.
    def visitMethod_declare(self, ctx:D96Parser.Method_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_declare.
    def visitAttribute_declare(self, ctx:D96Parser.Attribute_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_name_list.
    def visitVariable_name_list(self, ctx:D96Parser.Variable_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#value_list.
    def visitValue_list(self, ctx:D96Parser.Value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_and_constant_stmt.
    def visitVariable_and_constant_stmt(self, ctx:D96Parser.Variable_and_constant_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_name_list_in_method.
    def visitVariable_name_list_in_method(self, ctx:D96Parser.Variable_name_list_in_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#value_list_stmt.
    def visitValue_list_stmt(self, ctx:D96Parser.Value_list_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:D96Parser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_variable.
    def visitScalar_variable(self, ctx:D96Parser.Scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_exp_for_scalar_variable.
    def visitIndex_exp_for_scalar_variable(self, ctx:D96Parser.Index_exp_for_scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_stmt.
    def visitFor_in_stmt(self, ctx:D96Parser.For_in_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocation_stmt.
    def visitMethod_invocation_stmt(self, ctx:D96Parser.Method_invocation_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method_invocation.
    def visitStatic_method_invocation(self, ctx:D96Parser.Static_method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_method_invocation.
    def visitInstance_method_invocation(self, ctx:D96Parser.Instance_method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#pre_exp.
    def visitPre_exp(self, ctx:D96Parser.Pre_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp1.
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp10.
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literals.
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#boolean_literal.
    def visitBoolean_literal(self, ctx:D96Parser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_literal.
    def visitArray_literal(self, ctx:D96Parser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multidimensional_array.
    def visitMultidimensional_array(self, ctx:D96Parser.Multidimensional_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_list.
    def visitArray_list(self, ctx:D96Parser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexed_array.
    def visitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_list.
    def visitExp_list(self, ctx:D96Parser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operator.
    def visitIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        return self.visitChildren(ctx)



del D96Parser
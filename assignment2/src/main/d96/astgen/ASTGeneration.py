from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce

from main.d96.utils.AST import *
from main.d96.parser.D96Parser import D96Parser
from main.d96.parser.D96Visitor import D96Visitor

class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        # class_declare_list = []
        # for each_declare in ctx.class_declare():
        #     class_declare_list.append(self.visit(each_declare))
        # return Program(class_declare_list)
        
        return Program([self.visit(each_declare) for each_declare in ctx.class_declare()])
        
    def visitClass_declare(self, ctx: D96Parser.Class_declareContext):
        class_name = self.visit(ctx.name_class())
        mem_list = self.visit_class_program_mem_list(ctx.body_class()) if class_name.name == "Program" else self.visit(ctx.body_class())
        parent_name = Id(ctx.ID().getText()) if ctx.COLON() else None
        return ClassDecl(class_name, mem_list, parent_name)
    
    def visitName_class(self, ctx: D96Parser.Name_classContext):
        return Id(ctx.ID().getText())
    
    def visitBody_class(self, ctx: D96Parser.Body_classContext):
        # list_declare_in_class = []
        # for each_declare in ctx.mem_class_declare():
        #     visit_res = self.visit(each_declare)
        #     if (isinstance(visit_res, list)):   # vì attribute_declare trả về list, phải xài extend
        #         list_declare_in_class.extend(visit_res)
        #     else:
        #         # if isinstance(visit_res, MethodDecl):
        #         #     if visit_res.name.name == 'Constructor' or visit_res.name.name == 'Destructor':
        #         #         visit_res.kind = Static()
        #         list_declare_in_class.append(visit_res)
                
        list_declare_in_class = reduce(lambda x, y: x + y if isinstance(y, list) else x + [y], [self.visit(each_declare) for each_declare in ctx.mem_class_declare()], [])
        return list_declare_in_class
    
    def check_main_function(self, method):
        if method.name.name == 'main' and method.param == []:
            method.kind = Static()
        return method
    
    def visit_class_program_mem_list(self, ctx: D96Parser.Body_classContext):
        # list_declare_in_class = []
        # for each_declare in ctx.mem_class_declare():
        #     visit_res = self.visit(each_declare)
        #     if (isinstance(visit_res, list)):   # vì attribute_declare trả về list, phải xài extend
        #         list_declare_in_class.extend(visit_res)
        #     else:
        #         if isinstance(visit_res, MethodDecl):
        #             if visit_res.name.name == 'main' and visit_res.param == []:
        #                 visit_res.kind = Static()
        #             # if visit_res.name.name == 'Constructor' or visit_res.name.name == 'Destructor':
        #             #     visit_res.kind = Static()
        #         list_declare_in_class.append(visit_res)
        
        list_declare_in_class = reduce(lambda x, y: x + y if isinstance(y, list) else x + [self.check_main_function(y)], [self.visit(each_declare) for each_declare in ctx.mem_class_declare()], [])
        return list_declare_in_class
    
    def visitMem_class_declare(self, ctx: D96Parser.Mem_class_declareContext):
        if ctx.constructor_declare():
            return self.visit(ctx.constructor_declare())
        elif ctx.destructor_declare():
            return self.visit(ctx.destructor_declare())
        elif ctx.method_declare():
            return self.visit(ctx.method_declare())
        return self.visit(ctx.attribute_declare())
    
    def visitConstructor_declare(self, ctx: D96Parser.Constructor_declareContext):
        kind = Instance()
        name = Id('Constructor')
        param = self.visit(ctx.params_list()) if ctx.params_list() else []
        body = self.visit(ctx.block_stmt())
        return MethodDecl(kind, name, param, body)
    
    def visitParams_list(self, ctx: D96Parser.Params_listContext):
        # params_list = []
        # for each_params_declare in ctx.params_declare():
        #     params_list.extend(self.visit(each_params_declare))     # xài extend vì self.visit(each_params_declare) trả về 1 list
        
        params_list = reduce(lambda x, y: x + y, [self.visit(each_params_declare) for each_params_declare in ctx.params_declare()],[])
        return params_list
    
    def visitParams_declare(self, ctx: D96Parser.Params_declareContext):
        res = []
        id_list = self.visit(ctx.id_list())
        type_data = self.visit(ctx.type_data())
        # for each_id in id_list:
        #     res.append(VarDecl(each_id, type_data))
        
        res += [VarDecl(each_id, type_data) for each_id in id_list]
        return res
        
    
    def visitId_list(self, ctx: D96Parser.Id_listContext):
        # id_list = []
        # for each_id in ctx.ID():
        #     id_list.append(Id(each_id.getText()))
        # return id_list
        
        return [Id(each_id.getText()) for each_id in ctx.ID()] if ctx.ID() else []
    
    def visitType_data(self, ctx: D96Parser.Type_dataContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        return self.visit(ctx.class_type())
            
    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        if ctx.BOOLEAN():
            return BoolType()
        elif ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
    
    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        element_type = self.visit(ctx.element_type())
        size = self.visit(ctx.size())
        return ArrayType(size, element_type)
    
    def visitElement_type(self, ctx: D96Parser.Element_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        return self.visit(ctx.array_type())
    
    def visitSize(self, ctx: D96Parser.SizeContext):
        return self.changeFormatInteger(ctx.INT_LIT().getText())
    
    def visitClass_type(self, ctx: D96Parser.Class_typeContext):
        return ClassType(Id(ctx.ID().getText()))
    
    def visitDestructor_declare(self, ctx: D96Parser.Destructor_declareContext):
        kind = Instance()
        name = Id('Destructor')
        param = []
        body = self.visit(ctx.block_stmt())
        return MethodDecl(kind, name, param, body)
    
    def visitMethod_declare(self, ctx: D96Parser.Method_declareContext):
        kind = Instance() if ctx.ID() else Static()  
        name = Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.STATIC_ID().getText())
        param = self.visit(ctx.params_list()) if ctx.params_list() else []
        body = self.visit(ctx.block_stmt())
        return MethodDecl(kind, name, param, body)
        
    def visitAttribute_declare(self, ctx: D96Parser.Attribute_declareContext):
        variable_name_list = self.visit(ctx.variable_name_list())
        type_data = self.visit(ctx.type_data())
        value_list = self.visit(ctx.value_list()) if ctx.value_list() else []
        res = []
        # for i in range(len(variable_name_list)):
        #     res.append(AttributeDecl(Static() if variable_name_list[i].name[0] == '$' else Instance(),  # first param
                                     
        #                             VarDecl(variable_name_list[i], type_data, value_list[i] if value_list else None) if ctx.VAR()   # second param
        #                             else ConstDecl(variable_name_list[i], type_data, value_list[i] if value_list else None)
        #                             )
        #                )
            
        # for i in range(len(variable_name_list)):
        #     res.append(AttributeDecl(Static() if variable_name_list[i].name[0] == '$' else Instance(),  # first param
                                     
        #                             VarDecl(variable_name_list[i], type_data, value_list[i] if value_list else (NullLiteral() if isinstance(type_data, ClassType) else None)) if ctx.VAR()   # second param
        #                             else ConstDecl(variable_name_list[i], type_data, value_list[i] if value_list else (NullLiteral() if isinstance(type_data, ClassType) else None))
        #                             )
        #                )
        
        res += [AttributeDecl(Static() if variable_name_list[i].name[0] == '$' else Instance(),     # first param
                            
                            VarDecl(variable_name_list[i], type_data, value_list[i] if value_list else (NullLiteral() if isinstance(type_data, ClassType) else None)) if ctx.VAR()   # second param
                            else ConstDecl(variable_name_list[i], type_data, value_list[i] if value_list else (NullLiteral() if isinstance(type_data, ClassType) else None))
                            )

                    for i in range(len(variable_name_list))
                ]
        return res
                 
    
    def visitVariable_name_list(self, ctx: D96Parser.Variable_name_listContext):
        return [self.visit(each_var) for each_var in ctx.id_or_staticID()]
        
    def visitId_or_staticID(self, ctx: D96Parser.Id_or_staticIDContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return Id(ctx.STATIC_ID().getText())
    
    def visitValue_list(self, ctx: D96Parser.Value_listContext):
        # value_list = []
        # for each_value in ctx.exp():
        #     value_list.append(self.visit(each_value))
        # return value_list
        
        return [self.visit(each_value) for each_value in ctx.exp()] if ctx.exp() else []
    
    def visitBlock_stmt(self, ctx: D96Parser.Block_stmtContext):
        # res = []
        # for each_stmt in ctx.stmt():
        #     if (isinstance(self.visit(each_stmt), list)):   # vì visitVariable_and_constant_stmt trả về list, phải xài extend
        #         res.extend(self.visit(each_stmt))
        #     else:
        #         res.append(self.visit(each_stmt))
        res = reduce(lambda x, y: x + y if isinstance(y, list) else x + [y], [self.visit(each_stmt) for each_stmt in ctx.stmt()], [])
        return Block(res)
    
    def visitStmt(self, ctx: D96Parser.StmtContext):
        return self.visit(ctx.getChild(0))
    
    def visitVariable_and_constant_stmt(self, ctx: D96Parser.Variable_and_constant_stmtContext):
        variable_name_list = self.visit(ctx.variable_name_list_in_method()) 
        varType = self.visit(ctx.type_data())
        value_list_stmt = self.visit(ctx.value_list_stmt()) if ctx.value_list_stmt() else []
        res = []
        if ctx.VAR():
            # for i in range(len(variable_name_list)):
            #     initial_exp = value_list_stmt[i] if value_list_stmt else None
            #     if isinstance(varType, ClassType) and initial_exp is None:
            #         initial_exp = NullLiteral()
            #     res.append(VarDecl(variable_name_list[i], varType, initial_exp))
                
            res += [VarDecl(variable_name_list[i], varType, value_list_stmt[i] if value_list_stmt else (NullLiteral() if isinstance(varType, ClassType) else None)) for i in range(len(variable_name_list))]
        else:
            # for i in range(len(variable_name_list)):
            #     initial_exp = value_list_stmt[i] if value_list_stmt else None
            #     if isinstance(varType, ClassType) and initial_exp is None:
            #         initial_exp = NullLiteral()
            #     res.append(ConstDecl(variable_name_list[i], varType, initial_exp))
            
            res += [ConstDecl(variable_name_list[i], varType, value_list_stmt[i] if value_list_stmt else (NullLiteral() if isinstance(varType, ClassType) else None)) for i in range(len(variable_name_list))]
        return res
    
    def visitVariable_name_list_in_method(self, ctx: D96Parser.Variable_name_list_in_methodContext):
        variable_list = []
        for each_variable in ctx.ID():
            variable_list.append(Id(each_variable.getText()))
        return variable_list
    
    def visitValue_list_stmt(self, ctx: D96Parser.Value_list_stmtContext):
        value_list = []
        for each_value in ctx.exp():
            value_list.append(self.visit(each_value))
        return value_list
    
    def visitAssignment_stmt(self, ctx: D96Parser.Assignment_stmtContext):
        lhs = self.visit(ctx.scalar_variable())
        rhs = self.visit(ctx.exp())
        return Assign(lhs, rhs)
    
    def visitScalar_variable(self, ctx: D96Parser.Scalar_variableContext):
        if ctx.ID() and ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        elif ctx.name_class():
            return FieldAccess(self.visit(ctx.name_class()), Id(ctx.STATIC_ID().getText()))
        elif ctx.exp8():
            return FieldAccess(self.visit(ctx.exp8()), Id(ctx.ID().getText()))
        return self.visit(ctx.index_exp_for_scalar_variable())
        
    def visitIndex_exp_for_scalar_variable(self, ctx: D96Parser.Index_exp_for_scalar_variableContext):
        return ArrayCell(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(1)))
            
    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        expr = self.visit(ctx.exp())
        thenStmt = self.visit(ctx.block_stmt())
        elseif_block_list = [self.visit(each_elseif_block) for each_elseif_block in ctx.elseif_block()] if ctx.elseif_block() else []   # trả về [ [elseif]... ]
        else_block = self.visit(ctx.else_block()) if ctx.else_block() else None

        if else_block:
            elseif_block_list.append([else_block]) # vì mỗi phần tử của elseif_block_list là list ---> [else_block]

        if elseif_block_list == []:
            return If(expr, thenStmt, else_block)
        return If(expr, thenStmt, self.supportElseStmt(elseif_block_list))
    
    def supportElseStmt(self, elseif_block_list):
        # if len(elseif_block_list) == 0: return None     # trường hợp chỉ có elseif, k có else ---> vế elseStmt là None
        # if len(elseif_block_list) == 1 and len(elseif_block_list[0]) == 2:  # trường hợp chỉ có elseif, k có else, tiếp tục đệ quy đến trường hợp return None ở hàng trên
        #     return Block([If(elseif_block_list[0][0], elseif_block_list[0][1], self.supportElseStmt(elseif_block_list[1:]))])
        # if len(elseif_block_list) == 1 and len(elseif_block_list[0]) == 1:  # trường hợp vừa elseIf và else, trong list chỉ còn lại elseStmt ---> trả về block_stmt luôn
        #     return elseif_block_list[0][0]
        # return Block([If(elseif_block_list[0][0], elseif_block_list[0][1], self.supportElseStmt(elseif_block_list[1:]))])   # đệ quy hết cái list
        
        
        if len(elseif_block_list) == 0: return None     # trường hợp chỉ có elseif, k có else ---> vế elseStmt là None
        if len(elseif_block_list) == 1 and len(elseif_block_list[0]) == 2:  # trường hợp chỉ có elseif, k có else, tiếp tục đệ quy đến trường hợp return None ở hàng trên
            return If(elseif_block_list[0][0], elseif_block_list[0][1], self.supportElseStmt(elseif_block_list[1:]))
        if len(elseif_block_list) == 1 and len(elseif_block_list[0]) == 1:  # trường hợp vừa elseIf và else, trong list chỉ còn lại elseStmt ---> trả về block_stmt luôn
            return elseif_block_list[0][0]
        return If(elseif_block_list[0][0], elseif_block_list[0][1], self.supportElseStmt(elseif_block_list[1:]))   # đệ quy hết cái list
    
    def visitElseif_block(self, ctx: D96Parser.Elseif_blockContext):
        return [self.visit(ctx.exp()), self.visit(ctx.block_stmt())]
    
    def visitElse_block(self, ctx: D96Parser.Else_blockContext):
        return self.visit(ctx.block_stmt())
    
    def visitFor_in_stmt(self, ctx: D96Parser.For_in_stmtContext):
        var = Id(ctx.ID().getText())
        exp1 = self.visit(ctx.exp(0))
        exp2 = self.visit(ctx.exp(1))
        exp3 = IntLiteral(1)
        loop = self.visit(ctx.block_stmt())
        if ctx.BY():
            exp3 = self.visit(ctx.exp(2))
        return For(var, exp1, exp2, loop, exp3)
    
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return Break()
    
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return Continue()
    
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        return Return(None)
    
    def visitMethod_invocation_stmt(self, ctx:D96Parser.Method_invocation_stmtContext):
        if ctx.static_method_invocation():
            return self.visit(ctx.static_method_invocation())
        return self.visit(ctx.instance_method_invocation())
    
    def visitStatic_method_invocation(self, ctx:D96Parser.Static_method_invocationContext):
        name_class = self.visit(ctx.name_class())
        static_id = Id(ctx.STATIC_ID().getText())
        list_exp = []
        if ctx.exp_list():
            list_exp = self.visit(ctx.exp_list())
        return CallStmt(name_class, static_id, list_exp)
    
    def visitInstance_method_invocation(self, ctx:D96Parser.Instance_method_invocationContext):
        pre_exp = self.visit(ctx.pre_exp())
        id  = Id(ctx.ID().getText())
        list_exp = []
        if ctx.exp_list():
            list_exp = self.visit(ctx.exp_list())
        return CallStmt(pre_exp, id, list_exp)
    
    def visitPre_exp(self, ctx:D96Parser.Pre_expContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp9())
        elif ctx.LB() and ctx.RB():
            list_exp = []
            if ctx.exp_list():
                list_exp = self.visit(ctx.exp_list())
            return CallExpr(self.visit(ctx.pre_exp()), Id(ctx.ID().getText()), list_exp)
        return FieldAccess(self.visit(ctx.pre_exp()), Id(ctx.ID().getText()))
        
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
        
        # if ctx.getChildCount() == 1:
        #     return self.visit(ctx.getChild(0))  
        # return ArrayCell(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(1)))
        
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp9())
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.exp8()), Id(ctx.ID().getText()))
        list_exp = []
        if ctx.exp_list():
            list_exp = self.visit(ctx.exp_list())
        return CallExpr(self.visit(ctx.exp8()), Id(ctx.ID().getText()), list_exp)
    
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp10())
        elif ctx.getChildCount() == 3:
            return FieldAccess(Id(ctx.ID().getText()), Id(ctx.STATIC_ID().getText()))
        list_exp = []
        if ctx.exp_list():
            list_exp = self.visit(ctx.exp_list())
        return CallExpr(Id(ctx.ID().getText()), Id(ctx.STATIC_ID().getText()), list_exp)    
    
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
        
    def changeFormatInteger(self, int_string):
        if int_string[0] != '0' or (len(int_string) == 1 and int_string[0] == '0'):      # số 0 hệ decimal
            return (int(int_string, 10))
        elif int_string[0] == '0' and (int_string[1] == 'x' or int_string[1] == 'X'):
            return (int(int_string, 16))
        elif int_string[0] == '0' and (int_string[1] == 'b' or int_string[1] == 'B'):
            return (int(int_string, 2))
        return (int(int_string, 8))
        
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        if ctx.ZERO_LIT():
            return IntLiteral(self.changeFormatInteger(ctx.ZERO_LIT().getText()))
        elif ctx.INT_LIT():
            return IntLiteral(self.changeFormatInteger(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            float_str = ctx.FLOAT_LIT().getText()
            if float_str[0] == '.':
                float_str = '0' + float_str
            return FloatLiteral(float(float_str))
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
        # array_list = []
        # if ctx.array_list():
        #     array_list = self.visit(ctx.array_list())
        # return ArrayLiteral(array_list)
        return ArrayLiteral(self.visit(ctx.array_list()))
    
    def visitArray_list(self, ctx: D96Parser.Array_listContext):
        # array_literal_list = []
        # for each_array_literal in ctx.array_literal():
        #     array_literal_list.append(self.visit(each_array_literal))
        # return array_literal_list
        
        return [self.visit(each_array_literal) for each_array_literal in ctx.array_literal()] if ctx.array_literal() else []
    
    def visitIndexed_array(self, ctx: D96Parser.Indexed_arrayContext):
        literal_list = []
        if ctx.exp_list():
            literal_list.extend(self.visit(ctx.exp_list()))
        return ArrayLiteral(literal_list)
        
    def visitExp_list(self, ctx: D96Parser.Exp_listContext):
        # exp_list = []
        # for each_exp in ctx.exp():
        #     exp_list.append(self.visit(each_exp))
        # return exp_list
        return [self.visit(each_exp) for each_exp in ctx.exp()] if ctx.exp() else []
    
    def visitIndex_operator(self, ctx: D96Parser.Index_operatorContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.exp())]
        return [self.visit(ctx.exp())] + self.visit(ctx.index_operator())
    
        # viết cách index_operator: (LSB exp RSB)+;
        # exp_list = []
        # print("bug: ", type(ctx.exp()))
        # print("bug: ", (ctx.exp()))
        # for each_exp in ctx.exp():
        #     exp_res = self.visit(each_exp)
        #     if isinstance(exp_res,list):
        #         exp_list.extend(exp_res)
        #     else:
        #         exp_list.append(exp_res)
        # return exp_list
        
        # viết cách cũ --> index_operator: LSB exp RSB | LSB exp RSB index_operator;
        # exp_list = []
        # if isinstance(self.visit(ctx.exp()), list): 
        #     exp_list.extend(self.visit(ctx.exp()))
        # else:
        #     exp_list.append(self.visit(ctx.exp()))
        # if ctx.getChildCount() == 3:
        #     return exp_list
        # return exp_list + self.visitIndex_operator(ctx.index_operator())

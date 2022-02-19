import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_300_class_declare(self):
        input = """ 
                    Class Program {}
                    Class Main {}
                    Class Shape {}
                    Class Square : Shape {}
                    Class Square : Main {}
                """ 
        expect = """Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Main),[]),ClassDecl(Id(Shape),[]),ClassDecl(Id(Square),Id(Shape),[]),ClassDecl(Id(Square),Id(Main),[])])"""
        self.assertTrue(TestAST.test(input,expect,300))
        
    def test_301_constructor(self):
        input = """ 
                    Class Program {
                        Constructor() {
                            Self.a = 1;
                        }
                        
                        Constructor(a: Int; b, c: Float) {
                            Self.a = 1;
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(1))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(1))]))])])"""
        self.assertTrue(TestAST.test(input,expect,301))
        
    def test_302_destructor(self):
        input = """ 
                    Class Program {
                        Destructor() {
                            Self.a = 1;
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(1))]))])])"""
        self.assertTrue(TestAST.test(input,expect,302))
        
    def test_303_params_list_in_method(self):
        input = """ 
                    Class Program {
                        method1(a: Int) {
                            obj = 1;
                        }
                        
                        method2(a: Float; b, c, d: String) {
                            obj = 2;
                        }
                        
                        method3() {
                            obj = 3;
                        }
                        
                        method4(a, b, c: Boolean) {}
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method1),Instance,[param(Id(a),IntType)],Block([AssignStmt(Id(obj),IntLit(1))])),MethodDecl(Id(method2),Instance,[param(Id(a),FloatType),param(Id(b),StringType),param(Id(c),StringType),param(Id(d),StringType)],Block([AssignStmt(Id(obj),IntLit(2))])),MethodDecl(Id(method3),Instance,[],Block([AssignStmt(Id(obj),IntLit(3))])),MethodDecl(Id(method4),Instance,[param(Id(a),BoolType),param(Id(b),BoolType),param(Id(c),BoolType)],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,303))
        
    def test_304_type_data_of_params_list(self):
        input = """ 
                    Class Program {
                        method1(a: SomeClass; b, c: Array[Int, 3]) {}
                        method2(a: Array[Array[Float, 3], 3]) {
                            a[1] = 7;
                        }
                        method3(a: Array[Array[Array[String, 3], 4], 5]) {
                            a[a[1]] = 10;
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method1),Instance,[param(Id(a),ClassType(Id(SomeClass))),param(Id(b),ArrayType(3,IntType)),param(Id(c),ArrayType(3,IntType))],Block([])),MethodDecl(Id(method2),Instance,[param(Id(a),ArrayType(3,ArrayType(3,FloatType)))],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1)]),IntLit(7))])),MethodDecl(Id(method3),Instance,[param(Id(a),ArrayType(5,ArrayType(4,ArrayType(3,StringType))))],Block([AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])]),IntLit(10))]))])])"""
        self.assertTrue(TestAST.test(input,expect,304))
        
    def test_305_size_of_array_type_1(self):
        input = """ 
                    Class Program {
                        method1(a: Array[Int, 10]) {
                            Val x: Int;
                        }
                        
                        method2(a: Array[Int, 0x10]) {
                            Var y: Float;
                        }
                        
                        method3(a: Array[Int, 0X10]) {
                            Break;
                        }
                        
                        method4(a: Array[Int, 0b10]) {
                            Continue;
                        }
                        
                        method5(a: Array[Int, 0B10]) {}
                        
                        method6(a: Array[Int, 0100]) {}
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method1),Instance,[param(Id(a),ArrayType(10,IntType))],Block([ConstDecl(Id(x),IntType,None)])),MethodDecl(Id(method2),Instance,[param(Id(a),ArrayType(16,IntType))],Block([VarDecl(Id(y),FloatType)])),MethodDecl(Id(method3),Instance,[param(Id(a),ArrayType(16,IntType))],Block([Break])),MethodDecl(Id(method4),Instance,[param(Id(a),ArrayType(2,IntType))],Block([Continue])),MethodDecl(Id(method5),Instance,[param(Id(a),ArrayType(2,IntType))],Block([])),MethodDecl(Id(method6),Instance,[param(Id(a),ArrayType(64,IntType))],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,305))
        
    def test_306_size_of_array_type_2(self):
        input = """ 
                    Class Program {
                        method1(a: Array[Array[Int, 0XABCDEF], 0XABCDEF1234567890]) {
                            Return;
                        }
                        
                        method2(a: Array[Array[Float, 01234567], 0123]) {
                            Return 7;
                        }
                        
                        method3(a: Array[Array[Boolean, 01234567], 0B101010]) {
                            a.b();
                        }
                        
                        method4(a: Array[Array[String, 01234567], 0B101010]) {
                            Shape::$func();
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method1),Instance,[param(Id(a),ArrayType(12379813812177893520,ArrayType(11259375,IntType)))],Block([Return()])),MethodDecl(Id(method2),Instance,[param(Id(a),ArrayType(83,ArrayType(342391,FloatType)))],Block([Return(IntLit(7))])),MethodDecl(Id(method3),Instance,[param(Id(a),ArrayType(42,ArrayType(342391,BoolType)))],Block([Call(Id(a),Id(b),[])])),MethodDecl(Id(method4),Instance,[param(Id(a),ArrayType(42,ArrayType(342391,StringType)))],Block([Call(Id(Shape),Id($func),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,306))
        
    def test_307_method_declare(self):
        input = """ 
                    Class Program : Parent {
                        method1(){}
                        
                        method2(a: Int; b,c,d: Float) {}
                        
                        $method3() {}
                        
                        $method4(a: SomeClass; b, c: Boolean) {}
                        
                        $method5(a: Array[Int, 0X1ABCD63EF]) {
                            Foreach (x In 1 .. 10 By 20) {
                                Break;
                            }
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),Id(Parent),[MethodDecl(Id(method1),Instance,[],Block([])),MethodDecl(Id(method2),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),FloatType),param(Id(d),FloatType)],Block([])),MethodDecl(Id($method3),Static,[],Block([])),MethodDecl(Id($method4),Static,[param(Id(a),ClassType(Id(SomeClass))),param(Id(b),BoolType),param(Id(c),BoolType)],Block([])),MethodDecl(Id($method5),Static,[param(Id(a),ArrayType(7177331695,IntType))],Block([For(Id(x),IntLit(1),IntLit(10),IntLit(20),Block([Break])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,307))
        
    def test_308_variable_declare_1(self):
        input = """ 
                    Class Program : Parent {
                        Var x: Int;
                        Var y: Float;
                        Var x, y: String;
                        Var m, n, p: Boolean;
                        Var a: Array[Int, 5];
                        Var b: Array[Array[Float, 3], 5];
                        Var c: SomeClass;
                        Var x, y, z: Array[Int, 01234567];
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),Id(Parent),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),FloatType)),AttributeDecl(Instance,VarDecl(Id(x),StringType)),AttributeDecl(Instance,VarDecl(Id(y),StringType)),AttributeDecl(Instance,VarDecl(Id(m),BoolType)),AttributeDecl(Instance,VarDecl(Id(n),BoolType)),AttributeDecl(Instance,VarDecl(Id(p),BoolType)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,ArrayType(3,FloatType)))),AttributeDecl(Instance,VarDecl(Id(c),ClassType(Id(SomeClass)))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(342391,IntType))),AttributeDecl(Instance,VarDecl(Id(y),ArrayType(342391,IntType))),AttributeDecl(Instance,VarDecl(Id(z),ArrayType(342391,IntType)))])])"""
        self.assertTrue(TestAST.test(input,expect,308))
        
    def test_309_variable_declare_2(self):
        input = """ 
                    Class Program : Parent {
                        Val x: Int;
                        Val y: Float;
                        Val x, y: String;
                        Val m, n, p: Boolean;
                        Val a: Array[Int, 5];
                        Val b: Array[Array[Float, 3], 5];
                        Val c: SomeClass;
                        Val x, y, z: Array[Int, 01234567];
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(x),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(y),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(x),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(y),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(m),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(n),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(p),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(5,IntType),None)),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(5,ArrayType(3,FloatType)),None)),AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(SomeClass)),None)),AttributeDecl(Instance,ConstDecl(Id(x),ArrayType(342391,IntType),None)),AttributeDecl(Instance,ConstDecl(Id(y),ArrayType(342391,IntType),None)),AttributeDecl(Instance,ConstDecl(Id(z),ArrayType(342391,IntType),None))])])"""
        self.assertTrue(TestAST.test(input,expect,309))
        
    def test_310_variable_declare_3(self):
        input = """ 
                    Class Program {
                        Var m: Int = 2;
                        Val x, $y, z: String = "Nhan", "Vo", "Nguyen";
                        Var a: Array[Int, 5] = Array(1,2,3,4,5);
                        Val $b: Array[Float, 5] = Array(1,2,3,4,"String");
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(m),IntType,IntLit(2))),AttributeDecl(Instance,ConstDecl(Id(x),StringType,StringLit(Nhan))),AttributeDecl(Static,ConstDecl(Id($y),StringType,StringLit(Vo))),AttributeDecl(Instance,ConstDecl(Id(z),StringType,StringLit(Nguyen))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])),AttributeDecl(Static,ConstDecl(Id($b),ArrayType(5,FloatType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(String)]))])])"""
        self.assertTrue(TestAST.test(input,expect,310))
        
    def test_311_variable_declare_4(self):
        input = """ 
                    Class Program {
                        Var $x, $y: Array[Array[String, 3], 3] = "Vo" + "Thien", !"Nguyen";
                        Val a: Int = arr[1] + arr[2] * arr[3] / arr[4][5][6];
                        Val e, f: Boolean = False, !True;
                        Var $m, $n, p: Int = -9, 0, !7;
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,VarDecl(Id($x),ArrayType(3,ArrayType(3,StringType)),BinaryOp(+,StringLit(Vo),StringLit(Thien)))),AttributeDecl(Static,VarDecl(Id($y),ArrayType(3,ArrayType(3,StringType)),UnaryOp(!,StringLit(Nguyen)))),AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,ArrayCell(Id(arr),[IntLit(1)]),BinaryOp(/,BinaryOp(*,ArrayCell(Id(arr),[IntLit(2)]),ArrayCell(Id(arr),[IntLit(3)])),ArrayCell(Id(arr),[IntLit(4),IntLit(5),IntLit(6)]))))),AttributeDecl(Instance,ConstDecl(Id(e),BoolType,BooleanLit(False))),AttributeDecl(Instance,ConstDecl(Id(f),BoolType,UnaryOp(!,BooleanLit(True)))),AttributeDecl(Static,VarDecl(Id($m),IntType,UnaryOp(-,IntLit(9)))),AttributeDecl(Static,VarDecl(Id($n),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(p),IntType,UnaryOp(!,IntLit(7))))])])"""
        
        self.assertTrue(TestAST.test(input,expect,311))
        
    def test_312_float_literal_1(self):
        input = """ 
                    Class Program {
                        method() {
                            a = 1.2;
                            b = 3.4000;
                            c = 1.2e-10;
                            d = 3.56e+10;
                            e = 12.0;
                            f = 12.00;
                            h = 0.00232e+002;
                            i = 0.00004;
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(Id(a),FloatLit(1.2)),AssignStmt(Id(b),FloatLit(3.4)),AssignStmt(Id(c),FloatLit(1.2e-10)),AssignStmt(Id(d),FloatLit(35600000000.0)),AssignStmt(Id(e),FloatLit(12.0)),AssignStmt(Id(f),FloatLit(12.0)),AssignStmt(Id(h),FloatLit(0.232)),AssignStmt(Id(i),FloatLit(4e-05))]))])])"""
        self.assertTrue(TestAST.test(input,expect,312))
    
    # D96 được nhưng python ko được ??
    def test_313_float_literal_2(self):
        input = """ 
                    Class Program {
                        method() {
                            a = .e10;
                            b = .123e0000;
                            c = .e-10000000;
                            d = .e+00000001;
                            e = .e000000002;
                            f = .e30000000;    
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(Id(a),FloatLit(0.0)),AssignStmt(Id(b),FloatLit(0.123)),AssignStmt(Id(c),FloatLit(0.0)),AssignStmt(Id(d),FloatLit(0.0)),AssignStmt(Id(e),FloatLit(0.0)),AssignStmt(Id(f),FloatLit(0.0))]))])])"""
        self.assertTrue(TestAST.test(input,expect,313))
        
    def test_314_float_literal_3(self):
        input = """ 
                    Class Program {
                        method() {
                            a = 2.e00000000;
                            b = 0.00232e+002;
                            c = 2.e00000000;
                            d = 12.00002;
                            e = 0.0000000e0000000;
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([AssignStmt(Id(a),FloatLit(2.0)),AssignStmt(Id(b),FloatLit(0.232)),AssignStmt(Id(c),FloatLit(2.0)),AssignStmt(Id(d),FloatLit(12.00002)),AssignStmt(Id(e),FloatLit(0.0))]))])])"""
        self.assertTrue(TestAST.test(input,expect,314))
        
    def test_315_foreach_stmt_1(self):
        input = """ 
                    Class Program {
                        method() {
                            Foreach (x In 1 .. 100) {
                                Self.a = 1;
                            }
                            
                            Foreach (x In 1 .. 100 By 2) {
                                Self.b = 2;
                            }
                            
                            Foreach (x In -9 .. -100 By 3) {
                                Self.b = 3;
                            }
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([For(Id(x),IntLit(1),IntLit(100),IntLit(1),Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(1))])]),For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(FieldAccess(Self(),Id(b)),IntLit(2))])]),For(Id(x),UnaryOp(-,IntLit(9)),UnaryOp(-,IntLit(100)),IntLit(3),Block([AssignStmt(FieldAccess(Self(),Id(b)),IntLit(3))])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,315))
        
    def test_316_foreach_stmt_2(self):
        input = """ 
                    Class Program {
                        method() {
                            Foreach (x In arr[1] .. arr[arr[2]]) {}
                            Foreach (x In arr[1] - 12.3 + 5.0 .. arr[1][2][3][4][5]) {}
                            Foreach (x In "Nhan" ..  "Vo" By "LDPV") {
                                {
                                    {
                                        a = 2;
                                    }
                                }
                            }
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([For(Id(x),ArrayCell(Id(arr),[IntLit(1)]),ArrayCell(Id(arr),[ArrayCell(Id(arr),[IntLit(2)])]),IntLit(1),Block([])]),For(Id(x),BinaryOp(+,BinaryOp(-,ArrayCell(Id(arr),[IntLit(1)]),FloatLit(12.3)),FloatLit(5.0)),ArrayCell(Id(arr),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]),IntLit(1),Block([])]),For(Id(x),StringLit(Nhan),StringLit(Vo),StringLit(LDPV),Block([Block([Block([AssignStmt(Id(a),IntLit(2))])])])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,316))
        
    def test_317_break_stmt(self):
        input = """ 
                    Class Program {
                        method() {
                            Break;
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Break]))])])""" 
        self.assertTrue(TestAST.test(input,expect,317))
        
    def test_318_continue_stmt(self):
        input = """ 
                    Class Program {
                        method() {
                            Continue;
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Continue]))])])""" 
        self.assertTrue(TestAST.test(input,expect,318))
        
    def test_319_return_stmt(self):
        input = """ 
                    Class Program {
                        method1() {
                            Return;
                        }
                        
                        method2() {
                            Return 0x123 + 0b1011;
                        }
                        
                        $method3() {
                            Return Array(1,2,3);
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method1),Instance,[],Block([Return()])),MethodDecl(Id(method2),Instance,[],Block([Return(BinaryOp(+,IntLit(291),IntLit(11)))])),MethodDecl(Id($method3),Static,[],Block([Return([IntLit(1),IntLit(2),IntLit(3)])]))])])""" 
        self.assertTrue(TestAST.test(input,expect,319))
        
    def test_320_method_invocation_stmt_1(self):
        input = """ 
                    Class Program {
                        method() {
                            x.func();
                            x.func(a, b);
                            x.func1().func2();
                            x.func1().func2().func3();
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Call(Id(x),Id(func),[]),Call(Id(x),Id(func),[Id(a),Id(b)]),Call(CallExpr(Id(x),Id(func1),[]),Id(func2),[]),Call(CallExpr(CallExpr(Id(x),Id(func1),[]),Id(func2),[]),Id(func3),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,320))
        
    def test_321_method_invocation_stmt_2(self):
        input = """ 
                    Class Program {
                        method() {
                            New X().func();
                            New X().func().func2();
                            (New X().func().objInClass).func2();
                            (Shape::$obj).func();
                            obj.obj2.func();
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Call(NewExpr(Id(X),[]),Id(func),[]),Call(CallExpr(NewExpr(Id(X),[]),Id(func),[]),Id(func2),[]),Call(FieldAccess(CallExpr(NewExpr(Id(X),[]),Id(func),[]),Id(objInClass)),Id(func2),[]),Call(FieldAccess(Id(Shape),Id($obj)),Id(func),[]),Call(FieldAccess(Id(obj),Id(obj2)),Id(func),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,321))
        
    def test_322_method_invocation_stmt_3(self):
        input = """ 
                    Class Program {
                        method() {
                            Shape::$getLength().func1().func2();
                            Shape::$getLength();
                            Shape::$getLength(arr[1]);
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Call(CallExpr(CallExpr(Id(Shape),Id($getLength),[]),Id(func1),[]),Id(func2),[]),Call(Id(Shape),Id($getLength),[]),Call(Id(Shape),Id($getLength),[ArrayCell(Id(arr),[IntLit(1)])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,322))
        
    def test_323_method_invocation_stmt_4(self):
        input = """ 
                    Class Program {
                        method() {
                            a.b(m, "Nhan", 1+2, arr[1][2]).c.d();
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Call(FieldAccess(CallExpr(Id(a),Id(b),[Id(m),StringLit(Nhan),BinaryOp(+,IntLit(1),IntLit(2)),ArrayCell(Id(arr),[IntLit(1),IntLit(2)])]),Id(c)),Id(d),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,323))
        
    def test_324_method_invocation_stmt_5(self):
        input = """ 
                    Class Program {
                        method() {
                            x.func();
                            x.func(a, b, c, d, "nhanvo", 1+2, "str1" + "str2");
                            x.func(a, "nhanvo", 1+2, "str1" + "str2").func2(a, "nhanvo", 1+2, "str1" + "str2");
                            x.func(a, "nhanvo", 1+2, "str1" + "str2").func2(a, "nhanvo", 1+2, "str1" + "str2").func3(a, "nhanvo", 1+2, "str1" + "str2");
                            New X().func();
                            New X().func().func2();
                            (New X().func().objInClass).func2();
                            (Shape::$obj).func();
                            New X().c.func();
                            (arr[1]).c.func();
                            Shape::$obj.obj2.func();
                            obj.obj2.func();
                            ("str" + "str").func();     ## ???? ##
                            Shape::$getLength();
                            Shape::$getLength(a, b, "nhan", 1+2-3*4/5, arr[1]);
                            Shape::$func2(1+2-3*4/5%6);
                            Shape.func().func().func();
                            Shape::$x.y.y.y.func();
                            Shape::$func2().y.y.y.func();
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([Call(Id(x),Id(func),[]),Call(Id(x),Id(func),[Id(a),Id(b),Id(c),Id(d),StringLit(nhanvo),BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(+,StringLit(str1),StringLit(str2))]),Call(CallExpr(Id(x),Id(func),[Id(a),StringLit(nhanvo),BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(+,StringLit(str1),StringLit(str2))]),Id(func2),[Id(a),StringLit(nhanvo),BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(+,StringLit(str1),StringLit(str2))]),Call(CallExpr(CallExpr(Id(x),Id(func),[Id(a),StringLit(nhanvo),BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(+,StringLit(str1),StringLit(str2))]),Id(func2),[Id(a),StringLit(nhanvo),BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(+,StringLit(str1),StringLit(str2))]),Id(func3),[Id(a),StringLit(nhanvo),BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(+,StringLit(str1),StringLit(str2))]),Call(NewExpr(Id(X),[]),Id(func),[]),Call(CallExpr(NewExpr(Id(X),[]),Id(func),[]),Id(func2),[]),Call(FieldAccess(CallExpr(NewExpr(Id(X),[]),Id(func),[]),Id(objInClass)),Id(func2),[]),Call(FieldAccess(Id(Shape),Id($obj)),Id(func),[]),Call(FieldAccess(NewExpr(Id(X),[]),Id(c)),Id(func),[]),Call(FieldAccess(ArrayCell(Id(arr),[IntLit(1)]),Id(c)),Id(func),[]),Call(FieldAccess(FieldAccess(Id(Shape),Id($obj)),Id(obj2)),Id(func),[]),Call(FieldAccess(Id(obj),Id(obj2)),Id(func),[]),Call(BinaryOp(+,StringLit(str),StringLit(str)),Id(func),[]),Call(Id(Shape),Id($getLength),[]),Call(Id(Shape),Id($getLength),[Id(a),Id(b),StringLit(nhan),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(/,BinaryOp(*,IntLit(3),IntLit(4)),IntLit(5))),ArrayCell(Id(arr),[IntLit(1)])]),Call(Id(Shape),Id($func2),[BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(%,BinaryOp(/,BinaryOp(*,IntLit(3),IntLit(4)),IntLit(5)),IntLit(6)))]),Call(CallExpr(CallExpr(Id(Shape),Id(func),[]),Id(func),[]),Id(func),[]),Call(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($x)),Id(y)),Id(y)),Id(y)),Id(func),[]),Call(FieldAccess(FieldAccess(FieldAccess(CallExpr(Id(Shape),Id($func2),[]),Id(y)),Id(y)),Id(y)),Id(func),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,324))
        
    def test_325_main_method_1(self):
        input = """ 
                    Class Program {
                        main() {}
                        main(a: Int) {}
                        method() {}
                        func(b: Float) {}
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([])),MethodDecl(Id(method),Instance,[],Block([])),MethodDecl(Id(func),Instance,[param(Id(b),FloatType)],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,325))
        
    def test_326_main_method_2(self):
        input = """ 
                    Class Program {
                        main() {}
                        main() {}
                        main(a: Int) {}
                    }
                    
                    Class Shapee {
                        main() {}
                        main(b: String) {}
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([]))]),ClassDecl(Id(Shapee),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(b),StringType)],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,326))
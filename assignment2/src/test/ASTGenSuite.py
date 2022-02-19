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
        
    def test_327_expression_1(self):
        input = """ 
                    Class Program : Parent {
                        main() {
                            a = "Nhan" +. "Vo";
                            b = "Nhan" ==. "Vo";
                            c = 0b1110 && 0B1100 || 0b1111;
                            d = 1 == 2;
                            e = 1 < 2;
                            f = 1 > 2;
                            g = 1 <= 2;
                            h = 1 >= 2;
                            i = 1 != 2;
                            j = 1 + 2;
                            k = (-1) - (-2);
                            l = (-1) * (-9);
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),Id(Parent),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(+.,StringLit(Nhan),StringLit(Vo))),AssignStmt(Id(b),BinaryOp(==.,StringLit(Nhan),StringLit(Vo))),AssignStmt(Id(c),BinaryOp(||,BinaryOp(&&,IntLit(14),IntLit(12)),IntLit(15))),AssignStmt(Id(d),BinaryOp(==,IntLit(1),IntLit(2))),AssignStmt(Id(e),BinaryOp(<,IntLit(1),IntLit(2))),AssignStmt(Id(f),BinaryOp(>,IntLit(1),IntLit(2))),AssignStmt(Id(g),BinaryOp(<=,IntLit(1),IntLit(2))),AssignStmt(Id(h),BinaryOp(>=,IntLit(1),IntLit(2))),AssignStmt(Id(i),BinaryOp(!=,IntLit(1),IntLit(2))),AssignStmt(Id(j),BinaryOp(+,IntLit(1),IntLit(2))),AssignStmt(Id(k),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2)))),AssignStmt(Id(l),BinaryOp(*,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(9))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,327))
        
    def test_328_expression_2(self):
        input = """ 
                    Class Program : Parent {
                        main() {
                            a = New X() / 2;
                            b = a[1][2][3] % Array(1,2,3,Array(4,5));
                            c = !Null + (-Self);
                            d = b[c[1][2][3]][4][5];
                            e = obj.func();
                            f = obj.func(1, 1.20, New Shape());
                            g = Shape::$func().method().obj.method();
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),Id(Parent),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(/,NewExpr(Id(X),[]),IntLit(2))),AssignStmt(Id(b),BinaryOp(%,ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),[IntLit(1),IntLit(2),IntLit(3),[IntLit(4),IntLit(5)]])),AssignStmt(Id(c),BinaryOp(+,UnaryOp(!,NullLiteral()),UnaryOp(-,Self()))),AssignStmt(Id(d),ArrayCell(Id(b),[ArrayCell(Id(c),[IntLit(1),IntLit(2),IntLit(3)]),IntLit(4),IntLit(5)])),AssignStmt(Id(e),CallExpr(Id(obj),Id(func),[])),AssignStmt(Id(f),CallExpr(Id(obj),Id(func),[IntLit(1),FloatLit(1.2),NewExpr(Id(Shape),[])])),AssignStmt(Id(g),CallExpr(FieldAccess(CallExpr(CallExpr(Id(Shape),Id($func),[]),Id(method),[]),Id(obj)),Id(method),[]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,328))
        
    def test_329_expression_3(self):
        input = """ 
                    Class Program : Parent {
                        main() {
                            a = Shape::$obj;
                            b = Shape::$func();
                            c = Shape::$func(1, "Nhan", Array(1.2, 3, True, False, !False));
                            d = New X();
                            e = New X(New Shape(), 1.2, Array(New Square()), Array());
                        }
                    }
                    
                """ 
        expect = """Program([ClassDecl(Id(Program),Id(Parent),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),FieldAccess(Id(Shape),Id($obj))),AssignStmt(Id(b),CallExpr(Id(Shape),Id($func),[])),AssignStmt(Id(c),CallExpr(Id(Shape),Id($func),[IntLit(1),StringLit(Nhan),[FloatLit(1.2),IntLit(3),BooleanLit(True),BooleanLit(False),UnaryOp(!,BooleanLit(False))]])),AssignStmt(Id(d),NewExpr(Id(X),[])),AssignStmt(Id(e),NewExpr(Id(X),[NewExpr(Id(Shape),[]),FloatLit(1.2),[NewExpr(Id(Square),[])],[]]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,329))
        
    def test_330_zero_literal(self):
        input = """ 
                    Class Program{
                        main() {
                            a = 0;
                            b = 0X0 - 0;
                            c = -0x0 * 0b0;
                            d = 0B0 + 00;
                            e = 00 - 00 + 0x0;
                            f = 0.0 - 00 + 0 / a[0x0];
                            g = a[0b0] * a[0X0] / a[0B0] + a[00] - a[0] + a[0x0];
                        }
                    }
                    
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),IntLit(0)),AssignStmt(Id(b),BinaryOp(-,IntLit(0),IntLit(0))),AssignStmt(Id(c),BinaryOp(*,UnaryOp(-,IntLit(0)),IntLit(0))),AssignStmt(Id(d),BinaryOp(+,IntLit(0),IntLit(0))),AssignStmt(Id(e),BinaryOp(+,BinaryOp(-,IntLit(0),IntLit(0)),IntLit(0))),AssignStmt(Id(f),BinaryOp(+,BinaryOp(-,FloatLit(0.0),IntLit(0)),BinaryOp(/,IntLit(0),ArrayCell(Id(a),[IntLit(0)])))),AssignStmt(Id(g),BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(/,BinaryOp(*,ArrayCell(Id(a),[IntLit(0)]),ArrayCell(Id(a),[IntLit(0)])),ArrayCell(Id(a),[IntLit(0)])),ArrayCell(Id(a),[IntLit(0)])),ArrayCell(Id(a),[IntLit(0)])),ArrayCell(Id(a),[IntLit(0)])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,330))
        
    def test_331_boolean_literal(self):
        input = """ 
                    Class Program{
                        main() {
                            a = True;
                            b = False;
                            c = !True;
                            d = !False;
                            e = True || !False;
                            f = !True && !False;
                            g = -True;
                            h = -False;
                            i = True + !False - (-False) * True / !False;
                        }
                    }
                    
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BooleanLit(True)),AssignStmt(Id(b),BooleanLit(False)),AssignStmt(Id(c),UnaryOp(!,BooleanLit(True))),AssignStmt(Id(d),UnaryOp(!,BooleanLit(False))),AssignStmt(Id(e),BinaryOp(||,BooleanLit(True),UnaryOp(!,BooleanLit(False)))),AssignStmt(Id(f),BinaryOp(&&,UnaryOp(!,BooleanLit(True)),UnaryOp(!,BooleanLit(False)))),AssignStmt(Id(g),UnaryOp(-,BooleanLit(True))),AssignStmt(Id(h),UnaryOp(-,BooleanLit(False))),AssignStmt(Id(i),BinaryOp(-,BinaryOp(+,BooleanLit(True),UnaryOp(!,BooleanLit(False))),BinaryOp(/,BinaryOp(*,UnaryOp(-,BooleanLit(False)),BooleanLit(True)),UnaryOp(!,BooleanLit(False)))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,331))
        
    def test_332_array_literal(self):
        input = """ 
                    Class Program{
                        main() {
                            Var a: Array[Int, 5] = Array(1, 1.2, Self, Null, a[1][2][3], "Nhan", True, !False);
                            Val b: Array[Float, 4] = Array(1, 2, Array(1, 1.2, Self, Null, a[1][2][3]), 0.0);
                            Var c: Array[String, 3] = Array();
                            Val d: Array[Array[Int, 3], 5] = Array(
                                                                Array(1, 2, "Nhan"),
                                                                Array(1.4, Self, "Nhan"),
                                                                Array(Null, 2, "Nhan"),
                                                                Array(!True, a[1 - a[a[1]]][2], "Nhan"),
                                                                Array(False, 2, "Nhan")
                                                            );
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(5,IntType),[IntLit(1),FloatLit(1.2),Self(),NullLiteral(),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),StringLit(Nhan),BooleanLit(True),UnaryOp(!,BooleanLit(False))]),ConstDecl(Id(b),ArrayType(4,FloatType),[IntLit(1),IntLit(2),[IntLit(1),FloatLit(1.2),Self(),NullLiteral(),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])],FloatLit(0.0)]),VarDecl(Id(c),ArrayType(3,StringType),[]),ConstDecl(Id(d),ArrayType(5,ArrayType(3,IntType)),[[IntLit(1),IntLit(2),StringLit(Nhan)],[FloatLit(1.4),Self(),StringLit(Nhan)],[NullLiteral(),IntLit(2),StringLit(Nhan)],[UnaryOp(!,BooleanLit(True)),ArrayCell(Id(a),[BinaryOp(-,IntLit(1),ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1)])])),IntLit(2)]),StringLit(Nhan)],[BooleanLit(False),IntLit(2),StringLit(Nhan)]])]))])])"""
        self.assertTrue(TestAST.test(input,expect,332))
        
    def test_333_index_operator(self):
        input = """ 
                    Class Program{
                        main() {
                            Var a: Int = arr[1];
                            Val b: Int = arr[1][2];
                            Var c: SomeClass = arr[arr[arr[1]]][2][arr[3]];
                            Var d: SomeClass = arr[1][2][3][4][5][arr[6]];
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,ArrayCell(Id(arr),[IntLit(1)])),ConstDecl(Id(b),IntType,ArrayCell(Id(arr),[IntLit(1),IntLit(2)])),VarDecl(Id(c),ClassType(Id(SomeClass)),ArrayCell(Id(arr),[ArrayCell(Id(arr),[ArrayCell(Id(arr),[IntLit(1)])]),IntLit(2),ArrayCell(Id(arr),[IntLit(3)])])),VarDecl(Id(d),ClassType(Id(SomeClass)),ArrayCell(Id(arr),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5),ArrayCell(Id(arr),[IntLit(6)])]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,333))
        
    def test_334_some_sample_code_1(self):
        input = """ 
                    Class Program {
                        Var $abc: Float = 12.0000;
                        Var arr: Array[Int, 5] = Array (1, 2, 3, 4, 5);
                        Var length: Int = 0;
                        Val $width : Int = 0;
                        
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                            Return;
                        }
                        
                        getLength() {
                            Self.length = 12 - 5 + 5 / 7 * 6 - arr[1];
                            Return Self.length;
                        }
                        
                        $getWidth(a, b: Int; str: String) {
                            Shape::$width = 12 - 5 + 5 / 7 * 6 - arr[4];
                            Return Shape::$width;
                        }
                        
                        main() {
                            Var a: Int = obj.getLength();   ## calling method inside class ##
                            Var b: Int = Shape::$getWidth(a, b, "nhan");   ## calling method inside class ##
                            Return a-b;
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,VarDecl(Id($abc),FloatType,FloatLit(12.0))),AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])),AttributeDecl(Instance,VarDecl(Id(length),IntType,IntLit(0))),AttributeDecl(Static,ConstDecl(Id($width),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType),param(Id(x),StringType),param(Id(y),StringType),param(Id(z),StringType),param(Id(arr),ArrayType(3,IntType))],Block([VarDecl(Id(a),IntType),Return()])),MethodDecl(Id(getLength),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(length)),BinaryOp(-,BinaryOp(+,BinaryOp(-,IntLit(12),IntLit(5)),BinaryOp(*,BinaryOp(/,IntLit(5),IntLit(7)),IntLit(6))),ArrayCell(Id(arr),[IntLit(1)]))),Return(FieldAccess(Self(),Id(length)))])),MethodDecl(Id($getWidth),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(str),StringType)],Block([AssignStmt(FieldAccess(Id(Shape),Id($width)),BinaryOp(-,BinaryOp(+,BinaryOp(-,IntLit(12),IntLit(5)),BinaryOp(*,BinaryOp(/,IntLit(5),IntLit(7)),IntLit(6))),ArrayCell(Id(arr),[IntLit(4)]))),Return(FieldAccess(Id(Shape),Id($width)))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,CallExpr(Id(obj),Id(getLength),[])),VarDecl(Id(b),IntType,CallExpr(Id(Shape),Id($getWidth),[Id(a),Id(b),StringLit(nhan)])),Return(BinaryOp(-,Id(a),Id(b)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,334))
        
    def test_335_some_sample_code_2(self):
        input = """ 
                    Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        
                        $getNumOfShape() {
                            Return Shape::$numOfShape;
                        }
                    }
                    
                    Class Rectangle: Shape {
                        getArea() {
                            Return Self.length * Self.width;
                        }
                    }
                    
                    Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(FieldAccess(Id(Shape),Id($numOfShape)))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"""
        self.assertTrue(TestAST.test(input,expect,335))
        
    def test_336_some_sample_code_3(self):
        input = """ 
                    Class Program {
                        Var arr: Array[Array[Int, 5], 5] = Array (
                                                            Array(1,2,3,4,54),
                                                            Array(1,2,3,4,55),
                                                            Array(1,2,3,4,56),
                                                            Array(1,2,3,4,57),
                                                            Array(1,2,3,4,58)
                                                                );
                        main() {
                            Var arr: Array[Array[Array[Int, 2], 1], 2] 
                                = Array (
                                    Array(
                                        Array(1,2)
                                    ),
                                    Array (
                                        Array(3,4)
                                    )
                                );
                                
                            Val arr: Array[Int, 0b111];
                            Var arr: Array[Int, 0x123];
                            Val arr: Array[Int, 0xABCD];
                            Var arr: Array[Int, 0XEF099];
                            Var arr: Array[Int, 0123];
                            Val arr: Array[Int, 0456];
                            Var arr: Array[Int, 100];
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(5,ArrayType(5,IntType)),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(54)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(55)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(56)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(57)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(58)]])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(arr),ArrayType(2,ArrayType(1,ArrayType(2,IntType))),[[[IntLit(1),IntLit(2)]],[[IntLit(3),IntLit(4)]]]),ConstDecl(Id(arr),ArrayType(7,IntType),None),VarDecl(Id(arr),ArrayType(291,IntType)),ConstDecl(Id(arr),ArrayType(43981,IntType),None),VarDecl(Id(arr),ArrayType(979097,IntType)),VarDecl(Id(arr),ArrayType(83,IntType)),ConstDecl(Id(arr),ArrayType(302,IntType),None),VarDecl(Id(arr),ArrayType(100,IntType))]))])])"""
        self.assertTrue(TestAST.test(input,expect,336))
        
    def test_337_some_sample_code_4(self):
        input = """ 
                    Class Shape {
                        main() {
                            a = Array();
                            Shape::$b = Array (
                                    Array("Volvo", "22", "18"),
                                    Array("Saab", "5", "2"),
                                    Array("Land Rover", "17", "15")
                                );
                            arr[arr[arr[3+4]]] = Array (
                                    Array("Volvo", "22", "18"),
                                    Array("Saab", "5", "2"),
                                    Array("Land Rover", "17", "15")
                                );
                        }
                    }
        
                    Class Program : Shape {
                        Var obj: Shape = Null;
                        
                        Constructor() {
                            Self.obj = New Shape(New Shape(a, b, c));
                            Return Self.obj;
                        }
                        
                        Destructor() {
                            Self.obj = Null;
                        }
                        
                        main() {
                            Val x, y,  z: Int = Null, Null, Null;
                            Var obj: Shape = New Shape(Null);
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Shape),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),[]),AssignStmt(FieldAccess(Id(Shape),Id($b)),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]]),AssignStmt(ArrayCell(Id(arr),[ArrayCell(Id(arr),[ArrayCell(Id(arr),[BinaryOp(+,IntLit(3),IntLit(4))])])]),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])]))]),ClassDecl(Id(Program),Id(Shape),[AttributeDecl(Instance,VarDecl(Id(obj),ClassType(Id(Shape)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(obj)),NewExpr(Id(Shape),[NewExpr(Id(Shape),[Id(a),Id(b),Id(c)])])),Return(FieldAccess(Self(),Id(obj)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(obj)),NullLiteral())])),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(x),IntType,NullLiteral()),ConstDecl(Id(y),IntType,NullLiteral()),ConstDecl(Id(z),IntType,NullLiteral()),VarDecl(Id(obj),ClassType(Id(Shape)),NewExpr(Id(Shape),[NullLiteral()]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,337))
        
    def test_338_some_sample_code_5(self):
        input = """ 
                    Class Program {
                        Var x: Array[Boolean, 1];
                        Var x: Array[String, 1] = ____[True && False -45 + 2 / 2];
                        Var x: Array[Float, 1] = _["nhan" - 12 + 4];
                        Var x, $y: Array[Int, 1] = "Nhan", "Vo";
                        
                        main() {
                            x = 1[1];
                            x = 1.23434e+10[1];
                            x = 1.23434e+10[12/3%2-4514+34141];
                            x = True[Null];
                            x = 1[1.000000000];
                            x = 1_2_3_4_5_6[Array(1,2,3,4,"nhan")];
                            x = 1_2_3_4_5_6.e-00000000[Array(1,2,3,4,"nhan")];
                            x = 0[Array(1,2,3,4,"nhan")];
                            x = 00[Array(1,2,3,4,"nhan")];
                            x = 0b0[Array(1,2,3,4,"nhan")];
                            x = 0B0[Array(1,2,3,4,"nhan")];
                            x = 0x0[Array(1,2,3,4,"nhan")];
                            x = 0X0[Array(1,2,3,4,"nhan")];
                            x = New X()[2];
                            x = !New X()[2];
                            x = -New X()[2];
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),ArrayType(1,BoolType))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(1,StringType),ArrayCell(Id(____),[BinaryOp(&&,BooleanLit(True),BinaryOp(+,BinaryOp(-,BooleanLit(False),IntLit(45)),BinaryOp(/,IntLit(2),IntLit(2))))]))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(1,FloatType),ArrayCell(Id(_),[BinaryOp(+,BinaryOp(-,StringLit(nhan),IntLit(12)),IntLit(4))]))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(1,IntType),StringLit(Nhan))),AttributeDecl(Static,VarDecl(Id($y),ArrayType(1,IntType),StringLit(Vo))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(x),ArrayCell(IntLit(1),[IntLit(1)])),AssignStmt(Id(x),ArrayCell(FloatLit(12343400000.0),[IntLit(1)])),AssignStmt(Id(x),ArrayCell(FloatLit(12343400000.0),[BinaryOp(+,BinaryOp(-,BinaryOp(%,BinaryOp(/,IntLit(12),IntLit(3)),IntLit(2)),IntLit(4514)),IntLit(34141))])),AssignStmt(Id(x),ArrayCell(BooleanLit(True),[NullLiteral()])),AssignStmt(Id(x),ArrayCell(IntLit(1),[FloatLit(1.0)])),AssignStmt(Id(x),ArrayCell(IntLit(123456),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]])),AssignStmt(Id(x),ArrayCell(FloatLit(123456.0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]])),AssignStmt(Id(x),ArrayCell(IntLit(0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]])),AssignStmt(Id(x),ArrayCell(IntLit(0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]])),AssignStmt(Id(x),ArrayCell(IntLit(0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]])),AssignStmt(Id(x),ArrayCell(IntLit(0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]])),AssignStmt(Id(x),ArrayCell(IntLit(0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]])),AssignStmt(Id(x),ArrayCell(IntLit(0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]])),AssignStmt(Id(x),ArrayCell(NewExpr(Id(X),[]),[IntLit(2)])),AssignStmt(Id(x),UnaryOp(!,ArrayCell(NewExpr(Id(X),[]),[IntLit(2)]))),AssignStmt(Id(x),UnaryOp(-,ArrayCell(NewExpr(Id(X),[]),[IntLit(2)])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,338))
        
    def test_339_some_sample_code_6(self):
        input = """ 
                    Class Program {
                        Var x: Array[Boolean, 1];
                        Var x: Array[String, 1] = ____[True && False -45 + 2 / 2];
                        Var x: Array[Float, 1] = _["nhan" - 12 + 4];
                        Var x, $y: Array[Int, 1] = "Nhan", "Vo";
                        
                        main() {
                            x = (123).func();
                            x = (1_234_456_789).func().func();
                            x = (1_234_456_789.10e-10000000).func();
                            x = "string".func();
                            x = Null.func();
                            x = True.func();
                            x = someID::$attribute.func();
                            x = someID::$func(a,b,c,Null).func();
                            x = Array(1,2,3,4,5,6).func();
                            x = Array(Array(1,2,3), Array(4,5), Array("nhan", "vo", "nguyen")).func();
                            x = Shape::$func(xyz).func();
                            x = (0).func();
                            x = (0b0).func();
                            x = (0B0).func();
                            x = (0x0).func();
                            x = (0X0).func();
                            x = (00).func();
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),ArrayType(1,BoolType))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(1,StringType),ArrayCell(Id(____),[BinaryOp(&&,BooleanLit(True),BinaryOp(+,BinaryOp(-,BooleanLit(False),IntLit(45)),BinaryOp(/,IntLit(2),IntLit(2))))]))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(1,FloatType),ArrayCell(Id(_),[BinaryOp(+,BinaryOp(-,StringLit(nhan),IntLit(12)),IntLit(4))]))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(1,IntType),StringLit(Nhan))),AttributeDecl(Static,VarDecl(Id($y),ArrayType(1,IntType),StringLit(Vo))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(x),CallExpr(IntLit(123),Id(func),[])),AssignStmt(Id(x),CallExpr(CallExpr(IntLit(1234456789),Id(func),[]),Id(func),[])),AssignStmt(Id(x),CallExpr(FloatLit(0.0),Id(func),[])),AssignStmt(Id(x),CallExpr(StringLit(string),Id(func),[])),AssignStmt(Id(x),CallExpr(NullLiteral(),Id(func),[])),AssignStmt(Id(x),CallExpr(BooleanLit(True),Id(func),[])),AssignStmt(Id(x),CallExpr(FieldAccess(Id(someID),Id($attribute)),Id(func),[])),AssignStmt(Id(x),CallExpr(CallExpr(Id(someID),Id($func),[Id(a),Id(b),Id(c),NullLiteral()]),Id(func),[])),AssignStmt(Id(x),CallExpr([IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5),IntLit(6)],Id(func),[])),AssignStmt(Id(x),CallExpr([[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5)],[StringLit(nhan),StringLit(vo),StringLit(nguyen)]],Id(func),[])),AssignStmt(Id(x),CallExpr(CallExpr(Id(Shape),Id($func),[Id(xyz)]),Id(func),[])),AssignStmt(Id(x),CallExpr(IntLit(0),Id(func),[])),AssignStmt(Id(x),CallExpr(IntLit(0),Id(func),[])),AssignStmt(Id(x),CallExpr(IntLit(0),Id(func),[])),AssignStmt(Id(x),CallExpr(IntLit(0),Id(func),[])),AssignStmt(Id(x),CallExpr(IntLit(0),Id(func),[])),AssignStmt(Id(x),CallExpr(IntLit(0),Id(func),[]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,339))
        
    def test_340_some_sample_code_7(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        
                        main() {
                            x = Array();
                            Shape::$x = Shape::$obj.obj2.pbj3.func();
                            a.b = Shape::$obj.obj2.pbj3.func();
                            a.b().a = Shape::$obj.obj2.pbj3.func();
                            a.b(a,True,Array(1,2,3)).attr = Shape::$obj.obj2.pbj3.func();
                            a.b(a,True,Array(1,2,3)).attr = Shape::$obj.obj2.pbj3.func();
                            Shape::$attr = Shape::$obj.obj2.pbj3.func();
                            Shape::$attr.func().attr = Shape::$obj.obj2.pbj3.func();
                            Shape::$attr.attr.func().attr = Shape::$obj.obj2.obj3.func();
                            Shape::$attr.attr.attr.attr.func().attr = Shape::$obj.obj2.pbj3.func();
                            Shape::$attr.attr.attr.attr.func().func().func().attr = Shape::$obj.obj2.pbj3.func();
                            1[1]                                          = Shape::$obj.func();          
                            1.23434e+10[1]                                = Shape::$obj.func();      
                            1.23434e+10[12/3%2-4514+34141]                = Shape::$obj.func();      
                            True[Null]                                    = Shape::$obj.func();      
                            1[1.000000000]                                = Shape::$obj.func();      
                            1_2_3_4_5_6[Array(1,2,3,4,"nhan")]            = Shape::$obj.func();  
                            1_2_3_4_5_6.e-00000000[Array(1,2,3,4,"nhan")] = Shape::$obj.func(); 
                            0[Array(1,2,3,4,"nhan")]                      = Shape::$obj.func();  
                            00[Array(1,2,3,4,"nhan")]                     = Shape::$obj.func();
                            0B0[Array(1,2,3,4,"nhan")]                    = Shape::$obj.func();  
                            0x0[Array(1,2,3,4,"nhan")]                    = Shape::$obj.func();      
                            0X0[Array(1,2,3,4,"nhan")]                    = Shape::$obj.func();      
                            New X()[2]                                    = Shape::$obj.func();      
                            New X()[2]                                   = Shape::$obj.func();          
                            New X()[2]                                   = Shape::$obj.func();      
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(5))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(x),[]),AssignStmt(FieldAccess(Id(Shape),Id($x)),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($obj)),Id(obj2)),Id(pbj3)),Id(func),[])),AssignStmt(FieldAccess(Id(a),Id(b)),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($obj)),Id(obj2)),Id(pbj3)),Id(func),[])),AssignStmt(FieldAccess(CallExpr(Id(a),Id(b),[]),Id(a)),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($obj)),Id(obj2)),Id(pbj3)),Id(func),[])),AssignStmt(FieldAccess(CallExpr(Id(a),Id(b),[Id(a),BooleanLit(True),[IntLit(1),IntLit(2),IntLit(3)]]),Id(attr)),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($obj)),Id(obj2)),Id(pbj3)),Id(func),[])),AssignStmt(FieldAccess(CallExpr(Id(a),Id(b),[Id(a),BooleanLit(True),[IntLit(1),IntLit(2),IntLit(3)]]),Id(attr)),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($obj)),Id(obj2)),Id(pbj3)),Id(func),[])),AssignStmt(FieldAccess(Id(Shape),Id($attr)),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($obj)),Id(obj2)),Id(pbj3)),Id(func),[])),AssignStmt(FieldAccess(CallExpr(FieldAccess(Id(Shape),Id($attr)),Id(func),[]),Id(attr)),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($obj)),Id(obj2)),Id(pbj3)),Id(func),[])),AssignStmt(FieldAccess(CallExpr(FieldAccess(FieldAccess(Id(Shape),Id($attr)),Id(attr)),Id(func),[]),Id(attr)),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($obj)),Id(obj2)),Id(obj3)),Id(func),[])),AssignStmt(FieldAccess(CallExpr(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($attr)),Id(attr)),Id(attr)),Id(attr)),Id(func),[]),Id(attr)),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($obj)),Id(obj2)),Id(pbj3)),Id(func),[])),AssignStmt(FieldAccess(CallExpr(CallExpr(CallExpr(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($attr)),Id(attr)),Id(attr)),Id(attr)),Id(func),[]),Id(func),[]),Id(func),[]),Id(attr)),CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Shape),Id($obj)),Id(obj2)),Id(pbj3)),Id(func),[])),AssignStmt(ArrayCell(IntLit(1),[IntLit(1)]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(FloatLit(12343400000.0),[IntLit(1)]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(FloatLit(12343400000.0),[BinaryOp(+,BinaryOp(-,BinaryOp(%,BinaryOp(/,IntLit(12),IntLit(3)),IntLit(2)),IntLit(4514)),IntLit(34141))]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(BooleanLit(True),[NullLiteral()]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(IntLit(1),[FloatLit(1.0)]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(IntLit(123456),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(FloatLit(123456.0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(IntLit(0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(IntLit(0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(IntLit(0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(IntLit(0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(IntLit(0),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),StringLit(nhan)]]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(NewExpr(Id(X),[]),[IntLit(2)]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(NewExpr(Id(X),[]),[IntLit(2)]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[])),AssignStmt(ArrayCell(NewExpr(Id(X),[]),[IntLit(2)]),CallExpr(FieldAccess(Id(Shape),Id($obj)),Id(func),[]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,340))
        
    def test_341_some_sample_code_8(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            x = 1.e+101010101 - 0b10101011;
                            x = "nhan" +. 0xABCD;
                            x = "vo" ==. 123;
                            x = Array(1,2,3,4) + 4%3/arr[1] + Null._123_4534_4823_42374893;
                            x = Array(Array(1,2), Array()) - !!!!!!!!!!!-------------------True;
                            x = Shape::$calling_method();
                            x = Shape::$calling_method(a-b%c+d, Array(1,2,Array(3,4)), New Shape(), Shape::$func(), 0x0, 00, 0b0);
                            x = a.calling_method(1 > 2, 2 < 3, 3 <= 4, 5 >= 3, 5 != 3, 5 == 3, 1.2 +. 3.e1, 0xAB123 ==. 0b1010101);                        
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),ArrayType(1,ArrayType(1,IntType)),[])),AttributeDecl(Static,ConstDecl(Id($x),StringType,StringLit(nhan))),AttributeDecl(Instance,ConstDecl(Id(y),StringType,BinaryOp(+,FloatLit(1.0),StringLit(nhan)))),AttributeDecl(Static,ConstDecl(Id($z),StringType,BinaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,BooleanLit(True)))),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,BooleanLit(False))))))))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(x),BinaryOp(-,FloatLit(inf),IntLit(171))),AssignStmt(Id(x),BinaryOp(+.,StringLit(nhan),IntLit(43981))),AssignStmt(Id(x),BinaryOp(==.,StringLit(vo),IntLit(123))),AssignStmt(Id(x),BinaryOp(+,BinaryOp(+,[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],BinaryOp(/,BinaryOp(%,IntLit(4),IntLit(3)),ArrayCell(Id(arr),[IntLit(1)]))),FieldAccess(NullLiteral(),Id(_123_4534_4823_42374893)))),AssignStmt(Id(x),BinaryOp(-,[[IntLit(1),IntLit(2)],[]],UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,BooleanLit(True))))))))))))))))))))))))))))))))),AssignStmt(Id(x),CallExpr(Id(Shape),Id($calling_method),[])),AssignStmt(Id(x),CallExpr(Id(Shape),Id($calling_method),[BinaryOp(+,BinaryOp(-,Id(a),BinaryOp(%,Id(b),Id(c))),Id(d)),[IntLit(1),IntLit(2),[IntLit(3),IntLit(4)]],NewExpr(Id(Shape),[]),CallExpr(Id(Shape),Id($func),[]),IntLit(0),IntLit(0),IntLit(0)])),AssignStmt(Id(x),CallExpr(Id(a),Id(calling_method),[BinaryOp(>,IntLit(1),IntLit(2)),BinaryOp(<,IntLit(2),IntLit(3)),BinaryOp(<=,IntLit(3),IntLit(4)),BinaryOp(>=,IntLit(5),IntLit(3)),BinaryOp(!=,IntLit(5),IntLit(3)),BinaryOp(==,IntLit(5),IntLit(3)),BinaryOp(+.,FloatLit(1.2),FloatLit(30.0)),BinaryOp(==.,IntLit(700707),IntLit(85))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,341))
        
    def test_342_blockStmt_in_blockStmt(self):
        input = """ 
                    Class Program {
                        main() {
                            ## Here is a block stmt inside another block stmt ##
                            {
                                {
                                    {
                                        {
                                            {
                                                Return "NHAN VO" +. "LDPV";
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([Block([Block([Block([Block([Return(BinaryOp(+.,StringLit(NHAN VO),StringLit(LDPV)))])])])])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,342))
        
    def test_343_code_related_Lexer(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            x = "My name is Nhan. This name has two \\'N\\' characters";
                            input = "He asked me: '"Where is John?'"";
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),ArrayType(1,ArrayType(1,IntType)),[])),AttributeDecl(Static,ConstDecl(Id($x),StringType,StringLit(nhan))),AttributeDecl(Instance,ConstDecl(Id(y),StringType,BinaryOp(+,FloatLit(1.0),StringLit(nhan)))),AttributeDecl(Static,ConstDecl(Id($z),StringType,BinaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,BooleanLit(True)))),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,BooleanLit(False))))))))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(x),StringLit(My name is Nhan. This name has two \\'N\\' characters)),AssignStmt(Id(input),StringLit(He asked me: '"Where is John?'"))]))])])"""
        self.assertTrue(TestAST.test(input,expect,343))
        
    def test_344_some_sample_code_9(self):
        input = """ 
                    Class Program {
                        main() {
                            Var x: Int;
                            Var x: Int = 5;
                            Var x, y: Int = 5, 6;
                            Var x, y, z: Int = -5, ------------6, "nhanvo" + "vo" + "nguyen" + "thien";
                            Var x, y, z: Int = 5, 6, New Shape(New Shape(New Shape(New Shape(New Shape(New Shape(12, 3))))));
                            Var x: Array[Array[Int, 3], 3] = Array (Array(1,2,3), Array(4,5,6), Array(8,9,10));
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType),VarDecl(Id(x),IntType,IntLit(5)),VarDecl(Id(x),IntType,IntLit(5)),VarDecl(Id(y),IntType,IntLit(6)),VarDecl(Id(x),IntType,UnaryOp(-,IntLit(5))),VarDecl(Id(y),IntType,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(6)))))))))))))),VarDecl(Id(z),IntType,BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLit(nhanvo),StringLit(vo)),StringLit(nguyen)),StringLit(thien))),VarDecl(Id(x),IntType,IntLit(5)),VarDecl(Id(y),IntType,IntLit(6)),VarDecl(Id(z),IntType,NewExpr(Id(Shape),[NewExpr(Id(Shape),[NewExpr(Id(Shape),[NewExpr(Id(Shape),[NewExpr(Id(Shape),[NewExpr(Id(Shape),[IntLit(12),IntLit(3)])])])])])])),VarDecl(Id(x),ArrayType(3,ArrayType(3,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)],[IntLit(8),IntLit(9),IntLit(10)]])]))])])"""
        self.assertTrue(TestAST.test(input,expect,344))
        
    def test_345_some_sample_code_10(self):
        input = """ 
                    Class Shape {
                        
                    }
                    
                    Class Program {
                        main() {
                            a = New Shape();
                            a = New Shape(a, "nhanvo", 12+5-12*23, 8/2);
                            a = New Shape(New Shape(12, 3));
                            a = New Shape(New Shape(New Shape(New Shape(New Shape(New Shape(12, 3))))));
                            a = New Shape(arr[arr[arr[1]]][2]);
                            a = New Shape(Shape.length, Shape.arr[arr[arr[2]]], obj.getLength(12, 3));
                            a = (New Shape())[arr[1]];
                            a = (New Shape()).a.a.a.a;
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Shape),[]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(Shape),[])),AssignStmt(Id(a),NewExpr(Id(Shape),[Id(a),StringLit(nhanvo),BinaryOp(-,BinaryOp(+,IntLit(12),IntLit(5)),BinaryOp(*,IntLit(12),IntLit(23))),BinaryOp(/,IntLit(8),IntLit(2))])),AssignStmt(Id(a),NewExpr(Id(Shape),[NewExpr(Id(Shape),[IntLit(12),IntLit(3)])])),AssignStmt(Id(a),NewExpr(Id(Shape),[NewExpr(Id(Shape),[NewExpr(Id(Shape),[NewExpr(Id(Shape),[NewExpr(Id(Shape),[NewExpr(Id(Shape),[IntLit(12),IntLit(3)])])])])])])),AssignStmt(Id(a),NewExpr(Id(Shape),[ArrayCell(Id(arr),[ArrayCell(Id(arr),[ArrayCell(Id(arr),[IntLit(1)])]),IntLit(2)])])),AssignStmt(Id(a),NewExpr(Id(Shape),[FieldAccess(Id(Shape),Id(length)),ArrayCell(FieldAccess(Id(Shape),Id(arr)),[ArrayCell(Id(arr),[ArrayCell(Id(arr),[IntLit(2)])])]),CallExpr(Id(obj),Id(getLength),[IntLit(12),IntLit(3)])])),AssignStmt(Id(a),ArrayCell(NewExpr(Id(Shape),[]),[ArrayCell(Id(arr),[IntLit(1)])])),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(FieldAccess(NewExpr(Id(Shape),[]),Id(a)),Id(a)),Id(a)),Id(a)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,345))
        
    def test_346_some_sample_code_111(self):
        input = """ 
                    Class Program {
                        Var x: Int;
                        Var arr: Array[Array[Int, 1], 1] = some_arr[1][another_arr[2]];
                        Var $length: Float;
                        Var $width: Float;
                        
                        Constructor() {
                            Shape::$length = 12;
                            Shape::$width = 12;
                        }
                        
                        Constructor(l, w: Float) {
                            Shape::$length = l;
                            Shape::$width = w;
                        }
                        
                        $getLength() {
                            Return Shape::$length;
                        }
                        
                        $getWidth() {
                            Return Shape::$width;
                        }
                        
                        main() {
                            Var obj: Shape = New Shape(20, 20);
                            Var l: Float = Shape::$getLength();
                            Var l2: Float = Program::$getLength();
                            Var w: Float = Shape::$getWidth();
                            Var w2: Float = Program::$getWidth();
                            
                            Foreach (x In 5 .. 2) {
                                obj.printInt(arr[x]);
                            }
                            Break;
                            Continue;
                            Return;
                            Return Program::$getLength();
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1,ArrayType(1,IntType)),ArrayCell(Id(some_arr),[IntLit(1),ArrayCell(Id(another_arr),[IntLit(2)])]))),AttributeDecl(Static,VarDecl(Id($length),FloatType)),AttributeDecl(Static,VarDecl(Id($width),FloatType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Shape),Id($length)),IntLit(12)),AssignStmt(FieldAccess(Id(Shape),Id($width)),IntLit(12))])),MethodDecl(Id(Constructor),Instance,[param(Id(l),FloatType),param(Id(w),FloatType)],Block([AssignStmt(FieldAccess(Id(Shape),Id($length)),Id(l)),AssignStmt(FieldAccess(Id(Shape),Id($width)),Id(w))])),MethodDecl(Id($getLength),Static,[],Block([Return(FieldAccess(Id(Shape),Id($length)))])),MethodDecl(Id($getWidth),Static,[],Block([Return(FieldAccess(Id(Shape),Id($width)))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(obj),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(20),IntLit(20)])),VarDecl(Id(l),FloatType,CallExpr(Id(Shape),Id($getLength),[])),VarDecl(Id(l2),FloatType,CallExpr(Id(Program),Id($getLength),[])),VarDecl(Id(w),FloatType,CallExpr(Id(Shape),Id($getWidth),[])),VarDecl(Id(w2),FloatType,CallExpr(Id(Program),Id($getWidth),[])),For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(obj),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])]),Break,Continue,Return(),Return(CallExpr(Id(Program),Id($getLength),[]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,346))
        
    def test_347_variable_declare_5(self):
        input = """ 
                    Class Program {
                        Var x, y, $z: Int;
                        Val a, $b, c: Float;
                        Var m, n, p: String;
                        Var $m, $n, $p: Boolean;
                        Val $i, $j, $k: SomeClass;
                        
                        main() {
                            Var x, y, z: Int;
                            Val a, b, c: Float;
                            Var m, n, p: String;
                            Var m, n, p: Boolean;
                            Val i, j, k: SomeClass;
                        }
                        
                        $main() {}
                        $method() {}
                        method() {}
                        
                        $main(a: Int; b: SomeClass; c, d: Array[Int, 5]; e: Boolean) {}
                        $method(a: Float; b: SomeClass; c, d: Array[Int, 5]; e: String) {}
                        method(a: Array[Array[Float, 5], 5]; b: SomeClass; c, d: Array[Int, 5]; e: Boolean) {}
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),IntType)),AttributeDecl(Static,VarDecl(Id($z),IntType)),AttributeDecl(Instance,ConstDecl(Id(a),FloatType,None)),AttributeDecl(Static,ConstDecl(Id($b),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,None)),AttributeDecl(Instance,VarDecl(Id(m),StringType)),AttributeDecl(Instance,VarDecl(Id(n),StringType)),AttributeDecl(Instance,VarDecl(Id(p),StringType)),AttributeDecl(Static,VarDecl(Id($m),BoolType)),AttributeDecl(Static,VarDecl(Id($n),BoolType)),AttributeDecl(Static,VarDecl(Id($p),BoolType)),AttributeDecl(Static,ConstDecl(Id($i),ClassType(Id(SomeClass)),None)),AttributeDecl(Static,ConstDecl(Id($j),ClassType(Id(SomeClass)),None)),AttributeDecl(Static,ConstDecl(Id($k),ClassType(Id(SomeClass)),None)),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType),VarDecl(Id(y),IntType),VarDecl(Id(z),IntType),ConstDecl(Id(a),FloatType,None),ConstDecl(Id(b),FloatType,None),ConstDecl(Id(c),FloatType,None),VarDecl(Id(m),StringType),VarDecl(Id(n),StringType),VarDecl(Id(p),StringType),VarDecl(Id(m),BoolType),VarDecl(Id(n),BoolType),VarDecl(Id(p),BoolType),ConstDecl(Id(i),ClassType(Id(SomeClass)),None),ConstDecl(Id(j),ClassType(Id(SomeClass)),None),ConstDecl(Id(k),ClassType(Id(SomeClass)),None)])),MethodDecl(Id($main),Static,[],Block([])),MethodDecl(Id($method),Static,[],Block([])),MethodDecl(Id(method),Instance,[],Block([])),MethodDecl(Id($main),Static,[param(Id(a),IntType),param(Id(b),ClassType(Id(SomeClass))),param(Id(c),ArrayType(5,IntType)),param(Id(d),ArrayType(5,IntType)),param(Id(e),BoolType)],Block([])),MethodDecl(Id($method),Static,[param(Id(a),FloatType),param(Id(b),ClassType(Id(SomeClass))),param(Id(c),ArrayType(5,IntType)),param(Id(d),ArrayType(5,IntType)),param(Id(e),StringType)],Block([])),MethodDecl(Id(method),Instance,[param(Id(a),ArrayType(5,ArrayType(5,FloatType))),param(Id(b),ClassType(Id(SomeClass))),param(Id(c),ArrayType(5,IntType)),param(Id(d),ArrayType(5,IntType)),param(Id(e),BoolType)],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,347))
        
    def test_348_some_array(self):
        input = """ 
                    Class Program {
                        main() {
                            a = Array();
                            Shape::$b = Array (
                                    Array("Volvo", "22", "18"),
                                    Array("Saab", "5", "2"),
                                    Array("Land Rover", "17", "15")
                                );
                            arr[arr[arr[3+4]]] = Array (
                                    Array("Volvo", "22", "18"),
                                    Array("Saab", "5", "2"),
                                    Array("Land Rover", "17", "15")
                                );
                            Var arr: Array[Array[Int, 3], 3] = Array (
                                                            Array (3,4,5),
                                                            Array (6,7,8),
                                                            Array (9,10,11)
                                                                );
                            Var x: Array[Array[Int, 3], 3] = Array (Array(1,2,3), Array(4,5,6), Array(8,9,10));
                            Shape::$b = Array (
                                    Array("Volvo", "22", "18"),
                                    Array("Saab", "5", "2"),
                                    Array("Land Rover", "17", "15")
                                );
                            arr[arr[arr[3+4]]] = Array (
                                    Array("Volvo", "22", "18"),
                                    Array("Saab", "5", "2"),
                                    Array("Land Rover", "17", "15")
                                );
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),[]),AssignStmt(FieldAccess(Id(Shape),Id($b)),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]]),AssignStmt(ArrayCell(Id(arr),[ArrayCell(Id(arr),[ArrayCell(Id(arr),[BinaryOp(+,IntLit(3),IntLit(4))])])]),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]]),VarDecl(Id(arr),ArrayType(3,ArrayType(3,IntType)),[[IntLit(3),IntLit(4),IntLit(5)],[IntLit(6),IntLit(7),IntLit(8)],[IntLit(9),IntLit(10),IntLit(11)]]),VarDecl(Id(x),ArrayType(3,ArrayType(3,IntType)),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)],[IntLit(8),IntLit(9),IntLit(10)]]),AssignStmt(FieldAccess(Id(Shape),Id($b)),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]]),AssignStmt(ArrayCell(Id(arr),[ArrayCell(Id(arr),[ArrayCell(Id(arr),[BinaryOp(+,IntLit(3),IntLit(4))])])]),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]])]))])])"""
        self.assertTrue(TestAST.test(input,expect,348))
        
    def test_349_some_array(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        
                        main() {
                            x = 2 + Array(1,2);
                            x = Num + "123";
                            x = Array(1,2,3) + Array(Array(1,2,3), Array(4,5,6,7,8,9));
                            x = 1 + Array(Array(Shape::$attribute,2,3), Array(obj.getLength(),5,Shape::$func(a,b,c,d),7,8,a.func()));
                        }
                    }
                """ 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(5))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(x),BinaryOp(+,IntLit(2),[IntLit(1),IntLit(2)])),AssignStmt(Id(x),BinaryOp(+,Id(Num),StringLit(123))),AssignStmt(Id(x),BinaryOp(+,[IntLit(1),IntLit(2),IntLit(3)],[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6),IntLit(7),IntLit(8),IntLit(9)]])),AssignStmt(Id(x),BinaryOp(+,IntLit(1),[[FieldAccess(Id(Shape),Id($attribute)),IntLit(2),IntLit(3)],[CallExpr(Id(obj),Id(getLength),[]),IntLit(5),CallExpr(Id(Shape),Id($func),[Id(a),Id(b),Id(c),Id(d)]),IntLit(7),IntLit(8),CallExpr(Id(a),Id(func),[])]]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,349))
    
    
    # def test_350_example(self):
    #     input = """ 
    #                 Class Program {
    #                     main() {
    #                         a = Array();
    #                     }
    #                 }
    #             """ 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,350))
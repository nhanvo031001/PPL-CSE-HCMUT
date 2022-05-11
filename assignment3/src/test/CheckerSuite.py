import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_400_no_entry_point_1(self):
        input = """
            Class Program{

            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_401_no_entry_point_2(self):
        input = """
            Class A{
                main() {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402_no_entry_point_3(self):
        input = """
            Class Program{
                main(a: Int; b,c: String) {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_403_no_entry_point_4(self):
        input = """
            Class A{
                main() {}
            }
            Class Program{
                main(a: Int; b,c: String) {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404_no_entry_point_5(self):
        input = """
            Class Program{
                main(a: Int; b,c: String) {}
                main() {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405_no_entry_point_6(self):
        input = """
            Class Program{
                main() {}
                main(a: Int; b,c: String) {}
            }
        """
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406_redeclared_variable_1(self):
        input = """
            Class Program{
                main() {
                    Var a : Int;
                    Var a : Float = 1.2;
                }
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_407_redeclared_variable_2(self):
        input = """
            Class Program{
                main() {}
                func(a, b: Int) {
                    Var a : Int;
                }
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_408_redeclared_variable_3(self):
        input = """
            Class Program{
                main() {
                    Val a : Int = 1;
                    Var a : String;
                }
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test_409_redeclared_constant_1(self):
        input = """
            Class Program{
                main() {
                    Val a : Int = 1;
                    Val a : String = "Nhan";
                }
            }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 409))
        
    def test_410_redeclared_constant_2(self):
        input = """
            Class Program{
                main(a, b:Int) {
                    Val a : Float = 1.3;
                }
            }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test_411_redeclared_constant_3(self):
        input = """
            Class Program{
                main() {
                    Var a : Float = 1.3;
                    Val a : Float = 1.3;
                }
            }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
    def test_412_redeclared_attribute_1(self):
        input = """
            Class Program{
                Var a : Int = 1;
                Var a : Float = 1.4;
                main(){}
            }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test_413_redeclared_attribute_2(self):
        input = """
            Class Program{
                Var a : Int = 1;
                Val a : Float = 1.4;
                main(){}
            }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test_414_redeclared_attribute_3(self):
        input = """
            Class Program{
                Val a : Float = 1.4;
                Var a : Int = 1;
                main(){}
            }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 414))
        
    def test_415_redeclared_attribute_4(self):
        input = """
            Class Program{
                Val a : Float = 1.4;
                Val a : Int = 1;
                main(){}
            }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 415))
        
    def test_416_redeclared_class_1(self):
        input = """
            Class Program{
                main(){}
            }
            Class Program{}
        """
        expect = "Redeclared Class: Program"
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test_417_redeclared_method_1(self):
        input = """
            Class Program {
                Var a : Int;
                a() {}
                a() {}
                main(){}
                
            }
        """
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
    def test_418_redeclared_method_2(self):
        input = """
            Class Program{
                Val $a : Int = 1;
                $a() {}
                $a() {}
                main(){}
            }
        """
        expect = "Redeclared Method: $a"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test_419_redeclared_parameter_1(self):
        input = """
            Class Program{
                Var a : Float = 1.2;
                Val b : String = "Nhan";
                func(a, b: Int; c: Float; c: String) {}
                main() {}
            }
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
    def test_420_undeclared_identifier_1(self):
        input = """
            Class Program{
                Var a, b: Int;
                main() {
                    Var a : Int = Self.a;
                    b = a;
                }
            }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test_421_undeclared_identifier_2(self):
        input = """
            Class Program{
                Var a, b: Int;
                Var c, d : Int = Self.a, x;
                main(){}
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 421))
        
    def test_422_undeclared_identifier_3(self):
        input = """
            Class Program{
                Var a, b: Int = a, b;
                main(){}
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 422))
        
    def test_423_undeclared_attribute_1(self):
        input = """
            Class Program{
                Var a: Int = Self.x;
                main(){}
            }
        """
        expect = "Undeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
    def test_424_undeclared_attribute_2(self):
        input = """
            Class Program{
                Val $b: Int = 1;
                main(){
                    Var a : Int = Program::$a;
                }
            }
        """
        expect = "Undeclared Attribute: $a"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
    def test_425_undeclared_attribute_3(self):
        input = """
            Class Program{
                Val b: Int = 1;
                main(){
                    Var a : Int = Self.a;
                }
            }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test_426_undeclared_attribute_4(self):
        input = """
            Class A {
                Var a : Int = 1;
            }
            
            Class Program : A {
                Val b: Int = 1;
                main(){
                    Var a : Int = Self.a;
                }
            }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
    def test_427_undeclared_method_1(self):
        input = """
            Class Program{
                func_1() {}
                main(){
                    Self.func();
                }
            }
        """
        expect = "Undeclared Method: func"
        self.assertTrue(TestChecker.test(input, expect, 427))
        
    def test_428_undeclared_method_2(self):
        input = """
            Class Program{
                $func() {}
                main(){
                    Program::$func();
                    Self.func();
                }
            }
        """
        expect = "Undeclared Method: func"
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test_429_undeclared_method_3(self):
        input = """
            Class A {
                func() {Return 1;}
            }
            
            Class Program : A {
                main(){
                    Self.func();
                }
            }
        """
        expect = "Undeclared Method: func"
        self.assertTrue(TestChecker.test(input, expect, 429))
        
    def test_430_undeclared_method_4(self):
        input = """
            Class Program{
                main() {
                    Self.func();
                }
                
                func() {}
            }
        """
        expect = "Undeclared Method: func"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test_431_undeclared_class_1(self):
        input = """
            Class Program : A {
                main() {
                    
                }
            }
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 431))
        
    def test_432_undeclared_class_2(self):
        input = """
            Class Program : A{
                main() {
                    
                }
            }
            
            Class A {
                
            }
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 432))
        
    def test_433_undeclared_class_3(self):
        input = """
            Class Program{
                main() {
                    A::$func();
                }
            }
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
    def test_434_cannot_assign_to_constant_1(self):
        input = """
            Class Program{
                Var a : Int = 2;
                main() {
                    Val a : Int =  1;
                    a = Self.a;
                }
            }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),FieldAccess(Self(),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test_435_cannot_assign_to_constant_2(self):
        input = """
            Class A {
                Val a : Int = 1;
            }
            Class Program{
                main() {
                    Var obj : A = New A();
                    obj.a = 1;
                }
            }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(obj),Id(a)),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 435))
        
    def test_436_type_mismatch_in_statement_1(self):
        input = """
            Class Program{
                main() {
                    Var a,b,c,d : Boolean;
                    Var e : Int;
                    If (!a) {}
                    Elseif(!b) {}
                    Elseif(c) {}
                    Elseif(!d) {}
                    Elseif(e) {}
                }
            }
        """
        expect = "Type Mismatch In Statement: If(UnaryOp(!,Id(a)),Block([]),If(UnaryOp(!,Id(b)),Block([]),If(Id(c),Block([]),If(UnaryOp(!,Id(d)),Block([]),If(Id(e),Block([]))))))"
        self.assertTrue(TestChecker.test(input, expect, 436))
        
    def test_437_type_mismatch_in_statement_2(self):
        input = """
            Class Program{
                main() {
                    Var a, b, i : Int;
                    Var x : Float; 
                    Foreach (i In a .. b By a) {}
                    Foreach (i In x .. b By a) {}
                }
            }
        """
        expect = "Type Mismatch In Statement: For(Id(i),Id(x),Id(b),Id(a),Block([])])"
        self.assertTrue(TestChecker.test(input, expect, 437))
        
    def test_438_type_mismatch_in_statement_3(self):
        input = """
            Class Program{
                main() {
                    Var a : Int;
                    Var b : Float;
                    b = a;      ## infer type ##
                    a = b;
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
    def test_439_type_mismatch_in_statement_4(self):
        input = """
            Class Program{
                main() {
                    Var arr : Array[Int, 2];
                    arr[0] = 1.23;
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr),[IntLit(0)]),FloatLit(1.23))"
        self.assertTrue(TestChecker.test(input, expect, 439))
        
    def test_440_type_mismatch_in_statement_5(self):
        input = """
            Class Program{
                main() {
                    Var arr : Array[Array[Int, 5], 2];    
                    arr[0] = Array(1,2,3,4,5,6);        ## not same size ##
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr),[IntLit(0)]),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5),IntLit(6)])"
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test_441_type_mismatch_in_statement_6(self):
        input = """
            Class Program{
                main() {
                    Var arr : Array[Array[Float, 2], 2];    
                    arr[0][0] = 2;          ## ok, 2d array ##
                    arr[0][0] = Array(1,2);
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr),[IntLit(0),IntLit(0)]),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 441))
        
    def test_442_type_mismatch_in_statement_7(self):
        input = """
            Class Program{
                main() {
                    Var a, b, c, d : String;
                    Var arr : Array[Float, 4] = Array(a,b,c,d);
                }
            }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(arr),ArrayType(4,FloatType),[Id(a),Id(b),Id(c),Id(d)])"
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test_443_type_mismatch_in_statement_8(self):
        input = """
            Class A {
                Var func, $func : Int;
                func(a,b: Int; c,d: Boolean) {}
                $func(a,b: Int; c,d: Boolean) {}
            }
            
            Class Program{
                main() {
                    Var a : A = New A();
                    Var b : Int;
                    a.func();           ## OK ##
                    b.func();
                }
            }
        """
        expect = "Type Mismatch In Statement: Call(Id(a),Id(func),[])"
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_444_type_mismatch_in_statement_9(self):
        input = """
            Class A {
                Var func, $func : Int;
                func(a,b: Int; c,d: Boolean) {}
                $func(a,b: Int; c,d: Boolean) {}
            }
            
            Class Program{
                main() {
                    Var a : A = New A();
                    Var b, c : Int;
                    Var d, e : Boolean;
                    a.func(b, c, d, 1.2);
                }
            }
        """
        expect = "Type Mismatch In Statement: Call(Id(a),Id(func),[Id(b),Id(c),Id(d),FloatLit(1.2)])"
        self.assertTrue(TestChecker.test(input, expect, 444))
        
    def test_445_type_mismatch_in_statement_10(self):
        input = """
            Class A {
                Var func, $func : Int;
                func(a,b: Int; c,d: Boolean) {}
                $func(a,b: Int; c,d: Boolean) {}
            }
            
            Class Program{
                main() {
                    Var a : A = New A();
                    A::$func();
                }
            }
        """
        expect = "Type Mismatch In Statement: Call(Id(A),Id($func),[])"
        self.assertTrue(TestChecker.test(input, expect, 445))
        
    def test_446_type_mismatch_in_statement_11(self):
        input = """
            Class A {
                Var func, $func : Int;
                func(a,b: Float; c,d: Boolean) {}
                $func(a,b: Float; c,d: Boolean) {}
            }
            
            Class Program{
                main() {
                    Var a : A = New A();
                    A::$func(1.2, 1, !False, "True");       ## param type error with coercion ##
                }
            }
        """
        expect = "Type Mismatch In Statement: Call(Id(A),Id($func),[FloatLit(1.2),IntLit(1),UnaryOp(!,BooleanLit(False)),StringLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 446))
        
    def test_447_type_mismatch_in_statement_12(self):
        input = """
            Class A {
                Var func, $func : Int;
                func(a,b: Float; c,d: Boolean) {
                    Return;
                }
                $func(a,b: Float; c,d: Boolean) {
                    Return 1;
                }
            }
            
            Class Program{
                main() {
                    Var a : A = New A();
                    a.func(1, 2, True, True);       ## OK ##
                    A::$func(1, 2, True, True);     ## Failed, not void type return ##
                }
            }
        """
        expect = "Type Mismatch In Statement: Call(Id(A),Id($func),[IntLit(1),IntLit(2),BooleanLit(True),BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 447))
        
    def test_448_type_mismatch_in_statement_13(self):
        input = """
            Class Program{
                func() {
                    Return 1;
                    Return 1.2;
                }
                main() {}
            }
        """
        expect = "Type Mismatch In Statement: Return(FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 448))
        
    def test_449_type_mismatch_in_statement_14(self):
        input = """
            Class Program{
                func() {
                    Return;
                    Return 1.2;
                }
                main() {}
            }
        """
        expect = "Type Mismatch In Statement: Return(FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 449))
        
    def test_450_type_mismatch_in_expression_1(self):
        input = """
            Class Program{
                main() {
                    Var idx : Float = 1.2;
                    Var arr : Array[Int, 3];
                    arr[idx] = 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),[Id(idx)])"
        self.assertTrue(TestChecker.test(input, expect, 450))
        
    def test_451_type_mismatch_in_expression_2(self):
        input = """
            Class Program{
                main() {
                    Var a,b : Int;
                    Var c,d : String;
                    a = a + c;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 451))
        
    def test_452_type_mismatch_in_expression_3(self):
        input = """
            Class Program{
                main() {
                    Var a : Float = 1.2 / 4;
                    Var b : Float = 1.2 / 4.5;
                    Var c : Float = 1 / 4;
                    Var d : Float = 1.2 / "Nhan";
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,FloatLit(1.2),StringLit(Nhan))"
        self.assertTrue(TestChecker.test(input, expect, 452))
        
    def test_453_type_mismatch_in_expression_4(self):
        input = """
            Class Program{
                main() {
                    Var a : Int = 1 % 2;
                    Var b : Float = 1 % 2;
                    Var c : Int = 1.5 % 2;      ## failed ##
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(1.5),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 453))
        
    def test_454_type_mismatch_in_expression_5(self):
        input = """
            Class Program{
                Var x , y : Int;
                main() {
                    Var a : Boolean = True || False && True;
                    Var b : Boolean = Self.x && Self.y;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,FieldAccess(Self(),Id(x)),FieldAccess(Self(),Id(y)))"
        self.assertTrue(TestChecker.test(input, expect, 454))
        
    def test_455_type_mismatch_in_expression_6(self):
        input = """
            Class Program{
                Var x , y : Int;
                main() {
                    Var b : Boolean = Self.x ==. Self.y;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,FieldAccess(Self(),Id(x)),FieldAccess(Self(),Id(y)))"
        self.assertTrue(TestChecker.test(input, expect, 455))
        
    def test_456_type_mismatch_in_expression_7(self):
        input = """
            Class Program{
                Var x, y : String;
                Var m, n : Int;
                main() {
                    Var b : String = Self.x +. Self.y;
                    Var c : String = Self.m +. Self.x;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+.,FieldAccess(Self(),Id(m)),FieldAccess(Self(),Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 456))
        
    def test_457_type_mismatch_in_expression_8(self):
        input = """
            Class Program{
                Var x, y : String;
                Var m, n : Int;
                Var a, b : Float;
                main() {
                    Var temp1 : Boolean = Self.m == Self.n;
                    Var temp2 : Boolean = Self.m < Self.a;
                    Var temp3 : Boolean = Self.b < Self.a;
                    Var temp4 : Boolean = Self.x < Self.a;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<,FieldAccess(Self(),Id(x)),FieldAccess(Self(),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 457))
        
    def test_458_type_mismatch_in_expression_9(self):
        input = """
            Class Program{
                Var x, y : Boolean;
                Var m, n : Int;
                Var a, b : Float;
                main() {
                    Var temp1 : Boolean = Self.m == Self.n;
                    Var temp2 : Boolean = Self.x != Self.y;
                    Var temp3 : Boolean = Self.a != Self.b;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,FieldAccess(Self(),Id(a)),FieldAccess(Self(),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test_459_type_mismatch_in_expression_10(self):
        input = """
            Class Program{
                Var x, y : Boolean;
                Var m, n : Int;
                Var a, b : Float;
                main() {
                    Var temp1 : Float = Self.m + Self.a;
                    Var temp2 : Float = Self.m - Self.a;
                    Var temp3 : Float = Self.m - Self.n;
                    Var temp4 : Float = Self.m / Self.n;
                    Var temp5 : Float = Self.m * Self.n;
                    Var temp6 : Float = Self.m / Self.n;
                    Var temp7 : Float = Self.a * Self.b;
                    Var temp8 : Float = Self.a * Self.x;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,FieldAccess(Self(),Id(a)),FieldAccess(Self(),Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 459))
        
    def test_460_type_mismatch_in_expression_11(self):
        input = """
            Class Program{
                main() {
                    Var a,b: Int;
                    Var c,d: Float;
                    Var m,n: Boolean = True, False;
                    
                    Var x : Int = -a;
                    Var y : Float = -c;
                    Var e : Boolean = !m;
                    Var f : Boolean = -m;
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(m))"
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test_461_type_mismatch_in_expression_12(self):
        input = """
            Class Program{
                main() {
                    Var a : Boolean;
                    Var b : Int = -a;
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
    def test_462_type_mismatch_in_expression_13(self):
        input = """
            Class Program{
                func() {
                    Return 1;
                }
                
                main() {
                    Val x : Int = Self.func();
                    Val y : Float = Self.func() + 1;
                    Var z : Int = Self.func(1);         ## error params ##
                }
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(func),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 462))
        
    def test_463_type_mismatch_in_expression_14(self):
        input = """
            Class Program{
                func() {
                    Return;
                }
                
                main() {
                    Val x : Int = Self.func();      ## error cuz Void ##
                }
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(func),[])"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
    def test_464_type_mismatch_in_expression_15(self):
        input = """
            Class A {
                func() {
                    Return 1;
                }
            }
            
            Class Program{
                main() {
                    Var a : A = New A();
                    Val x : Int = a.func();
                    Var y : Int = x.func();     ## error cuz pbject is not class type ##
                }
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(x),Id(func),[])"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test_465_type_mismatch_in_expression_16(self):
        input = """
            Class A {
                func(a: Int) {
                    Return New A();
                }
                
            }
            
            Class Program{
                main() {
                    Var a : A = New A();
                    Val x : A = a.func(1);       ## ok cuz function return object A ##
                    Var y : A = a.func();       ## error params ##
                }
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(func),[])"
        self.assertTrue(TestChecker.test(input, expect, 465))
        
    def test_466_type_mismatch_in_expression_17(self):
        input = """
            Class A {
                Val a, $a: Int = 1, 2;
            }
            
            Class Program{
                main() {
                   Var a : A;
                   Val x : Int = a.a;
                   Val y : Float = A::$a;
                   Var z : Int = x.a;           ## error cuz object is not class type ##
                }
            }
        """
        expect = "Type Mismatch In Expression: FieldAccess(Id(x),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 466))
        
    def test_467_type_mismatch_in_expression_18(self):
        input = """
            Class A {
                Var a : Int = 1;
            }
            
            Class B {
                Var b : Int = 2;
                Var obj_a : A;
            }
            
            Class C {
                Var c : Int = 2;
                Var obj_b : B;
                func_C() {
                    Return New B();
                }
            }
            
            Class Program{
                main() {
                   Var c : C;
                   Var x : Int = c.obj_b.obj_a.a;
                   Var y : Int = c.func_C().obj_a.a;
                   Var m : Int = c.func_C().b.a;
                }
            }
        """
        expect = "Type Mismatch In Expression: FieldAccess(FieldAccess(CallExpr(Id(c),Id(func_C),[]),Id(b)),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 467))
        
    def test_468_type_mismatch_in_constant_1(self):
        input = """    
            Class Program{
                Val a : Int = 1;
                main() {
                    Val x : String = Self.a;
                }
            }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(x),StringType,FieldAccess(Self(),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 468))
        
    def test_469_type_mismatch_in_constant_2(self):
        input = """    
            Class Program{
                Val a : Int = 1;
                main() {
                    Val x : Float = Self.a;
                    Val y : String = x;
                }
            }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),StringType,Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 469))
        
    def test_470_type_mismatch_in_constant_3(self):
        input = """    
            Class A {}
            Class Program : A {
                Val a : A = New A();
                main() {
                    Val obj : Program = Self.a;
                }
            }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(obj),ClassType(Id(Program)),FieldAccess(Self(),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
    def test_471_break_not_in_loop(self):
        input = """    
            Class Program {
                main() {
                    Var lower, upper, step : Int = 1, 2, 3;
                    Var i : Int = 1;
                    Foreach (i In lower .. upper) {
                        Break;
                    }
                    Foreach (i In lower .. upper By step) {
                        {
                            {
                                {
                                    Break;
                                }
                            }
                        }
                    }
                    
                    Break;          ## error ##
                }
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 471))
        
    def test_472_continue_not_in_loop(self):
        input = """    
            Class Program {
                main() {
                    Var lower, upper, step : Int = 1, 2, 3;
                    Var i : Int = 1;
                    Foreach (i In lower .. upper) {
                        Continue;
                    }
                    Foreach (i In lower .. upper By step) {
                        {
                            {
                                {
                                    Continue;
                                }
                            }
                        }
                    }
                    
                    Continue;          ## error ##
                }
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 472))
        
    def test_473_illegal_constant_expression_1(self):
        input = """    
            Class Program {
                main() {
                    Var x : Float = 1.2;
                    Val y : Float = x;
                }
            }
        """
        expect = "Illegal Constant Expression: Id(x)"
        self.assertTrue(TestChecker.test(input, expect, 473))
        
    def test_474_illegal_constant_expression_2(self):
        input = """    
            Class Program {
                func1() {
                    Return 1;
                }
                
                func2() {
                    Return 2.3;
                }
                
                main() {
                    Var x : Float = Self.func1();
                    Val y : Float = Self.func2() + 1;
                    Val z : Float = Self.func1() + Self.func2() / Self.func1() * Self.func2();
                    Val m : Float = Self.func1() + x;
                }
            }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,CallExpr(Self(),Id(func1),[]),Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 474))
        
    def test_475_illegal_constant_expression_3(self):
        input = """    
            Class Program {
                func1(a: String) {
                    Var x : Int = 1;
                    Return x;
                }
                
                main() {
                    Val x : Int = Self.func1("Nhan");
                }
            }
        """
        expect = "Illegal Constant Expression: CallExpr(Self(),Id(func1),[StringLit(Nhan)])"
        self.assertTrue(TestChecker.test(input, expect, 475))
        
    def test_476_illegal_constant_expression_4(self):
        input = """    
            Class A {
                Var a : Int = 1;
                Val b : Int = 2;
                func_A() {
                    Return Self.a;
                }
            }
            
            Class B {
                Var b : Int = 1;
                Var obj_a : A = New A();
            }
            
            Class Program {
                func1() {
                    Var obj : B;
                    Return obj.obj_a.b;
                }
                
                main() {
                    Val x : Int = Self.func1();
                }
            }
        """
        expect = "Illegal Constant Expression: CallExpr(Self(),Id(func1),[])"
        self.assertTrue(TestChecker.test(input, expect, 476))
        
        
        

    # def test_999(self):
    #     input = """
        
    #         Class A {
    #             Val a : Int = 1;
    #         }
            
    #         Class B {
    #             Var b : Int;
    #             Var obj : A;
    #         }
            
    #         Class C {
    #             Val c : Int = 1;
    #             Var obj : B;
    #             func() {
    #                 Return Self.c;
    #             }
    #         }

    #         Class Program {
    #             func() {
    #                 Var c : C = New C(); 
    #                 Return c.func();
    #             }
                
    #             main() {
    #                 Val x : Int = 1 + Self.func();
    #             }
    #         }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 999))







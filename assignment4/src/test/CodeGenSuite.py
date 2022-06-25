import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    def test_500_simple_program_1(self):
        input = """
            Class Program {
                Var a : Int = 1;
                func() {
                    Var b : Int = 2;
                    io.putInt(Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,500))
        
    def test_501_simple_program_2(self):
        input = """
            Class Program {
                Var a : Float = 1.2;
                func() {
                    io.putFloat(Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1.2"
        self.assertTrue(TestCodeGen.test(input,expect,501))
        
    def test_502_simple_program_3(self):
        input = """
            Class Program {
                Var a : String = "Nhan Vo";
                func() {
                    io.putString(Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "Nhan Vo"
        self.assertTrue(TestCodeGen.test(input,expect,502))
        
    def test_503_simple_program_4(self):
        input = """
            Class Program {
                Var a : Boolean = False;
                func() {
                    io.putBool(Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,503))
        
    def test_504_simple_program_5(self):
        input = """
            Class Program {
                Var a : Int = 1;
                Var b : Float = 0.45;
                func() {
                    io.putIntLn(Self.a);
                    io.putFloatLn(Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1\n0.45\n"
        self.assertTrue(TestCodeGen.test(input,expect,504))
        
    def test_505_simple_program_6(self):
        input = """
            Class Program {
                Var c : Boolean = False;
                Var d : String = "Nhan";
                func() {
                    io.putBoolLn(Self.c);
                    io.putString(Self.d);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false\nNhan"
        self.assertTrue(TestCodeGen.test(input,expect,505))
        
    def test_506_unary_op_1(self):
        input = """
            Class Program {
                Var a : Int = 1;
                func() {
                    io.putInt(-Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,506))
        
    def test_507_unary_op_2(self):
        input = """
            Class Program {
                Var a : Float = 1.4;
                func() {
                    io.putFloat(-Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "-1.4"
        self.assertTrue(TestCodeGen.test(input,expect,507))
        
    def test_508_unary_op_3(self):
        input = """
            Class Program {
                Var a : Boolean = False;
                func() {
                    io.putBool(!Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,508))
        
    def test_509_unary_op_4(self):
        input = """
            Class Program {
                Var a : Boolean = True;
                func() {
                    io.putBool(!Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,509))
        
    def test_510_binary_op_1(self):
        input = """
            Class Program {
                func() {
                    io.putInt(1 + 2);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,510))
        
    def test_511_binary_op_2(self):
        input = """
            Class Program {
                func() {
                    io.putInt(100 - 200);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "-100"
        self.assertTrue(TestCodeGen.test(input,expect,511))
        
    def test_512_binary_op_3(self):
        input = """
            Class Program {
                func() {
                    io.putFloat(3.5 - 2.3);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1.2"
        self.assertTrue(TestCodeGen.test(input,expect,512))
        
    def test_513_binary_op_4(self):
        input = """
            Class Program {
                func() {
                    io.putFloat(3.5 / 2.5);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1.4"
        self.assertTrue(TestCodeGen.test(input,expect,513))
        
    def test_514_binary_op_5(self):
        input = """
            Class Program {
                func() {
                    io.putFloat(3.5 * 2.5);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "8.75"
        self.assertTrue(TestCodeGen.test(input,expect,514))
        
    def test_515_binary_op_6(self):
        input = """
            Class Program {
                func() {
                    io.putBool(True || False);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,515))
        
    def test_516_binary_op_7(self):
        input = """
            Class Program {
                func() {
                    io.putBool(False || False);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,516))
        
    def test_517_binary_op_8(self):
        input = """
            Class Program {
                func() {
                    io.putBool(False && False);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,517))
        
    def test_518_binary_op_9(self):
        input = """
            Class Program {
                func() {
                    io.putBool(True && True);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,518))
        
    def test_519_compare_operator_1(self):
        input = """
            Class Program {
                func() {
                    io.putBool(1 < 2);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,519))
        
    def test_520_compare_operator_2(self):
        input = """
            Class Program {
                func() {
                    io.putBool(100 > 200);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,520))
        
    def test_521_compare_operator_3(self):
        input = """
            Class Program {
                func() {
                    io.putBool(100 >= 100);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,521))
        
    def test_522_compare_operator_4(self):
        input = """
            Class Program {
                func() {
                    io.putBool(100 == 100);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,522))
        
    def test_523_compare_operator_5(self):
        input = """
            Class Program {
                func() {
                    io.putBool(100 != 101);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,523))
        
    def test_524_division_operator_1(self):
        input = """
            Class Program {
                func() {
                    io.putFloat(3.0 / 2.0);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1.5"
        self.assertTrue(TestCodeGen.test(input,expect,524))
        
    def test_525_rem_operator_1(self):
        input = """
            Class Program {
                func() {
                    io.putInt(3 % 2);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,525))
        
    def test_526_mixed_program_1(self):
        input = """
            Class Program {
                Var a : Int = 1;
                func() {
                    Var a : Int = 2;
                    io.putInt(a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,526))
        
    def test_527_mixed_program_2(self):
        input = """
            Class Program {
                Var a : Int = 1;
                Var b : Int = 20;
                func() {
                    Var a : Int = 2;
                    io.putInt(a + Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "22"
        self.assertTrue(TestCodeGen.test(input,expect,527))
        
    def test_528_mixed_program_3(self):
        input = """
            Class Program {
                Var a : Float = 3.5;
                func() {
                    Var a : Float = 2.5;
                    io.putFloat(a + Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input,expect,528))
        
    def test_529_mixed_program_4(self):
        input = """
            Class Program {
                Var a : Float = 3.5;
                Var b : Float = 1.2;
                func() {
                    io.putFloat(Self.a - Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "2.3"
        self.assertTrue(TestCodeGen.test(input,expect,529))
        
    def test_530_mixed_program_5(self):
        input = """
            Class Program {
                Val a : Boolean = False;
                func() {
                    io.putBool(Self.a || True);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,530))
        
    def test_531_mixed_program_6(self):
        input = """
            Class Program {
                Val a : Boolean = False;
                func() {
                    Val a : Boolean = False;
                    io.putBool(Self.a || a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,531))
        
    def test_532_assign_stmt_2(self):
        input = """
            Class Program {
                func() {
                    Var a : Float = 1.2;
                    a = 2.2;
                    io.putFloat(a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "2.2"
        self.assertTrue(TestCodeGen.test(input,expect,532))
        
    def test_533_assign_stmt_3(self):
        input = """
            Class Program {
                func() {
                    Var a : Int = 1;
                    Var b : Int = 2;
                    a = b;
                    io.putInt(a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,533))
        
    def test_534_assign_stmt_4(self):
        input = """
            Class Program {
                func() {
                    Var a : Float = 1.1;
                    Val b : Float = 2.2;
                    a = b;
                    io.putFloat(a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "2.2"
        self.assertTrue(TestCodeGen.test(input,expect,534))
        
    def test_535_assign_stmt_5(self):
        input = """
            Class Program {
                func() {
                    Var a : String = "Nhan";
                    Var b : String = "Vo";
                    b = a;
                    io.putStringLn(a);
                    io.putString(b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "Nhan\nNhan"
        self.assertTrue(TestCodeGen.test(input,expect,535))
        
    def test_536_assign_stmt_6(self):
        input = """
            Class Program {
                func() {
                    Var a : Float = 2.2;
                    Var b : Int = 1;
                    a = b;
                    io.putFloat(a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,536))
        
    def test_537_attribute_decl_1(self):
        input = """
            Class Program {
                Var a : Int = 1;
                Var b : Int = 2;
                func() {
                    io.putInt(Self.a - Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    
    def test_538_attribute_decl_2(self):
        input = """
            Class Program {
                Var a : Boolean = False;
                Val b : Boolean = True;
                func() {
                    io.putBool(Self.a || Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,538))
        
    def test_539_attribute_decl_3(self):
        input = """
            Class Program {
                Var $a : Boolean = False;
                Val $b : Boolean = True;
                func() {
                    io.putBool(Program::$a || Program::$b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,539))
        
    def test_540_attribute_decl_4(self):
        input = """
            Class Program {
                Var $a : Float = 1.2;
                Var b : Float = 3.42;
                func() {
                    io.putFloat(Program::$a + Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "4.62"
        self.assertTrue(TestCodeGen.test(input,expect,540))
        
    def test_541_attribute_decl_5(self):
        input = """
            Class Program {
                Var $a : Int = 1;
                Var b : Int = 3;
                func() {
                    io.putBool(Program::$a < Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,541))
        
    def test_542_attribute_decl_6(self):
        input = """
            Class Program {
                Var $a : Int = 1;
                Var b : Float = 3.2;
                Var c : String = "Class";
                Var d : Boolean = False;
                func() {
                    io.putIntLn(-Program::$a);
                    io.putFloatLn(-Self.b);
                    io.putStringLn(Self.c);
                    io.putBool(!Self.d);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "-1\n-3.2\nClass\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,542))
        
    def test_543_const_decl_1(self):
        input = """
            Class Program {
                func() {
                    Val a : Int = 2;
                    io.putInt(a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,543))
        
    def test_544_const_decl_2(self):
        input = """
            Class Program {
                Val a : Float = 1.0;
                func() {
                    io.putFloat(Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,544))
        
    def test_545_const_decl_3(self):
        input = """
            Class Program {
                Val $a : Float = 1.0;
                func() {
                    io.putFloat(Program::$a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,545))
        
    def test_546_field_access_1(self):
        input = """
            Class Program {
                Var a : String = "Vo Nhan";
                func() {
                    io.putString(Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "Vo Nhan"
        self.assertTrue(TestCodeGen.test(input,expect,546))
        
    def test_547_field_access_2(self):
        input = """
            Class Program {
                Var a : Int = 100;
                Var b : Int = 200;
                func() {
                    io.putIntLn(Self.a);
                    io.putIntLn(Self.b);
                    io.putInt(Self.a - (-Self.b));
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "100\n200\n300"
        self.assertTrue(TestCodeGen.test(input,expect,547))
        
    def test_548_complex_operator_1(self):
        input = """
            Class Program {
                Var a : Int = 100;
                Var b : Int = 200;
                func() {
                    io.putInt(Self.a + (-Self.b));
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "-100"
        self.assertTrue(TestCodeGen.test(input,expect,548))
        
    def test_549_complex_operator_2(self):
        input = """
            Class Program {
                Var a : Boolean = False;
                Var b : Boolean = False;
                func() {
                    io.putBool(Self.a || (!Self.b));
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,549))
        
    def test_550_assign_stmt_1(self):
        input = """
            Class Program {
                func() {
                    Var a : Int = 1;
                    a = 2;
                    io.putInt(a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,550))
        
    def test_551_self_access_1(self):
        input = """
            Class Program {
                Var a : Int = 100;
                Val b : Float = 100.2;
                func() {
                    io.putIntLn(Self.a);
                    io.putFloat(Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "100\n100.2"
        self.assertTrue(TestCodeGen.test(input,expect,551))
        
    def test_552_self_access_2(self):
        input = """
            Class Program {
                Var c : Boolean = True;
                func() {
                    io.putBool(Self.c);
                    io.putBool(!Self.c);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "truefalse"
        self.assertTrue(TestCodeGen.test(input,expect,552))
        
    def test_553_self_access_3(self):
        input = """
            Class Program {
                Var a : String = "Nhan Vo";
                func() {
                    io.putString(Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "Nhan Vo"
        self.assertTrue(TestCodeGen.test(input,expect,553))
        
    def test_554_self_access_4(self):
        input = """
            Class Program {
                Var a, b : Int = 1, 2;
                func() {
                    io.putInt(Self.a);
                    io.putInt(Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,554))
        
    def test_555_multiple_var_declare_1(self):
        input = """
            Class Program {
                Var a, b : Float = 1.1, 2.2;
                func() {
                    io.putFloatLn(Self.a);
                    io.putFloat(Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1.1\n2.2"
        self.assertTrue(TestCodeGen.test(input,expect,555))
        
    def test_556_multiple_var_declare_2(self):
        input = """
            Class Program {
                Var a, b : Boolean = False, True;
                func() {
                    io.putBoolLn(!Self.a);
                    io.putBool(Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,556))
        
    def test_557_multiple_var_declare_3(self):
        input = """
            Class Program {
                Var a, b : String = "Nhan ", "Vo";
                func() {
                    io.putStringLn(Self.a);
                    io.putString(Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "Nhan \nVo"
        self.assertTrue(TestCodeGen.test(input,expect,557))
        
    def test_558_multiple_var_declare_4(self):
        input = """
            Class Program {
                Var a, b : String = "Nhan", "Vo";
                Var c, d : Boolean = True, False;
                func() {
                    io.putStringLn(Self.a);
                    io.putBool(Self.c);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "Nhan\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,558))
        
    def test_559_multiple_var_declare_5(self):
        input = """
            Class Program {    
                Var a, b: Float = 1.1, 5.4;
                func() {
                    io.putFloat(Self.a);
                    io.putFloat(Self.b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1.15.4"
        self.assertTrue(TestCodeGen.test(input,expect,559))
        
    def test_560_redeclared_variable_1(self):
        input = """
            Class Program {    
                Var a, b: Float = 1.1, 5.4;
                func() {
                    Var a : Int = 1;
                    io.putIntLn(a);
                    io.putFloat(Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1\n1.1"
        self.assertTrue(TestCodeGen.test(input,expect,560))
        
    def test_561_redeclared_variable_2(self):
        input = """
            Class Program {    
                Var a, b: String = "string 1", "string 2";
                func() {
                    Var a : String = "string 3";
                    io.putString(a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "string 3"
        self.assertTrue(TestCodeGen.test(input,expect,561))
        
    def test_562_redeclared_variable_3(self):
        input = """
            Class Program {    
                Var a, b: String = "string 1", "string 2";
                Var c, d: Boolean = False, True;
                func() {
                    Var a, b: String = "string 1", "string 2";
                    Var c, d: Boolean = False, True;
                    io.putStringLn(a);
                    io.putStringLn(Self.a);
                    io.putBoolLn(!Self.c);
                    io.putBool(!d);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "string 1\nstring 1\ntrue\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,562))
        
    def test_563_redeclared_variable_4(self):
        input = """
            Class Program {    
                Var a, b, c: Int = 100, 200, 300;
                func() {
                    Var a, b, c: Int = 10, 20, 30;
                    io.putInt(a);
                    io.putInt(b);
                    io.putInt(c);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "102030"
        self.assertTrue(TestCodeGen.test(input,expect,563))
        
    def test_564_complicated_operators_1(self):
        input = """
            Class Program {    
                func() {
                    io.putFloat(1.2 - 1.1 * 2.0);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input,expect,564))
        
    def test_565_complicated_operators_2(self):
        input = """
            Class Program {    
                func() {
                    io.putFloat(3.0 / 2.0 * 2.0);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,565))
        
    def test_566_complicated_operators_3(self):
        input = """
            Class Program {    
                func() {
                    io.putFloat((3.1 + 2.0)*2.0);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "10.2"
        self.assertTrue(TestCodeGen.test(input,expect,566))
        
    def test_567_complicated_operators_4(self):
        input = """
            Class Program {    
                func() {
                    io.putBool((!False || !False) && False);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,567))
        
    def test_568_mixed_boolean_combination_1(self):
        input = """
            Class Program {    
                func() {
                    io.putBool(True && False || False);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,568))
        
    def test_569_mixed_boolean_combination_2(self):
        input = """
            Class Program {    
                func() {
                    io.putBool(True || False || False || False || False || False && False);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,569))
        
    def test_570_mixed_boolean_combination_3(self):
        input = """
            Class Program {    
                func() {
                    io.putBool((!False && !False) || (!False && !False));
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,570))
        
    def test_571_float_with_operators_1(self):
        input = """
            Class Program {    
                Var a : Float = 1.2;
                func() {
                    io.putFloat(Self.a*2.0 + 2.0 - 1.1);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "3.3000002"
        self.assertTrue(TestCodeGen.test(input,expect,571))
        
    def test_572_float_with_operators_2(self):
        input = """
            Class Program {    
                func() {
                    io.putFloat(2.2 - 1.1 + 2.3 - (-3.0));
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "6.4"
        self.assertTrue(TestCodeGen.test(input,expect,572))
        
    def test_573_float_with_operators_3(self):
        input = """
            Class Program {    
                func() {
                    io.putFloat(3.0 / 2.0 + 8.5);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,573))
        
    def test_574_float_with_operators_4(self):
        input = """
            Class Program {    
                func() {
                    Var a, b, c, d : Float = 1.0, 2.0, 10.0, 20.0;
                    io.putFloat(-a - b - c - d);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "-33.0"
        self.assertTrue(TestCodeGen.test(input,expect,574))
        
    def test_575_compare_boolean_operands_1(self):
        input = """
            Class Program {    
                func() {
                    io.putBool( (!False) == True );
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,575))
        
    def test_576_compare_boolean_operands_2(self):
        input = """
            Class Program {    
                func() {
                    io.putBool( (!False) != True );
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,576))
        
    def test_577_assoc_boolean_1(self):
        input = """
            Class Program {    
                func() {
                    io.putBool( (False && True) || True == True );
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,577))
    
    def test_578_assoc_boolean_2(self):
        input = """
            Class Program {    
                func() {
                    io.putBool( False || True && False || True == True );
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,578))
        
    def test_579_assoc_boolean_3(self):
        input = """
            Class Program {    
                func() {
                    io.putBool( False && True || False == True && False);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,579))
        
    def test_580_program_mixed_structured_1(self):
        input = """
            Class Program {
                Var a : Boolean = False;    
                func() {
                    io.putBool( False && True || False == True && Self.a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,580))
        
    def test_581_program_mixed_structured_2(self):
        input = """
            Class Program {
                Var a : Boolean = False;    
                Var b, c, d : Int = 1, 2, 3;
                func() {
                    io.putBoolLn( False && True || False == True && Self.a);
                    io.putBool (Self.b + Self.c == Self.d);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,581))
        
    def test_582_program_mixed_structured_3(self):
        input = """
            Class Program {
                Var a : Boolean = False;    
                Var b, c, d : Int = 1, 2, 3;
                func() {
                    Var b, c, d : Int = 1, 2, 3;
                    io.putBoolLn( False && True || False == True && Self.a);
                    io.putBoolLn(Self.b + Self.c == Self.d);
                    io.putBool(b + c != d);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true\ntrue\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,582))
        
    def test_583_program_mixed_structured_4(self):
        input = """
            Class Program {
                Var a : Boolean = False;    
                Var b, c, d : Int = 1, 2, 3;
                func() {
                    Var b, c, d : Int = 1, 2, 3;
                    Val e, f, g : Boolean = True, True, True;
                    io.putBoolLn( False && True || False == True && !e);
                    io.putBoolLn( (Self.b + Self.c == Self.d) == !(!f) );
                    io.putBool( (b + c != d) == !g);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true\ntrue\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,583))
        
    def test_584_program_mixed_structured_5(self):
        input = """
            Class Program {
                Var a : Boolean = False;    
                Var b, c, d : Int = 1, 2, 3;
                func() {
                    Var b, c, d : Int = 1, 2, 3;
                    Val e, f, g : Boolean = True, True, True;
                    io.putBoolLn( False && True || False == True && !e);
                    io.putBoolLn( (Self.b + Self.c == Self.d) == !(!f) );
                    io.putBoolLn( (b + c != d) == !g);
                    io.putInt(Self.b - b + Self.c - c + Self.d - d);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true\ntrue\ntrue\n0"
        self.assertTrue(TestCodeGen.test(input,expect,584))
        
    def test_585_with_assignment_stmt_1(self):
        input = """
            Class Program {
                Var a : Boolean = False;    
                Var b, c, d : Int = 1, 2, 3;
                func() {
                    Var b, c, d : Int = 1, 2, 3;
                    Val e, f, g : Boolean = True, True, True;
                    d = 1;
                    c = 2;
                    b = 3;
                    io.putBoolLn(d + c == b);
                    io.putInt(d + c - b);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true\n0"
        self.assertTrue(TestCodeGen.test(input,expect,585))
        
    def test_586_with_assignment_stmt_2(self):
        input = """
            Class Program {
                Var a : Boolean = False;    
                Var b, c, d : Int = 1, 2, 3;
                func() {
                    Var a : Boolean = True;
                    a = False;
                    io.putBool(!a);
                    a = True;
                    io.putBool(!a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "truefalse"
        self.assertTrue(TestCodeGen.test(input,expect,586))
        
    def test_587_with_assignment_stmt_3(self):
        input = """
            Class Program {
                Var a : Boolean = False;    
                Var b, c, d : Int = 1, 2, 3;
                func() {
                    Var a : Float = 1.0;
                    io.putFloatLn(-a);
                    a = 2.0;
                    io.putFloat(a * 2.0);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "-1.0\n4.0"
        self.assertTrue(TestCodeGen.test(input,expect,587))
        
    def test_588_with_assignment_stmt_4(self):
        input = """
            Class Program {
                func() {
                    Var a, b : Int;
                    a = 10;
                    b = 20;
                    io.putInt(a*2 + b*2);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "60"
        self.assertTrue(TestCodeGen.test(input,expect,588))
        
    def test_589_some_sample_program_1(self):
        input = """
            Class Program {
                func() {
                    io.putBool((0 + 9 - 9 + 1) == (1 + 0 - 0 - 1 + 1));
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,589))
        
    def test_590_some_sample_program_2(self):
        input = """
            Class Program {
                func() {
                    io.putFloatLn(1.1 - 2.2);
                    io.putFloatLn(1.1 * 2.0 - 2.2);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "-1.1\n0.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,590))
        
    def test_591_some_sample_program_3(self):
        input = """
            Class Program {
                func() {
                    io.putBoolLn(!!!!!!!!!!!False);
                    io.putBool(!!!!!!!!!!!!False);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "true\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,591))
        
    def test_592_some_sample_program_4(self):
        input = """
            Class Program {
                func() {
                    io.putIntLn(---------------1 - ---------------1);
                    io.putIntLn(3%2 - 1);
                    io.putInt(4%2 - 1);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "0\n0\n-1"
        self.assertTrue(TestCodeGen.test(input,expect,592))
    
    def test_593_continue_stmt_1(self):
        input = """
            Class Program {
                Var a : Boolean = False;
                func() {
                    Var i : Int;
                    Foreach(i In 1 .. 5) {
                        Continue;
                    }
                    io.putInt(1);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,593))
        
    def test_594_some_sample_program_6(self):
        input = """
            Class Program {
                Var a : Boolean = False;
                Var $a : Boolean = True;
                func() {
                    io.putBool(Self.a != !Program::$a);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,594))
        
    def test_595_some_program_very_simple_1(self):
        input = """
            Class Program {
                func() {
                    io.putInt(1);
                    io.putInt(2);
                    io.putInt(3);
                    io.putFloat(1.0);
                    io.putFloat(2.0);
                    io.putFloat(3.0);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1231.02.03.0"
        self.assertTrue(TestCodeGen.test(input,expect,595))
        
    def test_596_break_stmt_1(self):
        input = """
            Class Program {
                Val a : Float = 1.1;
                func() {
                    Var i : Int;
                    Foreach(i In 1 .. 5) {
                        io.putInt(i);
                        Break;
                    }
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,596))
        
    def test_597_if_stmt_1(self):
        input = """
            Class Program {
                Val a : String = "str";
                func() {
                    If(Self.a ==. "str") {
                        io.putString(Self.a);
                    }
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "str"
        self.assertTrue(TestCodeGen.test(input,expect,597))
        
    def test_598_some_program_very_simple_4(self):
        input = """
            Class Program {
                Var a, b, c : Int = 10, 20, 30;
                Val d, e, f : Float = 10.1, 20.2, 30.3;
                func() {
                    Var a, b, c : Int = 10, 20, 30;
                    Val d, e, f : Float = 10.1, 20.2, 30.3;
                    io.putIntLn(Self.a + Self.b + Self.c);
                    io.putFloatLn(Self.d + Self.e - -Self.f);
                    io.putIntLn(a - b - c*2);
                    io.putFloat(d + e + f);
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "60\n60.6\n-70\n60.6"
        self.assertTrue(TestCodeGen.test(input,expect,598))
        
    def test_599_foreach_stmt_1(self):
        input = """
            Class Program {
                func() {
                    Var i : Int;
                    Foreach(i In 1 .. 5) {
                        io.putInt(i);
                    }
                }
                main() {
                    Var obj : Program = New Program();
                    obj.func();
                }
            }
        """
        expect = "12345"
        self.assertTrue(TestCodeGen.test(input,expect,599))
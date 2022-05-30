import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_999(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 Var a : Float;
    #                 a = 2.4 + 2.4;
    #                 io.putFloat(a);
    #             }
    #         }
    #     """
    #     expect = "22"
    #     self.assertTrue(TestCodeGen.test(input,expect,999))
        
    # def test_500_simple_program_1(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Int = 1;
    #             main() {
    #                 io.putInt(Self.a);
    #             }
    #         }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
        
    # def test_501_simple_program_2(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Float = 1.2;
    #             main() {
    #                 io.putFloat(Self.a);
    #             }
    #         }
    #     """
    #     expect = "1.2"
    #     self.assertTrue(TestCodeGen.test(input,expect,501))
        
    # def test_502_simple_program_3(self):
    #     input = """
    #         Class D96Class {
    #             Var a : String = "Nhan Vo";
    #             main() {
    #                 io.putString(Self.a);
    #             }
    #         }
    #     """
    #     expect = "Nhan Vo"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))
        
    # def test_503_simple_program_4(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Boolean = False;
    #             main() {
    #                 io.putBool(Self.a);
    #             }
    #         }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))
        
    # def test_504_simple_program_5(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Int = 1;
    #             Var b : Float = 0.45;
    #             main() {
    #                 io.putIntLn(Self.a);
    #                 io.putFloatLn(Self.b);
    #             }
    #         }
    #     """
    #     expect = "1\n0.45\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))
        
    # def test_505_simple_program_6(self):
    #     input = """
    #         Class D96Class {
    #             Var c : Boolean = False;
    #             Var d : String = "Nhan";
    #             main() {
    #                 io.putBoolLn(Self.c);
    #                 io.putString(Self.d);
    #             }
    #         }
    #     """
    #     expect = "false\nNhan"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))
        
    # def test_506_unary_op_1(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Int = 1;
    #             main() {
    #                 io.putInt(-Self.a);
    #             }
    #         }
    #     """
    #     expect = "-1"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))
        
    # def test_507_unary_op_2(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Float = 1.4;
    #             main() {
    #                 io.putFloat(-Self.a);
    #             }
    #         }
    #     """
    #     expect = "-1.4"
    #     self.assertTrue(TestCodeGen.test(input,expect,507))
        
    # def test_508_unary_op_3(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Boolean = False;
    #             main() {
    #                 io.putBool(!Self.a);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,508))
        
    # def test_509_unary_op_4(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Boolean = True;
    #             main() {
    #                 io.putBool(!Self.a);
    #             }
    #         }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,509))
        
    # def test_510_binary_op_1(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putInt(1 + 2);
    #             }
    #         }
    #     """
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input,expect,510))
        
    # def test_511_binary_op_2(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putInt(100 - 200);
    #             }
    #         }
    #     """
    #     expect = "-100"
    #     self.assertTrue(TestCodeGen.test(input,expect,511))
        
    # def test_512_binary_op_3(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putFloat(3.5 - 2.3);
    #             }
    #         }
    #     """
    #     expect = "1.2"
    #     self.assertTrue(TestCodeGen.test(input,expect,512))
        
    # def test_513_binary_op_4(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putFloat(3.5 / 2.5);
    #             }
    #         }
    #     """
    #     expect = "1.4"
    #     self.assertTrue(TestCodeGen.test(input,expect,513))
        
    # def test_514_binary_op_5(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putFloat(3.5 * 2.5);
    #             }
    #         }
    #     """
    #     expect = "8.75"
    #     self.assertTrue(TestCodeGen.test(input,expect,514))
        
    # def test_515_binary_op_6(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putBool(True || False);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,515))
        
    # def test_516_binary_op_7(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putBool(False || False);
    #             }
    #         }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,516))
        
    # def test_517_binary_op_8(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putBool(False && False);
    #             }
    #         }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,517))
        
    # def test_518_binary_op_9(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putBool(True && True);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,518))
        
    # def test_519_compare_operator_1(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putBool(1 < 2);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,519))
        
    # def test_520_compare_operator_2(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putBool(100 > 200);
    #             }
    #         }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,520))
        
    # def test_521_compare_operator_3(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putBool(100 >= 100);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,521))
        
    # def test_522_compare_operator_4(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putBool(100 == 100);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,522))
        
    # def test_523_compare_operator_5(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putBool(100 != 101);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,523))
        
    # def test_524_division_operator_1(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putFloat(3.0 / 2.0);
    #             }
    #         }
    #     """
    #     expect = "1.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,524))
        
    # def test_524_division_operator_1(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putFloat(3.0 / 2.0);
    #             }
    #         }
    #     """
    #     expect = "1.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,524))
        
    # def test_525_rem_operator_1(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 io.putInt(3 % 2);
    #             }
    #         }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,525))
        
    # def test_526_mixed_program_1(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Int = 1;
    #             main() {
    #                 Var a : Int = 2;
    #                 io.putInt(a);
    #             }
    #         }
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input,expect,526))
        
    # def test_527_mixed_program_2(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Int = 1;
    #             Var b : Int = 20;
    #             main() {
    #                 Var a : Int = 2;
    #                 io.putInt(a + Self.b);
    #             }
    #         }
    #     """
    #     expect = "22"
    #     self.assertTrue(TestCodeGen.test(input,expect,527))
        
    # def test_528_mixed_program_3(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Float = 3.5;
    #             main() {
    #                 Var a : Float = 2.5;
    #                 io.putFloat(a + Self.a);
    #             }
    #         }
    #     """
    #     expect = "6.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,528))
        
    # def test_529_mixed_program_4(self):
    #     input = """
    #         Class D96Class {
    #             Var a : Float = 3.5;
    #             Var b : Float = 1.2;
    #             main() {
    #                 io.putFloat(Self.a - Self.b);
    #             }
    #         }
    #     """
    #     expect = "2.3"
    #     self.assertTrue(TestCodeGen.test(input,expect,529))
        
    # def test_530_mixed_program_5(self):
    #     input = """
    #         Class D96Class {
    #             Val a : Boolean = False;
    #             main() {
    #                 io.putBool(Self.a || True);
    #             }
    #         }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,530))
        
    # def test_531_mixed_program_6(self):
    #     input = """
    #         Class D96Class {
    #             Val a : Boolean = False;
    #             main() {
    #                 Val a : Boolean = False;
    #                 io.putBool(Self.a || a);
    #             }
    #         }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,531))
    
    # def test_531_assign_stmt_1(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 Var a : Int = 1;
    #                 a = 2;
    #                 io.putInt(a);
    #             }
    #         }
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input,expect,531))
        
    # def test_532_assign_stmt_2(self):
    #     input = """
    #         Class D96Class {
    #             main() {
    #                 Var a : Float = 1.2;
    #                 a = 2.2;
    #                 io.putFloat(a);
    #             }
    #         }
    #     """
    #     expect = "2.2"
    #     self.assertTrue(TestCodeGen.test(input,expect,532))
        
    def test_533_assign_stmt_3(self):
        input = """
            Class D96Class {
                
                main() {
                    Var a : Int = 1;
                    Var b : Int = 2;
                    a = b;
                    io.putInt(a);
                }
            }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,533))

        
    

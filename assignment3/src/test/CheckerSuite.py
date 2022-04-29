import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_400_redeclared_class(self):
    #     input = """
    #         Class A {}
    #         Class B {}
    #         Class B {}
    #     """
    #     expect = "Redeclared Class: B"
    #     self.assertTrue(TestChecker.test(input, expect, 400))
        
    # def test_401_undeclared_class_1(self):
    #     input = """
    #         Class A {}
    #         Class B : D {}
    #     """
    #     expect = "Undeclared Class: D"
    #     self.assertTrue(TestChecker.test(input, expect, 401))
        
    # def test_402_undeclared_class_2(self):
    #     # not forward declaration
    #     input = """
    #         Class A : B{}
    #         Class B {}
    #     """
    #     expect = "Undeclared Class: B"
    #     self.assertTrue(TestChecker.test(input, expect, 402))
    
    # def test_403_redeclared_attribute_1(self):
    #     input = """
    #         Class A {
    #             Var x : Int;
    #             Var x : Float;
    #         }
    #     """
    #     expect = "Redeclared Attribute: x"
    #     self.assertTrue(TestChecker.test(input, expect, 403))
    
    # def test_404_redeclared_attribute_2(self):
    #     input = """
    #         Class A {
    #             Var x, x : Int;
    #         }
    #     """
    #     expect = "Redeclared Attribute: x"
    #     self.assertTrue(TestChecker.test(input, expect, 404))
        
    # def test_405_redeclared_attribute_3(self):
    #     input = """
    #         Class A {
    #             Var x, x : Int;
    #         }
    #     """
    #     expect = "Redeclared Attribute: x"
    #     self.assertTrue(TestChecker.test(input, expect, 405))
    
    # def test_406_undeclared_id_1(self):
    #     input = """
    #         Class A {
    #             Var x : Int = y;
    #         }
    #     """
    #     expect = "Undeclared Identifier: y"
    #     self.assertTrue(TestChecker.test(input, expect, 406))
    
    # def test_407_undeclared_id_2(self):
    #     input = """
    #         Class A {
    #             Var x,y,z : Int = 1, 2, a;
    #         }
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input, expect, 407))
    
    # def test_408_redeclared_parameter_1(self):
    #     input = """
    #         Class A {
    #             main(a, a:Int) {}
    #         }
    #     """
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input, expect, 408))
        
    # def test_409_redeclared_parameter_2(self):
    #     input = """
    #         Class A {
    #             main(a,b:Int; c,d:Float; c:String) {}
    #         }
    #     """
    #     expect = "Redeclared Parameter: c"
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    
    # def test_410_redeclared_variable_1(self):
    #     # redeclared with parameter
    #     input = """
    #         Class A {
    #             main(a, b:Int) {
    #                 Var x, a: Float;
    #             }
    #         }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 410))
        
    # def test_411_redeclared_variable_2(self):
    #     # redeclared with variable
    #     input = """
    #         Class A {
    #             main(a, b:Int) {
    #                 Var x, y: Float;
    #                 Var y: String;
    #             }
    #         }
    #     """
    #     expect = "Redeclared Variable: y"
    #     self.assertTrue(TestChecker.test(input, expect, 411))
        
    # def test_412_redeclared_variable_3(self):
    #     # redeclared with constant
    #     input = """
    #         Class A {
    #             main(a, b:Int) {
    #                 Var y: Float;
    #                 Var y: Int;
    #             }
    #         }
    #     """
    #     expect = "Redeclared Variable: y"
    #     self.assertTrue(TestChecker.test(input, expect, 412))
    
    # def test_413_redeclared_constant_1(self):
    #     # redeclared constant with param
    #     input = """
    #         Class A {
    #             main(a, b:Int) {
    #                 Val a : Float = 5.4;
    #             }
    #         }
    #     """
    #     expect = "Redeclared Constant: a"
    #     self.assertTrue(TestChecker.test(input, expect, 413))
        
    # def test_414_redeclared_constant_2(self):
    #     # redeclared constant with constant (same line)
    #     input = """
    #         Class A {
    #             main(a, b:Int) {
    #                 Val m, n, m : Float = 2.4, 5.6, 7.8;
    #             }
    #         }
    #     """
    #     expect = "Redeclared Constant: m"
    #     self.assertTrue(TestChecker.test(input, expect, 414))
        
    # def test_415_redeclared_constant_3(self):
    #     # redeclared constant with constant
    #     input = """
    #         Class A {
    #             main(a, b:Int) {
    #                 Val m, n: Float = 2.3, 4.5;
    #                 Val c, n: String = "Nhan", "Vo";
    #             }
    #         }
    #     """
    #     expect = "Redeclared Constant: n"
    #     self.assertTrue(TestChecker.test(input, expect, 415))
        
    # def test_416_undeclared_id_3(self):
        
    #     input = """
    #         Class A {
    #             Var m : Int;
    #             Var a,b : Int;
    #             main(a,b:Int) {
    #                 Var m: Float = u;
    #             }
    #         }
    #     """
    #     expect = "Undeclared Identifier: u"
    #     self.assertTrue(TestChecker.test(input, expect, 416))
    
    # def test_417_undeclared_id_4(self):
    #     # find attribute of parent class
    #     input = """
    #         Class B {
    #             Var x, y, z: Float;
    #         }
            
    #         Class A : B {
    #             Var a,b : Int;
    #             main(c,d:Int) {
    #                 Var Nhan, Vo, Nguyen : Float = x, y, z;
    #                 Var somevalue : String = m;
    #             }
    #         }
    #     """
    #     expect = "Undeclared Identifier: m"
    #     self.assertTrue(TestChecker.test(input, expect, 417))
        
    # def test_418_undeclared_id_5(self):
    #     # find attribute of parent class
    #     input = """
    #         Class B {
    #             Var x, y, z: Float;
    #         }
            
    #         Class A : B {
    #             Var a,b : Int;
    #             main(c,d:Int) {
    #                 Var Nhan, Vo, Nguyen : Float = x, y, z;
    #                 Var somevalue : String = m;
    #             }
    #         }
    #     """
    #     expect = "Undeclared Identifier: m"
    #     self.assertTrue(TestChecker.test(input, expect, 418))
    
    # def test_419_redeclared_method_1(self):
    #     # method with method
    #     input = """
    #         Class A {
    #             function() {}
    #             function() {}
    #         }
    #     """
    #     expect = "Redeclared Method: function"
    #     self.assertTrue(TestChecker.test(input, expect, 419))
        
    # def test_420_redeclared_method_2(self):
    #     # method with attribute
    #     input = """
    #         Class A {
    #             Var function : Float;
    #             function() {}
    #         }
    #     """
    #     expect = "Redeclared Method: function"
    #     self.assertTrue(TestChecker.test(input, expect, 420))
        
    # def test_421_redeclared_attribute_4(self):
    #     # attribute with method
    #     input = """
    #         Class A {
    #             Var function : Float;
    #             $function() {}
    #             Var $function : String = function;
    #         }
    #     """
    #     expect = "Redeclared Attribute: $function"
    #     self.assertTrue(TestChecker.test(input, expect, 421))
        
    # def test_422_type_mistmatch_unary_1(self):
    #     # 
    #     input = """
    #         Class A {
    #             Var a : Float = 2.4;
    #             Var b : Int = -a;
                
    #             Var c : Boolean = True;
    #             Var d : Boolean = -c;
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: UnaryOp(-,Id(c))"
    #     self.assertTrue(TestChecker.test(input, expect, 422))
        
    # def test_423_type_mistmatch_unary_2(self):
    #     # 
    #     input = """
    #         Class A {
    #             Var a, b, c : Boolean;
    #             Var d : Int = -b;
    #         }
    #     """
    #     expect = "Type Mismatch In Expression: UnaryOp(-,Id(b))"
    #     self.assertTrue(TestChecker.test(input, expect, 423))
    
    # def test_424_illegal_const_exp_1(self):
    #     # no initialize value
    #     input = """
    #         Class A {
    #             Val a : Float; 
    #         }
    #     """
    #     expect = "Illegal Constant Expression: None"
    #     self.assertTrue(TestChecker.test(input, expect, 424))
        
    # def test_425_illegal_const_exp_2(self):
    #     # assign to mutable attribute
    #     input = """
    #         Class Nhan {
    #             method() {
    #                 Var a : Float = 2;
    #                 Var b : Int = a;
    #             }
    #         }
    #     """
    #     expect = "Illegal Constant Expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input, expect, 425))
          
    # def test_426_illegal_const_exp_3(self):
    #     # 
    #     input = """
    #         Class A {
    #             Var c : String;
    #             Val d : String = -c;
    #         }
    #     """
    #     expect = "Illegal Constant Expression: UnaryOp(-,Id(c))"
    #     self.assertTrue(TestChecker.test(input, expect, 426))
        
    def test_427_illegal_const_exp_4(self):
        # 
        input = """
            Class A {
                Var c : Boolean = True;
                Val d : String = !c;
            }
        """
        expect = "Illegal Constant Expression: UnaryOp(!,Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 427))
    


    
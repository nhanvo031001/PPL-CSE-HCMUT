import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_999(self):
        input = """
            Class D96Class {

                main() {
                    Var a : Int = 1;
                    Var b : Int = 2;
                    io.writeIntLn(b);
                }
            }
        """
        expect = "22"
        self.assertTrue(TestCodeGen.test(input,expect,999))
        
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """void main() {putInt(100);}"""
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
        
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],VoidType(),Block([],[
    # 			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))

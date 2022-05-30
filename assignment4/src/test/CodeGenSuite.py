import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_999(self):
        input = """
            Class D96Class {
                Var c : String = "Nhan Vo";
                Var d: Boolean = False;
                main() {
                    Var a : Int = 1;
                    Var b : Float = 2.2;
                    io.writeIntLn(a);
                    io.writeFloatLn(b);
                    io.writeStrLn(Self.c);
                    io.writeBoolLn(Self.d);
                
                    Val e : Int = 100;
                    Val f : Float = 200.2;
                    io.writeIntLn(-e);
                    io.writeFloatLn(f);
                    io.writeIntLn(-e + a);
                    io.writeIntLn(e * 2);
                    io.writeFloatLn(3.0 / 2.0);
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

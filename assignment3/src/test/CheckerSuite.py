import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
            Class Program{
                main() {
                    Var a,b,c:Boolean;
                    Var d : String;
                    If (a) {}
                    Elseif(b) {
                        If (a) {}
                        Elseif(d) {}
                    }
                    Elseif(c) {}
                    Elseif(a) {}
                }
                
                func() {
                    Var d,e,f:Boolean;
                    Var g : String;
                    If (d) {}
                    Elseif(e) {}
                    Elseif(f) {}
                    Elseif(d) {}
                }
            }
        """
        expect = "Redeclared Class: B"
        self.assertTrue(TestChecker.test(input, expect, 400))



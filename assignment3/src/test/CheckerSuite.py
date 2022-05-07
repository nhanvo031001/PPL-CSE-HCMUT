import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
            Class Program {
                main() {}
            }
        """
        expect = "Redeclared Class: B"
        self.assertTrue(TestChecker.test(input, expect, 400))
    
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))
    
    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: "
    #     self.assertTrue(TestParser.test(input,expect,203))
    
    def test_some_relational_expressions(self):
        input = "-5 == 5\n"
        input += "5 != 4\n"
        input += "5 > 4\n"
        input += "3 < 4\n"
        input += "5 >= 4\n"
        input += "3 <= 4\n"
        input += "a == 5\n"
        input += "a < 5\n"
        input += "a > 5\n"
        input += "a <= 5\n"
        input += "a >= 5\n"
        input += "a == xyz\n"
        input += "a != $xyz\n"
        input += "a > nhanvo\n"
        input += "a < ldpv\n"
        input += "a >= abc\n"
        input += "a <= abc\n"
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test_some_arithmetic_expressions(self):
        input = "-130703100310 + -255255255255\n"
        input += "-130703100310 - 255255255255\n"
        input += "-130703100310 / 255255255255\n"
        input += "130703100310 % 255255255255\n"
        input += "-130703100310.213e-10 + -255255255255.3e+10\n"
        input += "0.0000001e10 - -0.00000000000000008e-10\n"
        input += "99999.10e30 / -123456789.10e-20\n"
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
        
    def test_some_boolean_expressions(self):
        input = "!5 !6 !7 \n"
        input += "!xyz !True !False\n"
        input += """0b1111111111 && 0B0101010101\n"""
        input += """0b1111111111 || 0B0101010101\n"""
        input += """ "First string compare with" ==. "Second string"\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
        
    def test_string_expression(self):
        input = """str1 +. str2\n"""
        input += """ "Nhan Vo Nguyen Thien" +. str2\n"""
        input += """ str1 +. "Nhan Vo Nguyen Thien"\n"""
        input += """ "Nhan Vo Nguyen Thien" +. "LDPV"\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
        
    def test_index_operator_expression(self):
        input = """arr[1] x[1][2] x[1][2][3] x[1][2][3][4]\n"""
        input += """arr[arr[1]] arr[arr[arr[1]]]"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
        
    def test_statement_assignment(self):
        input = """a = 2;\n"""
        input += """$abc = 2+5;\n"""
        input += """$abc = (0x010101 && 0x1100100);\n"""
        input += """$abc = (0x010101 || 0x1100100);\n"""
        input += """$abc = "first string" + "second string";\n"""
        input += """$abc = arr[1][2];\n"""
        input += """$abc = arr[arr[arr[1]]];\n"""
        input += """arr[2] = arr[arr[arr[1]]];\n"""
        input += """arr[arr[arr[arr[100]]]] = a.b;\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
        
    def test_statement_if(self):
        input = """If (a == 5) {##nothing##}\n"""
        input += """If (2+5 == 5) {##nothing##}\n"""
        input += """If (arr[arr[arr[arr[100]]]] == (0x010101 && 0x1100100)) {##nothing##}\n"""
        input += """If (True) {##nothing##}\n"""
        input += """If (!True && False && ( (a == 5) || (b == 6) ) ) {##nothing##}\n"""
        input += """If (!True && False) { ##nothing## } Else {##nothing##}\n"""
        input += """If (!True && False) { ##nothing## } 
                    Elseif (a == 5) {##nothing##}
                    Elseif (b == 6) {  }
                    Elseif (!False) {##nothing##}
                    Elseif (a < b) {##nothing##}
                    Elseif ($xyz >= 3) {##nothing##}
                    Elseif (ar[2] > 3) {##nothing##}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
        
    def test_statement_if_2(self):
        input = """If (!True && False) { ##nothing## } 
                    Else {
                        If (!True && False && ( (a == 5) || (b == 6) ) ) {##nothing##}
                    }\n
                """
        input += """If (!True && False) { ##nothing## } 
                    Elseif (a == 5) {
                        If (!True && False) { ##nothing## } 
                        Elseif (a == 5) {##nothing##}
                        Elseif (b == 6) {  }
                        Elseif (!False) {##nothing##}
                        Elseif (a < b) {##nothing##}
                        Elseif ($xyz >= 3) {##nothing##}
                        Elseif (ar[2] > 3) {##nothing##}    
                    }
                    Elseif (b == 6) {
                        If (!True && False) { ##nothing## } 
                        Elseif (a == 5) {##nothing##}
                        Elseif (b == 6) {  }
                        Elseif (!False) {##nothing##}
                        Elseif (a < b) {##nothing##}
                        Elseif ($xyz >= 3) {##nothing##}
                        Elseif (ar[2] > 3) {##nothing##}    
                    }
                    Else {
                        If (!True && False) { ##nothing## } 
                        Elseif (a == 5) {##nothing##}
                        Elseif (b == 6) { 
                            If (!True && False) { ##nothing## } 
                            Elseif (a == 5) {##nothing##}
                            Elseif (b == 6) {  }
                            Elseif (!False) {##nothing##}
                            Elseif (a < b) {##nothing##}
                            Elseif ($xyz >= 3) {##nothing##}
                            Elseif (ar[2] > 3) {##nothing##}
                        }
                        Elseif (!False) {##nothing##}
                        Elseif (a < b) {##nothing##}
                        Elseif ($xyz >= 3) {##nothing##}
                        Elseif (ar[2] > 3) {##nothing##}
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
        
    def test_statement_for_in(self):
        input = """Foreach (i In 1 .. 100 By 2) {
                    If (!True && False) { ##nothing## } 
                    Elseif (a == 5) {##nothing##}
                    Elseif (b == 6) {  }
                    Elseif (!False) {##nothing##}
                    Elseif (a < b) {##nothing##}
                    Elseif ($xyz >= 3) {##nothing##}
                    Elseif (ar[2] > 3) {##nothing##}
                }               
                \n"""
        input += """
                    Foreach (x In 5+2 .. 100*3) {
                        a = a + 1;
                        b = b - 1;
                        arr[arr[arr[arr[100]]]] = a.b;
                    }
                \n"""
        input += """
                    Foreach ($abc In (-123456 + -34231) .. 2) {
                        If ($abc == 4) {
                            Continue;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
        
    def test_statement_break(self):
        input = """Foreach (i In 1 .. 100 By 2) {
                    If (!True && False) { Break; } 
                    Elseif (a == 5) { Break; }
                    Elseif (b == 6) {  }
                    Elseif (!False) {##nothing##}
                    Elseif (a < b) {##nothing##}
                    Elseif ($xyz >= 3) {##nothing##}
                    Elseif (ar[2] > 3) {##nothing##}
                }               
                \n"""
        input += """
                    Foreach (x In 5+2 .. 100*3) {
                        Break;
                    }
                \n"""
        input += """
                    Foreach ($abc In (-123456 + -34231) .. 2) {
                        If ($abc == 4) {
                            Break;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
        
    def test_statement_continue(self):
        input = """Foreach (i In 1 .. 100 By 2) {
                    If (!True && False) { Continue; } 
                    Elseif (a == 5) { Break; }
                    Elseif (b == 6) {  }
                    Elseif (!False) {Continue;}
                    Elseif (a < b) {##nothing##}
                    Elseif ($xyz >= 3) {##nothing##}
                    Elseif (ar[2] > 3) {##nothing##}
                }               
                \n"""
        input += """
                    Foreach (x In 5+2 .. 100*3) {
                        Continue;
                    }
                \n"""
        input += """
                    Foreach ($abc In (-123456 + -34231) .. 2) {
                        If ($abc == 4) {
                            Continue;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
        
    def test_statement_return(self):
        input = """Foreach (i In 1 .. 100 By 2) {
                    If (!True && False) { Continue; } 
                    Elseif (a == 5) { Break; }
                }               
                \n"""
        input += """
                    Foreach (x In 5+2 .. 100*3) {
                        If (x == (3*2--3)) {
                            Return "Nhan Vo";   
                        }
                    }
                \n"""
        input += """
                    Foreach ($abc In (-123456 + -34231) .. 2) {
                        If ($abc == 4) {
                            Return;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    
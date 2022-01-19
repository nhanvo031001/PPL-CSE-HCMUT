import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_some_relational_expressions(self):
        input = """
                Class Program {
                    
                    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                    Var $x, $y : Int = 0, 0;
                    
                    Constructor(a: Int; B: Float) {
                        $x = 10;
                        $y = 1000;
                        My1stCons = 5 + 2;
                        My2ndCons = (0b1101010 && 0b1101110);
                    }
                    
                    Destructor() {
                        $x = 0;
                        $y = 0;
                        My1stCons = 0;
                        My2ndCons = 0;
                    }
                    
                    test() {
                        If (-5 == 5) {##nothing##}
                        If (5 != 4) {##nothing##}
                        If (5 > 4) {##nothing##}
                        If (3 < 4) {##nothing##}
                        If (5 >= 4) {##nothing##}
                        If (3 <= 4) {##nothing##}
                        If (a == 5) {##nothing##}
                        If (a < 5) {##nothing##}
                        If (a > 5) {##nothing##}
                        If (a <= 5) {##nothing##}
                        If (a >= 5) {##nothing##}
                        If (a == xyz) {##nothing##}
                        If (a != $xyz) {##nothing##}
                        If (a > nhanvo) {##nothing##}
                        If (a < ldpv) {##nothing##}
                        If (a >= abc) {##nothing##}
                        If (a <= abc) {##nothing##}
                    }
                    
                    main() {
                        
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    
    def test_some_arithmetic_expressions(self):
        input = """
                Class Program {
                    
                    Val a: Int = 130703100310 + -255255255255;
                    Val b: Int = -130703100310 - 255255255255;
                    Var m: Int =-130703100310 / 255255255255;
                    Var c: Int = 130703100310 % 255255255255;
                    Var d: Float = -130703100310.213e-10 + -255255255255.3e+10;
                    Var e: Float = 0.0000001e10 - -0.00000000000000008e-10;
                    Var f: Float = 99999.10e30 / -123456789.10e-20;
        
                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
        
    def test_some_boolean_expressions(self):
        input = """
                Class Program {
                    
                    Val a: Int = 0b1111111111 && 0B1101010101;
                    Val b: Int = 0b1111111111 || 0B1101010101;
                    Var m: String = "First string compare with" ==. "Second string";
                    Var c: Int = 130703100310 % 255255255255;
                    Var d: Float = -130703100310.213e-10 + -255255255255.3e+10;
                    Var e: Float = 0.0000001e10 - -0.00000000000000008e-10;
                    Var f: Float = 99999.10e30 / -123456789.10e-20;
        
                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        If (!True) {
                            ##nothing##
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
        
    def test_string_expression(self):
        input = """
                Class Program {
                    
                    Val str1: String = "xyz";
                    Val str2: String = "double xyz";
                    Val a: String = str1 +. str2;
                    Var c: String =  "Nhan Vo Nguyen Thien" +. str2;
                    Var c: String =  str1 +. "Nhan Vo Nguyen Thien";
                    Var c: String =  "Nhan Vo Nguyen Thien" +. "LDPV";

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
        
    def test_index_operator_expression(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];
                    Val str2: String = x[1][2];
                    Val a: String = x[1][2][3];
                    Var c: String =  x[1][2][3][4];
                    Var c: String =  arr[arr[arr[1]]];
                    Var c: String =  arr[arr[1]];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
        
    def test_statement_assignment(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];
                    Val str2: String = x[1][2];
                    Val a: String = x[1][2][3];
                    Var c: String =  x[1][2][3][4];
                    Var c: String =  arr[arr[arr[1]]];
                    Var c: String =  arr[arr[1]];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        a = 2;
                        abc = 2+5;
                        abc = (0b110101 && 0b1100100);
                        abc = (0b010101 || 0b1100100);
                        abc = "first string" + "second string";
                        abc = arr[1][2];
                        $abc = arr[arr[arr[1]]];
                        arr[2] = arr[arr[arr[1]]];
                        arr[arr[arr[arr[100]]]] = a.b;
                    }
                }
                """
        expect = "Error on line 19 col 34: 10101"
        self.assertTrue(TestParser.test(input,expect,206))
        
    def test_statement_if(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        If (a == 5) {##nothing##}
                        If (2+5 == 5) {##nothing##}
                        If (arr[arr[arr[arr[100]]]] == (0b110101 && 0B1100100)) {##nothing##}
                        If (True) {##nothing##}
                        If (!True && False && ( (a == 5) || (b == 6) ) ) {##nothing##}
                        
                        If (!True && False) { ##nothing## } Else {##nothing##}
                        
                        If (!True && False) { ##nothing## } 
                        Elseif (a == 5) {##nothing##}
                        Elseif (b == 6) {  }
                        Elseif (!False) {##nothing##}
                        Elseif (a < b) {##nothing##}
                        Elseif ($xyz >= 3) {##nothing##}
                        Elseif (ar[2] > 3) {##nothing##}
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
        
    def test_statement_if_2(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        If (!True && False) { ##nothing## } 
                        Else {
                            If (!True && False && ( (a == 5) || (b == 6) ) ) {##nothing##}
                        }
                        
                        If (!True && False) { ##nothing## } 
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
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
        
    def test_statement_for_in(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        Foreach (i In 1 .. 100 By 2) {
                            If (!True && False) { ##nothing## } 
                            Elseif (a == 5) {##nothing##}
                            Elseif (b == 6) {  }
                            Elseif (!False) {##nothing##}
                            Elseif (a < b) {##nothing##}
                            Elseif ($xyz >= 3) {##nothing##}
                            Elseif (ar[2] > 3) {##nothing##}
                        }
                        
                        Foreach (x In 5+2 .. 100*3) {
                            a = a + 1;
                            b = b - 1;
                            arr[arr[arr[arr[100]]]] = a.b;
                        }
                        
                        Foreach ($abc In (-123456 + -34231) .. 2) {
                            If ($abc == 4) {
                                Continue;
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
        
    def test_statement_break(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        Foreach (i In 1 .. 100 By 2) {
                            If (!True && False) { Break; } 
                            Elseif (a == 5) { Break; }
                            Elseif (b == 6) {  }
                        }
                        
                        Foreach (x In 5+2 .. 100*3) {
                            Break;
                        }
                        
                        Foreach ($abc In (-123456 + -34231) .. 2) {
                            If ($abc == 4) {
                                Break;
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
        
    def test_statement_continue(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        Foreach (i In 1 .. 100 By 2) {
                            If (!True && False) { Continue; } 
                            Elseif (a == 5) { Break; }
                            Elseif (b == 6) {  }
                            Elseif (!False) {Continue;}
                        }
                        
                        Foreach (x In 5+2 .. 100*3) {
                            Continue;
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
        
    def test_statement_return(self):
        input = """
                Class Program {
                    
                    Val str1: String = arr[1];

                    Constructor(a: Int; B: Float) {}
                    
                    Destructor() {}

                    main() {
                        Foreach (i In 1 .. 100 By 2) {
                            If (!True && False) { Continue; } 
                            Elseif (a == 5) { Break; }
                        }
                        
                        Foreach (x In 5+2 .. 100*3) {
                            If (x == (3*2--3)) {
                                Return "Nhan Vo";   
                            }
                        }
                        
                        Foreach ($abc In (-123456 + -34231) .. 2) {
                            If ($abc == 4) {
                                Return;
                            }
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
        
    def test_some_class_declare(self):
        input = """Class Program {

                }
                \n"""
        input += """
                    Class NhanVo {
                        Constructor() {
                            Foreach (x In 5+2 .. 100*3) {
                                If (x == (3*2--3)) {
                                    Return "Nhan Vo";   
                                }
                            }
                        }
                        
                        Constructor(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            Foreach (i In 1 .. 100 By 2) {
                                If (!True && False) { Continue; } 
                                Elseif (a == 5) { Break; }
                                Elseif (b == 6) {  }
                                Elseif (!False) {Continue;}
                                Elseif (a < b) {##nothing##}
                                Elseif ($xyz >= 3) {##nothing##}
                                Elseif (ar[2] > 3) {##nothing##}
                            }      
                        }
                        
                        Destructor() {
                            If (a == b) {
                                If (c == d) {
                                    ##nothing##
                                }
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
        
    def test_some_class_declare_2(self):
        input = """
                    Class NhanVo {
                        
                        Constructor(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            Foreach (i In 1 .. 100 By 2) {
                                If (!True && False) { Continue; } 
                                Elseif (a == 5) { Break; }
                                Elseif (b == 6) {  }
                                Elseif (!False) {Continue;}
                                Elseif (a < b) {##nothing##}
                                Elseif ($xyz >= 3) {##nothing##}
                                Elseif (ar[2] > 3) {##nothing##}
                            }      
                        }
                        
                        Destructor(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            If (a == b) {
                                If (c == d) {
                                    ##nothing##
                                }
                            }
                        }
                    }
                """
        expect = "Error on line 16 col 35: a"
        self.assertTrue(TestParser.test(input,expect,214))
        
    def test_some_class_declare_3(self):
        input = """
                    Class NhanVo {
                        
                        Constructor(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            Foreach (i In 1 .. 100 By 2) {
                                If (!True && False) { Continue; } 
                                Elseif (a == 5) { Break; }
                                Elseif (b == 6) {  }
                                Elseif (!False) {Continue;}
                                Elseif (a < b) {##nothing##}
                                Elseif ($xyz >= 3) {##nothing##}
                                Elseif (ar[2] > 3) {##nothing##}
                            }      
                        }
                        
                        Destructor() {
                            If (a == b) {
                                If (c == d) {
                                    ##nothing##
                                }
                            }
                        }
                        
                        getElement(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            ##nothing##
                        }
                        
                        getIndex(a, b, c, d: Int; d, e, f: NhanVo; m: Float; n: String) {
                            If (a == b) {
                                If (c == d) {
                                    ##nothing##
                                }
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
        
    def test_some_class_declare_4(self):
        input = """
                    Class Shape {
                        $getNumofShape( {
                            Return self.length;
                        }
                    }
                """
        expect = "Error on line 3 col 40: {"
        self.assertTrue(TestParser.test(input,expect,216))
        
    def test_some_array(self):
        input = """
                    Class Shape {
                        Var a: Float = 45;
                        Var b: Float = 45.67;
                        Var c: Array[Int, 5] = Array(1, 2, 3, 4, 5);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
        
    def test_some_multidimensional_array(self):
        input = """
                    Class Shape {
                        main() {
                            a = Array();
                            $b = Array (
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
        
    def test_some_member_access(self):
        input = """
                    Class Shape {
                        main() {
                            a = object.length;
                            c = Shape::$width;
                            d = obj.getLength("abcd", 12);
                            f = Shape::$getWidth();
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
        
    def test_simple_progeam(self):
        input = """
                    Class Shape {
                        Var a: Int;
                        Notmain() {
                            x = 4;
                        }
                    }
                    
                    Class _program {
                        main() {
                            Val x: Float;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
        
    def test_error_simple_program(self):
        input = """
                    Class Shape {
                        Var a: Int;
                        Notmain() {
                            x = 4;
                        }
                    }
                    
                    class _program {
                        main() {
                            Val x: Float;
                        }
                    }
                """
        expect = "Error on line 9 col 20: class"
        self.assertTrue(TestParser.test(input,expect,221))
        
    def test_some_define_method(self):
        input = """
                    Class Shape {
                        method1() {}
                        method2(a, b: Int; c: Array[Int, 5]) {}
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
        
    def test_some_error_declare_var(self):
        input = """
                    Class Shape {
                        method2() {
                            Var a: Int;
                        }
                        
                        method1() {
                            Var $a: Int;
                        }
                    }
                """
        expect = "Error on line 8 col 32: $a"
        self.assertTrue(TestParser.test(input,expect,223))
        
    def test_some_method_invoke(self):
        input = """
                    Class Shape {
                        method2() {
                            obj.method1();
                        }
                        
                        method1() {
                            obj.method2();
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
        
    def test_multidimensional_array_declare(self):
        input = """
                    Class Shape {
                        Var arr: Array[Array[Int, 3], 3] = Array (
                                                            Array (3,4,5),
                                                            Array (6,7,8),
                                                            Array (9,10,11)
                                                                );
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
        
    def test_invalid_member_access(self):
        input = """
                    Class Shape {
                        main() {
                            a = b.$c;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    
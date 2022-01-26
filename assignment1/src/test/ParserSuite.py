import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_some_relational_expressions(self):
        input = """
                Class Program {
                    
                    Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                    Var $x, $y, z : Int = 0, 0, 0;
                    
                    Constructor(a: Int; B: Float) {
                        x = 10;
                        y = 1000;
                        My1stCons = 5 + 2;
                        My2ndCons = (0b1101010 && 0b1101110);
                    }
                    
                    Destructor() {
                        x = 0;
                        y = 0;
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
                        If (a != Shape::$xyz) {##nothing##}
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
                        Elseif (Shape::$xyz >= 3) {##nothing##}
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
                            Elseif (Shape::$xyz >= 3) {##nothing##}
                            Elseif (ar[2] > 3) {##nothing##}    
                        }
                        Elseif (b == 6) {
                            If (!True && False) { ##nothing## } 
                            Elseif (a == 5) {##nothing##}
                            Elseif (b == 6) {  }
                            Elseif (!False) {##nothing##}
                            Elseif (a < b) {##nothing##}
                            Elseif (Shape::$xyz >= 3) {##nothing##}
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
                                Elseif (Shape::$xyz >= 3) {##nothing##}
                                Elseif (ar[2] > 3) {##nothing##}
                            }
                            Elseif (!False) {##nothing##}
                            Elseif (a < b) {##nothing##}
                            Elseif (Shape::$xyz >= 3) {##nothing##}
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
                            Elseif (Shape::$xyz >= 3) {##nothing##}
                            Elseif (ar[2] > 3) {##nothing##}
                        }
                        
                        Foreach (x In 5+2 .. 100*3) {
                            a = a + 1;
                            b = b - 1;
                            arr[arr[arr[arr[100]]]] = a.b;
                        }
                        
                        Foreach (abc In (-123456 + -34231) .. 2) {
                            If (Shape::$abc == 4) {
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
                        
                        Foreach (bc In (-123456 + -34231) .. 2) {
                            If (Shape::$abc == 4) {
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
                        
                        Foreach (abc In (-123456 + -34231) .. 2) {
                            If (Shape::$abc == 4) {
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
                                Elseif (Shape::$xyz >= 3) {##nothing##}
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
                                Elseif (Shape::$xyz >= 3) {##nothing##}
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
                                Elseif (Shape::$xyz >= 3) {##nothing##}
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
                            Shape::$b = Array (
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
        
    def test_error_keyword_Val(self):
        input = """
                    Class Shape {
                        main() {
                            val x: String = "Nhan vo";
                        }
                    }
                """
        expect = "Error on line 4 col 32: x"
        self.assertTrue(TestParser.test(input,expect,226))
        
    def test_unequal_vars_and_values(self):
        input = """
                    Class Shape {
                        Val x, y: Int = 4;
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 3 col 41: ;"
        self.assertTrue(TestParser.test(input,expect,227))
        
    def test_unequal_vars_and_values_2(self):
        input = """
                    Class Shape {
                        Val x, y, $a: Int = 4, 6, 7, 9;
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 3 col 51: ,"
        self.assertTrue(TestParser.test(input,expect,228))
        
    def test_unequal_vars_and_values_3(self):
        input = """
                    Class Shape {
                        Var a, b: Float = 10;
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 3 col 44: ;"
        self.assertTrue(TestParser.test(input,expect,229))
        
    def test_unequal_vars_and_values_4(self):
        input = """
                    Class Shape {
                        Var a, b: Float = 10.e10, 3.23;
                        Val $x, $y: String = "nhanvo", "nguyenthien", "blabla";
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 4 col 68: ,"
        self.assertTrue(TestParser.test(input,expect,230))
        
    def test_unequal_vars_and_values_5(self):
        input = """
                    Class Shape {
                        Var a, b: Float = 10.e10, 3.23;
                        Val $x, $y: String = "nhanvo", "nguyenthien", "blabla","xyz", "str1" + "str2";
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 4 col 68: ,"
        self.assertTrue(TestParser.test(input,expect,231))
    
    def test_valid_attribute_declare(self):
        input = """
                    Class Shape {
                        Var a, b: Float = 10.e10, 3.23;
                        Val $x, $y, $z: String = "nhanvo", "xyz", "str1" + "str2";
                        main() {
                            a = b;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
        
    def test_valid_attribute_declare_2(self):
        input = """
                    Class Shape {
                        Var x, $y, z: Boolean;
                        Var m, $n, p: Boolean = True, False, False;
                        main() {
                            a = b;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
        
    def test_valid_attribute_declare_3(self):
        input = """
                    Class Shape {
                        Var m: Array[Int, 5] = Array(1, 2, 3, 4, 5);
                        main() {
                            
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
        
    def test_valid_attribute_declare_4(self):
        input = """
                Class Shape {
                    Var m: Array[Array[Int, 3], 3] = Array (Array(1,2,3), Array(4,5,6), Array(8,9,10));
                    main() {
                        
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
        
    def test_class_inhertance(self):
        input = """
                    Class Shape {}
                    Class Triangle : Shape {}
                    Class Circle : Triangle {}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
        
    def test_method_declare(self):
        input = """
                    Class Shape {
                        getLength() {
                            Return length;
                        }
                        
                        getShape(a, b, c, d: Int; str1, str2: String) {
                            Return str1 + str2;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
        
    def test_static_method_declare(self):
        input = """
                    Class Shape {
                        $getLength() {
                            Return Shape::$length;
                        }
                        
                        $getShape(a, b, c, d: Int; str1, str2: String) {
                            Return str1 + str2;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
        
    def test_wrong_declare_class(self):
        input = """
                    Class Shape {
                        main() {
                            a = "nhan" + "vo";
                        }
                        
                        Constructor() {}
                        Destructor() {}
                    };
                """
        expect = "Error on line 9 col 21: ;"
        self.assertTrue(TestParser.test(input,expect,239))
        
    def test_some_object_creation(self):
        input = """
                    Class Shape {
                        
                    }
                    
                    Class Program {
                        main() {
                            a = New Shape();
                            a = New Shape(a, "nhanvo", 12+5-12*23, 8/2);
                            a = New Shape(New Shape(12, 3));
                            a = New Shape(New Shape(New Shape(New Shape(New Shape(New Shape(12, 3))))));
                            a = New Shape(arr[arr[arr[1]]][2]);
                            a = New Shape(Shape.length, Shape.arr[arr[arr[2]]], obj.getLength(12, 3));
                            a = (New Shape())[arr[1]];
                            a = (New Shape()).a.a.a.a;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
        
    def test_unary_operator(self):
        input = """
                    Class Program {
                        main() {
                            a = -4;
                            a = --4;
                            a = ---4;
                            a = !True;
                            a = !!True;
                            a = !!!True;
                            a = !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!True;
                            a = !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(True && False);
                            a = ------------ (12 + 5 * 3 - 6 + 3 / 14 - 7);
                            a =  !(12 + 5 * 3 - 6 + 3 / 14 - 7);
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
        
    def test_variable_and_constant_declare(self):
        input = """
                    Class Program {
                        main() {
                            Var x: Int;
                            Var x: Int = 5;
                            Var x, y: Int = 5, 6;
                            Var x, y, z: Int = -5, ------------6, "nhanvo" + "vo" + "nguyen" + "thien";
                            Var x, y, z: Int = 5, 6, New Shape(New Shape(New Shape(New Shape(New Shape(New Shape(12, 3))))));
                            Var x: Array[Array[Int, 3], 3] = Array (Array(1,2,3), Array(4,5,6), Array(8,9,10));
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
        
    def test_invalid_variable_and_constant_declare(self):
        input = """
                    Class Program {
                        main() {
                            Var x: Float = 3.4, 5.6;
                        }
                    }
                """
        expect = "Error on line 4 col 46: ,"
        self.assertTrue(TestParser.test(input,expect,243))
        
    def test_invalid_variable_and_constant_declare_1(self):
        input = """
                    Class Program {
                        main() {
                            Var x, y, z, m, n, p: Float = 3.4, 5.6;
                        }
                    }
                """
        expect = "Error on line 4 col 66: ;"
        self.assertTrue(TestParser.test(input,expect,244))
        
    def test_invalid_variable_and_constant_declare_2(self):
        input = """
                    Class Program {
                        Var $x: Int = 5;
                        Var $y, $z: Float;
                        
                        main() {
                            Var $a: Int;
                        }
                    }
                """
        expect = "Error on line 7 col 32: $a"
        self.assertTrue(TestParser.test(input,expect,245))
        
    def test_invalid_variable_and_constant_declare_3(self):
        input = """
                    Class Program {
                        Var $x: Int = 5;
                        Var $y, $z: Float;
                        
                        main() {
                            Var a Int = 5;
                        }
                    }
                """
        expect = "Error on line 7 col 34: Int"
        self.assertTrue(TestParser.test(input,expect,246))
        
    def test_array_type_declare(self):
        input = """
                    Class Program {
                        Var x: Array[Int, 1000];
                        Var x: Array[Int, 0];
                        
                        main() {
                            
                        }
                    }
                """
        expect = "Error on line 4 col 42: 0"
        self.assertTrue(TestParser.test(input,expect,247))
        
    def test_some_method_declaration(self):
        input = """
                    Class Program {
                        
                        method(arr1, arr2: Array[Int, 5]; arr3: Array[Array[Int, 3], 3]) {
                            ## nothing ##
                        }
                        
                        main() {
                            ## nothing ##
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
        
    def test_array_type_declare_2(self):
        input = """
                    Class Program {
                        
                        method(arr1, arr2: Array[Int, 5]; arr3: Array[Array[Int, 3], 3]) {
                            Var newArr: Array[Float, 3] = Array (1.2, 4.3, 5.600);
                        }
                        
                        main() {
                            Var arr: Array[String, 0] = Array();
                        }
                    }
                """
        expect = "Error on line 9 col 51: 0"
        self.assertTrue(TestParser.test(input,expect,249))
        
    def test_program_no_class(self):
        input = """
                
                """
        expect = "Error on line 3 col 16: <EOF>"
        self.assertTrue(TestParser.test(input,expect,250))
        
    def test_multidimensional_array(self):
        input = """
                    Class Program {
                        Var a: Array[Int, 1] = Array(Array(Array(1,2,3)));
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
        
    def test_multiple_inheritance(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                    }
                    
                    Class Shape {
                        Constructor() {
                            Var x: String = "nhanvo" + "nguyenthien";
                        }
                    }
                    
                    Class Child : Program : Shape {
                        
                    }
                """
        expect = "Error on line 14 col 42: :"
        self.assertTrue(TestParser.test(input,expect,252))
        
    def test_instance_attribute_access(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            x = a.b;
                            x = New X().b;
                            x = (arr[1]).b;
                            x = Shape::$obj.b;
                            x = Shape::$obj.b;
                            x = a.func(a, b, "xyz").b;
                            x = a.func(a, b, "xyz").func2(a, b, "xyz").b;
                            x = a.func(a, b, "xyz").func2(a, b, "xyz").func3(a, b, "xyz").b;
                            x = Shape::$func(a, b, c).b;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
        
    def test_static_attribute_access(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            x = Shape::$attr;
                            x = Circle::$area;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
        
    def test_static_attribute_access_2(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            ## no chaining calling ##
                            x = Shape::$attr::$attr2;
                        }
                    }
                """
        expect = "Error on line 9 col 44: ::"
        self.assertTrue(TestParser.test(input,expect,255))
        
    def test_instance_method_invocation(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            x.func();
                            x.func(a, b, c, d, "nhanvo", 1+2, "str1" + "str2");
                            x.func(a, "nhanvo", 1+2, "str1" + "str2").func2(a, "nhanvo", 1+2, "str1" + "str2");
                            x.func(a, "nhanvo", 1+2, "str1" + "str2").func2(a, "nhanvo", 1+2, "str1" + "str2").func3(a, "nhanvo", 1+2, "str1" + "str2");
                            New X().func();
                            New X().func().func2();
                            (New X().func().objInClass).func2();
                            (Shape::$obj).func();
                            New X().c.func();
                            (arr[1]).c.func();
                            Shape::$obj.obj2.func();
                            obj.obj2.func();
                            ("str" + "str").func();     ## ???? ##
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
        
    def test_static_method_invocation(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            Shape::$getLength();
                            Shape::$getLength(a, b, "nhan", 1+2-3*4/5, arr[1]);
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
        
    def test_invalid_static_method_invocation(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            Shape::getLength();
                            Shape::$getLength(a, b, "nhan", 1+2-3*4/5, arr[1]);
                        }
                    }
                """
        expect = "Error on line 8 col 35: getLength"
        self.assertTrue(TestParser.test(input,expect,258))
        
    def test_keyword_self(self):
        input = """
                    Class Program {
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        main() {
                            Return Self.length * Self.width;
                        }
                        
                        getArea() {
                            r = Self.getR();
                            area = pi * r * r;
                            Return area;
                        }
                        
                        getR() {
                            Return Self.r;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
        
    def test_keyword_self_2(self):
        ## Self not used with static attribute and static method ???
        input = """
                    Class Program {
                        Var $abc: Float = 12.0000;
                        
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                        }
                        
                        $getWidth(a, b: Int; c: Float) {
                            Return (a-b)*c;
                        }
                        
                        main() {
                            Self.garbage = Self.$abc;
                            Self.w = Self.$getWidth();
                            Return Self.$length * Self.$width;
                        }
                    }
                """
        expect = "Error on line 14 col 48: $abc"
        self.assertTrue(TestParser.test(input,expect,260))
    
    def test_method_invocation_statement(self):
        ## Self not used with static attribute and static method ???
        input = """
                    Class Program {
                        Var $abc: Float = 12.0000;
                        Var arr: Array[Int, 5] = Array (1, 2, 3, 4, 5);
                        Var length: Int = 0;
                        Val $width : Int = 0;
                        
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                            Return;
                        }
                        
                        getLength() {
                            Self.length = 12 - 5 + 5 / 7 * 6 - arr[1];
                            Return Self.length;
                        }
                        
                        $getWidth(a, b: Int; str: String) {
                            Shape::$width = 12 - 5 + 5 / 7 * 6 - arr[4];
                            Return $width;
                        }
                        
                        main() {
                            Var a: Int = getLength();   ## calling method inside class ##
                            Var b: Int = $getWidth(a, b, "nhan");   ## calling method inside class ##
                            Return a-b;
                        }
                    }
                """
        # expect = "successful"
        expect = "Error on line 20 col 35: $width"
        self.assertTrue(TestParser.test(input,expect,261))
        
    def test_method_invocation_statement_2(self):
        input = """
                    Class Program {
                        Var $abc: Float = 12.0000;
                        Var arr: Array[Int, 5] = Array (1, 2, 3, 4, 5);
                        Var length: Int = 0;
                        Val $width : Int = 0;
                        
                        Constructor(a, b, c, d: Int; x, y, z: String; arr: Array[Int, 3]) {
                            Var a: Int;
                            Return;
                        }
                        
                        getLength() {
                            Self.length = 12 - 5 + 5 / 7 * 6 - arr[1];
                            Return Self.length;
                        }
                        
                        $getWidth(a, b: Int; str: String) {
                            Shape::$width = 12 - 5 + 5 / 7 * 6 - arr[4];
                            Return Shape::$width;
                        }
                        
                        main() {
                            Var a: Int = a.getLength();   ## calling method inside class ##
                            Var b: Int = Shape::$getWidth(a, b, "nhan");   ## calling method inside class ##
                            Return a-b;
                        }
                    }
                    
                    Class Shape {
                        Var a: Int = 5;
                        
                        method1(a, b: Int) {
                            Var a: Program = New Program();
                            Var b: Int = a.getLength();
                            Var c: Int = Program::$getWidth(12, 3, some_string);
                            a.getLength();
                            Program::$getWidth(12, 3, some_string);
                            Return;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
        
    def test_sample_program(self):
        input = """
                    Class Shape {
                        Val $numOfShape: Int = 0;
                        Val immutableAttribute: Int = 0;
                        Var length, width: Int;
                        
                        $getNumOfShape() {
                            Return Shape::$numOfShape;
                        }
                    }
                    
                    Class Rectangle: Shape {
                        getArea() {
                            Return Self.length * Self.width;
                        }
                    }
                    
                    Class Program {
                        main() {
                            Out.printInt(Shape::$numOfShape);
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
        
    def test_invalid_multidimensional_array(self):
        input = """ 
                    Class Program {
                        Var arr: Array[Array[Int, 5], 5] = Array (
                                                            Array(1,2,3,4,54),
                                                            Array(1,2,3,4,55),
                                                            Array(1,2,3,4,56),
                                                            Array(1,2,3,4,57),
                                                            Array(1,2,3,4,58)
                                                                );
                        main() {
                            Var arr: Array[Array[Int, 5], 5] 
                                = Array (
                                    Array(1,2,3,4,54),
                                    Array(1,2,3,4,55),
                                    Array(1,2,3,4,56),
                                    Array(1,2,3,4,57),
                                    Array(1,2,3,4,58)
                                ),
                                Array (
                                    Array(1,2,3,4,54),
                                    Array(1,2,3,4,55),
                                    Array(1,2,3,4,56),
                                    Array(1,2,3,4,57),
                                    Array(1,2,3,4,58)
                                ),
                                Array (
                                    Array(1,2,3,4,54),
                                    Array(1,2,3,4,55),
                                    Array(1,2,3,4,56),
                                    Array(1,2,3,4,57),
                                    Array(1,2,3,4,58)
                                ),
                                Array (
                                    Array(1,2,3,4,54),
                                    Array(1,2,3,4,55),
                                    Array(1,2,3,4,56),
                                    Array(1,2,3,4,57),
                                    Array(1,2,3,4,58)
                                ),
                                Array (
                                    Array(1,2,3,4,54),
                                    Array(1,2,3,4,55),
                                    Array(1,2,3,4,56),
                                    Array(1,2,3,4,57),
                                    Array(1,2,3,4,58)
                                );
                        }
                    }
                """
        expect = "Error on line 18 col 33: ,"
        self.assertTrue(TestParser.test(input,expect,264))
        
    def test_multidimensional_array_more_than_two(self):
        input = """ 
                    Class Program {
                        Var arr: Array[Array[Int, 5], 5] = Array (
                                                            Array(1,2,3,4,54),
                                                            Array(1,2,3,4,55),
                                                            Array(1,2,3,4,56),
                                                            Array(1,2,3,4,57),
                                                            Array(1,2,3,4,58)
                                                                );
                        main() {
                            Var arr: Array[Array[Array[Int, 2], 1], 2] 
                                = Array (
                                    Array(
                                        Array(1,2)
                                    ),
                                    Array (
                                        Array(3,4)
                                    )
                                );
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
        
    def test_size_of_array_type(self):
        input = """ 
                    Class Program {
                        main() {
                            Var arr: Array[Int, 0b111];
                            Var arr: Array[Int, 0x123];
                            Var arr: Array[Int, 0xABCD];
                            Var arr: Array[Int, 0XEF099];
                            Var arr: Array[Int, 0123];
                            Var arr: Array[Int, 0456];
                            Var arr: Array[Int, 100];
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
        
    def test_invalid_size_of_array_type(self):
        input = """ 
                    Class Program {
                        main() {
                            Var arr: Array[Int, 0b0];
                        }
                    }
                """
        expect = "Error on line 4 col 48: 0b0"
        self.assertTrue(TestParser.test(input,expect,267))
        
    def test_invalid_size_of_array_type_2(self):
        input = """ 
                    Class Program {
                        main() {
                            Var arr: Array[Int, 0x0];
                        }
                    }
                """
        expect = "Error on line 4 col 48: 0x0"
        self.assertTrue(TestParser.test(input,expect,268))
        
    def test_invalid_size_of_array_type_3(self):
        input = """ 
                    Class Program {
                        main() {
                            Var arr: Array[Int, 00];
                        }
                    }
                """
        expect = "Error on line 4 col 48: 00"
        self.assertTrue(TestParser.test(input,expect,269))
        
    def test_combo_member_access_expression(self):
        input = """ 
                    Class Program {
                        Var x: Int;
                        
                        main() {
                            x = obj.attr;
                            x = obj.attr.attr;
                            x = obj.attr.attr.attr;
                            x = obj.attr.attr.attr.attr.attr.attr.attr.attr;
                            x = Shape::$attr;
                            x = Shape::$attr.attr;
                            x = Shape::$attr.attr.attr;
                            x = Shape::$attr.attr.attr.attr;
                            x = Shape::$attr.attr.attr.attr.attr;
                            x = Shape.func();
                            x = Shape.func().func2(m,n,p);
                            x = Shape.func().func2(m,n,p).func3(m,n,p,x,y,z,"string");
                            x = Shape.attr.func();
                            x = Shape.attr.func(x,y,z).func2(m,n,p);
                            x = Shape.attr.attr.func(m,n,p);
                            x = Shape.attr.attr.func(m,n,p).func(m,n,p);
                            x = Shape.func(m,n,p).attr;
                            x = Shape.func(m,n,p).attr.attr.attr.attr.attr;
                            x = Shape.func(m,n,p).func(m,n,p).attr;
                            x = Shape.func(m,n,p).func(m,n,p).attr.attr;
                            x = Shape.func(m,n,p).func(m,n,p).attr.attr.func(m,n,p);
                            x = Shape::$func().func(m,n,p);
                            x = Shape::$func().func(m,n,p).func(m,n,p);
                            x = Shape::$func().func(m,n,p).func(m,n,p).attr;
                            x = Shape::$func().func(m,n,p).func(m,n,p).attr.attr;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
        
    def test_invalid_if_statement(self):
        input = """ 
                    Class Program {
                        Var x: Int;
                        
                        main() {
                            If (True) {
                                ## do nothing##
                            }
                            Elseif (False) {
                                ## nothing ##
                            }
                            Else {
                                
                            }
                            Elseif (2 < 3) {
                                ## incorrect ##
                            }
                        }
                    }
                """
        expect = "Error on line 15 col 28: Elseif"
        self.assertTrue(TestParser.test(input,expect,271))
        
    def test_combo_statement(self):
        input = """ 
                    Class Program {
                        Var x: Int;
                        Var arr: Array[Array[Int, 1], 1] = some_arr[1][another_arr[2]];
                        Var $length: Float;
                        Var $width: Float;
                        
                        Constructor() {
                            Shape::$length = 12;
                            Shape::$width = 12;
                        }
                        
                        Constructor(l, w: Float) {
                            Shape::$length = l;
                            Shape::$width = w;
                        }
                        
                        $getLength() {
                            Return $length;
                        }
                        
                        $getWidth() {
                            Return Shape::$width;
                        }
                        
                        main() {
                            Var obj: Shape = New Shape(20, 20);
                            Var l: Float = $getLength();
                            Var l2: Float = Program::$getLength();
                            Var w: Float = $getWidth();
                            Var w2: Float = Program::$getWidth();
                            
                            Foreach (x In 5 .. 2) {
                                obj.printInt(arr[x]);
                            }
                            
                            Return;
                        }
                    }
                """
        # expect = "successful"
        expect = "Error on line 19 col 35: $length"
        self.assertTrue(TestParser.test(input,expect,272))
        
    def test_missed_data_type_declaration(self):
        input = """ 
                    Class Program {
                        Var x = 0;
                        Var arr: Array[Array[Int, 1], 1] = some_arr[1][another_arr[2]];
                        Var $length: Float;
                        Var $width: Float;
                        
                        Constructor() {
                            $length = 12;
                            $width = 12;
                        }
                        
                        Constructor(l, w: Float) {
                            $length = l;
                            $width = w;
                        }
                        
                        Destructor() {
                            Self.arr = Array(0, 0);
                        }
                        
                        main() {
                            Var obj: Shape = New Shape(20, 20);
                        }
                    }
                """
        expect = "Error on line 3 col 30: ="
        self.assertTrue(TestParser.test(input,expect,273))
        
    def test_array_empty_initialize(self):
        input = """ 
                    Class Program {
                        Var x: Float = 0;
                        Var arr: Array[Array[Int, 1], 1] = some_arr[1][another_arr[2]];
                        
                        main() {
                            Val arr: Array[Int, 1] = Array();
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
    
    def test_method_invocation_statement_3(self):
        input = """ 
                    Class Shape {    
                        Var $x, y: Float = 10.123, 10e00000;
                        
                        func1(x: Float; y: String) {
                            If (x == 100) {
                                Self.print("Nhan Vo" + y);
                            }
                            Elseif (x == 20+3423*4325) {
                                Self.print("Nhan Vo Nguyen" + y);
                            }
                        }  
                        
                        $func2(x: Float) {
                            If (x == 100) {
                                Self.print("Nhan Vo" + y);
                            }
                            Else {
                                Self.print("Nhan Vo Nguyen" + y);
                            }
                        }    
                        
                        Constructor(x: Float; str: String) {
                            Self.x = x;
                            y = str;
                        }
                        
                        Destructor() {
                            Self.x = 0;
                            y = "";
                        }
                    }
                    
                    Class Program {
                        main() {
                            Var obj: Shape = New Shape(1.35234e+1023123, "abc");
                            Shape::$func2(1+2-3*4/5%6);
                            Shape.func().func().func();
                            Shape::$x.y.y.y.func();
                            Shape::$func2().y.y.y.func();
                            
                            Foreach (i In Shape::$func2(1+2-3*4/5%6) .. obj.func(1+2+3) By 1) {
                                Self.print(i*2-10+65);
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
        
    def test_static_ID_in_method_declare(self):
        input = """ 
                    Class Program {
                        Constructor(x: Float; str: String) {
                            Self.x = x;
                            y = str;
                        }
                        
                        Destructor() {
                            Self.x = 0;
                            y = "";
                        }
                        
                        method(a, b, c: Int; a, $xyz: Float) {
                            Str = "It will cause errror because $xyz is static ID";
                            Return;
                        }
                    }
                """
        expect = "Error on line 13 col 48: $xyz"
        self.assertTrue(TestParser.test(input,expect,276))
        
    def test_size_and_type_one_dimensional_array(self):
        input = """ 
                    Class Program {
                        Var arr: Array[Int, 3] = Array(1, "nhanvo", 12.00000e+10); 
                        
                        main() {
                            Str = "No need same type in 1-dimensional array";
                        }
                        
                        Constructor(x: Float; str: String) {
                            Self.x = x;
                            y = str;
                        }
                        
                        Destructor() {
                            Self.x = 0;
                            y = "";
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
        
    def test_size_and_type_multi_dimensional_array(self):
        input = """ 
                    Class Program {
                        Var arr: Array[Array[Int, 2], 3] = Array(
                                                                Array(1, "nhan"),
                                                                Array (2, 4.5, 0.0000, 0x2341, "string"),
                                                                Array()
                                                            ); 
                        
                        main() {
                            Str = "No need same type in multi-dimensional array";
                        }
                        
                        Constructor(x: Float; str: String) {
                            Self.x = x;
                            y = str;
                        }
                        
                        Destructor() {
                            Self.x = 0;
                            y = "";
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
        
    def test_null_keyword(self):
        input = """ 
                    Class Shape {
                        main() {
                            a = Array();
                            Shape::$b = Array (
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
        
                    Class Program : Shape {
                        Var obj: Shape = Null;
                        
                        Constructor() {
                            Self.obj = New Shape(New Shape(a, b, c));
                            Return Self.obj;
                        }
                        
                        Destructor() {
                            Self.obj = Null;
                        }
                        
                        main() {
                            Val x, y,  z: Int = Null, Null, Null;
                            Var obj: Shape = New Shape(Null);
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
        
    def test_some_weird_index_expression(self):
        input = """ 
                    Class Program {
                        Var x: Array[Boolean, 1];
                        Var x: Array[String, 1] = ____[True && False -45 + 2 / 2];
                        Var x: Array[Float, 1] = _["nhan" - 12 + 4];
                        Var x, $y: Array[Int, 1] = "Nhan", "Vo";
                        
                        main() {
                            x = 1[1];
                            x = 1.23434e+10[1];
                            x = 1.23434e+10[12/3%2-4514+34141];
                            x = True[Null];
                            x = 1[1.000000000];
                            x = 1_2_3_4_5_6[Array(1,2,3,4,"nhan")];
                            x = 1_2_3_4_5_6.e-00000000[Array(1,2,3,4,"nhan")];
                            x = 0[Array(1,2,3,4,"nhan")];
                            x = 00[Array(1,2,3,4,"nhan")];
                            x = 0b0[Array(1,2,3,4,"nhan")];
                            x = 0B0[Array(1,2,3,4,"nhan")];
                            x = 0x0[Array(1,2,3,4,"nhan")];
                            x = 0X0[Array(1,2,3,4,"nhan")];
                            x = New X()[2];
                            x = !New X()[2];
                            x = -New X()[2];
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
        
    def test_some_weird_dot_expression(self):
        input = """ 
                    Class Program {
                        Var x: Array[Boolean, 1];
                        Var x: Array[String, 1] = ____[True && False -45 + 2 / 2];
                        Var x: Array[Float, 1] = _["nhan" - 12 + 4];
                        Var x, $y: Array[Int, 1] = "Nhan", "Vo";
                        
                        main() {
                            x = (123).func();
                            x = (1_234_456_789).func().func();
                            x = (1_234_456_789.10e-10000000).func();
                            x = "string".func();
                            x = Null.func();
                            x = True.func();
                            x = someID::$attribute.func();
                            x = someID::$func(a,b,c,Null).func();
                            x = Array(1,2,3,4,5,6).func();
                            x = Array(Array(1,2,3), Array(4,5), Array("nhan", "vo", "nguyen")).func();
                            x = Shape::$func(xyz).func();
                            x = (0).func();
                            x = (0b0).func();
                            x = (0B0).func();
                            x = (0x0).func();
                            x = (0X0).func();
                            x = (00).func();
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
        
    def test_invalid_return_statement(self):
        input = """ 
                    Class Program {
                        Var x: Array[Boolean, 1];
                        Var x: Array[String, 1] = ____[True && False -45 + 2 / 2];
                        Var x: Array[Float, 1] = _["nhan" - 12 + 4];
                        Var x, $y: Array[Int, 1] = "Nhan", "Vo";
                        
                        method() {
                            Return "nothing";
                        }
                        
                        method2() {
                            Return 1+23;
                        }
                        
                        main() {
                            x = someID::$attribute.func();
                            x = someID::$func(a,b,c,Null).func();
                            x = Array(1,2,3,4,5,6).func();
                            x = Array(Array(1,2,3), Array(4,5), Array("nhan", "vo", "nguyen")).func();
                            x = $func(xyz).func();
                            x = (0).func();
                            x = (0b0).func();
                            x = (0B0).func();
                            x = (0x0).func();
                            x = (0X0).func();
                            x = (00).func();
                            
                            return $obj;
                        }
                    }
                """
        # expect = "Error on line 29 col 35: $obj"
        expect = "Error on line 21 col 32: $func"
        self.assertTrue(TestParser.test(input,expect,282))
        
    def test_invalid_self_keyword(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        
                        main() {
                            x = Self.a;
                            x = Self.func();
                            x = Self.Self.Self.a;
                        }
                    }
                """
        expect = "Error on line 8 col 37: Self"
        self.assertTrue(TestParser.test(input,expect,283))
        
    def test_some_weird_operand(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        
                        main() {
                            x = 2 + Array(1,2);
                            x = Num + "123";
                            x = Array(1,2,3) + Array(Array(1,2,3), Array(4,5,6,7,8,9));
                            x = 1 + Array(Array(Shape::$attribute,2,3), Array(obj.getLength(),5,Shape::$func(a,b,c,d),7,8,a.func()));
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
        
    def test_some_weird_special_case(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        
                        main() {
                            x = a.b[i];
                            x = a[i].b;
                        }
                    }
                """
        expect = "Error on line 7 col 36: ."
        self.assertTrue(TestParser.test(input,expect,285))
        
    def test_left_hand_side_assign_stmt(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        
                        main() {
                            x = Array();
                            Shape::$x = Shape::$obj.obj2.pbj3.func();
                            a.b = Shape::$obj.obj2.pbj3.func();
                            a.b() = Shape::$obj.obj2.pbj3.func();
                            a.b(a,True,Array(1,2,3)) = Shape::$obj.obj2.pbj3.func();
                            a.b(a,True,Array(1,2,3)).attr = Shape::$obj.obj2.pbj3.func();
                            Shape::$attr = Shape::$obj.obj2.pbj3.func();
                            Shape::$attr.func() = Shape::$obj.obj2.pbj3.func();
                            Shape::$attr.attr.func() = Shape::$obj.obj2.obj3.func();
                            Shape::$attr.attr.attr.attr.func() = Shape::$obj.obj2.pbj3.func();
                            Shape::$attr.attr.attr.attr.func().func().func() = Shape::$obj.obj2.pbj3.func();
                            1[1]                                          = Shape::$obj.func();          
                            1.23434e+10[1]                                = Shape::$obj.func();      
                            1.23434e+10[12/3%2-4514+34141]                = Shape::$obj.func();      
                            True[Null]                                    = Shape::$obj.func();      
                            1[1.000000000]                                = Shape::$obj.func();      
                            1_2_3_4_5_6[Array(1,2,3,4,"nhan")]            = Shape::$obj.func();  
                            1_2_3_4_5_6.e-00000000[Array(1,2,3,4,"nhan")] = Shape::$obj.func(); 
                            0[Array(1,2,3,4,"nhan")]                      = Shape::$obj.func();  
                            00[Array(1,2,3,4,"nhan")]                     = Shape::$obj.func();
                            0B0[Array(1,2,3,4,"nhan")]                    = Shape::$obj.func();  
                            0x0[Array(1,2,3,4,"nhan")]                    = Shape::$obj.func();      
                            0X0[Array(1,2,3,4,"nhan")]                    = Shape::$obj.func();      
                            New X()[2]                                    = Shape::$obj.func();      
                            New X()[2]                                   = Shape::$obj.func();          
                            New X()[2]                                   = Shape::$obj.func();      
                        }
                    }
                """
        # expect = "successful"
        expect = "Error on line 9 col 34: ="
        self.assertTrue(TestParser.test(input,expect,286))
        
    def test_declare_method_outside_class(self):
        input = """
                    method() {
                        str = "This is invalid cuz all methods must be inside class";
                    }
                    
                    Class Program {
                        Var x: Int = 5;
                        
                        main() {
                                  
                        }
                    }
                """
        expect = "Error on line 2 col 20: method"
        self.assertTrue(TestParser.test(input,expect,287))
        
    def test_declare_class_inside_class(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        
                        main() {
                                  
                        }
                        
                        Class Inside {
                            Constructor() {
                                Out.print("Error);
                            }
                        }
                    }
                """
        expect = "Error on line 9 col 24: Class"
        self.assertTrue(TestParser.test(input,expect,288))
        
    def test_self_dot_static_function(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        
                        main() {
                            x = Self.$getLength();   
                        }
                    }
                """
        expect = "Error on line 6 col 37: $getLength"
        self.assertTrue(TestParser.test(input,expect,289))
        
    def test_declare_method_inside_method(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        
                        main() {
                            x = 2 + Array(1,2);
                            x = Num + "123";
                            x = Array(1,2,3) + Array(Array(1,2,3), Array(4,5,6,7,8,9));
                            x = 1 + Array(Array(Shape::$attribute,2,3), Array(obj.getLength(),5,Shape::$func(a,b,c,d),7,8,a.func()));

                            a.method() {
                                out.print("Error");
                            }
                        }
                    }
                """
        expect = "Error on line 11 col 39: {"
        self.assertTrue(TestParser.test(input,expect,290))
        
    def test_missed_close_bracket(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        
                        Constructor(x: Float; str: String) {
                            Self.x = x;
                            y = str;
                        }
                        
                        Destructor() {
                            Self.x = 0;
                            y = "";
                        }
                        
                        main() {
                            a.method().method();
                            x = 2 + Array(1,2);
                            x = Num + "123";
                            x = Array(1,2,3) + Array(Array(1,2,3), Array(4,5,6,7,8,9));
                            x = 1 + Array(Array(Shape::$attribute,2,3), Array(obj.getLength(),5,Shape::$func(a,b,c,d),7,8,a.func()));
                            a.method().method();
                        }
                    
                """
        expect = "Error on line 24 col 16: <EOF>"
        # expect = "Error on line 16 col 36: ."
        self.assertTrue(TestParser.test(input,expect,291))
        
    def test_foreach_statement(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        Var arr: Array[Float, 5];
                        
                        Constructor(x: Float; str: String) {
                            Self.x = x;
                            y = str;
                        }
                        
                        Destructor() {
                            Self.x = 0;
                            y = "";
                        }
                        
                        main() {
                            Foreach (arr[i] In 1 .. 10) {
                                out.print(i);
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
        
    def test_params_in_destructor(self):
        input = """ 
                    Class Program {
                        Var x: Int = 5;
                        Var arr: Array[Float, 5];
                        
                        Constructor() {
                            ## nothing ##
                        }
                        
                        Constructor(x: Float; str: String) {
                            Self.x = x;
                            y = str;
                        }
                        
                        Destructor() {
                            Self.x = 0;
                            y = "";
                        }
                        
                        Destructor(a, b, c, d: Int) {
                            Str = "Error";
                        }
                        
                        main() {
                            Foreach ($index In 1 .. 10) {
                                out.print(i);
                            }
                        }
                    }
                """
        expect = "Error on line 20 col 35: a"
        self.assertTrue(TestParser.test(input,expect,293))
        
    def test_some_weird_operand_2(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            x = 1.e+101010101 - 0b10101011;
                            x = "nhan" +. 0xABCD;
                            x = "vo" ==. 123;
                            x = Array(1,2,3,4) + 4%3/arr[1] + Null._123_4534_4823_42374893;
                            x = Array(Array(1,2), Array()) - !!!!!!!!!!!-------------------True;
                            x = Shape::$calling_method();
                            x = Shape::$calling_method(a-b%c+d, Array(1,2,Array(3,4)), New Shape(), Shape::$func(), 0x0, 00, 0b0);
                            x = a.calling_method(1 > 2, 2 < 3, 3 <= 4, 5 >= 3, 5 != 3, 5 == 3, 1.2 +. 3.e1, 0xAB123 ==. 0b1010101);                        
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
        
    def test_some_weird_member_access(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            x = a.b.c.d.e.f;
                            Shape::$x = Null.a;
                            Shape::$x = Self.Continue;
                        }
                    }
                """
        expect = "Error on line 9 col 45: Continue"
        self.assertTrue(TestParser.test(input,expect,295))
        
    def test_some_weird_member_access_2(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            Shape::$a;
                        }
                    }
                """
        expect = "Error on line 7 col 37: ;"
        self.assertTrue(TestParser.test(input,expect,296))
        
    def test_with_lexer(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            x = "My name is Nhan. This name has two \\'N\\' characters";
                            input = "He asked me: '"Where is John?'"";
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
        
    def test_invalid_variable_declare(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            Var _X_YZ, _123_123_123: Int = 5; 
                        }
                    }
                """
        expect = "Error on line 7 col 60: ;"
        self.assertTrue(TestParser.test(input,expect,298))
        
    def test_invalid_variable_declare_2(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            Var _X_YZ, _123_123_123: Int = 5, "nhan" +. 0.123123, x != 13; 
                        }
                    }
                """
        expect = "Error on line 7 col 80: ,"
        self.assertTrue(TestParser.test(input,expect,299))
        
    def test_invalid_variable_declare_3(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            Var _X_YZ, _123_123_123, $y: Int = 5, "nhan" +. 0.123123, x != 13; 
                        }
                    }
                """
        expect = "Error on line 7 col 53: $y"
        self.assertTrue(TestParser.test(input,expect,300))
        
        
    def test_something(self):
        input = """ 
                    Class Program {
                        main() {
                            a.a();
                            a.a();
                            a.a.a();
                            a.a.a.a();
                            a.a.a.a.a();
                            
                            a.a();
                            a.a().a();
                            a.a().a().a();
                            a.a().a().a().a();
                            a.method().method();
                            a.a().a().a().a().a();
                            
                            a.a().a.a();
                            a.a().a.a.a.a.a();
                            a.a().a.a.a.a().a();
                            a.a().a.a().a.a().a();
                            
                            Shape::$a().a();
                            Shape::$a().a.a.a.a();
                            Shape::$a().a.a().a.a();
                            Shape::$a().a.a.a.a.a().a().a();
                            
                            Shape::$a.a();
                            Shape::$a.a.a();
                            Shape::$a.a.a.a();
                            Shape::$a.a.a.a.a.a();
                            Shape::$a.a.a.a.a.a.a();
                                     
                            Shape::$a.a();
                            Shape::$a.a().a();
                            Shape::$a.a().a().a();
                            Shape::$a.a().a().a().a().a();
                            Shape::$a.a().a().a().a().a().a();
                            
                            Shape::$a().a();
                            Shape::$a().a.a.a.a();
                            Shape::$a().a.a().a.a(123);
                            Shape::$a().a.a.a().a.a(123).a().a(123);
                            
                            New X().a();
                            New X().a.a.a();
                            New X().a().a.a();
                            New X().a().a.a.a().a.a();
                            
                            (0).a();
                            (0).a.a.a();
                            (0).a().a.a();
                            
                            Shape::$a();
                            "nhan".a();
                            "nhan".a.a.a.a();
                            Shape::$a();
                        
                            a.method().method();
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,888))
        
    def test_lhs_1(self):
        input = """ 
                    Class Program {
                        main() {
                            a = 12;
                            a = "nhan" + 12;
                            Shape::$a = 12;
                            obj.a().a = 12;
                            Shape::$a().a = 12;
                            Shape::$a().a().a().a = 12;
                            obj.a().a().a().a = 12;
                            obj.a.a().a.a().a = 12;
                            arr[1] = 12;
                            a.b = 12;
                            Shape::$a().arr[1] = 12;
                            a.a().arr[1] = 12;
                            (arr[1]).a().a = 12;
                            arr[arr[arr[1]]] = 12;
                            (arr[arr[arr[1]]]).a.a.a.a().a.a.a().a = 12;
                            1[1] = 12;
                            "nhan"[1] = 12;
                            1.2e+10[1] = 12;
                            (Shape::$a)[1] = 12;
                            Shape::$a[1] = 12;
                            a.a(x)[1] = 12;
                            Shape::$a(x)[1] = 12;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1000))
        
    def test_lhs_2(self):
        input = """ 
                    Class Program {
                        main() {
                            $a = 12;
                        }
                    }
                """
        expect = "Error on line 4 col 28: $a"
        self.assertTrue(TestParser.test(input,expect,1001))
        
    def test_lhs_3(self):
        input = """ 
                    Class Program {
                        main() {
                            a() = 12;
                        }
                    }
                """
        expect = "Error on line 4 col 29: ("
        self.assertTrue(TestParser.test(input,expect,1002))
        
    def test_lhs_4(self):
        input = """ 
                    Class Program {
                        main() {
                            a.a() = 12;
                        }
                    }
                """
        expect = "Error on line 4 col 34: ="
        self.assertTrue(TestParser.test(input,expect,1003))
        
    def test_lhs_5(self):
        input = """ 
                    Class Program {
                        main() {
                            Shape::$a() = 12;
                        }
                    }
                """
        expect = "Error on line 4 col 40: ="
        self.assertTrue(TestParser.test(input,expect,1004))
        
    def test_lhs_6(self):
        input = """ 
                    Class Program {
                        main() {
                            1 = 2;
                        }
                    }
                """
        expect = "Error on line 4 col 30: ="
        self.assertTrue(TestParser.test(input,expect,1005))
        
    def test_lhs_7(self):
        input = """ 
                    Class Program {
                        main() {
                            a.a() = 12;
                        }
                    }
                """
        expect = "Error on line 4 col 34: ="
        self.assertTrue(TestParser.test(input,expect,1006))
        
    def test_lhs_8(self):
        input = """ 
                    Class Program {
                        main() {
                            (a.a.a.a.a.arr[1]).a() = 12;
                        }
                    }
                """
        expect = "Error on line 4 col 51: ="
        self.assertTrue(TestParser.test(input,expect,1007))
        
    def test_foreach_1(self):
        input = """ 
                    Class Program {
                        main() {
                            Foreach (i in 1 .. 10) {
                                ##nothing##
                            }
                        }
                    }
                """
        expect = "Error on line 4 col 39: in"
        self.assertTrue(TestParser.test(input,expect,1008))
        
    def test_foreach_2(self):
        input = """ 
                    Class Program {
                        main() {
                            
                            Foreach (i In 1 .. 10) {
                                ##nothing##
                            }
                            
                            Foreach (Shape::$a In 1 .. 10) {
                                ##nothing##
                            }
                            
                            Foreach (a.func().x In 1 .. 10) {
                                ##nothing##
                            }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1009))
    
    def test_declare_1(self):
        input = """ 
                    Class Program {
                        Var x, y, z: Int;
                        Val x, $y: Float = 12.3, 4.5e10;
                        Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                        Val x, $y: Int = 4, 5;
                        main() {
                            Var x, y, z: Int;
                            Val x, y: Float = 12.3, 4.5e10;
                            Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                            Val x, y: Int = 4, 5;
                            Var arr: Array[Int, 5] = Array();
                            Var arr1, arr2: Array[Int, 5] = Array(), Array();
                            Var arr1, arr2, arr3: Array[Int, 5] = Array(), Array(), Array(Array(1));
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1010))
        
    def test_declare_2(self):
        ##số biến nhiều hơn số value ##
        input = """ 
                    Class Program {
                        Var x, y, z: Int;
                        Val x, $y: Float = 12.3, 4.5e10;
                        Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                        Val x, $y, z: Int = 4, 5;   ## here ##
                        main() {
                            Var x, y, z: Int;
                            Val x, y: Float = 12.3, 4.5e10;
                            Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                            Val x, y: Int = 4, 5;
                            Var arr: Array[Int, 5] = Array();
                            Var arr1, arr2: Array[Int, 5] = Array(), Array();
                            Var arr1, arr2, arr3: Array[Int, 5] = Array(), Array(), Array(Array(1));
                        }
                    }
                """
        expect = "Error on line 6 col 48: ;"
        self.assertTrue(TestParser.test(input,expect,1011))
        
    def test_declare_3(self):
        ##số biến ít hơn số value ##
        input = """ 
                    Class Program {
                        Var x, y, z: Int;
                        Val x, $y: Float = 12.3, 4.5e10;
                        Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                        Val x, $y: Int = 4, 5, 6, 7, 8, 10;   ## here ##
                        main() {
                            Var x, y, z: Int;
                            Val x, y: Float = 12.3, 4.5e10;
                            Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                            Val x, y: Int = 4, 5;
                            Var arr: Array[Int, 5] = Array();
                            Var arr1, arr2: Array[Int, 5] = Array(), Array();
                            Var arr1, arr2, arr3: Array[Int, 5] = Array(), Array(), Array(Array(1));
                        }
                    }
                """
        expect = "Error on line 6 col 45: ,"
        self.assertTrue(TestParser.test(input,expect,1012))
        
    def test_declare_4(self):
        ##số biến nhiều hơn hơn số value trong method ##
        input = """ 
                    Class Program {
                        Var x, y, z: Int;
                        Val x, $y: Float = 12.3, 4.5e10;
                        Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                        Val x, $y: Int = 4, 5;
                        main() {
                            Var x, y, z: Int = 1, 2;        ## here ##
                            Val x, y: Float = 12.3, 4.5e10;
                            Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                            Val x, y: Int = 4, 5;
                            Var arr: Array[Int, 5] = Array();
                            Var arr1, arr2: Array[Int, 5] = Array(), Array();
                            Var arr1, arr2, arr3: Array[Int, 5] = Array(), Array(), Array(Array(1));
                        }
                    }
                """
        expect = "Error on line 8 col 51: ;"
        self.assertTrue(TestParser.test(input,expect,1013))
        
    def test_declare_5(self):
        ##số biến ít hơn hơn số value trong method ##
        input = """ 
                    Class Program {
                        Var x, y, z: Int;
                        Val x, $y: Float = 12.3, 4.5e10;
                        Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                        Val x, $y: Int = 4, 5;
                        main() {
                            Var x, y, z: Int = 1, 2, 3, 4, 5, 6, 7, 8;        ## here ##
                            Val x, y: Float = 12.3, 4.5e10;
                            Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                            Val x, y: Int = 4, 5;
                            Var arr: Array[Int, 5] = Array();
                            Var arr1, arr2: Array[Int, 5] = Array(), Array();
                            Var arr1, arr2, arr3: Array[Int, 5] = Array(), Array(), Array(Array(1));
                        }
                    }
                """
        expect = "Error on line 8 col 54: ,"
        self.assertTrue(TestParser.test(input,expect,1014))
        
    def test_declare_6(self):
        ## combo ##
        input = """ 
                    Class Program {
                        Var x, y, z: Int;
                        Val x, $y: Float = 12.3, 4.5e10;
                        Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                        Val x, $y: Int = 4, 5;
                        Val arr1, arr2: Array[Boolean, 1] = Array(), Array(Array(Array(Array(Array()))));
                        main() {
                            Var x, y, z: Int = 1, 2, 3;    
                            Val x, y: Float = 12.3, 4.5e10;
                            Var x, y, z, m, n, p: Float = 1,2,3,4,5,6;
                            Val x, y: Int = 4, 5;
                            Var arr: Array[Int, 5] = Array();
                            Var arr1, arr2: Array[Int, 5] = Array(), Array();
                            Var arr1, arr2, arr3: Array[Int, 5] = Array(), Array(), Array(Array(1));
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1015))
    
    def test_some_thing_very_confused_1(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            x = Self::ins;
                        }
                    }
                """
        expect = "Error on line 7 col 36: ::"
        self.assertTrue(TestParser.test(input,expect,1016))
        
    def test_some_thing_very_confused_2(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            x = Self::$ins;
                        }
                    }
                """
        expect = "Error on line 7 col 36: ::"
        self.assertTrue(TestParser.test(input,expect,1017))
        
    def test_some_thing_very_confused_3(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            x = "1+2"::$a;
                        }
                    }
                """
        expect = "Error on line 7 col 37: ::"
        self.assertTrue(TestParser.test(input,expect,1018))
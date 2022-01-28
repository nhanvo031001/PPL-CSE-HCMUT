        
        
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
    
            
    def test_abc_xyz_1(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            Var _X_YZ, _123_123_123, y: Int = 5, "nhan" +. 0.123123, x != 13; 
                            
                            {
                                Var $o: Int;
                            }                        
                        }
                    }
                """
        expect = "Error on line 10 col 36: $o"
        self.assertTrue(TestParser.test(input,expect,1019))
        
    def test_abc_xyz_2(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            Var _X_YZ, _123_123_123, y: Int = 5, "nhan" +. 0.123123, x != 13; 
                            
                            {
                                {
                                    {
                                        {
                                            {
                                                {
                                                    Var _X_YZ, _123_123_123, y: Int = 5, "nhan" +. 0.123123, x != 13;
                                                }
                                            }
                                        }
                                    }
                                }
                            }                        
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1020))
        
    def test_abc_xyz_3(self):
        input = """ 
                    Class Program {
                        Var x: Array[Array[Int, 1], 1] = Array();
                        Val $x, y, $z: String = "nhan", 1.000 + "nhan", ---True - !!!!!False;    
                    
                        main() {
                            Var _X_YZ, _123_123_123, y: Int = 5, "nhan" +. 0.123123, x != 13; 
                            
                            {
                                {
                                    {
                                        {
                                            {
                                                {
                                                    a = Array();
                                                    Shape::$b = Array (
                                                            Array("Volvo", "22", "18"),
                                                            Array("Saab", "5", "2"),
                                                            Array("Land Rover", "17", "15")
                                                        );
                                                    arr[arr[arr[3+4]]] = Array (
                                                            Array("Volvo", "22", "18"),
                                                            Array("Saab", "5", "2"),
                                                            Array("")
                                                            );
                                                            
                                                }
                                            }
                                        }
                                    }
                                }
                            }                        
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1021))
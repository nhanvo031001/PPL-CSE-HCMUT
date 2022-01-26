    
    def test_some_thing_confused_1(self):
        input = """"nhan\nsdnjas" """
        expect = "Unclosed String: nhan"
        self.assertTrue(TestLexer.test(input, expect, 1201))
        
    def test_some_thing_confused_2(self):
        input = """"nhan\rsdnjas" """
        expect = "Unclosed String: nhan"
        self.assertTrue(TestLexer.test(input, expect, 1202))
        
    def test_some_thing_confused_3(self):
        input = """"nhan \\n sdnjas" """
        expect = "nhan \\n sdnjas,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1203))
        
    def test_some_thing_confused_4(self):
        input = """"nhan \\r sdnjas" """
        expect = "nhan \\r sdnjas,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1204))
        
    def test_some_thing_confused_5(self):
        input = """"nhan \b \f \t sdnjas" """
        expect = "nhan \b \f \t sdnjas,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1205))
        
    def test_some_thing_confused_6(self):
        input = """"nhan" abc" """
        expect = "nhan,abc,Unclosed String:  "
        self.assertTrue(TestLexer.test(input, expect, 1206))
        
    def test_some_thing_confused_7(self):
        input = """"nhan ' abc" """
        expect = "nhan ' abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1207))
        
    def test_some_thing_confused_8(self):
        input = """"nhan '" abc" """
        expect = "nhan '\" abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1208))
        
    def test_some_thing_confused_9(self):
        input = """"nhan '"abc'" abc" """
        expect = "nhan '\"abc'\" abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1209))
        
    def test_some_thing_confused_10(self):
        input = """"nhan'\""""
        expect = "nhan',<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1210))
        
    def test_some_thing_confused_11(self):
        input = """"nhan'\" """
        expect = "Unclosed String: nhan'\" "
        self.assertTrue(TestLexer.test(input, expect, 1211))
        
    def test_some_thing_confused_12(self):
        input = """"nhan's handsome\""""
        expect = "nhan's handsome,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1212))
        
    def test_some_thing_confused_13(self):
        input = """"nhan's handsome" """
        expect = "nhan's handsome,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1213))
        
    def test_some_thing_confused_14(self):
        input = """ "nhan
        vo" """
        expect = "Unclosed String: nhan"
        self.assertTrue(TestLexer.test(input, expect, 1214))
    
    def test_some_thing_confused_15(self):
        input = """ "nhan\ybc" """
        expect = "Illegal Escape In String: nhan\y"
        self.assertTrue(TestLexer.test(input, expect, 1215))
        
    def test_some_thing_confused_16(self):
        input = """ "nhan\\ybc" """
        expect = "Illegal Escape In String: nhan\\y"
        self.assertTrue(TestLexer.test(input, expect, 1216))
        
    def test_some_thing_confused_17(self):
        input = """ "nhan\b\t\f \\b\\t\\f ''"" """
        expect = "nhan\b\t\f \\b\\t\\f ''\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1217))
        
    def test_some_thing_confused_18(self):
        input = """ "''''''''''''"" """
        expect = "''''''''''''\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1218))
        
    def test_some_thing_confused_19(self):
        input = """ "''''''''''''"" " """
        expect = "''''''''''''\",Unclosed String:  "
        self.assertTrue(TestLexer.test(input, expect, 1219))
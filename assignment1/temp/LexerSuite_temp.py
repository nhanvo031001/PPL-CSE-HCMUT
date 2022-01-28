        
        
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
        expect = "Unclosed String: nhan "
        self.assertTrue(TestLexer.test(input, expect, 1205))
        
    def test_some_thing_confused_6(self):
        input = """"nhan" abc" """
        expect = "nhan,abc,Unclosed String:  "
        self.assertTrue(TestLexer.test(input, expect, 1206))
        
    def test_some_thing_confused_7(self):
        input = """"nhan ' abc" """
        # expect = "Illegal Escape In String: nhan ' "
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
        # expect = "nhan',<EOF>"  ## code cũ
        expect = "Unclosed String: nhan'"  ## code MC
        self.assertTrue(TestLexer.test(input, expect, 1210))
        
    def test_some_thing_confused_11(self):
        input = """"nhan'\" """
        expect = "Unclosed String: nhan'\" "
        self.assertTrue(TestLexer.test(input, expect, 1211))
        
    def test_some_thing_confused_12(self):
        input = """"nhan's handsome\""""
        # expect = "Illegal Escape In String: nhan's"
        expect = "nhan's handsome,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1212))
        
    def test_some_thing_confused_13(self):
        input = """"nhan's handsome" """
        # expect = "Illegal Escape In String: nhan's"
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
        # expect = "nhan\b\t\f \\b\\t\\f ''\",<EOF>"
        expect = "Unclosed String: nhan"
        self.assertTrue(TestLexer.test(input, expect, 1217))
        
    def test_some_thing_confused_18(self):
        input = """ "''''''''''''"" """
        # expect = "Illegal Escape In String: ''"
        expect = "''''''''''''\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1218))
        
    def test_some_thing_confused_19(self):
        input = """ "''''''''''''"" " """
        # expect = "''''''''''''\",Unclosed String:  "
        # expect = "Illegal Escape In String: ''"
        expect = "''''''''''''\",Unclosed String:  "
        self.assertTrue(TestLexer.test(input, expect, 1219))
        
    def test_some_thing_confused_20(self):
        ## sửa code theo MC thì sẽ unclose, code cũ là hợp lệ"
        input = r"""
            "string'"
        """
        expect = "Unclosed String: string'\""
        self.assertTrue(TestLexer.test(input, expect, 1220))
        
    def test_some_thing_confused_21(self):
        ## sửa code theo MC thì unclose, code cũ ilegal do không cho dấu / đứng 1 mình
        input = """"string \\"""
        expect = "Unclosed String: string "
        self.assertTrue(TestLexer.test(input, expect, 1221))
        
    def test_some_thing_confused_22(self):
        input = """"string \n"""
        expect = "Unclosed String: string "
        self.assertTrue(TestLexer.test(input, expect, 1222))
    
    def test_some_thing_confused_23(self):
        input = """"string '"
        """
        expect = "Unclosed String: string '\""
        self.assertTrue(TestLexer.test(input, expect, 1223))
        
    def test_some_thing_confused_24(self):
        input = """"string '"\n"""
        expect = "Unclosed String: string '\""
        self.assertTrue(TestLexer.test(input, expect, 1224))
        
    def test_some_thing_confused_25(self):
        input = """"string '"\b\""""
        expect = "Unclosed String: string '\""
        self.assertTrue(TestLexer.test(input, expect, 1225))
        
    def test_some_thing_confused_26(self):
        input = """ "she \'\" """
        expect = "Unclosed String: she \'\" "
        self.assertTrue(TestLexer.test(input, expect, 1226))
        
    def test_some_thing_confused_27(self):
        input = """ "she \'\""""
        expect = "Unclosed String: she \'"
        self.assertTrue(TestLexer.test(input, expect, 1227))
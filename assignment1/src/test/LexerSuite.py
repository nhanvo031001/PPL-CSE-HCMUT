import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        input = """abc xyz nhanvo ldpv a9000 b000000003
                a_bcd_xyz____ a0________3343abcd___xyz
                """
        expect = "abc,xyz,nhanvo,ldpv,a9000,b000000003,a_bcd_xyz____,a0________3343abcd___xyz,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,101))
        
    def test_lower_upper_id(self):
        input = """aCBbdc nHanVONguyen nh_AAAAn_vo_NNNguyen____
                    aAsVN3 _xyz_der vo123_nhanvo _1234345 vo________123
                """
        expect = "aCBbdc,nHanVONguyen,nh_AAAAn_vo_NNNguyen____,aAsVN3,_xyz_der,vo123_nhanvo,_1234345,vo________123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,102))
        
    def test_confused_integer_literals(self):
        input = """000123
                    0x010101 
                    00345
                    0678
                    0
                    0XA_B_C_DEF0919
                    0X0123
                    0X_0123
                    0X0_123
                    00
                    0_X0123
                    0_X123
                    0_123
                    0_0123
                    0_0
                    0x0
                    0b0
                    0x_0
                    0b_0
                """
        expect = "00,0123,0x0,10101,00,345,067,8,0,0XABCDEF0919,0X0,123,0,X_0123,0X0,_123,00,0,_X0123,0,_X123,0,_123,0,_0123,0,_0,0x0,0b0,0,x_0,0,b_0,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,103))
        
    def test_integer(self):
        input = "123a123 0 687 99aa9aaa"
        expect = "123,a123,0,687,99,aa9aaa,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,104))
        
    def test_block_comment(self):
        input = """##nhan 
        vo
        nguyen
        thien
        ## 
        nhanvo
        ##nhan vo
        is in
        block comment
        ##
        ##nothing change##
        """
        expect = "nhanvo,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,105))
        
    def test_underscore_identifier(self):
        input = "_nhan _ ____"
        expect = "_nhan,_,____,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 106))
        
    def test_wrong_identifier(self):
        input = "1abc }abcd {xyzt ==nhanvo ..abcd"
        expect = "1,abc,},abcd,{,xyzt,==,nhanvo,..,abcd,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))
        
    def test_error_token(self):
        input = "abc nhanvo@"
        expect = "abc,nhanvo,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 108))
        
    def test_error_token_2(self):
        input = ",nhanvo?"
        expect = ",,nhanvo,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 109))
        
    def test_static_identifier(self):
        input = "$xyz $abcd_nhan0910 $____xyz0000 $nhan________vo01010_0000000___ $"
        expect = "$xyz,$abcd_nhan0910,$____xyz0000,$nhan________vo01010_0000000___,Error Token $"
        self.assertTrue(TestLexer.test(input, expect, 110))
        
    def test_case_sensitivity(self):
        input = "write writE WRite"
        expect = "write,writE,WRite,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 111))
        
    def test_all_keywords(self):
        input = """Break Continue If Elseif Else Foreach True False Float 
                Boolean String Int Null Var Val Array Self Return New In
                Class Constructor Destructor By
                """
        expect = "Break,Continue,If,Elseif,Else,Foreach,True,False,Float,Boolean,String,Int,Null,Var,Val,Array,Self,Return,New,In,Class,Constructor,Destructor,By,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))
        
    def test_with_seperators(self):
        input = "a { b } c {d} [abcd] <nhanvo> <=>= . , ; ::)))))) :((((((("
        expect = "a,{,b,},c,{,d,},[,abcd,],<,nhanvo,>,<=,>=,.,,,;,::,),),),),),),:,(,(,(,(,(,(,(,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 113))
    
    def test_string_with_double_quotes(self):
        input = """"He asked me: '"Where is John?'"" """
        expect = """He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 114))
    
    def test_string_with_tab(self):
        input = r""" "This is a string containing tab \t" """
        expect = r"""This is a string containing tab \t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 115))
    
    def test_string_with_newline(self):
        input = r""" "Newline \n" """
        expect = r"Newline \n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 116))
    
    def test_string_with_backslash(self):
        input = """ "Backslash \\\\" """
        expect = """Backslash \\\\,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 117))
    
    def test_string_with_single_quote(self):
        input = """ "My name is Nhan. This name has two \\'N\\' characters" """
        expect = """My name is Nhan. This name has two \\'N\\' characters,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 118))
        
    def test_comment_with_escape(self):
        input = "##Hello. This is comment has \\n \\n \\n \\\\ \\b##"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))
    
    def test_illegal_escape(self):
        input = r""" "My name is\o" """
        expect = "Illegal Escape In String: My name is\\o"
        self.assertTrue(TestLexer.test(input, expect, 120))
    
    def test_float_literal(self):
        input = "12345. 0.3e-1 0.001e+2 12.0e45 12.0e-12"
        expect = "12345.,0.3e-1,0.001e+2,12.0e45,12.0e-12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 121))
    
    def test_float_literal_2(self):
        input = "33.0E3 33e3 14.e5 12.0e3 33000. 140000E-7"
        expect = "33.0E3,33e3,14.e5,12.0e3,33000.,140000E-7,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 122))
    
    def test_float_literal_3(self):
        input = "0. 0.e10 0.0e-123 0.0"
        expect = "0.,0.e10,0.0e-123,0.0,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 123))
    
    def test_boolean_literal(self):
        input = "True False"
        expect = "True,False,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 124))
    
    def test_boolean_literal_identifier(self):  # like indentifiers
        input = "TruE FalSE"
        expect = "TruE,FalSE,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 125))
    
    def test_int_hexa(self):
        input = "0x314 0x140033523 0Xafbd 0X1a31cd"
        # expect = "0x314,0x140033523,0Xafbd,0X1a31cd,<EOF>"
        expect = "0x314,0x140033523,0,Xafbd,0X1,a31cd,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 126))
        
    def test_int_oct(self):
        input = "0123 01407"
        expect = "0123,01407,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 127))
        
    def test_int_oct_2(self):
        input = "00234"
        # expect = "00234,<EOF>"
        expect = "00,234,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 128))
    
    def test_int_decimal(self):
        input = "1407 23406 10 20"
        expect = "1407,23406,10,20,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 129))
        
    def test_int_binary(self):
        input = "0b1100 0B0011111111 0b1010101 0B00110011"
        # expect = "0b1100,0B0011111111,0b1010101,0B00110011,<EOF>"
        expect = "0b1100,0B0,011111111,0b1010101,0B0,0110011,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 130))
    
    def test_multiple_int_literal(self):
        input = "1407 0310 0xabcdef 000310 7890 0xefff"
        # expect = "1407,0310,0xabcdef,000310,7890,0xefff,<EOF>"
        # expect = "1407,0310,0,xabcdef,000310,7890,0,xefff,<EOF>"
        expect = "1407,0310,0,xabcdef,00,0310,7890,0,xefff,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 131))
    
    def test_integer_with_underscore(self):
        input = "1_234_678 1_000_000_123_6978"
        expect = "1234678,10000001236978,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 132))
    
    def test_float_with_underscore(self):
        input = "1_234.567 4_567_798.1e-10 3_145.5e+10"
        expect = "1234.567,4567798.1e-10,3145.5e+10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 133))
        
    def test_boolean_operators(self):
        input = "! && || == !="
        expect = "!,&&,||,==,!=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 134))
    
    def test_boolean_comparision(self):
        input = "a!=b a&&b a||b a==b"
        expect = "a,!=,b,a,&&,b,a,||,b,a,==,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 135))
    
    def test_wrong_boolean_comparision(self):
        input = "a=!b a&#b"
        expect = "a,=,!,b,a,Error Token &"
        self.assertTrue(TestLexer.test(input, expect, 136))
    
    def test__int_and_float_operators(self):
        input = "+ - * / % == != > >= < <= ="
        expect = "+,-,*,/,%,==,!=,>,>=,<,<=,=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 137))
    
    def test_string_operators(self):
        input = "+. ==."
        expect = "+.,==.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))
        
    def test_mixed_operands_operators(self):
        input = "str1+.str2 a=a+3.4 5*7 a%b 5<=7 c/d"
        expect = "str1,+.,str2,a,=,a,+,3.4,5,*,7,a,%,b,5,<=,7,c,/,d,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 139))
        
    def test_unclosed_string(self):
        input = """str = "Hello, my name is"""
        expect = "str,=,Unclosed String: Hello, my name is"
        self.assertTrue(TestLexer.test(input, expect, 140))
        
    def test_unclosed_string_2(self):       # has endline
        input = """ "abcdxyz
        
        """
        expect = "Unclosed String: abcdxyz"
        self.assertTrue(TestLexer.test(input, expect, 141))
        
    def test_unclosed_string_with_illegal_escape(self):
        input = r""" "ldpv \n nhanvo " """
        expect = "ldpv \\n nhanvo ,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 142))
        
    def test_string_with_legal_escape(self):
        input = """ "ldpv \\n \\t nhanvo" """
        expect = r"ldpv \n \t nhanvo,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 143))
    
    def test_multiple_unclosed_string(self):
        input = """ "nhanvo" "nguyenthien" "ledo"""
        expect = "nhanvo,nguyenthien,Unclosed String: ledo"
        self.assertTrue(TestLexer.test(input, expect, 144))
        
    def test_complex_string(self):
        input = """ "This is a complex string with '"quote'" and has comment ##abcd##" """
        expect = """This is a complex string with '"quote'" and has comment ##abcd##,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 145))
    
    def test_string_in_comment(self):
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
        expect = """Class,Program,{,Val,str1,:,String,=,arr,[,1,],;,Constructor,(,a,:,Int,;,B,:,Float,),{,},Destructor,(,),{,},main,(,),{,If,(,!,True,&&,False,),{,},Else,{,If,(,!,True,&&,False,&&,(,(,a,==,5,),||,(,b,==,6,),),),{,},},If,(,!,True,&&,False,),{,},Elseif,(,a,==,5,),{,If,(,!,True,&&,False,),{,},Elseif,(,a,==,5,),{,},Elseif,(,b,==,6,),{,},Elseif,(,!,False,),{,},Elseif,(,a,<,b,),{,},Elseif,(,$xyz,>=,3,),{,},Elseif,(,ar,[,2,],>,3,),{,},},Elseif,(,b,==,6,),{,If,(,!,True,&&,False,),{,},Elseif,(,a,==,5,),{,},Elseif,(,b,==,6,),{,},Elseif,(,!,False,),{,},Elseif,(,a,<,b,),{,},Elseif,(,$xyz,>=,3,),{,},Elseif,(,ar,[,2,],>,3,),{,},},Else,{,If,(,!,True,&&,False,),{,},Elseif,(,a,==,5,),{,},Elseif,(,b,==,6,),{,If,(,!,True,&&,False,),{,},Elseif,(,a,==,5,),{,},Elseif,(,b,==,6,),{,},Elseif,(,!,False,),{,},Elseif,(,a,<,b,),{,},Elseif,(,$xyz,>=,3,),{,},Elseif,(,ar,[,2,],>,3,),{,},},Elseif,(,!,False,),{,},Elseif,(,a,<,b,),{,},Elseif,(,$xyz,>=,3,),{,},Elseif,(,ar,[,2,],>,3,),{,},},},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 146))
    
    def test_legal_and_illegal_escape(self):
        input = """ "This is legal escape: \\n \\t \\b \\r \\f \\\\. This is illegal escape: \\os" """
        expect = """Illegal Escape In String: This is legal escape: \\n \\t \\b \\r \\f \\\\. This is illegal escape: \\o"""
        self.assertTrue(TestLexer.test(input, expect, 147))
        
    def test_error_token_3(self):
        input = "If (a ? b)"
        expect = "If,(,a,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 148))
        
    def test_error_token_4(self):
        input = "##Inside comment## var a = 12; val b = ~"
        expect = "var,a,=,12,;,val,b,=,Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 149))
        
    def test_nested_comment(self):
        input = "##First comment## Content ##Second comment##"
        expect = "Content,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))
        
    def test_some_equation(self):
        input = "12*(4+5) 36/7 8-2*(2+6) 300-200 400%3"
        expect = "12,*,(,4,+,5,),36,/,7,8,-,2,*,(,2,+,6,),300,-,200,400,%,3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))
    
    def test_sample_code_AVL_tree(self):
        input = r"""
                int V = 6;
                int visited = 0;

                Graph g(V);
                Adjacency* arr = new Adjacency(V);
                int edge[][2] = {{0,1},{0,2},{1,3},{1,4},{2,4},{3,4},{3,5},{4,5}};
                    
                for(int i = 0; i < 8; i++)
                {
                    g.addEdge(edge[i][0], edge[i][1]);
                }
                    
                arr = g.BFS(visited);
                arr->printArray();
                delete arr;
                """
        expect = "int,V,=,6,;,int,visited,=,0,;,Graph,g,(,V,),;,Adjacency,*,arr,=,new,Adjacency,(,V,),;,int,edge,[,],[,2,],=,{,{,0,,,1,},,,{,0,,,2,},,,{,1,,,3,},,,{,1,,,4,},,,{,2,,,4,},,,{,3,,,4,},,,{,3,,,5,},,,{,4,,,5,},},;,for,(,int,i,=,0,;,i,<,8,;,i,+,+,),{,g,.,addEdge,(,edge,[,i,],[,0,],,,edge,[,i,],[,1,],),;,},arr,=,g,.,BFS,(,visited,),;,arr,-,>,printArray,(,),;,delete,arr,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 152))
        
    def test_weird_escape(self):
        input = r""" "abcd\" """
        expect = r"""Illegal Escape In String: abcd\""""
        self.assertTrue(TestLexer.test(input, expect, 153))
        
    def test_weird_unclose(self):
        input = """ "xyz'" """
        expect = """Unclosed String: xyz'" """
        self.assertTrue(TestLexer.test(input, expect, 154))
        
    
    def test_multiple_string_comment(self):
        input = r"""
            "This is a string"
            ##"We have a string in a comment. Skip it!!"##
            "##But we have a comment in a string. Therefore, it is an empty string##"
            ""
            "'"Double quote in string'""
        """
        expect = r"""This is a string,##But we have a comment in a string. Therefore, it is an empty string##,,'"Double quote in string'",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 155))
        
    def test_all_escape_sequences(self):
        input = r"""
            "There are some escape seq here: \b\r\f\t\n\'\\'""    
            ""     
        """
        expect = r"""There are some escape seq here: \b\r\f\t\n\'\\'",,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 156))
        
    def test_weird_single_double_quotes(self):
        input = r"""
            "Nhan" "Nhan '"NhanVo'" '"VoNhan'" VoNhanNguyen" "ThienNhan" "" "'"Nhan'""
        """
        expect = r"""Nhan,Nhan '"NhanVo'" '"VoNhan'" VoNhanNguyen,ThienNhan,,'"Nhan'",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 157))
        
    def test_code_slinkedlist(self):
        input = r"""
            template<class T>
            T SLinkedList<T>::get(int index) {
                /* Give the data of the element at given index in the list. */
                if (index > this->count - 1)
                    index = this->count - 1;

                int count1 = 0;
                Node* temp = head;

                while (temp && count1 != index) {
                    temp = temp->next;
                    count1++;
                }

                return temp->data;
            }
        """
        expect = r"""template,<,class,T,>,T,SLinkedList,<,T,>,::,get,(,int,index,),{,/,*,Give,the,data,of,the,element,at,given,index,in,the,list,.,*,/,if,(,index,>,this,-,>,count,-,1,),index,=,this,-,>,count,-,1,;,int,count1,=,0,;,Node,*,temp,=,head,;,while,(,temp,&&,count1,!=,index,),{,temp,=,temp,-,>,next,;,count1,+,+,;,},return,temp,-,>,data,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 158))
        
    def test_sameple_code(self):
        input = r"""
            Class Shape {
                Val $numOfShape: Int = 0;
                Val immutableAttribute: Int = 0;
                Var length, width: Int;
                $getNumOfShape() {
                    return $numOfShape;
                }
            }
            Class Rectangle: Shape {
                getArea() {
                    return Self.length * Self.width;
                }
            }
            Class Program {
                main() {
                    Out.printInt(Shape::$numOfShape);
                }
            }     
        """
        expect = """Class,Shape,{,Val,$numOfShape,:,Int,=,0,;,Val,immutableAttribute,:,Int,=,0,;,Var,length,,,width,:,Int,;,$getNumOfShape,(,),{,return,$numOfShape,;,},},Class,Rectangle,:,Shape,{,getArea,(,),{,return,Self,.,length,*,Self,.,width,;,},},Class,Program,{,main,(,),{,Out,.,printInt,(,Shape,::,$numOfShape,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 159))
    
    def test_unclosedString_with_escape_seq(self):
        input = r"""
            "this is valid string \n \t \b \f"
            "
            ""
            "but here is an unclosed string \n \t \b \f
        """
        expect = "this is valid string \\n \\t \\b \\f,Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 160))
    
    def test_float_not_have_integer_part(self):
        input = ".123 .2e10 .3e-10 .014e+10"
        expect = ".,123,.2e10,.3e-10,.014e+10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))
        
    def test_sample_code_2(self):
        input = r"""
            var r, s: Int;
            r = 2.0;
            var a, b: Array[Int, 5];
            s = r * r * self.myPI;
            a[0] = s;
        """
        expect = "var,r,,,s,:,Int,;,r,=,2.0,;,var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,self,.,myPI,;,a,[,0,],=,s,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 162))
        
    def test_array_literal(self):
        input = r"""
            Array(1,2,3,4)
            Array(1, 5, 7, 12) or Array("Kangxi", "Yongzheng", "Qianlong")
        """
        expect = "Array,(,1,,,2,,,3,,,4,),Array,(,1,,,5,,,7,,,12,),or,Array,(,Kangxi,,,Yongzheng,,,Qianlong,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 163))
    
    def test_multi_dimensional_array(self):
        input = r"""
            Array (
                Array("Volvo", "22", "18"),
                Array("Saab", "5", "2"),
                Array("Land Rover", "17", "15")
            )
        """
        expect = "Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 164))
        
    def test_sample_code_iterator(self):
        ## has error token
        input = r"""
            Iterator(FragmentLinkedList<T> *pList = 0, bool begin = true);
            Iterator(int fragmentIndex, FragmentLinkedList<T> *pList = 0,  bool begin = true);
            Iterator &operator=(const Iterator &iterator);
            T &operator*();
            bool operator!=(const Iterator &iterator);
            void remove();
            void set(const T& element);
            Iterator &operator++();
            Iterator operator++(int);
        """
        expect = "Iterator,(,FragmentLinkedList,<,T,>,*,pList,=,0,,,bool,begin,=,true,),;,Iterator,(,int,fragmentIndex,,,FragmentLinkedList,<,T,>,*,pList,=,0,,,bool,begin,=,true,),;,Iterator,Error Token &"
        self.assertTrue(TestLexer.test(input, expect, 165))
        
    def test_sample_code_BKU_tree(self):
        ## has error token
        input = r"""
            void add(K key, V value) {

                Entry* newEntry = new Entry(key, value);
                typename SplayTree::Node* tempSlay = this->splay->addSplayForBKUTree(newEntry);

                if (tempSlay == nullptr) {  //same key
                    delete tempSlay;
                    tempSlay = nullptr;
                    throw "Duplicate key";
                }

                typename AVLTree::Node* tempAVL = this->avl->addAVLForBKUTree(newEntry);

                tempSlay->corr = tempAVL;
                tempAVL->corr = tempSlay;

                if ((int)keys.size() == this->maxNumOfKeys) {
                    keys.pop();
                    vectorKeys.erase(vectorKeys.begin() + 0);
                }
                keys.push(key);
                vectorKeys.push_back(key);
            }
        """
        expect = "void,add,(,K,key,,,V,value,),{,Entry,*,newEntry,=,new,Entry,(,key,,,value,),;,typename,SplayTree,::,Node,*,tempSlay,=,this,-,>,splay,-,>,addSplayForBKUTree,(,newEntry,),;,if,(,tempSlay,==,nullptr,),{,/,/,same,key,delete,tempSlay,;,tempSlay,=,nullptr,;,throw,Duplicate key,;,},typename,AVLTree,::,Node,*,tempAVL,=,this,-,>,avl,-,>,addAVLForBKUTree,(,newEntry,),;,tempSlay,-,>,corr,=,tempAVL,;,tempAVL,-,>,corr,=,tempSlay,;,if,(,(,int,),keys,.,size,(,),==,this,-,>,maxNumOfKeys,),{,keys,.,pop,(,),;,vectorKeys,.,erase,(,vectorKeys,.,begin,(,),+,0,),;,},keys,.,push,(,key,),;,vectorKeys,.,push_back,(,key,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 166))
        
    def test_combo_int_literals(self):
        input = r"""
            123 310_596______32424 34234_________________3243243 3_4_5___5546___565465_1407_____43423
            0b111101 0B000000000011111111 0b111111111111111110000000000000000
            0123 002344 0003432434234 00000000000000003123123213 02313123200000000000000
            0x0000000000000000001abcdf 0Xabcdef99999999999900000000000
        """
        expect = "123,310596,______32424,34234,_________________3243243,345,___5546___565465_1407_____43423,0b111101,0B0,00,00,00,00,011111111,0b111111111111111110000000000000000,0123,00,2344,00,03432434234,00,00,00,00,00,00,00,00,3123123213,02313123200000000000000,0x0,00,00,00,00,00,00,00,00,01,abcdf,0,Xabcdef99999999999900000000000,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 167))
    
    def test_string_operators_2(self):
        input = r"""
            Var str1 = "This is a string 1. In this string, we have content: '"nhanvonguyen'" "
            Var str2 = "This is a string 1. In this string, we have content: '"someoneilike'" "
            Concatenate: str1 +. str2
            Compare: str1 ==. str2
        """
        expect = """Var,str1,=,This is a string 1. In this string, we have content: '"nhanvonguyen'" ,Var,str2,=,This is a string 1. In this string, we have content: '"someoneilike'" ,Concatenate,:,str1,+.,str2,Compare,:,str1,==.,str2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 168))
        
    def test_mixed_some_statements(self):
        ## has error token
        input = r"""
            Foreach (i In 1 .. 100 By 2) {
                Out.printInt(i);
            }
            Foreach (<scalar variable> In <expr1> .. <expr2> [By <expr3>]?)
                ##<block statement>##
        """
        expect = "Foreach,(,i,In,1,..,100,By,2,),{,Out,.,printInt,(,i,),;,},Foreach,(,<,scalar,variable,>,In,<,expr1,>,..,<,expr2,>,[,By,<,expr3,>,],Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 169))
        
    def test_nothing(self):
        input = r"""
            "First string is valid"
            "I don\'t know what tests to write"
            "But this string is not"
            "I don't know what tests to write"
        """
        # expect = r"""First string is valid,I don\'t know what tests to write,But this string is not,Illegal Escape In String: I don't"""
        expect = r"""First string is valid,I don\'t know what tests to write,But this string is not,I don't know what tests to write,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 170))
        
    def test_string_unclosed(self):
        input = r"""
            ##String not enter for newline##
            "ldpv
            nhanvo
            "
            
        """
        expect = "Unclosed String: ldpv"
        self.assertTrue(TestLexer.test(input, expect, 171))
        
    def test_string_with_tabs(self):
        input = r"""
            ##String has tabs --> still valid##
            "nhanvo     x                       ldpv"
        """
        expect = "nhanvo     x                       ldpv,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))
    
    def test_sample_code_sorting(self):
        input = r"""
                template <class T>
                void Sorting<T>::hybridQuickSort(T *start, T *end, int min_size)
                {
                    while (start < end) {
                        if (end - start < min_size) {
                            cout << "Insertion sort: ";printArray(start, end);  
                            insertionSort(start, end);
                            
                            break;
                        }
                        else {
                            cout << "Quick sort: ";printArray(start, end);
                            T* pivot = Partition(start, end);
                            
                            hybridQuickSort(start, pivot, min_size);
                            start = pivot + 1;
                            hybridQuickSort(pivot + 1, end, min_size);
                            end = pivot;
                        }
                    }
                }
                """
        expect = "template,<,class,T,>,void,Sorting,<,T,>,::,hybridQuickSort,(,T,*,start,,,T,*,end,,,int,min_size,),{,while,(,start,<,end,),{,if,(,end,-,start,<,min_size,),{,cout,<,<,Insertion sort: ,;,printArray,(,start,,,end,),;,insertionSort,(,start,,,end,),;,break,;,},else,{,cout,<,<,Quick sort: ,;,printArray,(,start,,,end,),;,T,*,pivot,=,Partition,(,start,,,end,),;,hybridQuickSort,(,start,,,pivot,,,min_size,),;,start,=,pivot,+,1,;,hybridQuickSort,(,pivot,+,1,,,end,,,min_size,),;,end,=,pivot,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))
    
    def test_error_token_5(self):
        input = r"""
            str1 = "Can you give me some testcases"
            str2 = "No!"
            '":< T.T'"
        """
        expect = "str1,=,Can you give me some testcases,str2,=,No!,Error Token '"
        self.assertTrue(TestLexer.test(input, expect, 174))
    
    def test_sample_code_memo(self):
        input = r"""
            Class Program {
                    
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var $x, $y, z : Int = 0, 0, 0;
                
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
        expect = "Class,Program,{,Val,My1stCons,,,My2ndCons,:,Int,=,1,+,5,,,2,;,Var,$x,,,$y,,,z,:,Int,=,0,,,0,,,0,;,Constructor,(,a,:,Int,;,B,:,Float,),{,$x,=,10,;,$y,=,1000,;,My1stCons,=,5,+,2,;,My2ndCons,=,(,0b1101010,&&,0b1101110,),;,},Destructor,(,),{,$x,=,0,;,$y,=,0,;,My1stCons,=,0,;,My2ndCons,=,0,;,},test,(,),{,If,(,-,5,==,5,),{,},If,(,5,!=,4,),{,},If,(,5,>,4,),{,},If,(,3,<,4,),{,},If,(,5,>=,4,),{,},If,(,3,<=,4,),{,},If,(,a,==,5,),{,},If,(,a,<,5,),{,},If,(,a,>,5,),{,},If,(,a,<=,5,),{,},If,(,a,>=,5,),{,},If,(,a,==,xyz,),{,},If,(,a,!=,$xyz,),{,},If,(,a,>,nhanvo,),{,},If,(,a,<,ldpv,),{,},If,(,a,>=,abc,),{,},If,(,a,<=,abc,),{,},},main,(,),{,},},Class,Program,{,Val,a,:,Int,=,130703100310,+,-,255255255255,;,Val,b,:,Int,=,-,130703100310,-,255255255255,;,Var,m,:,Int,=,-,130703100310,/,255255255255,;,Var,c,:,Int,=,130703100310,%,255255255255,;,Var,d,:,Float,=,-,130703100310.213e-10,+,-,255255255255.3e+10,;,Var,e,:,Float,=,0.0000001e10,-,-,0.00000000000000008e-10,;,Var,f,:,Float,=,99999.10e30,/,-,123456789.10e-20,;,Constructor,(,a,:,Int,;,B,:,Float,),{,},Destructor,(,),{,},main,(,),{,},},Class,Program,{,Val,str1,:,String,=,arr,[,1,],;,Val,str2,:,String,=,x,[,1,],[,2,],;,Val,a,:,String,=,x,[,1,],[,2,],[,3,],;,Var,c,:,String,=,x,[,1,],[,2,],[,3,],[,4,],;,Var,c,:,String,=,arr,[,arr,[,arr,[,1,],],],;,Var,c,:,String,=,arr,[,arr,[,1,],],;,Constructor,(,a,:,Int,;,B,:,Float,),{,},Destructor,(,),{,},main,(,),{,a,=,2,;,abc,=,2,+,5,;,abc,=,(,0b110101,&&,0b1100100,),;,abc,=,(,0b0,10101,||,0b1100100,),;,abc,=,first string,+,second string,;,abc,=,arr,[,1,],[,2,],;,$abc,=,arr,[,arr,[,arr,[,1,],],],;,arr,[,2,],=,arr,[,arr,[,arr,[,1,],],],;,arr,[,arr,[,arr,[,arr,[,100,],],],],=,a,.,b,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))
        
    def test_string_with_some_tabs(self):
        input = """
            "abcd\t"
        """
        # expect = """abcd\t,<EOF>"""
        expect = """Unclosed String: abcd"""
        self.assertTrue(TestLexer.test(input, expect, 176))
        
    def test_string_with_some_escape(self):
        input = """
            "abc\b\f\t\t\t"
        """
        # expect = """abc\b\f\t\t\t,<EOF>"""
        expect = """Unclosed String: abc"""
        self.assertTrue(TestLexer.test(input, expect, 177))
    
    def test_invalid_escape_quote(self):
        input = """ "This is another invalid ''" quote" """
        # expect = """Illegal Escape In String: This is another invalid ''"""
        expect = """This is another invalid ''" quote,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 178))
        
    def test_invalid_keywords(self):
        input = """BReaK ContInuE IF ElSEif eLSe foreAch tRue fAlse floAt boOlean
                StrinG INt NUll VAR VaL ARRay sElf reTurn NEw IN class cONstructor dEstructor by"""
        expect = """BReaK,ContInuE,IF,ElSEif,eLSe,foreAch,tRue,fAlse,floAt,boOlean,StrinG,INt,NUll,VAR,VaL,ARRay,sElf,reTurn,NEw,IN,class,cONstructor,dEstructor,by,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 179))
        
    def test_some_invalid_identifiers(self):
        input = r"""
                    123_abcd 000_xyz 000234_123xyz
                """
        expect = """123,_abcd,00,0,_xyz,00,0234123,xyz,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 180))
        
    def test_some_invalid_float(self):
        input = r"""
                    e12 e-12 e+12 EEE-10 0000000000000002.32423
                """
        expect = """e12,e,-,12,e,+,12,EEE,-,10,00,00,00,00,00,00,00,02,.,32423,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 181))
        
    def test_some_confused_escape(self):
        input = """
                    "The first string \'"confused\'""
                    "The second string is or not illegal \'n"
                """
        expect = """The first string '"confused'",The second string is or not illegal 'n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 182))
        
    def test_some_confused_escape_2(self):
        input = r"""
                    "First string \ ' '"
                """
        expect = r"""Illegal Escape In String: First string \ """
        self.assertTrue(TestLexer.test(input, expect, 183))
        
    def test_some_combo_string(self):
        input = r"""
                    ""
                    "above is the empty string"
                    "##still print this line##"
                    ##""##
                    "nhanvo##still print this line##"
                    ""
                    "'"'""
                    "'"\t\b\n\f\r'""
                    "\t\b\n\f\r"
                """
        expect = r""",above is the empty string,##still print this line##,nhanvo##still print this line##,,'"'",'"\t\b\n\f\r'",\t\b\n\f\r,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 184))
        
    def test_some_sample_code(self):
        input = r"""
                    typedef pair<int,int> myPair;
                    int Dijkstra(int** graph, int src, int dst) {
                        // TODO: return the length of shortest path from src to dst.
                        int n = 6;

                        list<myPair> *li = new list<myPair>[n];
                        
                        
                        //adjacency list
                        for (int i = 0; i < n; i++) {
                            for (int j = 0; j < n; j++) {
                                //cout << graph[i][j] << "  ";
                                if (i != j && graph[i][j] != 0) {
                                    li[i].push_back(make_pair(graph[i][j], j));
                                }
                            }
                            //cout << endl;
                        }

                        vector<int> distance (n, 999999999);
                        priority_queue<myPair, vector<myPair>, greater<myPair>> q;
                        
                        q.push(make_pair(0, src));
                        distance[src] = 0;

                        while (!q.empty()) {
                            int u = q.top().second;
                            q.pop();

                            for (auto x = li[u].begin(); x != li[u].end(); x++) {
                                int weight = x->first;
                                int des = x->second;

                                if (distance[u] + weight < distance[des]) {
                                    distance[des] = distance[u] + weight;
                                    q.push(make_pair(distance[des], des));
                                }
                            }
                        }

                        /*for (int i = 0; i < 6; i++) {

                            cout << i << ": ";
                            for (auto x = li[i].begin(); x != li[i].end(); x++) {
                                cout << x->second << "  ";
                            }   
                            cout << endl;
                        }*/

                        int result = 0;

                        for (int i = 0; i < 9; i++) {
                            if (i == dst)   result = distance[i];
                        }

                        
                        return result;
                    }
                """
        expect = r"""typedef,pair,<,int,,,int,>,myPair,;,int,Dijkstra,(,int,*,*,graph,,,int,src,,,int,dst,),{,/,/,TODO,:,return,the,length,of,shortest,path,from,src,to,dst,.,int,n,=,6,;,list,<,myPair,>,*,li,=,new,list,<,myPair,>,[,n,],;,/,/,adjacency,list,for,(,int,i,=,0,;,i,<,n,;,i,+,+,),{,for,(,int,j,=,0,;,j,<,n,;,j,+,+,),{,/,/,cout,<,<,graph,[,i,],[,j,],<,<,  ,;,if,(,i,!=,j,&&,graph,[,i,],[,j,],!=,0,),{,li,[,i,],.,push_back,(,make_pair,(,graph,[,i,],[,j,],,,j,),),;,},},/,/,cout,<,<,endl,;,},vector,<,int,>,distance,(,n,,,999999999,),;,priority_queue,<,myPair,,,vector,<,myPair,>,,,greater,<,myPair,>,>,q,;,q,.,push,(,make_pair,(,0,,,src,),),;,distance,[,src,],=,0,;,while,(,!,q,.,empty,(,),),{,int,u,=,q,.,top,(,),.,second,;,q,.,pop,(,),;,for,(,auto,x,=,li,[,u,],.,begin,(,),;,x,!=,li,[,u,],.,end,(,),;,x,+,+,),{,int,weight,=,x,-,>,first,;,int,des,=,x,-,>,second,;,if,(,distance,[,u,],+,weight,<,distance,[,des,],),{,distance,[,des,],=,distance,[,u,],+,weight,;,q,.,push,(,make_pair,(,distance,[,des,],,,des,),),;,},},},/,*,for,(,int,i,=,0,;,i,<,6,;,i,+,+,),{,cout,<,<,i,<,<,: ,;,for,(,auto,x,=,li,[,i,],.,begin,(,),;,x,!=,li,[,i,],.,end,(,),;,x,+,+,),{,cout,<,<,x,-,>,second,<,<,  ,;,},cout,<,<,endl,;,},*,/,int,result,=,0,;,for,(,int,i,=,0,;,i,<,9,;,i,+,+,),{,if,(,i,==,dst,),result,=,distance,[,i,],;,},return,result,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 185))
        
    def test_some_illegal(self):
        input = """
                    "abc\\ "    
                """
        expect = """Illegal Escape In String: abc\ """
        self.assertTrue(TestLexer.test(input, expect, 186))
    
    def test_some_error_token(self):
        input = """
                    "abc " _____________nhanvo______________ xyz "
                """
        expect = "abc ,_____________nhanvo______________,xyz,Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, 187))
        
    def test_some_unclosed_2(self):
        input = """
                    "nhanvo \n "
                """
        expect = "Unclosed String: nhanvo "
        self.assertTrue(TestLexer.test(input, expect, 188))
        
    def test_some_unclosed_3(self):
        input = """
                    "nhanvo \r "
                """
        expect = "Unclosed String: nhanvo "
        self.assertTrue(TestLexer.test(input, expect, 189))
        
    def test_some_unclosed_4(self):
        input = """
                    "nhanvo \f "
                """
        # expect = "nhanvo \f ,<EOF>"
        expect = "Unclosed String: nhanvo "
        self.assertTrue(TestLexer.test(input, expect, 190))
        
    def test_some_unclosed_5(self):
        input = """
                    "nhanvo \t "
                """
        # expect = "nhanvo \t ,<EOF>"
        expect = "Unclosed String: nhanvo "
        self.assertTrue(TestLexer.test(input, expect, 191))
        
    def test_some_unclosed_6(self):
        input = """
                    "nhanvo \b "
                """
        # expect = "nhanvo \b ,<EOF>"
        expect = "Unclosed String: nhanvo "
        self.assertTrue(TestLexer.test(input, expect, 192))
        
    def test_keywords_in_string(self):
        input = """
                    "There are some keywords: Break,Continue,If,Elseif,Else,Foreach,True,False,Float"
                """
        expect = "There are some keywords: Break,Continue,If,Elseif,Else,Foreach,True,False,Float,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))
        
    def test_invalid_words_in_string(self):
        input = """
                    "Some invalid words: @ ? ` ~ | ^ /"
                """
        expect = "Some invalid words: @ ? ` ~ | ^ /,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))
        
    def test_escape(self):
        input = r"""
                    "\\\\ \\n \b \f \t \\b \\f \\t \f \f"
                """
        expect = r"""\\\\ \\n \b \f \t \\b \\f \\t \f \f,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 195))
    
    def test_unclosed_mixed(self):
        input = """
            "There are some escape seq here: \b \\b mid \f \\f mid \t \\t mid '"\tinsingle\t'"again insingle of before'"\t'"\f\t \b \n'""    
            ""     
        """
        # expect = """Unclosed String: There are some escape seq here: \b \\b mid \f \\f mid \t \\t mid '"\tinsingle\t'"again insingle of before'"\t'"\f\t \b """
        expect = """Unclosed String: There are some escape seq here: """
        self.assertTrue(TestLexer.test(input, expect, 196))
        
    def test_code_keywords(self):
        input = r"""
                Class ProgramCode {
                    $numOfShape = 100;
                    Val a: Array[Float, 10];
                    Var b: Array[String, 10];
                    
                    $getNumOfShape() {
                        i = 3*4/2 - 10 + 500
                        Foreach (i In 1..50 By 2)
                            print(Self.text);
                            Continue;
                            Break;
                        return $numOfShape;
                    }

                    Constructor() {}
                    
                    Destructor() {}
                }
                """
        expect = "Class,ProgramCode,{,$numOfShape,=,100,;,Val,a,:,Array,[,Float,,,10,],;,Var,b,:,Array,[,String,,,10,],;,$getNumOfShape,(,),{,i,=,3,*,4,/,2,-,10,+,500,Foreach,(,i,In,1.,.,50,By,2,),print,(,Self,.,text,),;,Continue,;,Break,;,return,$numOfShape,;,},Constructor,(,),{,},Destructor,(,),{,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 197))
        
    def test_some_comment(self):
        input = """
                    ##Inside
                    Block
                    Comment ? @@@@@ ^^^^^^ |||||||||||||||
                    Have # # # # # # # # # # \t \n \r
                    ##
                    ###
                """
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 198))
        
    def test_some_combo_int_literals(self):
        input = r"""
                    0 123 _123456 31074_ 1407_0310 1_234_5678_ _1_234_5678 000234
                    0x123abcdef 0Xabcdef 0xABCD99999 0XABCD912432
                    0x000123 0X000000abcdef 0xfffff000000 0xpefd9999
                    0000456 0067896 07865 088888
                    0b00001111 0B000111 0b111110101011 0B101010101 0b01010101
                """      
        expect = "0,123,_123456,31074,_,14070310,12345678,_,_1_234_5678,00,0234,0x123,abcdef,0,Xabcdef,0xABCD99999,0XABCD912432,0x0,00,123,0X0,00,00,0,abcdef,0,xfffff000000,0,xpefd9999,00,00,456,00,67896,07,865,0,88888,0b0,00,01111,0B0,00,111,0b111110101011,0B101010101,0b0,1010101,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))
        
    def test_some_combo_float_literals(self):
        input = r"""
                    0.2 0.03 0.00004 0.10000000000 0.100002 7.3 7.0000003 7.30000000000 100.00000000000000
                    0.2e10 0.0003e-10 0.300000E-10 0.40000e+10 7.33000e-10 8.4E+10
                    .234 .0000003 .3000000 .e10 .e-10 .e+10 e+10 e-10 12e10 45e+10 6e+00000001
                    0000023e-10 230000E+10
                    .e-10000000 .e+00000001 .e000000002 .e30000000
                    1_234_6756.234_342_234 1_234_6756.234_342_234__ __1_234_6756.234_342_234__
                    .e_10 .e-10_000_000 .E+111_1111_
                    7.3_456_567e+10_234_678 000_000_123_000.E+000_000_111
                    ## new ##
                    00002.345
                    2.e00000000
                    12.0000000
                    12.00002
                    2.e000012
                    0.00232e+002   
                    0.0
                    0.0000000e0000000
                    0.0000000000
                """
        expect = "0.2,0.03,0.00004,0.10000000000,0.100002,7.3,7.0000003,7.30000000000,100.00000000000000,0.2e10,0.0003e-10,0.300000E-10,0.40000e+10,7.33000e-10,8.4E+10,.,234,.,00,00,00,3,.,3000000,.e10,.e-10,.e+10,e,+,10,e,-,10,12e10,45e+10,6e+00000001,00,00,023,e,-,10,230000E+10,.e-10000000,.e+00000001,.e000000002,.e30000000,12346756.234,_342_234,12346756.234,_342_234__,__1_234_6756,.,234342234,__,.,e_10,.e-10,_000_000,.E+111,_1111_,7.3,_456_567e,+,10234678,00,0,_000_123_000,.E+000,_000_111,00,00,2.345,2.e00000000,12.0000000,12.00002,2.e000012,0.00232e+002,0.0,0.0000000e0000000,0.0000000000,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 200))
        
        
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
        # expect = "nhan\b\t\f \\b\\t\\f ''\",<EOF>"
        expect = "Unclosed String: nhan"
        self.assertTrue(TestLexer.test(input, expect, 1217))
        
    def test_some_thing_confused_18(self):
        input = """ "''''''''''''"" """
        expect = "''''''''''''\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 1218))
        
    def test_some_thing_confused_19(self):
        input = """ "''''''''''''"" " """
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
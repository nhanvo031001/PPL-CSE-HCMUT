# Generated from d:\OneDrive - hcmut.edu.vn\HK212\PPL\BTL\BTL1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import re



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2L")
        buf.write("\u029e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\3\16\3\16\5\16\u0106\n\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\7\21\u010f\n\21\f\21\16\21\u0112")
        buf.write("\13\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\38\38\78\u01cd\n8\f8\168\u01d0\138\38")
        buf.write("\38\38\39\39\3:\3:\3;\3;\5;\u01db\n;\3;\7;\u01de\n;\f")
        buf.write(";\16;\u01e1\13;\3<\3<\7<\u01e5\n<\f<\16<\u01e8\13<\3=")
        buf.write("\3=\5=\u01ec\n=\3=\6=\u01ef\n=\r=\16=\u01f0\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u0200\n>\3>\3>\3?\3?\3")
        buf.write("@\3@\3A\3A\6A\u020a\nA\rA\16A\u020b\3B\3B\5B\u0210\nB")
        buf.write("\3B\7B\u0213\nB\fB\16B\u0216\13B\3B\5B\u0219\nB\3C\3C")
        buf.write("\3C\6C\u021e\nC\rC\16C\u021f\3D\3D\3D\6D\u0225\nD\rD\16")
        buf.write("D\u0226\3E\3E\3E\3E\5E\u022d\nE\3E\3E\3F\3F\5F\u0233\n")
        buf.write("F\3G\3G\3H\3H\3H\3I\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3M\3")
        buf.write("M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3R\3S\3S\3T\3T\3T\3U\3")
        buf.write("U\3U\3V\3V\3V\3V\3W\3W\3X\6X\u0261\nX\rX\16X\u0262\3X")
        buf.write("\3X\3Y\3Y\5Y\u0269\nY\3Y\3Y\3Y\7Y\u026e\nY\fY\16Y\u0271")
        buf.write("\13Y\3Z\3Z\6Z\u0275\nZ\rZ\16Z\u0276\3[\3[\5[\u027b\n[")
        buf.write("\3\\\3\\\3\\\3\\\5\\\u0281\n\\\3]\3]\3]\3]\5]\u0287\n")
        buf.write("]\3^\3^\7^\u028b\n^\f^\16^\u028e\13^\3^\3^\3^\3_\3_\7")
        buf.write("_\u0295\n_\f_\16_\u0298\13_\3_\3_\3`\3`\3`\3\u0110\2a")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\2\25\2\27\2\31")
        buf.write("\2\33\2\35\2\37\2!\13#\f%\r\'\16)\17+\20-\21/\22\61\23")
        buf.write("\63\24\65\25\67\269\27;\30=\31?\32A\33C\34E\35G\36I\37")
        buf.write("K M!O\"Q#S$U%W&Y\'[(])_*a+c,e-g.i/k\60m\61o\62q\2s\2u")
        buf.write("\2w\2y\2{\63}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2")
        buf.write("\u0089\64\u008b\65\u008d\66\u008f\67\u00918\u00939\u0095")
        buf.write(":\u0097;\u0099<\u009b=\u009d>\u009f?\u00a1@\u00a3A\u00a5")
        buf.write("B\u00a7C\u00a9D\u00abE\u00adF\u00afG\u00b1H\u00b3I\u00b5")
        buf.write("\2\u00b7\2\u00b9\2\u00bbJ\u00bdK\u00bfL\3\2\22\3\2C\\")
        buf.write("\3\2c|\3\2\62;\4\2GGgg\4\2--//\4\2ZZzz\4\2DDdd\3\2\62")
        buf.write("9\3\2\63;\4\2\62;CH\3\2\62\63\5\2\n\f\16\17\"\"\6\2\62")
        buf.write(";C\\aac|\7\2\f\f\17\17$$))^^\t\2))^^ddhhppttvv\3\2$$\2")
        buf.write("\u02a8\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2{\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2")
        buf.write("\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\3\u00c1\3\2\2")
        buf.write("\2\5\u00c5\3\2\2\2\7\u00cc\3\2\2\2\t\u00cf\3\2\2\2\13")
        buf.write("\u00de\3\2\2\2\r\u00e8\3\2\2\2\17\u00ee\3\2\2\2\21\u00f5")
        buf.write("\3\2\2\2\23\u00fb\3\2\2\2\25\u00fd\3\2\2\2\27\u00ff\3")
        buf.write("\2\2\2\31\u0101\3\2\2\2\33\u0105\3\2\2\2\35\u0107\3\2")
        buf.write("\2\2\37\u010a\3\2\2\2!\u010c\3\2\2\2#\u0117\3\2\2\2%\u011b")
        buf.write("\3\2\2\2\'\u0120\3\2\2\2)\u0126\3\2\2\2+\u012f\3\2\2\2")
        buf.write("-\u0132\3\2\2\2/\u0139\3\2\2\2\61\u013e\3\2\2\2\63\u0146")
        buf.write("\3\2\2\2\65\u014b\3\2\2\2\67\u0151\3\2\2\29\u0157\3\2")
        buf.write("\2\2;\u015f\3\2\2\2=\u0166\3\2\2\2?\u016a\3\2\2\2A\u016f")
        buf.write("\3\2\2\2C\u0173\3\2\2\2E\u0177\3\2\2\2G\u017d\3\2\2\2")
        buf.write("I\u0182\3\2\2\2K\u0189\3\2\2\2M\u018d\3\2\2\2O\u0190\3")
        buf.write("\2\2\2Q\u0196\3\2\2\2S\u01a2\3\2\2\2U\u01ad\3\2\2\2W\u01b0")
        buf.write("\3\2\2\2Y\u01b2\3\2\2\2[\u01b4\3\2\2\2]\u01b6\3\2\2\2")
        buf.write("_\u01b8\3\2\2\2a\u01bb\3\2\2\2c\u01bd\3\2\2\2e\u01bf\3")
        buf.write("\2\2\2g\u01c1\3\2\2\2i\u01c3\3\2\2\2k\u01c5\3\2\2\2m\u01c8")
        buf.write("\3\2\2\2o\u01ca\3\2\2\2q\u01d4\3\2\2\2s\u01d6\3\2\2\2")
        buf.write("u\u01d8\3\2\2\2w\u01e2\3\2\2\2y\u01e9\3\2\2\2{\u01ff\3")
        buf.write("\2\2\2}\u0203\3\2\2\2\177\u0205\3\2\2\2\u0081\u0207\3")
        buf.write("\2\2\2\u0083\u0218\3\2\2\2\u0085\u021a\3\2\2\2\u0087\u0221")
        buf.write("\3\2\2\2\u0089\u022c\3\2\2\2\u008b\u0232\3\2\2\2\u008d")
        buf.write("\u0234\3\2\2\2\u008f\u0236\3\2\2\2\u0091\u0239\3\2\2\2")
        buf.write("\u0093\u023c\3\2\2\2\u0095\u023f\3\2\2\2\u0097\u0242\3")
        buf.write("\2\2\2\u0099\u0244\3\2\2\2\u009b\u0246\3\2\2\2\u009d\u0248")
        buf.write("\3\2\2\2\u009f\u024a\3\2\2\2\u00a1\u024c\3\2\2\2\u00a3")
        buf.write("\u024e\3\2\2\2\u00a5\u0251\3\2\2\2\u00a7\u0253\3\2\2\2")
        buf.write("\u00a9\u0256\3\2\2\2\u00ab\u0259\3\2\2\2\u00ad\u025d\3")
        buf.write("\2\2\2\u00af\u0260\3\2\2\2\u00b1\u0268\3\2\2\2\u00b3\u0272")
        buf.write("\3\2\2\2\u00b5\u027a\3\2\2\2\u00b7\u0280\3\2\2\2\u00b9")
        buf.write("\u0286\3\2\2\2\u00bb\u0288\3\2\2\2\u00bd\u0292\3\2\2\2")
        buf.write("\u00bf\u029b\3\2\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7")
        buf.write("u\2\2\u00c3\u00c4\7f\2\2\u00c4\4\3\2\2\2\u00c5\u00c6\7")
        buf.write("c\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8\7h\2\2\u00c8\u00c9")
        buf.write("\7t\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb\7j\2\2\u00cb\6")
        buf.write("\3\2\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce\7f\2\2\u00ce\b")
        buf.write("\3\2\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2")
        buf.write("\7f\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4\7f\2\2\u00d4\u00d5")
        buf.write("\7u\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7u\2\2\u00d7\u00d8")
        buf.write("\7f\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da\7u\2\2\u00da\u00db")
        buf.write("\7f\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7u\2\2\u00dd\n")
        buf.write("\3\2\2\2\u00de\u00df\7u\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1")
        buf.write("\7f\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7f\2\2\u00e3\u00e4")
        buf.write("\7u\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7u\2\2\u00e7\f\3\2\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea")
        buf.write("\7j\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed")
        buf.write("\7x\2\2\u00ed\16\3\2\2\2\u00ee\u00ef\7j\2\2\u00ef\u00f0")
        buf.write("\7l\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7j\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7c\2\2\u00f4\20\3\2\2\2\u00f5\u00f6")
        buf.write("\7j\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7j\2\2\u00f8\u00f9")
        buf.write("\7c\2\2\u00f9\u00fa\7j\2\2\u00fa\22\3\2\2\2\u00fb\u00fc")
        buf.write("\t\2\2\2\u00fc\24\3\2\2\2\u00fd\u00fe\t\3\2\2\u00fe\26")
        buf.write("\3\2\2\2\u00ff\u0100\7a\2\2\u0100\30\3\2\2\2\u0101\u0102")
        buf.write("\t\4\2\2\u0102\32\3\2\2\2\u0103\u0106\5\23\n\2\u0104\u0106")
        buf.write("\5\25\13\2\u0105\u0103\3\2\2\2\u0105\u0104\3\2\2\2\u0106")
        buf.write("\34\3\2\2\2\u0107\u0108\7%\2\2\u0108\u0109\7%\2\2\u0109")
        buf.write("\36\3\2\2\2\u010a\u010b\7&\2\2\u010b \3\2\2\2\u010c\u0110")
        buf.write("\5\35\17\2\u010d\u010f\13\2\2\2\u010e\u010d\3\2\2\2\u010f")
        buf.write("\u0112\3\2\2\2\u0110\u0111\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0111\u0113\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0114\5")
        buf.write("\35\17\2\u0114\u0115\3\2\2\2\u0115\u0116\b\21\2\2\u0116")
        buf.write("\"\3\2\2\2\u0117\u0118\7k\2\2\u0118\u0119\7p\2\2\u0119")
        buf.write("\u011a\7v\2\2\u011a$\3\2\2\2\u011b\u011c\7x\2\2\u011c")
        buf.write("\u011d\7q\2\2\u011d\u011e\7k\2\2\u011e\u011f\7f\2\2\u011f")
        buf.write("&\3\2\2\2\u0120\u0121\7D\2\2\u0121\u0122\7t\2\2\u0122")
        buf.write("\u0123\7g\2\2\u0123\u0124\7c\2\2\u0124\u0125\7m\2\2\u0125")
        buf.write("(\3\2\2\2\u0126\u0127\7E\2\2\u0127\u0128\7q\2\2\u0128")
        buf.write("\u0129\7p\2\2\u0129\u012a\7v\2\2\u012a\u012b\7k\2\2\u012b")
        buf.write("\u012c\7p\2\2\u012c\u012d\7w\2\2\u012d\u012e\7g\2\2\u012e")
        buf.write("*\3\2\2\2\u012f\u0130\7K\2\2\u0130\u0131\7h\2\2\u0131")
        buf.write(",\3\2\2\2\u0132\u0133\7G\2\2\u0133\u0134\7n\2\2\u0134")
        buf.write("\u0135\7u\2\2\u0135\u0136\7g\2\2\u0136\u0137\7k\2\2\u0137")
        buf.write("\u0138\7h\2\2\u0138.\3\2\2\2\u0139\u013a\7G\2\2\u013a")
        buf.write("\u013b\7n\2\2\u013b\u013c\7u\2\2\u013c\u013d\7g\2\2\u013d")
        buf.write("\60\3\2\2\2\u013e\u013f\7H\2\2\u013f\u0140\7q\2\2\u0140")
        buf.write("\u0141\7t\2\2\u0141\u0142\7g\2\2\u0142\u0143\7c\2\2\u0143")
        buf.write("\u0144\7e\2\2\u0144\u0145\7j\2\2\u0145\62\3\2\2\2\u0146")
        buf.write("\u0147\7V\2\2\u0147\u0148\7t\2\2\u0148\u0149\7w\2\2\u0149")
        buf.write("\u014a\7g\2\2\u014a\64\3\2\2\2\u014b\u014c\7H\2\2\u014c")
        buf.write("\u014d\7c\2\2\u014d\u014e\7n\2\2\u014e\u014f\7u\2\2\u014f")
        buf.write("\u0150\7g\2\2\u0150\66\3\2\2\2\u0151\u0152\7H\2\2\u0152")
        buf.write("\u0153\7n\2\2\u0153\u0154\7q\2\2\u0154\u0155\7c\2\2\u0155")
        buf.write("\u0156\7v\2\2\u01568\3\2\2\2\u0157\u0158\7D\2\2\u0158")
        buf.write("\u0159\7q\2\2\u0159\u015a\7q\2\2\u015a\u015b\7n\2\2\u015b")
        buf.write("\u015c\7g\2\2\u015c\u015d\7c\2\2\u015d\u015e\7p\2\2\u015e")
        buf.write(":\3\2\2\2\u015f\u0160\7U\2\2\u0160\u0161\7v\2\2\u0161")
        buf.write("\u0162\7t\2\2\u0162\u0163\7k\2\2\u0163\u0164\7p\2\2\u0164")
        buf.write("\u0165\7i\2\2\u0165<\3\2\2\2\u0166\u0167\7K\2\2\u0167")
        buf.write("\u0168\7p\2\2\u0168\u0169\7v\2\2\u0169>\3\2\2\2\u016a")
        buf.write("\u016b\7P\2\2\u016b\u016c\7w\2\2\u016c\u016d\7n\2\2\u016d")
        buf.write("\u016e\7n\2\2\u016e@\3\2\2\2\u016f\u0170\7X\2\2\u0170")
        buf.write("\u0171\7c\2\2\u0171\u0172\7t\2\2\u0172B\3\2\2\2\u0173")
        buf.write("\u0174\7X\2\2\u0174\u0175\7c\2\2\u0175\u0176\7n\2\2\u0176")
        buf.write("D\3\2\2\2\u0177\u0178\7C\2\2\u0178\u0179\7t\2\2\u0179")
        buf.write("\u017a\7t\2\2\u017a\u017b\7c\2\2\u017b\u017c\7{\2\2\u017c")
        buf.write("F\3\2\2\2\u017d\u017e\7U\2\2\u017e\u017f\7g\2\2\u017f")
        buf.write("\u0180\7n\2\2\u0180\u0181\7h\2\2\u0181H\3\2\2\2\u0182")
        buf.write("\u0183\7T\2\2\u0183\u0184\7g\2\2\u0184\u0185\7v\2\2\u0185")
        buf.write("\u0186\7w\2\2\u0186\u0187\7t\2\2\u0187\u0188\7p\2\2\u0188")
        buf.write("J\3\2\2\2\u0189\u018a\7P\2\2\u018a\u018b\7g\2\2\u018b")
        buf.write("\u018c\7y\2\2\u018cL\3\2\2\2\u018d\u018e\7K\2\2\u018e")
        buf.write("\u018f\7p\2\2\u018fN\3\2\2\2\u0190\u0191\7E\2\2\u0191")
        buf.write("\u0192\7n\2\2\u0192\u0193\7c\2\2\u0193\u0194\7u\2\2\u0194")
        buf.write("\u0195\7u\2\2\u0195P\3\2\2\2\u0196\u0197\7E\2\2\u0197")
        buf.write("\u0198\7q\2\2\u0198\u0199\7p\2\2\u0199\u019a\7u\2\2\u019a")
        buf.write("\u019b\7v\2\2\u019b\u019c\7t\2\2\u019c\u019d\7w\2\2\u019d")
        buf.write("\u019e\7e\2\2\u019e\u019f\7v\2\2\u019f\u01a0\7q\2\2\u01a0")
        buf.write("\u01a1\7t\2\2\u01a1R\3\2\2\2\u01a2\u01a3\7F\2\2\u01a3")
        buf.write("\u01a4\7g\2\2\u01a4\u01a5\7u\2\2\u01a5\u01a6\7v\2\2\u01a6")
        buf.write("\u01a7\7t\2\2\u01a7\u01a8\7w\2\2\u01a8\u01a9\7e\2\2\u01a9")
        buf.write("\u01aa\7v\2\2\u01aa\u01ab\7q\2\2\u01ab\u01ac\7t\2\2\u01ac")
        buf.write("T\3\2\2\2\u01ad\u01ae\7D\2\2\u01ae\u01af\7{\2\2\u01af")
        buf.write("V\3\2\2\2\u01b0\u01b1\7*\2\2\u01b1X\3\2\2\2\u01b2\u01b3")
        buf.write("\7+\2\2\u01b3Z\3\2\2\2\u01b4\u01b5\7]\2\2\u01b5\\\3\2")
        buf.write("\2\2\u01b6\u01b7\7_\2\2\u01b7^\3\2\2\2\u01b8\u01b9\7\60")
        buf.write("\2\2\u01b9\u01ba\7\60\2\2\u01ba`\3\2\2\2\u01bb\u01bc\7")
        buf.write("\60\2\2\u01bcb\3\2\2\2\u01bd\u01be\7.\2\2\u01bed\3\2\2")
        buf.write("\2\u01bf\u01c0\7=\2\2\u01c0f\3\2\2\2\u01c1\u01c2\7}\2")
        buf.write("\2\u01c2h\3\2\2\2\u01c3\u01c4\7\177\2\2\u01c4j\3\2\2\2")
        buf.write("\u01c5\u01c6\7<\2\2\u01c6\u01c7\7<\2\2\u01c7l\3\2\2\2")
        buf.write("\u01c8\u01c9\7<\2\2\u01c9n\3\2\2\2\u01ca\u01ce\7$\2\2")
        buf.write("\u01cb\u01cd\5\u00b5[\2\u01cc\u01cb\3\2\2\2\u01cd\u01d0")
        buf.write("\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d2\7$\2\2")
        buf.write("\u01d2\u01d3\b8\3\2\u01d3p\3\2\2\2\u01d4\u01d5\t\5\2\2")
        buf.write("\u01d5r\3\2\2\2\u01d6\u01d7\t\6\2\2\u01d7t\3\2\2\2\u01d8")
        buf.write("\u01df\t\4\2\2\u01d9\u01db\7a\2\2\u01da\u01d9\3\2\2\2")
        buf.write("\u01da\u01db\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01de\t")
        buf.write("\4\2\2\u01dd\u01da\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd")
        buf.write("\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0v\3\2\2\2\u01e1\u01df")
        buf.write("\3\2\2\2\u01e2\u01e6\5a\61\2\u01e3\u01e5\5\31\r\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3\2\2\2")
        buf.write("\u01e6\u01e7\3\2\2\2\u01e7x\3\2\2\2\u01e8\u01e6\3\2\2")
        buf.write("\2\u01e9\u01eb\5q9\2\u01ea\u01ec\5s:\2\u01eb\u01ea\3\2")
        buf.write("\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ee\3\2\2\2\u01ed\u01ef")
        buf.write("\5\31\r\2\u01ee\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1z\3\2\2\2\u01f2")
        buf.write("\u01f3\5u;\2\u01f3\u01f4\5w<\2\u01f4\u01f5\5y=\2\u01f5")
        buf.write("\u0200\3\2\2\2\u01f6\u01f7\5u;\2\u01f7\u01f8\5w<\2\u01f8")
        buf.write("\u0200\3\2\2\2\u01f9\u01fa\5u;\2\u01fa\u01fb\5y=\2\u01fb")
        buf.write("\u0200\3\2\2\2\u01fc\u01fd\5w<\2\u01fd\u01fe\5y=\2\u01fe")
        buf.write("\u0200\3\2\2\2\u01ff\u01f2\3\2\2\2\u01ff\u01f6\3\2\2\2")
        buf.write("\u01ff\u01f9\3\2\2\2\u01ff\u01fc\3\2\2\2\u0200\u0201\3")
        buf.write("\2\2\2\u0201\u0202\b>\4\2\u0202|\3\2\2\2\u0203\u0204\t")
        buf.write("\7\2\2\u0204~\3\2\2\2\u0205\u0206\t\b\2\2\u0206\u0080")
        buf.write("\3\2\2\2\u0207\u0209\7\62\2\2\u0208\u020a\t\t\2\2\u0209")
        buf.write("\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u0209\3\2\2\2")
        buf.write("\u020b\u020c\3\2\2\2\u020c\u0082\3\2\2\2\u020d\u0214\t")
        buf.write("\n\2\2\u020e\u0210\7a\2\2\u020f\u020e\3\2\2\2\u020f\u0210")
        buf.write("\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0213\t\4\2\2\u0212")
        buf.write("\u020f\3\2\2\2\u0213\u0216\3\2\2\2\u0214\u0212\3\2\2\2")
        buf.write("\u0214\u0215\3\2\2\2\u0215\u0219\3\2\2\2\u0216\u0214\3")
        buf.write("\2\2\2\u0217\u0219\7\62\2\2\u0218\u020d\3\2\2\2\u0218")
        buf.write("\u0217\3\2\2\2\u0219\u0084\3\2\2\2\u021a\u021b\7\62\2")
        buf.write("\2\u021b\u021d\5}?\2\u021c\u021e\t\13\2\2\u021d\u021c")
        buf.write("\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u021d\3\2\2\2\u021f")
        buf.write("\u0220\3\2\2\2\u0220\u0086\3\2\2\2\u0221\u0222\7\62\2")
        buf.write("\2\u0222\u0224\5\177@\2\u0223\u0225\t\f\2\2\u0224\u0223")
        buf.write("\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0224\3\2\2\2\u0226")
        buf.write("\u0227\3\2\2\2\u0227\u0088\3\2\2\2\u0228\u022d\5\u0083")
        buf.write("B\2\u0229\u022d\5\u0085C\2\u022a\u022d\5\u0081A\2\u022b")
        buf.write("\u022d\5\u0087D\2\u022c\u0228\3\2\2\2\u022c\u0229\3\2")
        buf.write("\2\2\u022c\u022a\3\2\2\2\u022c\u022b\3\2\2\2\u022d\u022e")
        buf.write("\3\2\2\2\u022e\u022f\bE\5\2\u022f\u008a\3\2\2\2\u0230")
        buf.write("\u0233\5\63\32\2\u0231\u0233\5\65\33\2\u0232\u0230\3\2")
        buf.write("\2\2\u0232\u0231\3\2\2\2\u0233\u008c\3\2\2\2\u0234\u0235")
        buf.write("\7#\2\2\u0235\u008e\3\2\2\2\u0236\u0237\7(\2\2\u0237\u0238")
        buf.write("\7(\2\2\u0238\u0090\3\2\2\2\u0239\u023a\7~\2\2\u023a\u023b")
        buf.write("\7~\2\2\u023b\u0092\3\2\2\2\u023c\u023d\7?\2\2\u023d\u023e")
        buf.write("\7?\2\2\u023e\u0094\3\2\2\2\u023f\u0240\7#\2\2\u0240\u0241")
        buf.write("\7?\2\2\u0241\u0096\3\2\2\2\u0242\u0243\7-\2\2\u0243\u0098")
        buf.write("\3\2\2\2\u0244\u0245\7/\2\2\u0245\u009a\3\2\2\2\u0246")
        buf.write("\u0247\7,\2\2\u0247\u009c\3\2\2\2\u0248\u0249\7\61\2\2")
        buf.write("\u0249\u009e\3\2\2\2\u024a\u024b\7\'\2\2\u024b\u00a0\3")
        buf.write("\2\2\2\u024c\u024d\7@\2\2\u024d\u00a2\3\2\2\2\u024e\u024f")
        buf.write("\7@\2\2\u024f\u0250\7?\2\2\u0250\u00a4\3\2\2\2\u0251\u0252")
        buf.write("\7>\2\2\u0252\u00a6\3\2\2\2\u0253\u0254\7>\2\2\u0254\u0255")
        buf.write("\7?\2\2\u0255\u00a8\3\2\2\2\u0256\u0257\7-\2\2\u0257\u0258")
        buf.write("\7\60\2\2\u0258\u00aa\3\2\2\2\u0259\u025a\7?\2\2\u025a")
        buf.write("\u025b\7?\2\2\u025b\u025c\7\60\2\2\u025c\u00ac\3\2\2\2")
        buf.write("\u025d\u025e\7?\2\2\u025e\u00ae\3\2\2\2\u025f\u0261\t")
        buf.write("\r\2\2\u0260\u025f\3\2\2\2\u0261\u0262\3\2\2\2\u0262\u0260")
        buf.write("\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0264\3\2\2\2\u0264")
        buf.write("\u0265\bX\2\2\u0265\u00b0\3\2\2\2\u0266\u0269\5\27\f\2")
        buf.write("\u0267\u0269\5\33\16\2\u0268\u0266\3\2\2\2\u0268\u0267")
        buf.write("\3\2\2\2\u0269\u026f\3\2\2\2\u026a\u026e\5\33\16\2\u026b")
        buf.write("\u026e\5\27\f\2\u026c\u026e\5\31\r\2\u026d\u026a\3\2\2")
        buf.write("\2\u026d\u026b\3\2\2\2\u026d\u026c\3\2\2\2\u026e\u0271")
        buf.write("\3\2\2\2\u026f\u026d\3\2\2\2\u026f\u0270\3\2\2\2\u0270")
        buf.write("\u00b2\3\2\2\2\u0271\u026f\3\2\2\2\u0272\u0274\5\37\20")
        buf.write("\2\u0273\u0275\t\16\2\2\u0274\u0273\3\2\2\2\u0275\u0276")
        buf.write("\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2\u0277")
        buf.write("\u00b4\3\2\2\2\u0278\u027b\n\17\2\2\u0279\u027b\5\u00b7")
        buf.write("\\\2\u027a\u0278\3\2\2\2\u027a\u0279\3\2\2\2\u027b\u00b6")
        buf.write("\3\2\2\2\u027c\u027d\7^\2\2\u027d\u0281\t\20\2\2\u027e")
        buf.write("\u027f\7)\2\2\u027f\u0281\7$\2\2\u0280\u027c\3\2\2\2\u0280")
        buf.write("\u027e\3\2\2\2\u0281\u00b8\3\2\2\2\u0282\u0283\7^\2\2")
        buf.write("\u0283\u0287\n\20\2\2\u0284\u0285\7)\2\2\u0285\u0287\n")
        buf.write("\21\2\2\u0286\u0282\3\2\2\2\u0286\u0284\3\2\2\2\u0287")
        buf.write("\u00ba\3\2\2\2\u0288\u028c\7$\2\2\u0289\u028b\5\u00b5")
        buf.write("[\2\u028a\u0289\3\2\2\2\u028b\u028e\3\2\2\2\u028c\u028a")
        buf.write("\3\2\2\2\u028c\u028d\3\2\2\2\u028d\u028f\3\2\2\2\u028e")
        buf.write("\u028c\3\2\2\2\u028f\u0290\5\u00b9]\2\u0290\u0291\b^\6")
        buf.write("\2\u0291\u00bc\3\2\2\2\u0292\u0296\7$\2\2\u0293\u0295")
        buf.write("\5\u00b5[\2\u0294\u0293\3\2\2\2\u0295\u0298\3\2\2\2\u0296")
        buf.write("\u0294\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u0299\3\2\2\2")
        buf.write("\u0298\u0296\3\2\2\2\u0299\u029a\b_\7\2\u029a\u00be\3")
        buf.write("\2\2\2\u029b\u029c\13\2\2\2\u029c\u029d\b`\b\2\u029d\u00c0")
        buf.write("\3\2\2\2\36\2\u0105\u0110\u01ce\u01da\u01df\u01e6\u01eb")
        buf.write("\u01f0\u01ff\u020b\u020f\u0214\u0218\u021f\u0226\u022c")
        buf.write("\u0232\u0262\u0268\u026d\u026f\u0276\u027a\u0280\u0286")
        buf.write("\u028c\u0296\t\b\2\2\38\2\3>\3\3E\4\3^\5\3_\6\3`\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    COMMENT = 9
    INTTYPE = 10
    VOIDTYPE = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSEIF = 15
    ELSE = 16
    FOREACH = 17
    TRUE = 18
    FALSE = 19
    FLOAT = 20
    BOOLEAN = 21
    STRING = 22
    INT = 23
    NULL = 24
    VAR = 25
    VAL = 26
    ARRAY = 27
    SELF = 28
    RETURN = 29
    NEW = 30
    IN = 31
    CLASS = 32
    CONSTRUCTOR = 33
    DESTRUCTOR = 34
    BY = 35
    LB = 36
    RB = 37
    LSB = 38
    RSB = 39
    DOUBLE_DOT = 40
    DOT = 41
    COMMA = 42
    SEMI = 43
    LP = 44
    RP = 45
    DOUBLE_COLON = 46
    COLON = 47
    STRING_LIT = 48
    FLOAT_LIT = 49
    INT_LIT = 50
    BOOLEAN_LIT = 51
    NOT = 52
    AND = 53
    OR = 54
    IS_EQUAL = 55
    NOT_EQUAL = 56
    ADD = 57
    SUB = 58
    MULTIPLY = 59
    DIV = 60
    MOD = 61
    GT = 62
    GTE = 63
    LT = 64
    LTE = 65
    ADD_STR = 66
    IS_EQUAL_STR = 67
    EQUAL = 68
    WS = 69
    ID = 70
    STATIC_ID = 71
    ILLEGAL_ESCAPE = 72
    UNCLOSE_STRING = 73
    ERROR_CHAR = 74

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'asd'", "'asfrth'", "'fd'", "'asdadsasdasdas'", "'sadadsaas'", 
            "'nhanv'", "'hjahaa'", "'hahah'", "'int'", "'void'", "'Break'", 
            "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
            "'False'", "'Float'", "'Boolean'", "'String'", "'Int'", "'Null'", 
            "'Var'", "'Val'", "'Array'", "'Self'", "'Return'", "'New'", 
            "'In'", "'Class'", "'Constructor'", "'Destructor'", "'By'", 
            "'('", "')'", "'['", "']'", "'..'", "'.'", "','", "';'", "'{'", 
            "'}'", "'::'", "':'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", "'>='", "'<'", "'<='", 
            "'+.'", "'==.'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTTYPE", "VOIDTYPE", "BREAK", "CONTINUE", "IF", 
            "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "FLOAT", "BOOLEAN", 
            "STRING", "INT", "NULL", "VAR", "VAL", "ARRAY", "SELF", "RETURN", 
            "NEW", "IN", "CLASS", "CONSTRUCTOR", "DESTRUCTOR", "BY", "LB", 
            "RB", "LSB", "RSB", "DOUBLE_DOT", "DOT", "COMMA", "SEMI", "LP", 
            "RP", "DOUBLE_COLON", "COLON", "STRING_LIT", "FLOAT_LIT", "INT_LIT", 
            "BOOLEAN_LIT", "NOT", "AND", "OR", "IS_EQUAL", "NOT_EQUAL", 
            "ADD", "SUB", "MULTIPLY", "DIV", "MOD", "GT", "GTE", "LT", "LTE", 
            "ADD_STR", "IS_EQUAL_STR", "EQUAL", "WS", "ID", "STATIC_ID", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "UPPERCASE", "LOWERCASE", "UNDERSCORE", "DIGIT", 
                  "LETTER", "DOUBLE_HASHTAG", "DOLLAR", "COMMENT", "INTTYPE", 
                  "VOIDTYPE", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "TRUE", "FALSE", "FLOAT", "BOOLEAN", "STRING", 
                  "INT", "NULL", "VAR", "VAL", "ARRAY", "SELF", "RETURN", 
                  "NEW", "IN", "CLASS", "CONSTRUCTOR", "DESTRUCTOR", "BY", 
                  "LB", "RB", "LSB", "RSB", "DOUBLE_DOT", "DOT", "COMMA", 
                  "SEMI", "LP", "RP", "DOUBLE_COLON", "COLON", "STRING_LIT", 
                  "E", "SIGN", "INTEGER_PART", "DEC_PART", "EXPONENT_PART", 
                  "FLOAT_LIT", "X", "B", "INT_OCT", "INT_DECIMAL", "INT_HEXA", 
                  "INT_BINARY", "INT_LIT", "BOOLEAN_LIT", "NOT", "AND", 
                  "OR", "IS_EQUAL", "NOT_EQUAL", "ADD", "SUB", "MULTIPLY", 
                  "DIV", "MOD", "GT", "GTE", "LT", "LTE", "ADD_STR", "IS_EQUAL_STR", 
                  "EQUAL", "WS", "ID", "STATIC_ID", "CHAR", "ESCAPE", "ILL_ESC", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.STRING_LIT_action 
            actions[60] = self.FLOAT_LIT_action 
            actions[67] = self.INT_LIT_action 
            actions[92] = self.ILLEGAL_ESCAPE_action 
            actions[93] = self.UNCLOSE_STRING_action 
            actions[94] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text[1:-1]

     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = re.sub('_','',self.text)

     

    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = re.sub('_','',self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                string_to_illegal = str(self.text)
                raise IllegalEscape(string_to_illegal[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                raise UncloseString(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                raise ErrorToken(self.text)

     



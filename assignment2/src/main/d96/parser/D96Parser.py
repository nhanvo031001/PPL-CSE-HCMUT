# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0255\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\6\2|\n\2\r\2\16\2}\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u0086\n\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\7\5\u008f")
        buf.write("\n\5\f\5\16\5\u0092\13\5\3\6\3\6\3\6\3\6\5\6\u0098\n\6")
        buf.write("\3\7\3\7\3\7\5\7\u009d\n\7\3\7\3\7\3\7\3\b\3\b\3\b\7\b")
        buf.write("\u00a5\n\b\f\b\16\b\u00a8\13\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\7\n\u00b1\n\n\f\n\16\n\u00b4\13\n\3\13\3\13\3\13")
        buf.write("\5\13\u00b9\n\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\5\16\u00c6\n\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\5\22\u00d4\n\22\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00e3\n\23\3\24\3\24\3\24\3\24\3\24\3\24\7")
        buf.write("\24\u00eb\n\24\f\24\16\24\u00ee\13\24\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\7\26\u00f9\n\26\f\26\16\26")
        buf.write("\u00fc\13\26\3\26\3\26\3\27\3\27\7\27\u0102\n\27\f\27")
        buf.write("\16\27\u0105\13\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u0112\n\30\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u011e\n\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\7\32\u0125\n\32\f\32\16\32\u0128")
        buf.write("\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0131\n")
        buf.write("\33\f\33\16\33\u0134\13\33\3\33\3\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u0147\n\35\3\36\3\36\3\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\7\37\u0152\n\37\f\37\16\37\u0155\13\37\3")
        buf.write("\37\5\37\u0158\n\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u016c\n\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3$\3$\3$\3%\3%\5%\u0179\n%\3%\3%\3&\3&\5&\u017f")
        buf.write("\n&\3&\3&\3\'\3\'\3\'\3\'\3\'\5\'\u0188\n\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3(\5(\u0191\n(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\5)\u01a0\n)\3)\7)\u01a3\n)\f)\16)\u01a6\13")
        buf.write(")\3*\3*\3*\3*\3*\5*\u01ad\n*\3+\3+\3+\3+\3+\5+\u01b4\n")
        buf.write("+\3,\3,\3,\3,\3,\3,\7,\u01bc\n,\f,\16,\u01bf\13,\3-\3")
        buf.write("-\3-\3-\3-\3-\7-\u01c7\n-\f-\16-\u01ca\13-\3.\3.\3.\3")
        buf.write(".\3.\3.\7.\u01d2\n.\f.\16.\u01d5\13.\3/\3/\3/\5/\u01da")
        buf.write("\n/\3\60\3\60\3\60\5\60\u01df\n\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\7\61\u01e6\n\61\f\61\16\61\u01e9\13\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u01f6")
        buf.write("\n\62\3\62\7\62\u01f9\n\62\f\62\16\62\u01fc\13\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u0206\n\63\3")
        buf.write("\63\3\63\5\63\u020a\n\63\3\64\3\64\3\64\3\64\5\64\u0210")
        buf.write("\n\64\3\64\3\64\5\64\u0214\n\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\5\65\u021e\n\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\5\66\u0226\n\66\3\67\3\67\38\38\58\u022c\n")
        buf.write("8\39\39\39\39\39\3:\3:\3:\7:\u0236\n:\f:\16:\u0239\13")
        buf.write(":\3;\3;\3;\5;\u023e\n;\3;\3;\3<\3<\3<\7<\u0245\n<\f<\16")
        buf.write("<\u0248\13<\3=\3=\3=\3=\3=\3=\3=\3=\3=\5=\u0253\n=\3=")
        buf.write("\2\bPVXZ`b>\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvx\2")
        buf.write("\13\3\2\f\17\3\2?@\3\2\21\22\3\2;<\4\2\60\61\67:\3\2.")
        buf.write("/\3\2\62\63\3\2\64\66\3\2\n\13\2\u025f\2{\3\2\2\2\4\u0081")
        buf.write("\3\2\2\2\6\u008b\3\2\2\2\b\u0090\3\2\2\2\n\u0097\3\2\2")
        buf.write("\2\f\u0099\3\2\2\2\16\u00a1\3\2\2\2\20\u00a9\3\2\2\2\22")
        buf.write("\u00ad\3\2\2\2\24\u00b8\3\2\2\2\26\u00ba\3\2\2\2\30\u00bc")
        buf.write("\3\2\2\2\32\u00c5\3\2\2\2\34\u00c7\3\2\2\2\36\u00c9\3")
        buf.write("\2\2\2 \u00cb\3\2\2\2\"\u00d0\3\2\2\2$\u00d8\3\2\2\2&")
        buf.write("\u00e4\3\2\2\2(\u00ef\3\2\2\2*\u00f1\3\2\2\2,\u00ff\3")
        buf.write("\2\2\2.\u0111\3\2\2\2\60\u0113\3\2\2\2\62\u011f\3\2\2")
        buf.write("\2\64\u0129\3\2\2\2\66\u0137\3\2\2\28\u0146\3\2\2\2:\u0148")
        buf.write("\3\2\2\2<\u014b\3\2\2\2>\u0159\3\2\2\2@\u015f\3\2\2\2")
        buf.write("B\u0162\3\2\2\2D\u0170\3\2\2\2F\u0173\3\2\2\2H\u0176\3")
        buf.write("\2\2\2J\u017e\3\2\2\2L\u0182\3\2\2\2N\u018b\3\2\2\2P\u0194")
        buf.write("\3\2\2\2R\u01ac\3\2\2\2T\u01b3\3\2\2\2V\u01b5\3\2\2\2")
        buf.write("X\u01c0\3\2\2\2Z\u01cb\3\2\2\2\\\u01d9\3\2\2\2^\u01de")
        buf.write("\3\2\2\2`\u01e0\3\2\2\2b\u01ea\3\2\2\2d\u0209\3\2\2\2")
        buf.write("f\u0213\3\2\2\2h\u021d\3\2\2\2j\u0225\3\2\2\2l\u0227\3")
        buf.write("\2\2\2n\u022b\3\2\2\2p\u022d\3\2\2\2r\u0232\3\2\2\2t\u023a")
        buf.write("\3\2\2\2v\u0241\3\2\2\2x\u0252\3\2\2\2z|\5\4\3\2{z\3\2")
        buf.write("\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0080")
        buf.write("\7\2\2\3\u0080\3\3\2\2\2\u0081\u0082\7\30\2\2\u0082\u0085")
        buf.write("\5\6\4\2\u0083\u0084\7\'\2\2\u0084\u0086\7?\2\2\u0085")
        buf.write("\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\3\2\2\2")
        buf.write("\u0087\u0088\7$\2\2\u0088\u0089\5\b\5\2\u0089\u008a\7")
        buf.write("%\2\2\u008a\5\3\2\2\2\u008b\u008c\7?\2\2\u008c\7\3\2\2")
        buf.write("\2\u008d\u008f\5\n\6\2\u008e\u008d\3\2\2\2\u008f\u0092")
        buf.write("\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\t\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0098\5\f\7\2\u0094")
        buf.write("\u0098\5 \21\2\u0095\u0098\5\"\22\2\u0096\u0098\5$\23")
        buf.write("\2\u0097\u0093\3\2\2\2\u0097\u0094\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0097\u0096\3\2\2\2\u0098\13\3\2\2\2\u0099\u009a")
        buf.write("\7\31\2\2\u009a\u009c\7\34\2\2\u009b\u009d\5\16\b\2\u009c")
        buf.write("\u009b\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\u009f\7\35\2\2\u009f\u00a0\5,\27\2\u00a0\r\3\2")
        buf.write("\2\2\u00a1\u00a6\5\20\t\2\u00a2\u00a3\7#\2\2\u00a3\u00a5")
        buf.write("\5\20\t\2\u00a4\u00a2\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\17\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a9\u00aa\5\22\n\2\u00aa\u00ab\7\'\2")
        buf.write("\2\u00ab\u00ac\5\24\13\2\u00ac\21\3\2\2\2\u00ad\u00b2")
        buf.write("\7?\2\2\u00ae\u00af\7\"\2\2\u00af\u00b1\7?\2\2\u00b0\u00ae")
        buf.write("\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\23\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5")
        buf.write("\u00b9\5\26\f\2\u00b6\u00b9\5\30\r\2\u00b7\u00b9\5\36")
        buf.write("\20\2\u00b8\u00b5\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7")
        buf.write("\3\2\2\2\u00b9\25\3\2\2\2\u00ba\u00bb\t\2\2\2\u00bb\27")
        buf.write("\3\2\2\2\u00bc\u00bd\7\23\2\2\u00bd\u00be\7\36\2\2\u00be")
        buf.write("\u00bf\5\32\16\2\u00bf\u00c0\7\"\2\2\u00c0\u00c1\5\34")
        buf.write("\17\2\u00c1\u00c2\7\37\2\2\u00c2\31\3\2\2\2\u00c3\u00c6")
        buf.write("\5\26\f\2\u00c4\u00c6\5\30\r\2\u00c5\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c4\3\2\2\2\u00c6\33\3\2\2\2\u00c7\u00c8\7*\2\2\u00c8")
        buf.write("\35\3\2\2\2\u00c9\u00ca\7?\2\2\u00ca\37\3\2\2\2\u00cb")
        buf.write("\u00cc\7\32\2\2\u00cc\u00cd\7\34\2\2\u00cd\u00ce\7\35")
        buf.write("\2\2\u00ce\u00cf\5,\27\2\u00cf!\3\2\2\2\u00d0\u00d1\t")
        buf.write("\3\2\2\u00d1\u00d3\7\34\2\2\u00d2\u00d4\5\16\b\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\u00d6\7\35\2\2\u00d6\u00d7\5,\27\2\u00d7#\3\2\2")
        buf.write("\2\u00d8\u00d9\t\4\2\2\u00d9\u00da\5&\24\2\u00da\u00db")
        buf.write("\7\'\2\2\u00db\u00e2\5\24\13\2\u00dc\u00dd\7=\2\2\u00dd")
        buf.write("\u00de\5*\26\2\u00de\u00df\6\23\2\3\u00df\u00e0\7#\2\2")
        buf.write("\u00e0\u00e3\3\2\2\2\u00e1\u00e3\7#\2\2\u00e2\u00dc\3")
        buf.write("\2\2\2\u00e2\u00e1\3\2\2\2\u00e3%\3\2\2\2\u00e4\u00e5")
        buf.write("\5(\25\2\u00e5\u00ec\b\24\1\2\u00e6\u00e7\7\"\2\2\u00e7")
        buf.write("\u00e8\5(\25\2\u00e8\u00e9\b\24\1\2\u00e9\u00eb\3\2\2")
        buf.write("\2\u00ea\u00e6\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea")
        buf.write("\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\'\3\2\2\2\u00ee\u00ec")
        buf.write("\3\2\2\2\u00ef\u00f0\t\3\2\2\u00f0)\3\2\2\2\u00f1\u00f2")
        buf.write("\5R*\2\u00f2\u00fa\b\26\1\2\u00f3\u00f4\6\26\3\3\u00f4")
        buf.write("\u00f5\7\"\2\2\u00f5\u00f6\5R*\2\u00f6\u00f7\b\26\1\2")
        buf.write("\u00f7\u00f9\3\2\2\2\u00f8\u00f3\3\2\2\2\u00f9\u00fc\3")
        buf.write("\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fd")
        buf.write("\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe\b\26\1\2\u00fe")
        buf.write("+\3\2\2\2\u00ff\u0103\7$\2\2\u0100\u0102\5.\30\2\u0101")
        buf.write("\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2")
        buf.write("\u0103\u0104\3\2\2\2\u0104\u0106\3\2\2\2\u0105\u0103\3")
        buf.write("\2\2\2\u0106\u0107\7%\2\2\u0107-\3\2\2\2\u0108\u0112\5")
        buf.write("\60\31\2\u0109\u0112\5\66\34\2\u010a\u0112\5<\37\2\u010b")
        buf.write("\u0112\5B\"\2\u010c\u0112\5D#\2\u010d\u0112\5F$\2\u010e")
        buf.write("\u0112\5H%\2\u010f\u0112\5J&\2\u0110\u0112\5,\27\2\u0111")
        buf.write("\u0108\3\2\2\2\u0111\u0109\3\2\2\2\u0111\u010a\3\2\2\2")
        buf.write("\u0111\u010b\3\2\2\2\u0111\u010c\3\2\2\2\u0111\u010d\3")
        buf.write("\2\2\2\u0111\u010e\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0110")
        buf.write("\3\2\2\2\u0112/\3\2\2\2\u0113\u0114\t\4\2\2\u0114\u0115")
        buf.write("\5\62\32\2\u0115\u0116\7\'\2\2\u0116\u011d\5\24\13\2\u0117")
        buf.write("\u0118\7=\2\2\u0118\u0119\5\64\33\2\u0119\u011a\6\31\4")
        buf.write("\3\u011a\u011b\7#\2\2\u011b\u011e\3\2\2\2\u011c\u011e")
        buf.write("\7#\2\2\u011d\u0117\3\2\2\2\u011d\u011c\3\2\2\2\u011e")
        buf.write("\61\3\2\2\2\u011f\u0120\7?\2\2\u0120\u0126\b\32\1\2\u0121")
        buf.write("\u0122\7\"\2\2\u0122\u0123\7?\2\2\u0123\u0125\b\32\1\2")
        buf.write("\u0124\u0121\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3")
        buf.write("\2\2\2\u0126\u0127\3\2\2\2\u0127\63\3\2\2\2\u0128\u0126")
        buf.write("\3\2\2\2\u0129\u012a\5R*\2\u012a\u0132\b\33\1\2\u012b")
        buf.write("\u012c\6\33\5\3\u012c\u012d\7\"\2\2\u012d\u012e\5R*\2")
        buf.write("\u012e\u012f\b\33\1\2\u012f\u0131\3\2\2\2\u0130\u012b")
        buf.write("\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132")
        buf.write("\u0133\3\2\2\2\u0133\u0135\3\2\2\2\u0134\u0132\3\2\2\2")
        buf.write("\u0135\u0136\b\33\1\2\u0136\65\3\2\2\2\u0137\u0138\58")
        buf.write("\35\2\u0138\u0139\7=\2\2\u0139\u013a\5R*\2\u013a\u013b")
        buf.write("\7#\2\2\u013b\67\3\2\2\2\u013c\u0147\7?\2\2\u013d\u013e")
        buf.write("\5\6\4\2\u013e\u013f\7&\2\2\u013f\u0140\7@\2\2\u0140\u0147")
        buf.write("\3\2\2\2\u0141\u0142\5b\62\2\u0142\u0143\7!\2\2\u0143")
        buf.write("\u0144\7?\2\2\u0144\u0147\3\2\2\2\u0145\u0147\5:\36\2")
        buf.write("\u0146\u013c\3\2\2\2\u0146\u013d\3\2\2\2\u0146\u0141\3")
        buf.write("\2\2\2\u0146\u0145\3\2\2\2\u01479\3\2\2\2\u0148\u0149")
        buf.write("\5b\62\2\u0149\u014a\5x=\2\u014a;\3\2\2\2\u014b\u014c")
        buf.write("\7\6\2\2\u014c\u014d\7\34\2\2\u014d\u014e\5R*\2\u014e")
        buf.write("\u014f\7\35\2\2\u014f\u0153\5,\27\2\u0150\u0152\5> \2")
        buf.write("\u0151\u0150\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3")
        buf.write("\2\2\2\u0153\u0154\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153")
        buf.write("\3\2\2\2\u0156\u0158\5@!\2\u0157\u0156\3\2\2\2\u0157\u0158")
        buf.write("\3\2\2\2\u0158=\3\2\2\2\u0159\u015a\7\7\2\2\u015a\u015b")
        buf.write("\7\34\2\2\u015b\u015c\5R*\2\u015c\u015d\7\35\2\2\u015d")
        buf.write("\u015e\5,\27\2\u015e?\3\2\2\2\u015f\u0160\7\b\2\2\u0160")
        buf.write("\u0161\5,\27\2\u0161A\3\2\2\2\u0162\u0163\7\t\2\2\u0163")
        buf.write("\u0164\7\34\2\2\u0164\u0165\7?\2\2\u0165\u0166\7\27\2")
        buf.write("\2\u0166\u0167\5R*\2\u0167\u0168\7 \2\2\u0168\u016b\5")
        buf.write("R*\2\u0169\u016a\7\33\2\2\u016a\u016c\5R*\2\u016b\u0169")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016e\7\35\2\2\u016e\u016f\5,\27\2\u016fC\3\2\2\2\u0170")
        buf.write("\u0171\7\4\2\2\u0171\u0172\7#\2\2\u0172E\3\2\2\2\u0173")
        buf.write("\u0174\7\5\2\2\u0174\u0175\7#\2\2\u0175G\3\2\2\2\u0176")
        buf.write("\u0178\7\25\2\2\u0177\u0179\5R*\2\u0178\u0177\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017b\7")
        buf.write("#\2\2\u017bI\3\2\2\2\u017c\u017f\5L\'\2\u017d\u017f\5")
        buf.write("N(\2\u017e\u017c\3\2\2\2\u017e\u017d\3\2\2\2\u017f\u0180")
        buf.write("\3\2\2\2\u0180\u0181\7#\2\2\u0181K\3\2\2\2\u0182\u0183")
        buf.write("\5\6\4\2\u0183\u0184\7&\2\2\u0184\u0185\7@\2\2\u0185\u0187")
        buf.write("\7\34\2\2\u0186\u0188\5v<\2\u0187\u0186\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\7\35\2")
        buf.write("\2\u018aM\3\2\2\2\u018b\u018c\5P)\2\u018c\u018d\7!\2\2")
        buf.write("\u018d\u018e\7?\2\2\u018e\u0190\7\34\2\2\u018f\u0191\5")
        buf.write("v<\2\u0190\u018f\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0192")
        buf.write("\3\2\2\2\u0192\u0193\7\35\2\2\u0193O\3\2\2\2\u0194\u0195")
        buf.write("\b)\1\2\u0195\u0196\5d\63\2\u0196\u01a4\3\2\2\2\u0197")
        buf.write("\u0198\f\5\2\2\u0198\u0199\7!\2\2\u0199\u01a3\7?\2\2\u019a")
        buf.write("\u019b\f\4\2\2\u019b\u019c\7!\2\2\u019c\u019d\7?\2\2\u019d")
        buf.write("\u019f\7\34\2\2\u019e\u01a0\5v<\2\u019f\u019e\3\2\2\2")
        buf.write("\u019f\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a3\7")
        buf.write("\35\2\2\u01a2\u0197\3\2\2\2\u01a2\u019a\3\2\2\2\u01a3")
        buf.write("\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5Q\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a8\5T+\2")
        buf.write("\u01a8\u01a9\t\5\2\2\u01a9\u01aa\5T+\2\u01aa\u01ad\3\2")
        buf.write("\2\2\u01ab\u01ad\5T+\2\u01ac\u01a7\3\2\2\2\u01ac\u01ab")
        buf.write("\3\2\2\2\u01adS\3\2\2\2\u01ae\u01af\5V,\2\u01af\u01b0")
        buf.write("\t\6\2\2\u01b0\u01b1\5V,\2\u01b1\u01b4\3\2\2\2\u01b2\u01b4")
        buf.write("\5V,\2\u01b3\u01ae\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4U")
        buf.write("\3\2\2\2\u01b5\u01b6\b,\1\2\u01b6\u01b7\5X-\2\u01b7\u01bd")
        buf.write("\3\2\2\2\u01b8\u01b9\f\4\2\2\u01b9\u01ba\t\7\2\2\u01ba")
        buf.write("\u01bc\5X-\2\u01bb\u01b8\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01beW\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01c0\u01c1\b-\1\2\u01c1\u01c2\5Z.\2\u01c2")
        buf.write("\u01c8\3\2\2\2\u01c3\u01c4\f\4\2\2\u01c4\u01c5\t\b\2\2")
        buf.write("\u01c5\u01c7\5Z.\2\u01c6\u01c3\3\2\2\2\u01c7\u01ca\3\2")
        buf.write("\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9Y\3")
        buf.write("\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\b.\1\2\u01cc\u01cd")
        buf.write("\5\\/\2\u01cd\u01d3\3\2\2\2\u01ce\u01cf\f\4\2\2\u01cf")
        buf.write("\u01d0\t\t\2\2\u01d0\u01d2\5\\/\2\u01d1\u01ce\3\2\2\2")
        buf.write("\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3")
        buf.write("\2\2\2\u01d4[\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7")
        buf.write("\7-\2\2\u01d7\u01da\5\\/\2\u01d8\u01da\5^\60\2\u01d9\u01d6")
        buf.write("\3\2\2\2\u01d9\u01d8\3\2\2\2\u01da]\3\2\2\2\u01db\u01dc")
        buf.write("\7\63\2\2\u01dc\u01df\5^\60\2\u01dd\u01df\5`\61\2\u01de")
        buf.write("\u01db\3\2\2\2\u01de\u01dd\3\2\2\2\u01df_\3\2\2\2\u01e0")
        buf.write("\u01e1\b\61\1\2\u01e1\u01e2\5b\62\2\u01e2\u01e7\3\2\2")
        buf.write("\2\u01e3\u01e4\f\4\2\2\u01e4\u01e6\5x=\2\u01e5\u01e3\3")
        buf.write("\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8")
        buf.write("\3\2\2\2\u01e8a\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01eb")
        buf.write("\b\62\1\2\u01eb\u01ec\5d\63\2\u01ec\u01fa\3\2\2\2\u01ed")
        buf.write("\u01ee\f\5\2\2\u01ee\u01ef\7!\2\2\u01ef\u01f9\7?\2\2\u01f0")
        buf.write("\u01f1\f\4\2\2\u01f1\u01f2\7!\2\2\u01f2\u01f3\7?\2\2\u01f3")
        buf.write("\u01f5\7\34\2\2\u01f4\u01f6\5v<\2\u01f5\u01f4\3\2\2\2")
        buf.write("\u01f5\u01f6\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f9\7")
        buf.write("\35\2\2\u01f8\u01ed\3\2\2\2\u01f8\u01f0\3\2\2\2\u01f9")
        buf.write("\u01fc\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2")
        buf.write("\u01fbc\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd\u01fe\7?\2\2")
        buf.write("\u01fe\u01ff\7&\2\2\u01ff\u020a\7@\2\2\u0200\u0201\7?")
        buf.write("\2\2\u0201\u0202\7&\2\2\u0202\u0203\7@\2\2\u0203\u0205")
        buf.write("\7\34\2\2\u0204\u0206\5v<\2\u0205\u0204\3\2\2\2\u0205")
        buf.write("\u0206\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u020a\7\35\2")
        buf.write("\2\u0208\u020a\5f\64\2\u0209\u01fd\3\2\2\2\u0209\u0200")
        buf.write("\3\2\2\2\u0209\u0208\3\2\2\2\u020ae\3\2\2\2\u020b\u020c")
        buf.write("\7\26\2\2\u020c\u020d\7?\2\2\u020d\u020f\7\34\2\2\u020e")
        buf.write("\u0210\5v<\2\u020f\u020e\3\2\2\2\u020f\u0210\3\2\2\2\u0210")
        buf.write("\u0211\3\2\2\2\u0211\u0214\7\35\2\2\u0212\u0214\5h\65")
        buf.write("\2\u0213\u020b\3\2\2\2\u0213\u0212\3\2\2\2\u0214g\3\2")
        buf.write("\2\2\u0215\u021e\7?\2\2\u0216\u0217\7\34\2\2\u0217\u0218")
        buf.write("\5R*\2\u0218\u0219\7\35\2\2\u0219\u021e\3\2\2\2\u021a")
        buf.write("\u021e\5j\66\2\u021b\u021e\7\24\2\2\u021c\u021e\7\20\2")
        buf.write("\2\u021d\u0215\3\2\2\2\u021d\u0216\3\2\2\2\u021d\u021a")
        buf.write("\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021c\3\2\2\2\u021e")
        buf.write("i\3\2\2\2\u021f\u0226\7,\2\2\u0220\u0226\7*\2\2\u0221")
        buf.write("\u0226\7)\2\2\u0222\u0226\7(\2\2\u0223\u0226\5l\67\2\u0224")
        buf.write("\u0226\5n8\2\u0225\u021f\3\2\2\2\u0225\u0220\3\2\2\2\u0225")
        buf.write("\u0221\3\2\2\2\u0225\u0222\3\2\2\2\u0225\u0223\3\2\2\2")
        buf.write("\u0225\u0224\3\2\2\2\u0226k\3\2\2\2\u0227\u0228\t\n\2")
        buf.write("\2\u0228m\3\2\2\2\u0229\u022c\5p9\2\u022a\u022c\5t;\2")
        buf.write("\u022b\u0229\3\2\2\2\u022b\u022a\3\2\2\2\u022co\3\2\2")
        buf.write("\2\u022d\u022e\7\23\2\2\u022e\u022f\7\34\2\2\u022f\u0230")
        buf.write("\5r:\2\u0230\u0231\7\35\2\2\u0231q\3\2\2\2\u0232\u0237")
        buf.write("\5n8\2\u0233\u0234\7\"\2\2\u0234\u0236\5n8\2\u0235\u0233")
        buf.write("\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238s\3\2\2\2\u0239\u0237\3\2\2\2\u023a")
        buf.write("\u023b\7\23\2\2\u023b\u023d\7\34\2\2\u023c\u023e\5v<\2")
        buf.write("\u023d\u023c\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023f\3")
        buf.write("\2\2\2\u023f\u0240\7\35\2\2\u0240u\3\2\2\2\u0241\u0246")
        buf.write("\5R*\2\u0242\u0243\7\"\2\2\u0243\u0245\5R*\2\u0244\u0242")
        buf.write("\3\2\2\2\u0245\u0248\3\2\2\2\u0246\u0244\3\2\2\2\u0246")
        buf.write("\u0247\3\2\2\2\u0247w\3\2\2\2\u0248\u0246\3\2\2\2\u0249")
        buf.write("\u024a\7\36\2\2\u024a\u024b\5R*\2\u024b\u024c\7\37\2\2")
        buf.write("\u024c\u024d\5x=\2\u024d\u0253\3\2\2\2\u024e\u024f\7\36")
        buf.write("\2\2\u024f\u0250\5R*\2\u0250\u0251\7\37\2\2\u0251\u0253")
        buf.write("\3\2\2\2\u0252\u0249\3\2\2\2\u0252\u024e\3\2\2\2\u0253")
        buf.write("y\3\2\2\2\65}\u0085\u0090\u0097\u009c\u00a6\u00b2\u00b8")
        buf.write("\u00c5\u00d3\u00e2\u00ec\u00fa\u0103\u0111\u011d\u0126")
        buf.write("\u0132\u0146\u0153\u0157\u016b\u0178\u017e\u0187\u0190")
        buf.write("\u019f\u01a2\u01a4\u01ac\u01b3\u01bd\u01c8\u01d3\u01d9")
        buf.write("\u01de\u01e7\u01f5\u01f8\u01fa\u0205\u0209\u020f\u0213")
        buf.write("\u021d\u0225\u022b\u0237\u023d\u0246\u0252")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Float'", "'Boolean'", "'String'", "'Int'", 
                     "'Null'", "'Var'", "'Val'", "'Array'", "'Self'", "'Return'", 
                     "'New'", "'In'", "'Class'", "'Constructor'", "'Destructor'", 
                     "'By'", "'('", "')'", "'['", "']'", "'..'", "'.'", 
                     "','", "';'", "'{'", "'}'", "'::'", "':'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'>'", "'>='", "'<'", "'<='", 
                     "'+.'", "'==.'", "'='" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "FLOAT", 
                      "BOOLEAN", "STRING", "INT", "NULL", "VAR", "VAL", 
                      "ARRAY", "SELF", "RETURN", "NEW", "IN", "CLASS", "CONSTRUCTOR", 
                      "DESTRUCTOR", "BY", "LB", "RB", "LSB", "RSB", "DOUBLE_DOT", 
                      "DOT", "COMMA", "SEMI", "LP", "RP", "DOUBLE_COLON", 
                      "COLON", "STRING_LIT", "FLOAT_LIT", "INT_LIT", "BOOLEAN_LIT", 
                      "ZERO_LIT", "NOT", "AND", "OR", "IS_EQUAL", "NOT_EQUAL", 
                      "ADD", "SUB", "MULTIPLY", "DIV", "MOD", "GT", "GTE", 
                      "LT", "LTE", "ADD_STR", "IS_EQUAL_STR", "EQUAL", "WS", 
                      "ID", "STATIC_ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declare = 1
    RULE_name_class = 2
    RULE_body_class = 3
    RULE_mem_class_declare = 4
    RULE_constructor_declare = 5
    RULE_params_list = 6
    RULE_params_declare = 7
    RULE_id_list = 8
    RULE_type_data = 9
    RULE_primitive_type = 10
    RULE_array_type = 11
    RULE_element_type = 12
    RULE_size = 13
    RULE_class_type = 14
    RULE_destructor_declare = 15
    RULE_method_declare = 16
    RULE_attribute_declare = 17
    RULE_variable_name_list = 18
    RULE_id_or_staticID = 19
    RULE_value_list = 20
    RULE_block_stmt = 21
    RULE_stmt = 22
    RULE_variable_and_constant_stmt = 23
    RULE_variable_name_list_in_method = 24
    RULE_value_list_stmt = 25
    RULE_assignment_stmt = 26
    RULE_scalar_variable = 27
    RULE_index_exp_for_scalar_variable = 28
    RULE_if_stmt = 29
    RULE_elseif_block = 30
    RULE_else_block = 31
    RULE_for_in_stmt = 32
    RULE_break_stmt = 33
    RULE_continue_stmt = 34
    RULE_return_stmt = 35
    RULE_method_invocation_stmt = 36
    RULE_static_method_invocation = 37
    RULE_instance_method_invocation = 38
    RULE_pre_exp = 39
    RULE_exp = 40
    RULE_exp1 = 41
    RULE_exp2 = 42
    RULE_exp3 = 43
    RULE_exp4 = 44
    RULE_exp5 = 45
    RULE_exp6 = 46
    RULE_exp7 = 47
    RULE_exp8 = 48
    RULE_exp9 = 49
    RULE_exp10 = 50
    RULE_operands = 51
    RULE_literals = 52
    RULE_boolean_literal = 53
    RULE_array_literal = 54
    RULE_multidimensional_array = 55
    RULE_array_list = 56
    RULE_indexed_array = 57
    RULE_exp_list = 58
    RULE_index_operator = 59

    ruleNames =  [ "program", "class_declare", "name_class", "body_class", 
                   "mem_class_declare", "constructor_declare", "params_list", 
                   "params_declare", "id_list", "type_data", "primitive_type", 
                   "array_type", "element_type", "size", "class_type", "destructor_declare", 
                   "method_declare", "attribute_declare", "variable_name_list", 
                   "id_or_staticID", "value_list", "block_stmt", "stmt", 
                   "variable_and_constant_stmt", "variable_name_list_in_method", 
                   "value_list_stmt", "assignment_stmt", "scalar_variable", 
                   "index_exp_for_scalar_variable", "if_stmt", "elseif_block", 
                   "else_block", "for_in_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_invocation_stmt", "static_method_invocation", 
                   "instance_method_invocation", "pre_exp", "exp", "exp1", 
                   "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", 
                   "exp9", "exp10", "operands", "literals", "boolean_literal", 
                   "array_literal", "multidimensional_array", "array_list", 
                   "indexed_array", "exp_list", "index_operator" ]

    EOF = Token.EOF
    COMMENT=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    FOREACH=7
    TRUE=8
    FALSE=9
    FLOAT=10
    BOOLEAN=11
    STRING=12
    INT=13
    NULL=14
    VAR=15
    VAL=16
    ARRAY=17
    SELF=18
    RETURN=19
    NEW=20
    IN=21
    CLASS=22
    CONSTRUCTOR=23
    DESTRUCTOR=24
    BY=25
    LB=26
    RB=27
    LSB=28
    RSB=29
    DOUBLE_DOT=30
    DOT=31
    COMMA=32
    SEMI=33
    LP=34
    RP=35
    DOUBLE_COLON=36
    COLON=37
    STRING_LIT=38
    FLOAT_LIT=39
    INT_LIT=40
    BOOLEAN_LIT=41
    ZERO_LIT=42
    NOT=43
    AND=44
    OR=45
    IS_EQUAL=46
    NOT_EQUAL=47
    ADD=48
    SUB=49
    MULTIPLY=50
    DIV=51
    MOD=52
    GT=53
    GTE=54
    LT=55
    LTE=56
    ADD_STR=57
    IS_EQUAL_STR=58
    EQUAL=59
    WS=60
    ID=61
    STATIC_ID=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    ERROR_CHAR=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declareContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declareContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 120
                self.class_declare()
                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 125
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def name_class(self):
            return self.getTypedRuleContext(D96Parser.Name_classContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def body_class(self):
            return self.getTypedRuleContext(D96Parser.Body_classContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declare" ):
                return visitor.visitClass_declare(self)
            else:
                return visitor.visitChildren(self)




    def class_declare(self):

        localctx = D96Parser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(D96Parser.CLASS)
            self.state = 128
            self.name_class()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 129
                self.match(D96Parser.COLON)
                self.state = 130
                self.match(D96Parser.ID)


            self.state = 133
            self.match(D96Parser.LP)
            self.state = 134
            self.body_class()
            self.state = 135
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_name_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_class" ):
                return visitor.visitName_class(self)
            else:
                return visitor.visitChildren(self)




    def name_class(self):

        localctx = D96Parser.Name_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_name_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mem_class_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Mem_class_declareContext)
            else:
                return self.getTypedRuleContext(D96Parser.Mem_class_declareContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_body_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_class" ):
                return visitor.visitBody_class(self)
            else:
                return visitor.visitChildren(self)




    def body_class(self):

        localctx = D96Parser.Body_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body_class)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.STATIC_ID))) != 0):
                self.state = 139
                self.mem_class_declare()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_class_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructor_declare(self):
            return self.getTypedRuleContext(D96Parser.Constructor_declareContext,0)


        def destructor_declare(self):
            return self.getTypedRuleContext(D96Parser.Destructor_declareContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(D96Parser.Method_declareContext,0)


        def attribute_declare(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declareContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mem_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMem_class_declare" ):
                return visitor.visitMem_class_declare(self)
            else:
                return visitor.visitChildren(self)




    def mem_class_declare(self):

        localctx = D96Parser.Mem_class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mem_class_declare)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.constructor_declare()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.destructor_declare()
                pass
            elif token in [D96Parser.ID, D96Parser.STATIC_ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.method_declare()
                pass
            elif token in [D96Parser.VAR, D96Parser.VAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.attribute_declare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_declare" ):
                return visitor.visitConstructor_declare(self)
            else:
                return visitor.visitChildren(self)




    def constructor_declare(self):

        localctx = D96Parser.Constructor_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constructor_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 152
            self.match(D96Parser.LB)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 153
                self.params_list()


            self.state = 156
            self.match(D96Parser.RB)
            self.state = 157
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Params_declareContext)
            else:
                return self.getTypedRuleContext(D96Parser.Params_declareContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = D96Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.params_declare()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 160
                self.match(D96Parser.SEMI)
                self.state = 161
                self.params_declare()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_data(self):
            return self.getTypedRuleContext(D96Parser.Type_dataContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_params_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_declare" ):
                return visitor.visitParams_declare(self)
            else:
                return visitor.visitChildren(self)




    def params_declare(self):

        localctx = D96Parser.Params_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_params_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.id_list()
            self.state = 168
            self.match(D96Parser.COLON)
            self.state = 169
            self.type_data()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(D96Parser.ID)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 172
                self.match(D96Parser.COMMA)
                self.state = 173
                self.match(D96Parser.ID)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_dataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_type_data

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_data" ):
                return visitor.visitType_data(self)
            else:
                return visitor.visitChildren(self)




    def type_data(self):

        localctx = D96Parser.Type_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_data)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING) | (1 << D96Parser.INT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def element_type(self):
            return self.getTypedRuleContext(D96Parser.Element_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def size(self):
            return self.getTypedRuleContext(D96Parser.SizeContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(D96Parser.ARRAY)
            self.state = 187
            self.match(D96Parser.LSB)
            self.state = 188
            self.element_type()
            self.state = 189
            self.match(D96Parser.COMMA)
            self.state = 190
            self.size()
            self.state = 191
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_type" ):
                return visitor.visitElement_type(self)
            else:
                return visitor.visitChildren(self)




    def element_type(self):

        localctx = D96Parser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_element_type)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(D96Parser.INT_LIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = D96Parser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(D96Parser.INT_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor_declare" ):
                return visitor.visitDestructor_declare(self)
            else:
                return visitor.visitChildren(self)




    def destructor_declare(self):

        localctx = D96Parser.Destructor_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_destructor_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(D96Parser.DESTRUCTOR)
            self.state = 202
            self.match(D96Parser.LB)
            self.state = 203
            self.match(D96Parser.RB)
            self.state = 204
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declare" ):
                return visitor.visitMethod_declare(self)
            else:
                return visitor.visitChildren(self)




    def method_declare(self):

        localctx = D96Parser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 207
            self.match(D96Parser.LB)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 208
                self.params_list()


            self.state = 211
            self.match(D96Parser.RB)
            self.state = 212
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._variable_name_list = None # Variable_name_listContext
            self._value_list = None # Value_listContext

        def variable_name_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_name_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_data(self):
            return self.getTypedRuleContext(D96Parser.Type_dataContext,0)


        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def value_list(self):
            return self.getTypedRuleContext(D96Parser.Value_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declare" ):
                return visitor.visitAttribute_declare(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declare(self):

        localctx = D96Parser.Attribute_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_attribute_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 215
            localctx._variable_name_list = self.variable_name_list()
            self.state = 216
            self.match(D96Parser.COLON)
            self.state = 217
            self.type_data()
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EQUAL]:
                self.state = 218
                self.match(D96Parser.EQUAL)
                self.state = 219
                localctx._value_list = self.value_list(localctx._variable_name_list.count)

                self.state = 220
                if not localctx._value_list.count_after == 0:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$value_list.count_after == 0")
                self.state = 221
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.SEMI]:
                self.state = 223
                self.match(D96Parser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_name_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.count = 0

        def id_or_staticID(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Id_or_staticIDContext)
            else:
                return self.getTypedRuleContext(D96Parser.Id_or_staticIDContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_name_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_name_list" ):
                return visitor.visitVariable_name_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_name_list(self):

        localctx = D96Parser.Variable_name_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_variable_name_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.id_or_staticID()
            localctx.count+=1
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 228
                self.match(D96Parser.COMMA)

                self.state = 229
                self.id_or_staticID()
                localctx.count+=1
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_or_staticIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_id_or_staticID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_or_staticID" ):
                return visitor.visitId_or_staticID(self)
            else:
                return visitor.visitChildren(self)




    def id_or_staticID(self):

        localctx = D96Parser.Id_or_staticIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_id_or_staticID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, count=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.count = None
            self.count_after = None
            self.count = count

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_value_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_list" ):
                return visitor.visitValue_list(self)
            else:
                return visitor.visitChildren(self)




    def value_list(self, count):

        localctx = D96Parser.Value_listContext(self, self._ctx, self.state, count)
        self.enterRule(localctx, 40, self.RULE_value_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.exp()
            localctx.count-=1
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 241
                    if not localctx.count > 0:
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$count > 0")
                    self.state = 242
                    self.match(D96Parser.COMMA)
                    self.state = 243
                    self.exp()
                    localctx.count-=1 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            localctx.count_after = localctx.count
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(D96Parser.LP)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.RETURN) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.ID))) != 0):
                self.state = 254
                self.stmt()
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_and_constant_stmt(self):
            return self.getTypedRuleContext(D96Parser.Variable_and_constant_stmtContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assignment_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def for_in_stmt(self):
            return self.getTypedRuleContext(D96Parser.For_in_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def method_invocation_stmt(self):
            return self.getTypedRuleContext(D96Parser.Method_invocation_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmt)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.variable_and_constant_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 265
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 266
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 267
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 268
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 269
                self.method_invocation_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 270
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_and_constant_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._variable_name_list_in_method = None # Variable_name_list_in_methodContext
            self._value_list_stmt = None # Value_list_stmtContext

        def variable_name_list_in_method(self):
            return self.getTypedRuleContext(D96Parser.Variable_name_list_in_methodContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_data(self):
            return self.getTypedRuleContext(D96Parser.Type_dataContext,0)


        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def value_list_stmt(self):
            return self.getTypedRuleContext(D96Parser.Value_list_stmtContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_and_constant_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_and_constant_stmt" ):
                return visitor.visitVariable_and_constant_stmt(self)
            else:
                return visitor.visitChildren(self)




    def variable_and_constant_stmt(self):

        localctx = D96Parser.Variable_and_constant_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_variable_and_constant_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 274
            localctx._variable_name_list_in_method = self.variable_name_list_in_method()
            self.state = 275
            self.match(D96Parser.COLON)
            self.state = 276
            self.type_data()
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EQUAL]:
                self.state = 277
                self.match(D96Parser.EQUAL)
                self.state = 278
                localctx._value_list_stmt = self.value_list_stmt(localctx._variable_name_list_in_method.count)

                self.state = 279
                if not localctx._value_list_stmt.count_after == 0:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$value_list_stmt.count_after == 0")
                self.state = 280
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.SEMI]:
                self.state = 282
                self.match(D96Parser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_name_list_in_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.count = 0

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_name_list_in_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_name_list_in_method" ):
                return visitor.visitVariable_name_list_in_method(self)
            else:
                return visitor.visitChildren(self)




    def variable_name_list_in_method(self):

        localctx = D96Parser.Variable_name_list_in_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_variable_name_list_in_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(D96Parser.ID)
            localctx.count+=1
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 287
                self.match(D96Parser.COMMA)
                self.state = 288
                self.match(D96Parser.ID)
                localctx.count+=1
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_list_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, count=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.count = None
            self.count_after = None
            self.count = count

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_value_list_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_list_stmt" ):
                return visitor.visitValue_list_stmt(self)
            else:
                return visitor.visitChildren(self)




    def value_list_stmt(self, count):

        localctx = D96Parser.Value_list_stmtContext(self, self._ctx, self.state, count)
        self.enterRule(localctx, 50, self.RULE_value_list_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.exp()
            localctx.count-=1
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 297
                    if not localctx.count > 0:
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$count > 0")
                    self.state = 298
                    self.match(D96Parser.COMMA)
                    self.state = 299
                    self.exp()
                    localctx.count-=1 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            localctx.count_after = localctx.count
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignment_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = D96Parser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.scalar_variable()
            self.state = 310
            self.match(D96Parser.EQUAL)
            self.state = 311
            self.exp()
            self.state = 312
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def name_class(self):
            return self.getTypedRuleContext(D96Parser.Name_classContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def index_exp_for_scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Index_exp_for_scalar_variableContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_scalar_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_variable" ):
                return visitor.visitScalar_variable(self)
            else:
                return visitor.visitChildren(self)




    def scalar_variable(self):

        localctx = D96Parser.Scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_scalar_variable)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.name_class()
                self.state = 316
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 317
                self.match(D96Parser.STATIC_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
                self.exp8(0)
                self.state = 320
                self.match(D96Parser.DOT)
                self.state = 321
                self.match(D96Parser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
                self.index_exp_for_scalar_variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exp_for_scalar_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_exp_for_scalar_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_exp_for_scalar_variable" ):
                return visitor.visitIndex_exp_for_scalar_variable(self)
            else:
                return visitor.visitChildren(self)




    def index_exp_for_scalar_variable(self):

        localctx = D96Parser.Index_exp_for_scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_index_exp_for_scalar_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.exp8(0)
            self.state = 327
            self.index_operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def elseif_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Elseif_blockContext)
            else:
                return self.getTypedRuleContext(D96Parser.Elseif_blockContext,i)


        def else_block(self):
            return self.getTypedRuleContext(D96Parser.Else_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(D96Parser.IF)
            self.state = 330
            self.match(D96Parser.LB)
            self.state = 331
            self.exp()
            self.state = 332
            self.match(D96Parser.RB)
            self.state = 333
            self.block_stmt()
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 334
                self.elseif_block()
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 340
                self.else_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_block" ):
                return visitor.visitElseif_block(self)
            else:
                return visitor.visitChildren(self)




    def elseif_block(self):

        localctx = D96Parser.Elseif_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elseif_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(D96Parser.ELSEIF)
            self.state = 344
            self.match(D96Parser.LB)
            self.state = 345
            self.exp()
            self.state = 346
            self.match(D96Parser.RB)
            self.state = 347
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_block" ):
                return visitor.visitElse_block(self)
            else:
                return visitor.visitChildren(self)




    def else_block(self):

        localctx = D96Parser.Else_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_else_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(D96Parser.ELSE)
            self.state = 350
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def DOUBLE_DOT(self):
            return self.getToken(D96Parser.DOUBLE_DOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_stmt" ):
                return visitor.visitFor_in_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_in_stmt(self):

        localctx = D96Parser.For_in_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_in_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(D96Parser.FOREACH)
            self.state = 353
            self.match(D96Parser.LB)
            self.state = 354
            self.match(D96Parser.ID)
            self.state = 355
            self.match(D96Parser.IN)
            self.state = 356
            self.exp()
            self.state = 357
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 358
            self.exp()
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 359
                self.match(D96Parser.BY)
                self.state = 360
                self.exp()


            self.state = 363
            self.match(D96Parser.RB)
            self.state = 364
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(D96Parser.BREAK)
            self.state = 367
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(D96Parser.CONTINUE)
            self.state = 370
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(D96Parser.RETURN)
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                self.state = 373
                self.exp()


            self.state = 376
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def static_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocationContext,0)


        def instance_method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_invocationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_stmt" ):
                return visitor.visitMethod_invocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_stmt(self):

        localctx = D96Parser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 378
                self.static_method_invocation()
                pass

            elif la_ == 2:
                self.state = 379
                self.instance_method_invocation()
                pass


            self.state = 382
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_class(self):
            return self.getTypedRuleContext(D96Parser.Name_classContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invocation" ):
                return visitor.visitStatic_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invocation(self):

        localctx = D96Parser.Static_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_static_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.name_class()
            self.state = 385
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 386
            self.match(D96Parser.STATIC_ID)
            self.state = 387
            self.match(D96Parser.LB)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                self.state = 388
                self.exp_list()


            self.state = 391
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pre_exp(self):
            return self.getTypedRuleContext(D96Parser.Pre_expContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invocation" ):
                return visitor.visitInstance_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invocation(self):

        localctx = D96Parser.Instance_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_instance_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.pre_exp(0)
            self.state = 394
            self.match(D96Parser.DOT)
            self.state = 395
            self.match(D96Parser.ID)
            self.state = 396
            self.match(D96Parser.LB)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                self.state = 397
                self.exp_list()


            self.state = 400
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pre_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def pre_exp(self):
            return self.getTypedRuleContext(D96Parser.Pre_expContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_pre_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPre_exp" ):
                return visitor.visitPre_exp(self)
            else:
                return visitor.visitChildren(self)



    def pre_exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Pre_expContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_pre_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 416
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Pre_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pre_exp)
                        self.state = 405
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 406
                        self.match(D96Parser.DOT)
                        self.state = 407
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Pre_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pre_exp)
                        self.state = 408
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 409
                        self.match(D96Parser.DOT)
                        self.state = 410
                        self.match(D96Parser.ID)
                        self.state = 411
                        self.match(D96Parser.LB)
                        self.state = 413
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                            self.state = 412
                            self.exp_list()


                        self.state = 415
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp1Context,i)


        def ADD_STR(self):
            return self.getToken(D96Parser.ADD_STR, 0)

        def IS_EQUAL_STR(self):
            return self.getToken(D96Parser.IS_EQUAL_STR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.exp1()
                self.state = 422
                _la = self._input.LA(1)
                if not(_la==D96Parser.ADD_STR or _la==D96Parser.IS_EQUAL_STR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 423
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp2Context,i)


        def IS_EQUAL(self):
            return self.getToken(D96Parser.IS_EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = D96Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.exp2(0)
                self.state = 429
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.IS_EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 430
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 443
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 438
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 439
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 440
                    self.exp3(0) 
                self.state = 445
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 454
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 449
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 450
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 451
                    self.exp4(0) 
                self.state = 456
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def MULTIPLY(self):
            return self.getToken(D96Parser.MULTIPLY, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 460
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 461
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 462
                    self.exp5() 
                self.state = 467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_exp5)
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.match(D96Parser.NOT)
                self.state = 469
                self.exp5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.STRING_LIT, D96Parser.FLOAT_LIT, D96Parser.INT_LIT, D96Parser.ZERO_LIT, D96Parser.SUB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_exp6)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(D96Parser.SUB)
                self.state = 474
                self.exp6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.STRING_LIT, D96Parser.FLOAT_LIT, D96Parser.INT_LIT, D96Parser.ZERO_LIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.exp7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 485
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 481
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 482
                    self.index_operator() 
                self.state = 487
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_exp8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 504
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 502
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 491
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 492
                        self.match(D96Parser.DOT)
                        self.state = 493
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 494
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 495
                        self.match(D96Parser.DOT)
                        self.state = 496
                        self.match(D96Parser.ID)
                        self.state = 497
                        self.match(D96Parser.LB)
                        self.state = 499
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                            self.state = 498
                            self.exp_list()


                        self.state = 501
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 506
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = D96Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_exp9)
        self._la = 0 # Token type
        try:
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.match(D96Parser.ID)
                self.state = 508
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 509
                self.match(D96Parser.STATIC_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                self.match(D96Parser.ID)
                self.state = 511
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 512
                self.match(D96Parser.STATIC_ID)
                self.state = 513
                self.match(D96Parser.LB)
                self.state = 515
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                    self.state = 514
                    self.exp_list()


                self.state = 517
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 518
                self.exp10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_exp10)
        self._la = 0 # Token type
        try:
            self.state = 529
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.match(D96Parser.NEW)
                self.state = 522
                self.match(D96Parser.ID)
                self.state = 523
                self.match(D96Parser.LB)
                self.state = 525
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                    self.state = 524
                    self.exp_list()


                self.state = 527
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.STRING_LIT, D96Parser.FLOAT_LIT, D96Parser.INT_LIT, D96Parser.ZERO_LIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 528
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_operands)
        try:
            self.state = 539
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.match(D96Parser.LB)
                self.state = 533
                self.exp()
                self.state = 534
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.STRING_LIT, D96Parser.FLOAT_LIT, D96Parser.INT_LIT, D96Parser.ZERO_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 536
                self.literals()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 537
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 538
                self.match(D96Parser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZERO_LIT(self):
            return self.getToken(D96Parser.ZERO_LIT, 0)

        def INT_LIT(self):
            return self.getToken(D96Parser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(D96Parser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(D96Parser.STRING_LIT, 0)

        def boolean_literal(self):
            return self.getTypedRuleContext(D96Parser.Boolean_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(D96Parser.Array_literalContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_literals)
        try:
            self.state = 547
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ZERO_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.match(D96Parser.ZERO_LIT)
                pass
            elif token in [D96Parser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
                self.match(D96Parser.INT_LIT)
                pass
            elif token in [D96Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 543
                self.match(D96Parser.FLOAT_LIT)
                pass
            elif token in [D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 544
                self.match(D96Parser.STRING_LIT)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 545
                self.boolean_literal()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 546
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = D96Parser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            _la = self._input.LA(1)
            if not(_la==D96Parser.TRUE or _la==D96Parser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multidimensional_array(self):
            return self.getTypedRuleContext(D96Parser.Multidimensional_arrayContext,0)


        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_array_literal)
        try:
            self.state = 553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.multidimensional_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.indexed_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multidimensional_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multidimensional_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultidimensional_array" ):
                return visitor.visitMultidimensional_array(self)
            else:
                return visitor.visitChildren(self)




    def multidimensional_array(self):

        localctx = D96Parser.Multidimensional_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_multidimensional_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(D96Parser.ARRAY)
            self.state = 556
            self.match(D96Parser.LB)
            self.state = 557
            self.array_list()
            self.state = 558
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Array_literalContext)
            else:
                return self.getTypedRuleContext(D96Parser.Array_literalContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.array_literal()
            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 561
                self.match(D96Parser.COMMA)
                self.state = 562
                self.array_literal()
                self.state = 567
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp_list(self):
            return self.getTypedRuleContext(D96Parser.Exp_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexed_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array" ):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(D96Parser.ARRAY)
            self.state = 569
            self.match(D96Parser.LB)
            self.state = 571
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                self.state = 570
                self.exp_list()


            self.state = 573
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = D96Parser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_exp_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.exp()
            self.state = 580
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 576
                self.match(D96Parser.COMMA)
                self.state = 577
                self.exp()
                self.state = 582
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_index_operator)
        try:
            self.state = 592
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 583
                self.match(D96Parser.LSB)
                self.state = 584
                self.exp()
                self.state = 585
                self.match(D96Parser.RSB)
                self.state = 586
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
                self.match(D96Parser.LSB)
                self.state = 589
                self.exp()
                self.state = 590
                self.match(D96Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.attribute_declare_sempred
        self._predicates[20] = self.value_list_sempred
        self._predicates[23] = self.variable_and_constant_stmt_sempred
        self._predicates[25] = self.value_list_stmt_sempred
        self._predicates[39] = self.pre_exp_sempred
        self._predicates[42] = self.exp2_sempred
        self._predicates[43] = self.exp3_sempred
        self._predicates[44] = self.exp4_sempred
        self._predicates[47] = self.exp7_sempred
        self._predicates[48] = self.exp8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def attribute_declare_sempred(self, localctx:Attribute_declareContext, predIndex:int):
            if predIndex == 0:
                return localctx._value_list.count_after == 0
         

    def value_list_sempred(self, localctx:Value_listContext, predIndex:int):
            if predIndex == 1:
                return localctx.count > 0
         

    def variable_and_constant_stmt_sempred(self, localctx:Variable_and_constant_stmtContext, predIndex:int):
            if predIndex == 2:
                return localctx._value_list_stmt.count_after == 0
         

    def value_list_stmt_sempred(self, localctx:Value_list_stmtContext, predIndex:int):
            if predIndex == 3:
                return localctx.count > 0
         

    def pre_exp_sempred(self, localctx:Pre_expContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         





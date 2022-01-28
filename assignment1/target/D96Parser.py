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
        buf.write("\u0265\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\6\2t\n")
        buf.write("\2\r\2\16\2u\3\2\3\2\3\3\3\3\3\3\3\3\5\3~\n\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\7\5\u008a\n\5\f\5\16")
        buf.write("\5\u008d\13\5\3\6\3\6\3\6\5\6\u0092\n\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\7\7\u009a\n\7\f\7\16\7\u009d\13\7\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\7\t\u00a6\n\t\f\t\16\t\u00a9\13\t\3")
        buf.write("\n\3\n\3\n\5\n\u00ae\n\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\5\r\u00bb\n\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\5\21\u00c9\n\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u00d8\n\22\3\23\3\23\3\23\3\23\3\23\7")
        buf.write("\23\u00df\n\23\f\23\16\23\u00e2\13\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\7\24\u00eb\n\24\f\24\16\24\u00ee\13")
        buf.write("\24\3\24\3\24\3\25\3\25\7\25\u00f4\n\25\f\25\16\25\u00f7")
        buf.write("\13\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u0104\n\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u0110\n\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\7\30\u0117\n\30\f\30\16\30\u011a\13\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\7\31\u0123\n\31\f\31\16\31")
        buf.write("\u0126\13\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0139")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\6\35\u0151\n\35\r\35\16\35\u0152\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\6\35\u0160\n")
        buf.write("\35\r\35\16\35\u0161\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\5\35\u016f\n\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\5\36\u017a\n\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\5!\u0187\n!\3!\3!")
        buf.write("\3\"\3\"\5\"\u018d\n\"\3\"\3\"\3#\3#\3#\3#\3#\5#\u0196")
        buf.write("\n#\3#\3#\3$\3$\3$\3$\3$\5$\u019f\n$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\5%\u01ae\n%\3%\7%\u01b1\n%\f%\16")
        buf.write("%\u01b4\13%\3&\3&\3&\3&\3&\5&\u01bb\n&\3\'\3\'\3\'\3\'")
        buf.write("\3\'\5\'\u01c2\n\'\3(\3(\3(\3(\3(\3(\7(\u01ca\n(\f(\16")
        buf.write("(\u01cd\13(\3)\3)\3)\3)\3)\3)\7)\u01d5\n)\f)\16)\u01d8")
        buf.write("\13)\3*\3*\3*\3*\3*\3*\7*\u01e0\n*\f*\16*\u01e3\13*\3")
        buf.write("+\3+\3+\5+\u01e8\n+\3,\3,\3,\5,\u01ed\n,\3-\3-\3-\3-\3")
        buf.write("-\7-\u01f4\n-\f-\16-\u01f7\13-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\5.\u0204\n.\3.\7.\u0207\n.\f.\16.\u020a\13")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\3/\5/\u0214\n/\3/\3/\5/\u0218\n")
        buf.write("/\3\60\3\60\3\60\3\60\5\60\u021e\n\60\3\60\3\60\5\60\u0222")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u022c")
        buf.write("\n\61\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0234\n\62\3")
        buf.write("\63\3\63\3\64\3\64\5\64\u023a\n\64\3\65\3\65\3\65\5\65")
        buf.write("\u023f\n\65\3\65\3\65\3\66\3\66\3\66\7\66\u0246\n\66\f")
        buf.write("\66\16\66\u0249\13\66\3\67\3\67\3\67\5\67\u024e\n\67\3")
        buf.write("\67\3\67\38\38\38\78\u0255\n8\f8\168\u0258\138\39\39\3")
        buf.write("9\39\39\39\39\39\39\59\u0263\n9\39\2\bHNPRXZ:\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\13\3\2\f\17\3\2?@\3\2")
        buf.write("\21\22\3\2;<\4\2\60\61\67:\3\2./\3\2\62\63\3\2\64\66\3")
        buf.write("\2\n\13\2\u0277\2s\3\2\2\2\4y\3\2\2\2\6\u0083\3\2\2\2")
        buf.write("\b\u008b\3\2\2\2\n\u008e\3\2\2\2\f\u0096\3\2\2\2\16\u009e")
        buf.write("\3\2\2\2\20\u00a2\3\2\2\2\22\u00ad\3\2\2\2\24\u00af\3")
        buf.write("\2\2\2\26\u00b1\3\2\2\2\30\u00ba\3\2\2\2\32\u00bc\3\2")
        buf.write("\2\2\34\u00be\3\2\2\2\36\u00c0\3\2\2\2 \u00c5\3\2\2\2")
        buf.write("\"\u00cd\3\2\2\2$\u00d9\3\2\2\2&\u00e3\3\2\2\2(\u00f1")
        buf.write("\3\2\2\2*\u0103\3\2\2\2,\u0105\3\2\2\2.\u0111\3\2\2\2")
        buf.write("\60\u011b\3\2\2\2\62\u0129\3\2\2\2\64\u0138\3\2\2\2\66")
        buf.write("\u013a\3\2\2\28\u016e\3\2\2\2:\u0170\3\2\2\2<\u017e\3")
        buf.write("\2\2\2>\u0181\3\2\2\2@\u0184\3\2\2\2B\u018c\3\2\2\2D\u0190")
        buf.write("\3\2\2\2F\u0199\3\2\2\2H\u01a2\3\2\2\2J\u01ba\3\2\2\2")
        buf.write("L\u01c1\3\2\2\2N\u01c3\3\2\2\2P\u01ce\3\2\2\2R\u01d9\3")
        buf.write("\2\2\2T\u01e7\3\2\2\2V\u01ec\3\2\2\2X\u01ee\3\2\2\2Z\u01f8")
        buf.write("\3\2\2\2\\\u0217\3\2\2\2^\u0221\3\2\2\2`\u022b\3\2\2\2")
        buf.write("b\u0233\3\2\2\2d\u0235\3\2\2\2f\u0239\3\2\2\2h\u023b\3")
        buf.write("\2\2\2j\u0242\3\2\2\2l\u024a\3\2\2\2n\u0251\3\2\2\2p\u0262")
        buf.write("\3\2\2\2rt\5\4\3\2sr\3\2\2\2tu\3\2\2\2us\3\2\2\2uv\3\2")
        buf.write("\2\2vw\3\2\2\2wx\7\2\2\3x\3\3\2\2\2yz\7\30\2\2z}\5\6\4")
        buf.write("\2{|\7\'\2\2|~\7?\2\2}{\3\2\2\2}~\3\2\2\2~\177\3\2\2\2")
        buf.write("\177\u0080\7$\2\2\u0080\u0081\5\b\5\2\u0081\u0082\7%\2")
        buf.write("\2\u0082\5\3\2\2\2\u0083\u0084\7?\2\2\u0084\7\3\2\2\2")
        buf.write("\u0085\u008a\5\n\6\2\u0086\u008a\5\36\20\2\u0087\u008a")
        buf.write("\5 \21\2\u0088\u008a\5\"\22\2\u0089\u0085\3\2\2\2\u0089")
        buf.write("\u0086\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2\2")
        buf.write("\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3")
        buf.write("\2\2\2\u008c\t\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f")
        buf.write("\7\31\2\2\u008f\u0091\7\34\2\2\u0090\u0092\5\f\7\2\u0091")
        buf.write("\u0090\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2")
        buf.write("\u0093\u0094\7\35\2\2\u0094\u0095\5(\25\2\u0095\13\3\2")
        buf.write("\2\2\u0096\u009b\5\16\b\2\u0097\u0098\7#\2\2\u0098\u009a")
        buf.write("\5\16\b\2\u0099\u0097\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\r\3\2\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009e\u009f\5\20\t\2\u009f\u00a0\7\'\2")
        buf.write("\2\u00a0\u00a1\5\22\n\2\u00a1\17\3\2\2\2\u00a2\u00a7\7")
        buf.write("?\2\2\u00a3\u00a4\7\"\2\2\u00a4\u00a6\7?\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\21\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa")
        buf.write("\u00ae\5\24\13\2\u00ab\u00ae\5\26\f\2\u00ac\u00ae\5\34")
        buf.write("\17\2\u00ad\u00aa\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ae\23\3\2\2\2\u00af\u00b0\t\2\2\2\u00b0\25")
        buf.write("\3\2\2\2\u00b1\u00b2\7\23\2\2\u00b2\u00b3\7\36\2\2\u00b3")
        buf.write("\u00b4\5\30\r\2\u00b4\u00b5\7\"\2\2\u00b5\u00b6\5\32\16")
        buf.write("\2\u00b6\u00b7\7\37\2\2\u00b7\27\3\2\2\2\u00b8\u00bb\5")
        buf.write("\24\13\2\u00b9\u00bb\5\26\f\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00bb\31\3\2\2\2\u00bc\u00bd\7*\2\2\u00bd")
        buf.write("\33\3\2\2\2\u00be\u00bf\7?\2\2\u00bf\35\3\2\2\2\u00c0")
        buf.write("\u00c1\7\32\2\2\u00c1\u00c2\7\34\2\2\u00c2\u00c3\7\35")
        buf.write("\2\2\u00c3\u00c4\5(\25\2\u00c4\37\3\2\2\2\u00c5\u00c6")
        buf.write("\t\3\2\2\u00c6\u00c8\7\34\2\2\u00c7\u00c9\5\f\7\2\u00c8")
        buf.write("\u00c7\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\3\2\2\2")
        buf.write("\u00ca\u00cb\7\35\2\2\u00cb\u00cc\5(\25\2\u00cc!\3\2\2")
        buf.write("\2\u00cd\u00ce\t\4\2\2\u00ce\u00cf\5$\23\2\u00cf\u00d0")
        buf.write("\7\'\2\2\u00d0\u00d7\5\22\n\2\u00d1\u00d2\7=\2\2\u00d2")
        buf.write("\u00d3\5&\24\2\u00d3\u00d4\6\22\2\3\u00d4\u00d5\7#\2\2")
        buf.write("\u00d5\u00d8\3\2\2\2\u00d6\u00d8\7#\2\2\u00d7\u00d1\3")
        buf.write("\2\2\2\u00d7\u00d6\3\2\2\2\u00d8#\3\2\2\2\u00d9\u00da")
        buf.write("\t\3\2\2\u00da\u00e0\b\23\1\2\u00db\u00dc\7\"\2\2\u00dc")
        buf.write("\u00dd\t\3\2\2\u00dd\u00df\b\23\1\2\u00de\u00db\3\2\2")
        buf.write("\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1")
        buf.write("\3\2\2\2\u00e1%\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4")
        buf.write("\5J&\2\u00e4\u00ec\b\24\1\2\u00e5\u00e6\6\24\3\3\u00e6")
        buf.write("\u00e7\7\"\2\2\u00e7\u00e8\5J&\2\u00e8\u00e9\b\24\1\2")
        buf.write("\u00e9\u00eb\3\2\2\2\u00ea\u00e5\3\2\2\2\u00eb\u00ee\3")
        buf.write("\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ef")
        buf.write("\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\b\24\1\2\u00f0")
        buf.write("\'\3\2\2\2\u00f1\u00f5\7$\2\2\u00f2\u00f4\5*\26\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2")
        buf.write("\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f5\3")
        buf.write("\2\2\2\u00f8\u00f9\7%\2\2\u00f9)\3\2\2\2\u00fa\u0104\5")
        buf.write(",\27\2\u00fb\u0104\5\62\32\2\u00fc\u0104\58\35\2\u00fd")
        buf.write("\u0104\5:\36\2\u00fe\u0104\5<\37\2\u00ff\u0104\5> \2\u0100")
        buf.write("\u0104\5@!\2\u0101\u0104\5B\"\2\u0102\u0104\5(\25\2\u0103")
        buf.write("\u00fa\3\2\2\2\u0103\u00fb\3\2\2\2\u0103\u00fc\3\2\2\2")
        buf.write("\u0103\u00fd\3\2\2\2\u0103\u00fe\3\2\2\2\u0103\u00ff\3")
        buf.write("\2\2\2\u0103\u0100\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0102")
        buf.write("\3\2\2\2\u0104+\3\2\2\2\u0105\u0106\t\4\2\2\u0106\u0107")
        buf.write("\5.\30\2\u0107\u0108\7\'\2\2\u0108\u010f\5\22\n\2\u0109")
        buf.write("\u010a\7=\2\2\u010a\u010b\5\60\31\2\u010b\u010c\6\27\4")
        buf.write("\3\u010c\u010d\7#\2\2\u010d\u0110\3\2\2\2\u010e\u0110")
        buf.write("\7#\2\2\u010f\u0109\3\2\2\2\u010f\u010e\3\2\2\2\u0110")
        buf.write("-\3\2\2\2\u0111\u0112\7?\2\2\u0112\u0118\b\30\1\2\u0113")
        buf.write("\u0114\7\"\2\2\u0114\u0115\7?\2\2\u0115\u0117\b\30\1\2")
        buf.write("\u0116\u0113\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3")
        buf.write("\2\2\2\u0118\u0119\3\2\2\2\u0119/\3\2\2\2\u011a\u0118")
        buf.write("\3\2\2\2\u011b\u011c\5J&\2\u011c\u0124\b\31\1\2\u011d")
        buf.write("\u011e\6\31\5\3\u011e\u011f\7\"\2\2\u011f\u0120\5J&\2")
        buf.write("\u0120\u0121\b\31\1\2\u0121\u0123\3\2\2\2\u0122\u011d")
        buf.write("\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0125\u0127\3\2\2\2\u0126\u0124\3\2\2\2")
        buf.write("\u0127\u0128\b\31\1\2\u0128\61\3\2\2\2\u0129\u012a\5\64")
        buf.write("\33\2\u012a\u012b\7=\2\2\u012b\u012c\5J&\2\u012c\u012d")
        buf.write("\7#\2\2\u012d\63\3\2\2\2\u012e\u0139\7?\2\2\u012f\u0130")
        buf.write("\5\6\4\2\u0130\u0131\7&\2\2\u0131\u0132\7@\2\2\u0132\u0139")
        buf.write("\3\2\2\2\u0133\u0134\5Z.\2\u0134\u0135\7!\2\2\u0135\u0136")
        buf.write("\7?\2\2\u0136\u0139\3\2\2\2\u0137\u0139\5\66\34\2\u0138")
        buf.write("\u012e\3\2\2\2\u0138\u012f\3\2\2\2\u0138\u0133\3\2\2\2")
        buf.write("\u0138\u0137\3\2\2\2\u0139\65\3\2\2\2\u013a\u013b\5X-")
        buf.write("\2\u013b\u013c\7\36\2\2\u013c\u013d\5J&\2\u013d\u013e")
        buf.write("\7\37\2\2\u013e\67\3\2\2\2\u013f\u0140\7\6\2\2\u0140\u0141")
        buf.write("\7\34\2\2\u0141\u0142\5J&\2\u0142\u0143\7\35\2\2\u0143")
        buf.write("\u0144\5(\25\2\u0144\u016f\3\2\2\2\u0145\u0146\7\6\2\2")
        buf.write("\u0146\u0147\7\34\2\2\u0147\u0148\5J&\2\u0148\u0149\7")
        buf.write("\35\2\2\u0149\u0150\5(\25\2\u014a\u014b\7\7\2\2\u014b")
        buf.write("\u014c\7\34\2\2\u014c\u014d\5J&\2\u014d\u014e\7\35\2\2")
        buf.write("\u014e\u014f\5(\25\2\u014f\u0151\3\2\2\2\u0150\u014a\3")
        buf.write("\2\2\2\u0151\u0152\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153")
        buf.write("\3\2\2\2\u0153\u016f\3\2\2\2\u0154\u0155\7\6\2\2\u0155")
        buf.write("\u0156\7\34\2\2\u0156\u0157\5J&\2\u0157\u0158\7\35\2\2")
        buf.write("\u0158\u015f\5(\25\2\u0159\u015a\7\7\2\2\u015a\u015b\7")
        buf.write("\34\2\2\u015b\u015c\5J&\2\u015c\u015d\7\35\2\2\u015d\u015e")
        buf.write("\5(\25\2\u015e\u0160\3\2\2\2\u015f\u0159\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2")
        buf.write("\u0162\u0163\3\2\2\2\u0163\u0164\7\b\2\2\u0164\u0165\5")
        buf.write("(\25\2\u0165\u016f\3\2\2\2\u0166\u0167\7\6\2\2\u0167\u0168")
        buf.write("\7\34\2\2\u0168\u0169\5J&\2\u0169\u016a\7\35\2\2\u016a")
        buf.write("\u016b\5(\25\2\u016b\u016c\7\b\2\2\u016c\u016d\5(\25\2")
        buf.write("\u016d\u016f\3\2\2\2\u016e\u013f\3\2\2\2\u016e\u0145\3")
        buf.write("\2\2\2\u016e\u0154\3\2\2\2\u016e\u0166\3\2\2\2\u016f9")
        buf.write("\3\2\2\2\u0170\u0171\7\t\2\2\u0171\u0172\7\34\2\2\u0172")
        buf.write("\u0173\5\64\33\2\u0173\u0174\7\27\2\2\u0174\u0175\5J&")
        buf.write("\2\u0175\u0176\7 \2\2\u0176\u0179\5J&\2\u0177\u0178\7")
        buf.write("\33\2\2\u0178\u017a\5J&\2\u0179\u0177\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\7\35\2\2\u017c")
        buf.write("\u017d\5(\25\2\u017d;\3\2\2\2\u017e\u017f\7\4\2\2\u017f")
        buf.write("\u0180\7#\2\2\u0180=\3\2\2\2\u0181\u0182\7\5\2\2\u0182")
        buf.write("\u0183\7#\2\2\u0183?\3\2\2\2\u0184\u0186\7\25\2\2\u0185")
        buf.write("\u0187\5J&\2\u0186\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u0189\7#\2\2\u0189A\3\2\2\2\u018a")
        buf.write("\u018d\5D#\2\u018b\u018d\5F$\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\7#\2\2")
        buf.write("\u018fC\3\2\2\2\u0190\u0191\5\6\4\2\u0191\u0192\7&\2\2")
        buf.write("\u0192\u0193\7@\2\2\u0193\u0195\7\34\2\2\u0194\u0196\5")
        buf.write("n8\2\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197\u0198\7\35\2\2\u0198E\3\2\2\2\u0199\u019a")
        buf.write("\5H%\2\u019a\u019b\7!\2\2\u019b\u019c\7?\2\2\u019c\u019e")
        buf.write("\7\34\2\2\u019d\u019f\5n8\2\u019e\u019d\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\7\35\2")
        buf.write("\2\u01a1G\3\2\2\2\u01a2\u01a3\b%\1\2\u01a3\u01a4\5\\/")
        buf.write("\2\u01a4\u01b2\3\2\2\2\u01a5\u01a6\f\5\2\2\u01a6\u01a7")
        buf.write("\7!\2\2\u01a7\u01b1\7?\2\2\u01a8\u01a9\f\4\2\2\u01a9\u01aa")
        buf.write("\7!\2\2\u01aa\u01ab\7?\2\2\u01ab\u01ad\7\34\2\2\u01ac")
        buf.write("\u01ae\5n8\2\u01ad\u01ac\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b1\7\35\2\2\u01b0\u01a5\3\2\2")
        buf.write("\2\u01b0\u01a8\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3I\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b5\u01b6\5L\'\2\u01b6\u01b7\t\5\2\2\u01b7")
        buf.write("\u01b8\5L\'\2\u01b8\u01bb\3\2\2\2\u01b9\u01bb\5L\'\2\u01ba")
        buf.write("\u01b5\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bbK\3\2\2\2\u01bc")
        buf.write("\u01bd\5N(\2\u01bd\u01be\t\6\2\2\u01be\u01bf\5N(\2\u01bf")
        buf.write("\u01c2\3\2\2\2\u01c0\u01c2\5N(\2\u01c1\u01bc\3\2\2\2\u01c1")
        buf.write("\u01c0\3\2\2\2\u01c2M\3\2\2\2\u01c3\u01c4\b(\1\2\u01c4")
        buf.write("\u01c5\5P)\2\u01c5\u01cb\3\2\2\2\u01c6\u01c7\f\4\2\2\u01c7")
        buf.write("\u01c8\t\7\2\2\u01c8\u01ca\5P)\2\u01c9\u01c6\3\2\2\2\u01ca")
        buf.write("\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01ccO\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01cf\b)\1\2")
        buf.write("\u01cf\u01d0\5R*\2\u01d0\u01d6\3\2\2\2\u01d1\u01d2\f\4")
        buf.write("\2\2\u01d2\u01d3\t\b\2\2\u01d3\u01d5\5R*\2\u01d4\u01d1")
        buf.write("\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7Q\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9")
        buf.write("\u01da\b*\1\2\u01da\u01db\5T+\2\u01db\u01e1\3\2\2\2\u01dc")
        buf.write("\u01dd\f\4\2\2\u01dd\u01de\t\t\2\2\u01de\u01e0\5T+\2\u01df")
        buf.write("\u01dc\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2")
        buf.write("\u01e1\u01e2\3\2\2\2\u01e2S\3\2\2\2\u01e3\u01e1\3\2\2")
        buf.write("\2\u01e4\u01e5\7-\2\2\u01e5\u01e8\5T+\2\u01e6\u01e8\5")
        buf.write("V,\2\u01e7\u01e4\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8U\3")
        buf.write("\2\2\2\u01e9\u01ea\7\63\2\2\u01ea\u01ed\5V,\2\u01eb\u01ed")
        buf.write("\5X-\2\u01ec\u01e9\3\2\2\2\u01ec\u01eb\3\2\2\2\u01edW")
        buf.write("\3\2\2\2\u01ee\u01ef\b-\1\2\u01ef\u01f0\5Z.\2\u01f0\u01f5")
        buf.write("\3\2\2\2\u01f1\u01f2\f\4\2\2\u01f2\u01f4\5p9\2\u01f3\u01f1")
        buf.write("\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5")
        buf.write("\u01f6\3\2\2\2\u01f6Y\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8")
        buf.write("\u01f9\b.\1\2\u01f9\u01fa\5\\/\2\u01fa\u0208\3\2\2\2\u01fb")
        buf.write("\u01fc\f\5\2\2\u01fc\u01fd\7!\2\2\u01fd\u0207\7?\2\2\u01fe")
        buf.write("\u01ff\f\4\2\2\u01ff\u0200\7!\2\2\u0200\u0201\7?\2\2\u0201")
        buf.write("\u0203\7\34\2\2\u0202\u0204\5n8\2\u0203\u0202\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0207\7")
        buf.write("\35\2\2\u0206\u01fb\3\2\2\2\u0206\u01fe\3\2\2\2\u0207")
        buf.write("\u020a\3\2\2\2\u0208\u0206\3\2\2\2\u0208\u0209\3\2\2\2")
        buf.write("\u0209[\3\2\2\2\u020a\u0208\3\2\2\2\u020b\u020c\7?\2\2")
        buf.write("\u020c\u020d\7&\2\2\u020d\u0218\7@\2\2\u020e\u020f\7?")
        buf.write("\2\2\u020f\u0210\7&\2\2\u0210\u0211\7@\2\2\u0211\u0213")
        buf.write("\7\34\2\2\u0212\u0214\5n8\2\u0213\u0212\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0218\7\35\2")
        buf.write("\2\u0216\u0218\5^\60\2\u0217\u020b\3\2\2\2\u0217\u020e")
        buf.write("\3\2\2\2\u0217\u0216\3\2\2\2\u0218]\3\2\2\2\u0219\u021a")
        buf.write("\7\26\2\2\u021a\u021b\7?\2\2\u021b\u021d\7\34\2\2\u021c")
        buf.write("\u021e\5n8\2\u021d\u021c\3\2\2\2\u021d\u021e\3\2\2\2\u021e")
        buf.write("\u021f\3\2\2\2\u021f\u0222\7\35\2\2\u0220\u0222\5`\61")
        buf.write("\2\u0221\u0219\3\2\2\2\u0221\u0220\3\2\2\2\u0222_\3\2")
        buf.write("\2\2\u0223\u022c\7?\2\2\u0224\u0225\7\34\2\2\u0225\u0226")
        buf.write("\5J&\2\u0226\u0227\7\35\2\2\u0227\u022c\3\2\2\2\u0228")
        buf.write("\u022c\5b\62\2\u0229\u022c\7\24\2\2\u022a\u022c\7\20\2")
        buf.write("\2\u022b\u0223\3\2\2\2\u022b\u0224\3\2\2\2\u022b\u0228")
        buf.write("\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022a\3\2\2\2\u022c")
        buf.write("a\3\2\2\2\u022d\u0234\7,\2\2\u022e\u0234\7*\2\2\u022f")
        buf.write("\u0234\7)\2\2\u0230\u0234\7(\2\2\u0231\u0234\5d\63\2\u0232")
        buf.write("\u0234\5f\64\2\u0233\u022d\3\2\2\2\u0233\u022e\3\2\2\2")
        buf.write("\u0233\u022f\3\2\2\2\u0233\u0230\3\2\2\2\u0233\u0231\3")
        buf.write("\2\2\2\u0233\u0232\3\2\2\2\u0234c\3\2\2\2\u0235\u0236")
        buf.write("\t\n\2\2\u0236e\3\2\2\2\u0237\u023a\5h\65\2\u0238\u023a")
        buf.write("\5l\67\2\u0239\u0237\3\2\2\2\u0239\u0238\3\2\2\2\u023a")
        buf.write("g\3\2\2\2\u023b\u023c\7\23\2\2\u023c\u023e\7\34\2\2\u023d")
        buf.write("\u023f\5j\66\2\u023e\u023d\3\2\2\2\u023e\u023f\3\2\2\2")
        buf.write("\u023f\u0240\3\2\2\2\u0240\u0241\7\35\2\2\u0241i\3\2\2")
        buf.write("\2\u0242\u0247\5f\64\2\u0243\u0244\7\"\2\2\u0244\u0246")
        buf.write("\5f\64\2\u0245\u0243\3\2\2\2\u0246\u0249\3\2\2\2\u0247")
        buf.write("\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248k\3\2\2\2\u0249")
        buf.write("\u0247\3\2\2\2\u024a\u024b\7\23\2\2\u024b\u024d\7\34\2")
        buf.write("\2\u024c\u024e\5n8\2\u024d\u024c\3\2\2\2\u024d\u024e\3")
        buf.write("\2\2\2\u024e\u024f\3\2\2\2\u024f\u0250\7\35\2\2\u0250")
        buf.write("m\3\2\2\2\u0251\u0256\5J&\2\u0252\u0253\7\"\2\2\u0253")
        buf.write("\u0255\5J&\2\u0254\u0252\3\2\2\2\u0255\u0258\3\2\2\2\u0256")
        buf.write("\u0254\3\2\2\2\u0256\u0257\3\2\2\2\u0257o\3\2\2\2\u0258")
        buf.write("\u0256\3\2\2\2\u0259\u025a\7\36\2\2\u025a\u025b\5J&\2")
        buf.write("\u025b\u025c\7\37\2\2\u025c\u0263\3\2\2\2\u025d\u025e")
        buf.write("\7\36\2\2\u025e\u025f\5J&\2\u025f\u0260\7\37\2\2\u0260")
        buf.write("\u0261\5p9\2\u0261\u0263\3\2\2\2\u0262\u0259\3\2\2\2\u0262")
        buf.write("\u025d\3\2\2\2\u0263q\3\2\2\2\67u}\u0089\u008b\u0091\u009b")
        buf.write("\u00a7\u00ad\u00ba\u00c8\u00d7\u00e0\u00ec\u00f5\u0103")
        buf.write("\u010f\u0118\u0124\u0138\u0152\u0161\u016e\u0179\u0186")
        buf.write("\u018c\u0195\u019e\u01ad\u01b0\u01b2\u01ba\u01c1\u01cb")
        buf.write("\u01d6\u01e1\u01e7\u01ec\u01f5\u0203\u0206\u0208\u0213")
        buf.write("\u0217\u021d\u0221\u022b\u0233\u0239\u023e\u0247\u024d")
        buf.write("\u0256\u0262")
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
    RULE_constructor_declare = 4
    RULE_params_list = 5
    RULE_params_declare = 6
    RULE_id_list = 7
    RULE_type_data = 8
    RULE_primitive_type = 9
    RULE_array_type = 10
    RULE_element_type = 11
    RULE_size = 12
    RULE_class_type = 13
    RULE_destructor_declare = 14
    RULE_method_declare = 15
    RULE_attribute_declare = 16
    RULE_variable_name_list = 17
    RULE_value_list = 18
    RULE_block_stmt = 19
    RULE_stmt = 20
    RULE_variable_and_constant_stmt = 21
    RULE_variable_name_list_in_method = 22
    RULE_value_list_stmt = 23
    RULE_assignment_stmt = 24
    RULE_scalar_variable = 25
    RULE_index_exp_for_scalar_variable = 26
    RULE_if_stmt = 27
    RULE_for_in_stmt = 28
    RULE_break_stmt = 29
    RULE_continue_stmt = 30
    RULE_return_stmt = 31
    RULE_method_invocation_stmt = 32
    RULE_static_method_invocation = 33
    RULE_instance_method_invocation = 34
    RULE_pre_exp = 35
    RULE_exp = 36
    RULE_exp1 = 37
    RULE_exp2 = 38
    RULE_exp3 = 39
    RULE_exp4 = 40
    RULE_exp5 = 41
    RULE_exp6 = 42
    RULE_exp7 = 43
    RULE_exp8 = 44
    RULE_exp9 = 45
    RULE_exp10 = 46
    RULE_operands = 47
    RULE_literals = 48
    RULE_boolean_literal = 49
    RULE_array_literal = 50
    RULE_multidimensional_array = 51
    RULE_array_list = 52
    RULE_indexed_array = 53
    RULE_exp_list = 54
    RULE_index_operator = 55

    ruleNames =  [ "program", "class_declare", "name_class", "body_class", 
                   "constructor_declare", "params_list", "params_declare", 
                   "id_list", "type_data", "primitive_type", "array_type", 
                   "element_type", "size", "class_type", "destructor_declare", 
                   "method_declare", "attribute_declare", "variable_name_list", 
                   "value_list", "block_stmt", "stmt", "variable_and_constant_stmt", 
                   "variable_name_list_in_method", "value_list_stmt", "assignment_stmt", 
                   "scalar_variable", "index_exp_for_scalar_variable", "if_stmt", 
                   "for_in_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "method_invocation_stmt", "static_method_invocation", 
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
            self.state = 113 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self.class_declare()
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 117
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
            self.state = 119
            self.match(D96Parser.CLASS)
            self.state = 120
            self.name_class()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 121
                self.match(D96Parser.COLON)
                self.state = 122
                self.match(D96Parser.ID)


            self.state = 125
            self.match(D96Parser.LP)
            self.state = 126
            self.body_class()
            self.state = 127
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
            self.state = 129
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

        def constructor_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Constructor_declareContext)
            else:
                return self.getTypedRuleContext(D96Parser.Constructor_declareContext,i)


        def destructor_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Destructor_declareContext)
            else:
                return self.getTypedRuleContext(D96Parser.Destructor_declareContext,i)


        def method_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Method_declareContext)
            else:
                return self.getTypedRuleContext(D96Parser.Method_declareContext,i)


        def attribute_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Attribute_declareContext)
            else:
                return self.getTypedRuleContext(D96Parser.Attribute_declareContext,i)


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
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.STATIC_ID))) != 0):
                self.state = 135
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.CONSTRUCTOR]:
                    self.state = 131
                    self.constructor_declare()
                    pass
                elif token in [D96Parser.DESTRUCTOR]:
                    self.state = 132
                    self.destructor_declare()
                    pass
                elif token in [D96Parser.ID, D96Parser.STATIC_ID]:
                    self.state = 133
                    self.method_declare()
                    pass
                elif token in [D96Parser.VAR, D96Parser.VAL]:
                    self.state = 134
                    self.attribute_declare()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 8, self.RULE_constructor_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 141
            self.match(D96Parser.LB)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 142
                self.params_list()


            self.state = 145
            self.match(D96Parser.RB)
            self.state = 146
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
        self.enterRule(localctx, 10, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.params_declare()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 149
                self.match(D96Parser.SEMI)
                self.state = 150
                self.params_declare()
                self.state = 155
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
        self.enterRule(localctx, 12, self.RULE_params_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.id_list()
            self.state = 157
            self.match(D96Parser.COLON)
            self.state = 158
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
        self.enterRule(localctx, 14, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(D96Parser.ID)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 161
                self.match(D96Parser.COMMA)
                self.state = 162
                self.match(D96Parser.ID)
                self.state = 167
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
        self.enterRule(localctx, 16, self.RULE_type_data)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
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
        self.enterRule(localctx, 18, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
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
        self.enterRule(localctx, 20, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(D96Parser.ARRAY)
            self.state = 176
            self.match(D96Parser.LSB)
            self.state = 177
            self.element_type()
            self.state = 178
            self.match(D96Parser.COMMA)
            self.state = 179
            self.size()
            self.state = 180
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
        self.enterRule(localctx, 22, self.RULE_element_type)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING, D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
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
        self.enterRule(localctx, 24, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
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
        self.enterRule(localctx, 26, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
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
        self.enterRule(localctx, 28, self.RULE_destructor_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(D96Parser.DESTRUCTOR)
            self.state = 191
            self.match(D96Parser.LB)
            self.state = 192
            self.match(D96Parser.RB)
            self.state = 193
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
        self.enterRule(localctx, 30, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 196
            self.match(D96Parser.LB)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 197
                self.params_list()


            self.state = 200
            self.match(D96Parser.RB)
            self.state = 201
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
        self.enterRule(localctx, 32, self.RULE_attribute_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 204
            localctx._variable_name_list = self.variable_name_list()
            self.state = 205
            self.match(D96Parser.COLON)
            self.state = 206
            self.type_data()
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EQUAL]:
                self.state = 207
                self.match(D96Parser.EQUAL)
                self.state = 208
                localctx._value_list = self.value_list(localctx._variable_name_list.count)

                self.state = 209
                if not localctx._value_list.count_after == 0:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$value_list.count_after == 0")
                self.state = 210
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.SEMI]:
                self.state = 212
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def STATIC_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.STATIC_ID)
            else:
                return self.getToken(D96Parser.STATIC_ID, i)

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
        self.enterRule(localctx, 34, self.RULE_variable_name_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            localctx.count+=1
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 217
                self.match(D96Parser.COMMA)
                self.state = 218
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.count+=1
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 36, self.RULE_value_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.exp()
            localctx.count-=1
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 227
                    if not localctx.count > 0:
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$count > 0")
                    self.state = 228
                    self.match(D96Parser.COMMA)
                    self.state = 229
                    self.exp()
                    localctx.count-=1 
                self.state = 236
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
        self.enterRule(localctx, 38, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(D96Parser.LP)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.RETURN) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.ID))) != 0):
                self.state = 240
                self.stmt()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
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
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.variable_and_constant_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.assignment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.for_in_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 252
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 253
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 254
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 255
                self.method_invocation_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 256
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
        self.enterRule(localctx, 42, self.RULE_variable_and_constant_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 260
            localctx._variable_name_list_in_method = self.variable_name_list_in_method()
            self.state = 261
            self.match(D96Parser.COLON)
            self.state = 262
            self.type_data()
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EQUAL]:
                self.state = 263
                self.match(D96Parser.EQUAL)
                self.state = 264
                localctx._value_list_stmt = self.value_list_stmt(localctx._variable_name_list_in_method.count)

                self.state = 265
                if not localctx._value_list_stmt.count_after == 0:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$value_list_stmt.count_after == 0")
                self.state = 266
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.SEMI]:
                self.state = 268
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
        self.enterRule(localctx, 44, self.RULE_variable_name_list_in_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(D96Parser.ID)
            localctx.count+=1
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 273
                self.match(D96Parser.COMMA)
                self.state = 274
                self.match(D96Parser.ID)
                localctx.count+=1
                self.state = 280
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
        self.enterRule(localctx, 46, self.RULE_value_list_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.exp()
            localctx.count-=1
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 283
                    if not localctx.count > 0:
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$count > 0")
                    self.state = 284
                    self.match(D96Parser.COMMA)
                    self.state = 285
                    self.exp()
                    localctx.count-=1 
                self.state = 292
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
        self.enterRule(localctx, 48, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.scalar_variable()
            self.state = 296
            self.match(D96Parser.EQUAL)
            self.state = 297
            self.exp()
            self.state = 298
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
        self.enterRule(localctx, 50, self.RULE_scalar_variable)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.name_class()
                self.state = 302
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 303
                self.match(D96Parser.STATIC_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 305
                self.exp8(0)
                self.state = 306
                self.match(D96Parser.DOT)
                self.state = 307
                self.match(D96Parser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 309
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

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_index_exp_for_scalar_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_exp_for_scalar_variable" ):
                return visitor.visitIndex_exp_for_scalar_variable(self)
            else:
                return visitor.visitChildren(self)




    def index_exp_for_scalar_variable(self):

        localctx = D96Parser.Index_exp_for_scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_index_exp_for_scalar_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.exp7(0)
            self.state = 313
            self.match(D96Parser.LSB)
            self.state = 314
            self.exp()
            self.state = 315
            self.match(D96Parser.RSB)
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

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LB)
            else:
                return self.getToken(D96Parser.LB, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RB)
            else:
                return self.getToken(D96Parser.RB, i)

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_stmtContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(D96Parser.IF)
                self.state = 318
                self.match(D96Parser.LB)
                self.state = 319
                self.exp()
                self.state = 320
                self.match(D96Parser.RB)
                self.state = 321
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.match(D96Parser.IF)
                self.state = 324
                self.match(D96Parser.LB)
                self.state = 325
                self.exp()
                self.state = 326
                self.match(D96Parser.RB)
                self.state = 327
                self.block_stmt()
                self.state = 334 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 328
                    self.match(D96Parser.ELSEIF)
                    self.state = 329
                    self.match(D96Parser.LB)
                    self.state = 330
                    self.exp()
                    self.state = 331
                    self.match(D96Parser.RB)
                    self.state = 332
                    self.block_stmt()
                    self.state = 336 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.ELSEIF):
                        break

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
                self.match(D96Parser.IF)
                self.state = 339
                self.match(D96Parser.LB)
                self.state = 340
                self.exp()
                self.state = 341
                self.match(D96Parser.RB)
                self.state = 342
                self.block_stmt()
                self.state = 349 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
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
                    self.state = 351 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.ELSEIF):
                        break

                self.state = 353
                self.match(D96Parser.ELSE)
                self.state = 354
                self.block_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 356
                self.match(D96Parser.IF)
                self.state = 357
                self.match(D96Parser.LB)
                self.state = 358
                self.exp()
                self.state = 359
                self.match(D96Parser.RB)
                self.state = 360
                self.block_stmt()

                self.state = 361
                self.match(D96Parser.ELSE)
                self.state = 362
                self.block_stmt()
                pass


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

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


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
        self.enterRule(localctx, 56, self.RULE_for_in_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(D96Parser.FOREACH)
            self.state = 367
            self.match(D96Parser.LB)
            self.state = 368
            self.scalar_variable()
            self.state = 369
            self.match(D96Parser.IN)
            self.state = 370
            self.exp()
            self.state = 371
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 372
            self.exp()
            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 373
                self.match(D96Parser.BY)
                self.state = 374
                self.exp()


            self.state = 377
            self.match(D96Parser.RB)
            self.state = 378
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
        self.enterRule(localctx, 58, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(D96Parser.BREAK)
            self.state = 381
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
        self.enterRule(localctx, 60, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(D96Parser.CONTINUE)
            self.state = 384
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
        self.enterRule(localctx, 62, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(D96Parser.RETURN)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                self.state = 387
                self.exp()


            self.state = 390
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
        self.enterRule(localctx, 64, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 392
                self.static_method_invocation()
                pass

            elif la_ == 2:
                self.state = 393
                self.instance_method_invocation()
                pass


            self.state = 396
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
        self.enterRule(localctx, 66, self.RULE_static_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.name_class()
            self.state = 399
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 400
            self.match(D96Parser.STATIC_ID)
            self.state = 401
            self.match(D96Parser.LB)
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                self.state = 402
                self.exp_list()


            self.state = 405
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
        self.enterRule(localctx, 68, self.RULE_instance_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.pre_exp(0)
            self.state = 408
            self.match(D96Parser.DOT)
            self.state = 409
            self.match(D96Parser.ID)
            self.state = 410
            self.match(D96Parser.LB)
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                self.state = 411
                self.exp_list()


            self.state = 414
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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_pre_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 430
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Pre_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pre_exp)
                        self.state = 419
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 420
                        self.match(D96Parser.DOT)
                        self.state = 421
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Pre_expContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pre_exp)
                        self.state = 422
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 423
                        self.match(D96Parser.DOT)
                        self.state = 424
                        self.match(D96Parser.ID)
                        self.state = 425
                        self.match(D96Parser.LB)
                        self.state = 427
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                            self.state = 426
                            self.exp_list()


                        self.state = 429
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 72, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.exp1()
                self.state = 436
                _la = self._input.LA(1)
                if not(_la==D96Parser.ADD_STR or _la==D96Parser.IS_EQUAL_STR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 437
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
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
        self.enterRule(localctx, 74, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.exp2(0)
                self.state = 443
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.IS_EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 444
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 457
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 452
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 453
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 454
                    self.exp3(0) 
                self.state = 459
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 468
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 463
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 464
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 465
                    self.exp4(0) 
                self.state = 470
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 479
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 474
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 475
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLY) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 476
                    self.exp5() 
                self.state = 481
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_exp5)
        try:
            self.state = 485
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.match(D96Parser.NOT)
                self.state = 483
                self.exp5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.STRING_LIT, D96Parser.FLOAT_LIT, D96Parser.INT_LIT, D96Parser.ZERO_LIT, D96Parser.SUB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
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
        self.enterRule(localctx, 84, self.RULE_exp6)
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self.match(D96Parser.SUB)
                self.state = 488
                self.exp6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.LB, D96Parser.STRING_LIT, D96Parser.FLOAT_LIT, D96Parser.INT_LIT, D96Parser.ZERO_LIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 499
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 495
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 496
                    self.index_operator() 
                self.state = 501
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_exp8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 518
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 516
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 505
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 506
                        self.match(D96Parser.DOT)
                        self.state = 507
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 508
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 509
                        self.match(D96Parser.DOT)
                        self.state = 510
                        self.match(D96Parser.ID)
                        self.state = 511
                        self.match(D96Parser.LB)
                        self.state = 513
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                            self.state = 512
                            self.exp_list()


                        self.state = 515
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 520
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 90, self.RULE_exp9)
        self._la = 0 # Token type
        try:
            self.state = 533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.match(D96Parser.ID)
                self.state = 522
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 523
                self.match(D96Parser.STATIC_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
                self.match(D96Parser.ID)
                self.state = 525
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 526
                self.match(D96Parser.STATIC_ID)
                self.state = 527
                self.match(D96Parser.LB)
                self.state = 529
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                    self.state = 528
                    self.exp_list()


                self.state = 531
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 532
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
        self.enterRule(localctx, 92, self.RULE_exp10)
        self._la = 0 # Token type
        try:
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.match(D96Parser.NEW)
                self.state = 536
                self.match(D96Parser.ID)
                self.state = 537
                self.match(D96Parser.LB)
                self.state = 539
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                    self.state = 538
                    self.exp_list()


                self.state = 541
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.STRING_LIT, D96Parser.FLOAT_LIT, D96Parser.INT_LIT, D96Parser.ZERO_LIT, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
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
        self.enterRule(localctx, 94, self.RULE_operands)
        try:
            self.state = 553
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
                self.match(D96Parser.LB)
                self.state = 547
                self.exp()
                self.state = 548
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.STRING_LIT, D96Parser.FLOAT_LIT, D96Parser.INT_LIT, D96Parser.ZERO_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 550
                self.literals()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 551
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 552
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
        self.enterRule(localctx, 96, self.RULE_literals)
        try:
            self.state = 561
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ZERO_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.match(D96Parser.ZERO_LIT)
                pass
            elif token in [D96Parser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
                self.match(D96Parser.INT_LIT)
                pass
            elif token in [D96Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 557
                self.match(D96Parser.FLOAT_LIT)
                pass
            elif token in [D96Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 558
                self.match(D96Parser.STRING_LIT)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 559
                self.boolean_literal()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 560
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
        self.enterRule(localctx, 98, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
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
        self.enterRule(localctx, 100, self.RULE_array_literal)
        try:
            self.state = 567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.multidimensional_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
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

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_multidimensional_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultidimensional_array" ):
                return visitor.visitMultidimensional_array(self)
            else:
                return visitor.visitChildren(self)




    def multidimensional_array(self):

        localctx = D96Parser.Multidimensional_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_multidimensional_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(D96Parser.ARRAY)
            self.state = 570
            self.match(D96Parser.LB)
            self.state = 572
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ARRAY:
                self.state = 571
                self.array_list()


            self.state = 574
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
        self.enterRule(localctx, 104, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.array_literal()
            self.state = 581
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 577
                self.match(D96Parser.COMMA)
                self.state = 578
                self.array_literal()
                self.state = 583
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
        self.enterRule(localctx, 106, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.match(D96Parser.ARRAY)
            self.state = 585
            self.match(D96Parser.LB)
            self.state = 587
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.LB) | (1 << D96Parser.STRING_LIT) | (1 << D96Parser.FLOAT_LIT) | (1 << D96Parser.INT_LIT) | (1 << D96Parser.ZERO_LIT) | (1 << D96Parser.NOT) | (1 << D96Parser.SUB) | (1 << D96Parser.ID))) != 0):
                self.state = 586
                self.exp_list()


            self.state = 589
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
        self.enterRule(localctx, 108, self.RULE_exp_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.exp()
            self.state = 596
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 592
                self.match(D96Parser.COMMA)
                self.state = 593
                self.exp()
                self.state = 598
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
        self.enterRule(localctx, 110, self.RULE_index_operator)
        try:
            self.state = 608
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 599
                self.match(D96Parser.LSB)
                self.state = 600
                self.exp()
                self.state = 601
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 603
                self.match(D96Parser.LSB)
                self.state = 604
                self.exp()
                self.state = 605
                self.match(D96Parser.RSB)
                self.state = 606
                self.index_operator()
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
        self._predicates[16] = self.attribute_declare_sempred
        self._predicates[18] = self.value_list_sempred
        self._predicates[21] = self.variable_and_constant_stmt_sempred
        self._predicates[23] = self.value_list_stmt_sempred
        self._predicates[35] = self.pre_exp_sempred
        self._predicates[38] = self.exp2_sempred
        self._predicates[39] = self.exp3_sempred
        self._predicates[40] = self.exp4_sempred
        self._predicates[43] = self.exp7_sempred
        self._predicates[44] = self.exp8_sempred
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
         





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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0243\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\7\2l\n\2\f\2\16\2o\13\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3w\n\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\7\5\u0083\n\5\f\5\16\5\u0086\13\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\7\6\u008e\n\6\f\6\16\6\u0091\13\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\5\7\u009a\n\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\7\b\u00a3\n\b\f\b\16\b\u00a6\13\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\5\t\u00ae\n\t\3\t\3\t\3\t\3\n\3\n\3\n\5\n\u00b6")
        buf.write("\n\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\7\f\u00c3\n\f\f\f\16\f\u00c6\13\f\3\r\3\r\3\r\7\r\u00cb")
        buf.write("\n\r\f\r\16\r\u00ce\13\r\3\r\3\r\3\r\3\16\3\16\5\16\u00d5")
        buf.write("\n\16\3\17\3\17\3\20\3\20\5\20\u00db\n\20\3\21\3\21\3")
        buf.write("\21\5\21\u00e0\n\21\3\21\3\21\3\22\3\22\3\22\5\22\u00e7")
        buf.write("\n\22\3\22\3\22\3\23\3\23\3\23\7\23\u00ee\n\23\f\23\16")
        buf.write("\23\u00f1\13\23\3\24\3\24\3\24\5\24\u00f6\n\24\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\5\26\u00fe\n\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\7\30\u0108\n\30\f\30\16\30\u010b")
        buf.write("\13\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u0117\n\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32")
        buf.write("\u011f\n\32\f\32\16\32\u0122\13\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\5\33\u012b\n\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\7\34\u0134\n\34\f\34\16\34\u0137\13\34\3")
        buf.write("\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u0145\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\6\37\u015a\n\37\r\37\16\37\u015b\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\6\37\u0164\n\37\r\37\16\37\u0165")
        buf.write("\3\37\3\37\5\37\u016a\n\37\3 \3 \3 \3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u017e\n\"\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3%\5%\u018f")
        buf.write("\n%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\5\'\u0199\n\'\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3)\3)\3)\5)\u01a4\n)\3*\3*\3*\3*\3*\5*\u01ab")
        buf.write("\n*\3+\3+\3+\3+\3+\3+\7+\u01b3\n+\f+\16+\u01b6\13+\3,")
        buf.write("\3,\3,\3,\3,\3,\7,\u01be\n,\f,\16,\u01c1\13,\3-\3-\3-")
        buf.write("\3-\3-\3-\7-\u01c9\n-\f-\16-\u01cc\13-\3.\3.\3.\5.\u01d1")
        buf.write("\n.\3/\3/\3/\3/\3/\5/\u01d8\n/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u01ea\n\60\3\60\3\60\3\60\3\60\3\60\7\60\u01f1\n")
        buf.write("\60\f\60\16\60\u01f4\13\60\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\5\61\u01ff\n\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\5\61\u020a\n\61\3\61\3\61\5")
        buf.write("\61\u020e\n\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\5\61\u0218\n\61\3\61\7\61\u021b\n\61\f\61\16\61\u021e")
        buf.write("\13\61\3\62\3\62\3\62\5\62\u0223\n\62\3\62\3\62\3\63\3")
        buf.write("\63\3\63\3\63\5\63\u022b\n\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0239\n\64\3")
        buf.write("\65\3\65\3\65\7\65\u023e\n\65\f\65\16\65\u0241\13\65\3")
        buf.write("\65\2\7TVX^`\66\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh\2\f\3")
        buf.write("\2\n\13\3\2;<\3\2\32\35\3\2\26\31\3\2-.\4\2&&(,\3\2$%")
        buf.write("\3\2\36\37\3\2 \"\4\2\f\f;;\2\u0257\2m\3\2\2\2\4r\3\2")
        buf.write("\2\2\6|\3\2\2\2\b\u0084\3\2\2\2\n\u0087\3\2\2\2\f\u0099")
        buf.write("\3\2\2\2\16\u009b\3\2\2\2\20\u00aa\3\2\2\2\22\u00b2\3")
        buf.write("\2\2\2\24\u00ba\3\2\2\2\26\u00bf\3\2\2\2\30\u00c7\3\2")
        buf.write("\2\2\32\u00d4\3\2\2\2\34\u00d6\3\2\2\2\36\u00da\3\2\2")
        buf.write("\2 \u00dc\3\2\2\2\"\u00e3\3\2\2\2$\u00ea\3\2\2\2&\u00f5")
        buf.write("\3\2\2\2(\u00f7\3\2\2\2*\u00f9\3\2\2\2,\u0103\3\2\2\2")
        buf.write(".\u0105\3\2\2\2\60\u0116\3\2\2\2\62\u0118\3\2\2\2\64\u012a")
        buf.write("\3\2\2\2\66\u012c\3\2\2\28\u013b\3\2\2\2:\u0144\3\2\2")
        buf.write("\2<\u0169\3\2\2\2>\u016b\3\2\2\2@\u0171\3\2\2\2B\u0174")
        buf.write("\3\2\2\2D\u0182\3\2\2\2F\u0185\3\2\2\2H\u018e\3\2\2\2")
        buf.write("J\u0190\3\2\2\2L\u0193\3\2\2\2N\u019c\3\2\2\2P\u01a3\3")
        buf.write("\2\2\2R\u01aa\3\2\2\2T\u01ac\3\2\2\2V\u01b7\3\2\2\2X\u01c2")
        buf.write("\3\2\2\2Z\u01d0\3\2\2\2\\\u01d7\3\2\2\2^\u01e9\3\2\2\2")
        buf.write("`\u020d\3\2\2\2b\u021f\3\2\2\2d\u0226\3\2\2\2f\u0238\3")
        buf.write("\2\2\2h\u023a\3\2\2\2jl\5\4\3\2kj\3\2\2\2lo\3\2\2\2mk")
        buf.write("\3\2\2\2mn\3\2\2\2np\3\2\2\2om\3\2\2\2pq\7\2\2\3q\3\3")
        buf.write("\2\2\2rs\7\24\2\2sv\5\6\4\2tu\7\67\2\2uw\5\6\4\2vt\3\2")
        buf.write("\2\2vw\3\2\2\2wx\3\2\2\2xy\79\2\2yz\5\b\5\2z{\7:\2\2{")
        buf.write("\5\3\2\2\2|}\7;\2\2}\7\3\2\2\2~\u0083\5\n\6\2\177\u0083")
        buf.write("\5\20\t\2\u0080\u0083\5\22\n\2\u0081\u0083\5\24\13\2\u0082")
        buf.write("~\3\2\2\2\u0082\177\3\2\2\2\u0082\u0080\3\2\2\2\u0082")
        buf.write("\u0081\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082\3\2\2\2")
        buf.write("\u0084\u0085\3\2\2\2\u0085\t\3\2\2\2\u0086\u0084\3\2\2")
        buf.write("\2\u0087\u0088\t\2\2\2\u0088\u0089\t\3\2\2\u0089\u008f")
        buf.write("\b\6\1\2\u008a\u008b\7\65\2\2\u008b\u008c\t\3\2\2\u008c")
        buf.write("\u008e\b\6\1\2\u008d\u008a\3\2\2\2\u008e\u0091\3\2\2\2")
        buf.write("\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0092\3")
        buf.write("\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\7\67\2\2\u0093")
        buf.write("\u0094\5&\24\2\u0094\u0095\5\f\7\2\u0095\13\3\2\2\2\u0096")
        buf.write("\u0097\7\'\2\2\u0097\u009a\5\16\b\2\u0098\u009a\7\66\2")
        buf.write("\2\u0099\u0096\3\2\2\2\u0099\u0098\3\2\2\2\u009a\r\3\2")
        buf.write("\2\2\u009b\u009c\5N(\2\u009c\u00a4\b\b\1\2\u009d\u009e")
        buf.write("\6\b\2\3\u009e\u009f\7\65\2\2\u009f\u00a0\5N(\2\u00a0")
        buf.write("\u00a1\b\b\1\2\u00a1\u00a3\3\2\2\2\u00a2\u009d\3\2\2\2")
        buf.write("\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3")
        buf.write("\2\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a8")
        buf.write("\6\b\3\3\u00a8\u00a9\7\66\2\2\u00a9\17\3\2\2\2\u00aa\u00ab")
        buf.write("\t\3\2\2\u00ab\u00ad\7/\2\2\u00ac\u00ae\5\26\f\2\u00ad")
        buf.write("\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00af\u00b0\7\60\2\2\u00b0\u00b1\5.\30\2\u00b1\21\3\2")
        buf.write("\2\2\u00b2\u00b3\7\21\2\2\u00b3\u00b5\7/\2\2\u00b4\u00b6")
        buf.write("\5\26\f\2\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\u00b7\3\2\2\2\u00b7\u00b8\7\60\2\2\u00b8\u00b9\5.\30")
        buf.write("\2\u00b9\23\3\2\2\2\u00ba\u00bb\7\22\2\2\u00bb\u00bc\7")
        buf.write("/\2\2\u00bc\u00bd\7\60\2\2\u00bd\u00be\5.\30\2\u00be\25")
        buf.write("\3\2\2\2\u00bf\u00c4\5\30\r\2\u00c0\u00c1\7\66\2\2\u00c1")
        buf.write("\u00c3\5\30\r\2\u00c2\u00c0\3\2\2\2\u00c3\u00c6\3\2\2")
        buf.write("\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\27\3")
        buf.write("\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00cc\7;\2\2\u00c8\u00c9")
        buf.write("\7\65\2\2\u00c9\u00cb\7;\2\2\u00ca\u00c8\3\2\2\2\u00cb")
        buf.write("\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\7")
        buf.write("\67\2\2\u00d0\u00d1\5&\24\2\u00d1\31\3\2\2\2\u00d2\u00d5")
        buf.write("\5\36\20\2\u00d3\u00d5\5\34\17\2\u00d4\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d3\3\2\2\2\u00d5\33\3\2\2\2\u00d6\u00d7\t\4\2\2\u00d7")
        buf.write("\35\3\2\2\2\u00d8\u00db\5 \21\2\u00d9\u00db\5\"\22\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\37\3\2\2\2\u00dc")
        buf.write("\u00dd\7\25\2\2\u00dd\u00df\7/\2\2\u00de\u00e0\5h\65\2")
        buf.write("\u00df\u00de\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\3")
        buf.write("\2\2\2\u00e1\u00e2\7\60\2\2\u00e2!\3\2\2\2\u00e3\u00e4")
        buf.write("\7\25\2\2\u00e4\u00e6\7/\2\2\u00e5\u00e7\5$\23\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e9\7\60\2\2\u00e9#\3\2\2\2\u00ea\u00ef\5\36")
        buf.write("\20\2\u00eb\u00ec\7\65\2\2\u00ec\u00ee\5\36\20\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00ef\u00f0\3\2\2\2\u00f0%\3\2\2\2\u00f1\u00ef\3\2\2")
        buf.write("\2\u00f2\u00f6\5(\25\2\u00f3\u00f6\5*\26\2\u00f4\u00f6")
        buf.write("\5,\27\2\u00f5\u00f2\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5")
        buf.write("\u00f4\3\2\2\2\u00f6\'\3\2\2\2\u00f7\u00f8\t\5\2\2\u00f8")
        buf.write(")\3\2\2\2\u00f9\u00fa\7\25\2\2\u00fa\u00fd\7\61\2\2\u00fb")
        buf.write("\u00fe\5(\25\2\u00fc\u00fe\5*\26\2\u00fd\u00fb\3\2\2\2")
        buf.write("\u00fd\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\7")
        buf.write("\65\2\2\u0100\u0101\7\32\2\2\u0101\u0102\7\62\2\2\u0102")
        buf.write("+\3\2\2\2\u0103\u0104\7;\2\2\u0104-\3\2\2\2\u0105\u0109")
        buf.write("\79\2\2\u0106\u0108\5\60\31\2\u0107\u0106\3\2\2\2\u0108")
        buf.write("\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2")
        buf.write("\u010a\u010c\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d\7")
        buf.write(":\2\2\u010d/\3\2\2\2\u010e\u0117\5\62\32\2\u010f\u0117")
        buf.write("\58\35\2\u0110\u0117\5<\37\2\u0111\u0117\5B\"\2\u0112")
        buf.write("\u0117\5D#\2\u0113\u0117\5F$\2\u0114\u0117\5H%\2\u0115")
        buf.write("\u0117\5J&\2\u0116\u010e\3\2\2\2\u0116\u010f\3\2\2\2\u0116")
        buf.write("\u0110\3\2\2\2\u0116\u0111\3\2\2\2\u0116\u0112\3\2\2\2")
        buf.write("\u0116\u0113\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0115\3")
        buf.write("\2\2\2\u0117\61\3\2\2\2\u0118\u0119\t\2\2\2\u0119\u011a")
        buf.write("\7;\2\2\u011a\u0120\b\32\1\2\u011b\u011c\7\65\2\2\u011c")
        buf.write("\u011d\t\3\2\2\u011d\u011f\b\32\1\2\u011e\u011b\3\2\2")
        buf.write("\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0120\3\2\2\2\u0123")
        buf.write("\u0124\7\67\2\2\u0124\u0125\5&\24\2\u0125\u0126\5\64\33")
        buf.write("\2\u0126\63\3\2\2\2\u0127\u0128\7\'\2\2\u0128\u012b\5")
        buf.write("\66\34\2\u0129\u012b\7\66\2\2\u012a\u0127\3\2\2\2\u012a")
        buf.write("\u0129\3\2\2\2\u012b\65\3\2\2\2\u012c\u012d\5N(\2\u012d")
        buf.write("\u0135\b\34\1\2\u012e\u012f\6\34\4\3\u012f\u0130\7\65")
        buf.write("\2\2\u0130\u0131\5N(\2\u0131\u0132\b\34\1\2\u0132\u0134")
        buf.write("\3\2\2\2\u0133\u012e\3\2\2\2\u0134\u0137\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0138\3\2\2\2")
        buf.write("\u0137\u0135\3\2\2\2\u0138\u0139\6\34\5\3\u0139\u013a")
        buf.write("\7\66\2\2\u013a\67\3\2\2\2\u013b\u013c\5:\36\2\u013c\u013d")
        buf.write("\7\'\2\2\u013d\u013e\5N(\2\u013e\u013f\7\66\2\2\u013f")
        buf.write("9\3\2\2\2\u0140\u0145\7;\2\2\u0141\u0145\7<\2\2\u0142")
        buf.write("\u0145\5^\60\2\u0143\u0145\5`\61\2\u0144\u0140\3\2\2\2")
        buf.write("\u0144\u0141\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0143\3")
        buf.write("\2\2\2\u0145;\3\2\2\2\u0146\u0147\7\6\2\2\u0147\u0148")
        buf.write("\7/\2\2\u0148\u0149\5N(\2\u0149\u014a\7\60\2\2\u014a\u014b")
        buf.write("\5.\30\2\u014b\u016a\3\2\2\2\u014c\u014d\7\6\2\2\u014d")
        buf.write("\u014e\7/\2\2\u014e\u014f\5N(\2\u014f\u0150\7\60\2\2\u0150")
        buf.write("\u0151\5.\30\2\u0151\u0152\5@!\2\u0152\u016a\3\2\2\2\u0153")
        buf.write("\u0154\7\6\2\2\u0154\u0155\7/\2\2\u0155\u0156\5N(\2\u0156")
        buf.write("\u0157\7\60\2\2\u0157\u0159\5.\30\2\u0158\u015a\5> \2")
        buf.write("\u0159\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0159\3")
        buf.write("\2\2\2\u015b\u015c\3\2\2\2\u015c\u016a\3\2\2\2\u015d\u015e")
        buf.write("\7\6\2\2\u015e\u015f\7/\2\2\u015f\u0160\5N(\2\u0160\u0161")
        buf.write("\7\60\2\2\u0161\u0163\5.\30\2\u0162\u0164\5> \2\u0163")
        buf.write("\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0165\u0166\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\5")
        buf.write("@!\2\u0168\u016a\3\2\2\2\u0169\u0146\3\2\2\2\u0169\u014c")
        buf.write("\3\2\2\2\u0169\u0153\3\2\2\2\u0169\u015d\3\2\2\2\u016a")
        buf.write("=\3\2\2\2\u016b\u016c\7\7\2\2\u016c\u016d\7/\2\2\u016d")
        buf.write("\u016e\5N(\2\u016e\u016f\7\60\2\2\u016f\u0170\5.\30\2")
        buf.write("\u0170?\3\2\2\2\u0171\u0172\7\b\2\2\u0172\u0173\5.\30")
        buf.write("\2\u0173A\3\2\2\2\u0174\u0175\7\t\2\2\u0175\u0176\7/\2")
        buf.write("\2\u0176\u0177\t\3\2\2\u0177\u0178\7\16\2\2\u0178\u0179")
        buf.write("\5N(\2\u0179\u017a\7\64\2\2\u017a\u017d\5N(\2\u017b\u017c")
        buf.write("\7\17\2\2\u017c\u017e\5N(\2\u017d\u017b\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\7\60\2")
        buf.write("\2\u0180\u0181\5.\30\2\u0181C\3\2\2\2\u0182\u0183\7\4")
        buf.write("\2\2\u0183\u0184\7\66\2\2\u0184E\3\2\2\2\u0185\u0186\7")
        buf.write("\5\2\2\u0186\u0187\7\66\2\2\u0187G\3\2\2\2\u0188\u0189")
        buf.write("\7\r\2\2\u0189\u018a\5N(\2\u018a\u018b\7\66\2\2\u018b")
        buf.write("\u018f\3\2\2\2\u018c\u018d\7\r\2\2\u018d\u018f\7\66\2")
        buf.write("\2\u018e\u0188\3\2\2\2\u018e\u018c\3\2\2\2\u018fI\3\2")
        buf.write("\2\2\u0190\u0191\5`\61\2\u0191\u0192\7\66\2\2\u0192K\3")
        buf.write("\2\2\2\u0193\u0194\5N(\2\u0194\u0195\7\63\2\2\u0195\u0196")
        buf.write("\7;\2\2\u0196\u0198\7/\2\2\u0197\u0199\5h\65\2\u0198\u0197")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u019b\7\60\2\2\u019bM\3\2\2\2\u019c\u019d\5P)\2\u019d")
        buf.write("O\3\2\2\2\u019e\u019f\5R*\2\u019f\u01a0\t\6\2\2\u01a0")
        buf.write("\u01a1\5R*\2\u01a1\u01a4\3\2\2\2\u01a2\u01a4\5R*\2\u01a3")
        buf.write("\u019e\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4Q\3\2\2\2\u01a5")
        buf.write("\u01a6\5T+\2\u01a6\u01a7\t\7\2\2\u01a7\u01a8\5T+\2\u01a8")
        buf.write("\u01ab\3\2\2\2\u01a9\u01ab\5T+\2\u01aa\u01a5\3\2\2\2\u01aa")
        buf.write("\u01a9\3\2\2\2\u01abS\3\2\2\2\u01ac\u01ad\b+\1\2\u01ad")
        buf.write("\u01ae\5V,\2\u01ae\u01b4\3\2\2\2\u01af\u01b0\f\4\2\2\u01b0")
        buf.write("\u01b1\t\b\2\2\u01b1\u01b3\5V,\2\u01b2\u01af\3\2\2\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5U\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b8\b,\1\2")
        buf.write("\u01b8\u01b9\5X-\2\u01b9\u01bf\3\2\2\2\u01ba\u01bb\f\4")
        buf.write("\2\2\u01bb\u01bc\t\t\2\2\u01bc\u01be\5X-\2\u01bd\u01ba")
        buf.write("\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf")
        buf.write("\u01c0\3\2\2\2\u01c0W\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2")
        buf.write("\u01c3\b-\1\2\u01c3\u01c4\5Z.\2\u01c4\u01ca\3\2\2\2\u01c5")
        buf.write("\u01c6\f\4\2\2\u01c6\u01c7\t\n\2\2\u01c7\u01c9\5Z.\2\u01c8")
        buf.write("\u01c5\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01ca\u01cb\3\2\2\2\u01cbY\3\2\2\2\u01cc\u01ca\3\2\2")
        buf.write("\2\u01cd\u01ce\7#\2\2\u01ce\u01d1\5Z.\2\u01cf\u01d1\5")
        buf.write("\\/\2\u01d0\u01cd\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1[\3")
        buf.write("\2\2\2\u01d2\u01d3\7\37\2\2\u01d3\u01d8\5\\/\2\u01d4\u01d8")
        buf.write("\5^\60\2\u01d5\u01d8\5`\61\2\u01d6\u01d8\5f\64\2\u01d7")
        buf.write("\u01d2\3\2\2\2\u01d7\u01d4\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d6\3\2\2\2\u01d8]\3\2\2\2\u01d9\u01da\b\60\1")
        buf.write("\2\u01da\u01db\5`\61\2\u01db\u01dc\7\61\2\2\u01dc\u01dd")
        buf.write("\5N(\2\u01dd\u01de\7\62\2\2\u01de\u01ea\3\2\2\2\u01df")
        buf.write("\u01e0\7;\2\2\u01e0\u01e1\7\61\2\2\u01e1\u01e2\5N(\2\u01e2")
        buf.write("\u01e3\7\62\2\2\u01e3\u01ea\3\2\2\2\u01e4\u01e5\7<\2\2")
        buf.write("\u01e5\u01e6\7\61\2\2\u01e6\u01e7\5N(\2\u01e7\u01e8\7")
        buf.write("\62\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01d9\3\2\2\2\u01e9")
        buf.write("\u01df\3\2\2\2\u01e9\u01e4\3\2\2\2\u01ea\u01f2\3\2\2\2")
        buf.write("\u01eb\u01ec\f\6\2\2\u01ec\u01ed\7\61\2\2\u01ed\u01ee")
        buf.write("\5N(\2\u01ee\u01ef\7\62\2\2\u01ef\u01f1\3\2\2\2\u01f0")
        buf.write("\u01eb\3\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3_\3\2\2\2\u01f4\u01f2\3\2\2")
        buf.write("\2\u01f5\u01f6\b\61\1\2\u01f6\u01f7\7;\2\2\u01f7\u01f8")
        buf.write("\78\2\2\u01f8\u020e\7<\2\2\u01f9\u01fa\7;\2\2\u01fa\u01fb")
        buf.write("\78\2\2\u01fb\u01fc\7<\2\2\u01fc\u01fe\7/\2\2\u01fd\u01ff")
        buf.write("\5h\65\2\u01fe\u01fd\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u020e\7\60\2\2\u0201\u0202\t\13\2")
        buf.write("\2\u0202\u0203\7\63\2\2\u0203\u020e\t\3\2\2\u0204\u0205")
        buf.write("\t\13\2\2\u0205\u0206\7\63\2\2\u0206\u0207\7;\2\2\u0207")
        buf.write("\u0209\7/\2\2\u0208\u020a\5h\65\2\u0209\u0208\3\2\2\2")
        buf.write("\u0209\u020a\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020e\7")
        buf.write("\60\2\2\u020c\u020e\5b\62\2\u020d\u01f5\3\2\2\2\u020d")
        buf.write("\u01f9\3\2\2\2\u020d\u0201\3\2\2\2\u020d\u0204\3\2\2\2")
        buf.write("\u020d\u020c\3\2\2\2\u020e\u021c\3\2\2\2\u020f\u0210\f")
        buf.write("\t\2\2\u0210\u0211\7\63\2\2\u0211\u021b\7;\2\2\u0212\u0213")
        buf.write("\f\b\2\2\u0213\u0214\7\63\2\2\u0214\u0215\7;\2\2\u0215")
        buf.write("\u0217\7/\2\2\u0216\u0218\5h\65\2\u0217\u0216\3\2\2\2")
        buf.write("\u0217\u0218\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021b\7")
        buf.write("\60\2\2\u021a\u020f\3\2\2\2\u021a\u0212\3\2\2\2\u021b")
        buf.write("\u021e\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2")
        buf.write("\u021da\3\2\2\2\u021e\u021c\3\2\2\2\u021f\u0220\t\3\2")
        buf.write("\2\u0220\u0222\7/\2\2\u0221\u0223\5h\65\2\u0222\u0221")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0224\3\2\2\2\u0224")
        buf.write("\u0225\7\60\2\2\u0225c\3\2\2\2\u0226\u0227\7\20\2\2\u0227")
        buf.write("\u0228\7;\2\2\u0228\u022a\7/\2\2\u0229\u022b\5h\65\2\u022a")
        buf.write("\u0229\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c\3\2\2\2")
        buf.write("\u022c\u022d\7\60\2\2\u022de\3\2\2\2\u022e\u0239\5d\63")
        buf.write("\2\u022f\u0239\7<\2\2\u0230\u0239\7;\2\2\u0231\u0239\7")
        buf.write("\f\2\2\u0232\u0239\5\32\16\2\u0233\u0239\7\23\2\2\u0234")
        buf.write("\u0235\7/\2\2\u0235\u0236\5N(\2\u0236\u0237\7\60\2\2\u0237")
        buf.write("\u0239\3\2\2\2\u0238\u022e\3\2\2\2\u0238\u022f\3\2\2\2")
        buf.write("\u0238\u0230\3\2\2\2\u0238\u0231\3\2\2\2\u0238\u0232\3")
        buf.write("\2\2\2\u0238\u0233\3\2\2\2\u0238\u0234\3\2\2\2\u0239g")
        buf.write("\3\2\2\2\u023a\u023f\5N(\2\u023b\u023c\7\65\2\2\u023c")
        buf.write("\u023e\5N(\2\u023d\u023b\3\2\2\2\u023e\u0241\3\2\2\2\u023f")
        buf.write("\u023d\3\2\2\2\u023f\u0240\3\2\2\2\u0240i\3\2\2\2\u0241")
        buf.write("\u023f\3\2\2\2\63mv\u0082\u0084\u008f\u0099\u00a4\u00ad")
        buf.write("\u00b5\u00c4\u00cc\u00d4\u00da\u00df\u00e6\u00ef\u00f5")
        buf.write("\u00fd\u0109\u0116\u0120\u012a\u0135\u0144\u015b\u0165")
        buf.write("\u0169\u017d\u018e\u0198\u01a3\u01aa\u01b4\u01bf\u01ca")
        buf.write("\u01d0\u01d7\u01e9\u01f2\u01fe\u0209\u020d\u0217\u021a")
        buf.write("\u021c\u0222\u022a\u0238\u023f")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Var'", 
                     "'Val'", "'Self'", "'Return'", "'In'", "'By'", "'New'", 
                     "'Constructor'", "'Destructor'", "'Null'", "'Class'", 
                     "'Array'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'==.'", "'+.'", "'('", "')'", "'['", "']'", "'.'", 
                     "'..'", "','", "';'", "':'", "'::'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "VAR", "VAL", "SELF", 
                      "RETURN", "IN", "BY", "NEW", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NULL", "CLASS", "ARRAY", "INTEGER", "FLOAT", "BOOLEAN", 
                      "STRING", "INTEGER_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "FLOAT_LITERAL", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                      "LT", "LTE", "GT", "GTE", "STRING_EQUAL", "STRING_ADD", 
                      "LP", "RP", "LSB", "RSB", "DOT", "DOUBLE_DOT", "COMMA", 
                      "SEMI", "COLON", "DOUBLE_COLON", "LCB", "RCB", "ID", 
                      "DOLLAR_ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_class_declaration = 1
    RULE_class_name = 2
    RULE_class_body = 3
    RULE_attribute_declaration = 4
    RULE_attribute_initialization = 5
    RULE_attribute_initialization_list = 6
    RULE_method_declaration = 7
    RULE_constructor_declaration = 8
    RULE_destructor_declaration = 9
    RULE_list_of_parameters = 10
    RULE_parameter_declaration = 11
    RULE_literal = 12
    RULE_primitive_literal = 13
    RULE_array_literal = 14
    RULE_indexed_array = 15
    RULE_multi_demensional_array = 16
    RULE_array_literal_list = 17
    RULE_type_name = 18
    RULE_primitive_type = 19
    RULE_array_type = 20
    RULE_class_type = 21
    RULE_block_statement = 22
    RULE_statement = 23
    RULE_variable_and_const_declaration = 24
    RULE_variable_initialization = 25
    RULE_variable_initialization_list = 26
    RULE_assign_statement = 27
    RULE_left_hand_side = 28
    RULE_if_statement = 29
    RULE_elseif_statement = 30
    RULE_else_statement = 31
    RULE_foreach_statement = 32
    RULE_break_statement = 33
    RULE_continue_statement = 34
    RULE_return_statement = 35
    RULE_method_invocation_statement = 36
    RULE_instance_method_invocation = 37
    RULE_expression = 38
    RULE_string_expression = 39
    RULE_relation_expression = 40
    RULE_logical_expression = 41
    RULE_adding_expression = 42
    RULE_multiplying_expression = 43
    RULE_negative_expression = 44
    RULE_sign_expression = 45
    RULE_index_expression = 46
    RULE_member_access_expression = 47
    RULE_self_method_call = 48
    RULE_object_creation_expression = 49
    RULE_operand = 50
    RULE_list_of_expressions = 51

    ruleNames =  [ "program", "class_declaration", "class_name", "class_body", 
                   "attribute_declaration", "attribute_initialization", 
                   "attribute_initialization_list", "method_declaration", 
                   "constructor_declaration", "destructor_declaration", 
                   "list_of_parameters", "parameter_declaration", "literal", 
                   "primitive_literal", "array_literal", "indexed_array", 
                   "multi_demensional_array", "array_literal_list", "type_name", 
                   "primitive_type", "array_type", "class_type", "block_statement", 
                   "statement", "variable_and_const_declaration", "variable_initialization", 
                   "variable_initialization_list", "assign_statement", "left_hand_side", 
                   "if_statement", "elseif_statement", "else_statement", 
                   "foreach_statement", "break_statement", "continue_statement", 
                   "return_statement", "method_invocation_statement", "instance_method_invocation", 
                   "expression", "string_expression", "relation_expression", 
                   "logical_expression", "adding_expression", "multiplying_expression", 
                   "negative_expression", "sign_expression", "index_expression", 
                   "member_access_expression", "self_method_call", "object_creation_expression", 
                   "operand", "list_of_expressions" ]

    EOF = Token.EOF
    COMMENT=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    FOREACH=7
    VAR=8
    VAL=9
    SELF=10
    RETURN=11
    IN=12
    BY=13
    NEW=14
    CONSTRUCTOR=15
    DESTRUCTOR=16
    NULL=17
    CLASS=18
    ARRAY=19
    INTEGER=20
    FLOAT=21
    BOOLEAN=22
    STRING=23
    INTEGER_LITERAL=24
    STRING_LITERAL=25
    BOOLEAN_LITERAL=26
    FLOAT_LITERAL=27
    ADD=28
    SUB=29
    MUL=30
    DIV=31
    MOD=32
    NOT=33
    AND=34
    OR=35
    EQUAL=36
    ASSIGN=37
    NOT_EQUAL=38
    LT=39
    LTE=40
    GT=41
    GTE=42
    STRING_EQUAL=43
    STRING_ADD=44
    LP=45
    RP=46
    LSB=47
    RSB=48
    DOT=49
    DOUBLE_DOT=50
    COMMA=51
    SEMI=52
    COLON=53
    DOUBLE_COLON=54
    LCB=55
    RCB=56
    ID=57
    DOLLAR_ID=58
    WS=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_TOKEN=62

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

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationContext,i)


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
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CLASS:
                self.state = 104
                self.class_declaration()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def class_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_nameContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_nameContext,i)


        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(D96Parser.CLASS)
            self.state = 113
            self.class_name()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 114
                self.match(D96Parser.COLON)
                self.state = 115
                self.class_name()


            self.state = 118
            self.match(D96Parser.LCB)
            self.state = 119
            self.class_body()
            self.state = 120
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_name" ):
                return visitor.visitClass_name(self)
            else:
                return visitor.visitChildren(self)




    def class_name(self):

        localctx = D96Parser.Class_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Attribute_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Attribute_declarationContext,i)


        def method_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Method_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Method_declarationContext,i)


        def constructor_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Constructor_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Constructor_declarationContext,i)


        def destructor_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Destructor_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Destructor_declarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 128
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAR, D96Parser.VAL]:
                    self.state = 124
                    self.attribute_declaration()
                    pass
                elif token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                    self.state = 125
                    self.method_declaration()
                    pass
                elif token in [D96Parser.CONSTRUCTOR]:
                    self.state = 126
                    self.constructor_declaration()
                    pass
                elif token in [D96Parser.DESTRUCTOR]:
                    self.state = 127
                    self.destructor_declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number_attribute = 0

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def attribute_initialization(self):
            return self.getTypedRuleContext(D96Parser.Attribute_initializationContext,0)


        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def DOLLAR_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR_ID)
            else:
                return self.getToken(D96Parser.DOLLAR_ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declaration" ):
                return visitor.visitAttribute_declaration(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 134
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.getInvokingContext(4).number_attribute+=1
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 136
                self.match(D96Parser.COMMA)
                self.state = 137
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.getInvokingContext(4).number_attribute+=1
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(D96Parser.COLON)
            self.state = 145
            self.type_name()
            self.state = 146
            self.attribute_initialization()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def attribute_initialization_list(self):
            return self.getTypedRuleContext(D96Parser.Attribute_initialization_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_initialization" ):
                return visitor.visitAttribute_initialization(self)
            else:
                return visitor.visitChildren(self)




    def attribute_initialization(self):

        localctx = D96Parser.Attribute_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute_initialization)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(D96Parser.ASSIGN)
                self.state = 149
                self.attribute_initialization_list()
                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
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


    class Attribute_initialization_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_initialization_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_initialization_list" ):
                return visitor.visitAttribute_initialization_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_initialization_list(self):

        localctx = D96Parser.Attribute_initialization_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute_initialization_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.expression()
            self.getInvokingContext(4).number_attribute -= 1
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 155
                    if not self.getInvokingContext(4).number_attribute > 0:
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$attribute_declaration::number_attribute > 0")
                    self.state = 156
                    self.match(D96Parser.COMMA)
                    self.state = 157
                    self.expression()
                    self.getInvokingContext(4).number_attribute -= 1 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 165
            if not self.getInvokingContext(4).number_attribute == 0:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$attribute_declaration::number_attribute == 0")
            self.state = 166
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def list_of_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_of_parametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declaration" ):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 169
            self.match(D96Parser.LP)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 170
                self.list_of_parameters()


            self.state = 173
            self.match(D96Parser.RP)
            self.state = 174
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def list_of_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_of_parametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_declaration" ):
                return visitor.visitConstructor_declaration(self)
            else:
                return visitor.visitChildren(self)




    def constructor_declaration(self):

        localctx = D96Parser.Constructor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 177
            self.match(D96Parser.LP)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 178
                self.list_of_parameters()


            self.state = 181
            self.match(D96Parser.RP)
            self.state = 182
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor_declaration" ):
                return visitor.visitDestructor_declaration(self)
            else:
                return visitor.visitChildren(self)




    def destructor_declaration(self):

        localctx = D96Parser.Destructor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_destructor_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(D96Parser.DESTRUCTOR)
            self.state = 185
            self.match(D96Parser.LP)
            self.state = 186
            self.match(D96Parser.RP)
            self.state = 187
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Parameter_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Parameter_declarationContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_of_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_parameters" ):
                return visitor.visitList_of_parameters(self)
            else:
                return visitor.visitChildren(self)




    def list_of_parameters(self):

        localctx = D96Parser.List_of_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_of_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.parameter_declaration()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 190
                self.match(D96Parser.SEMI)
                self.state = 191
                self.parameter_declaration()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


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
            return D96Parser.RULE_parameter_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration" ):
                return visitor.visitParameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration(self):

        localctx = D96Parser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(D96Parser.ID)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 198
                self.match(D96Parser.COMMA)
                self.state = 199
                self.match(D96Parser.ID)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self.match(D96Parser.COLON)
            self.state = 206
            self.type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal(self):
            return self.getTypedRuleContext(D96Parser.Array_literalContext,0)


        def primitive_literal(self):
            return self.getTypedRuleContext(D96Parser.Primitive_literalContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_literal)
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.array_literal()
                pass
            elif token in [D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.primitive_literal()
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


    class Primitive_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(D96Parser.BOOLEAN_LITERAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_literal" ):
                return visitor.visitPrimitive_literal(self)
            else:
                return visitor.visitChildren(self)




    def primitive_literal(self):

        localctx = D96Parser.Primitive_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitive_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL))) != 0)):
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

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def multi_demensional_array(self):
            return self.getTypedRuleContext(D96Parser.Multi_demensional_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = D96Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_literal)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.indexed_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.multi_demensional_array()
                pass


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

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexed_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array" ):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(D96Parser.ARRAY)
            self.state = 219
            self.match(D96Parser.LP)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 220
                self.list_of_expressions()


            self.state = 223
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_demensional_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def array_literal_list(self):
            return self.getTypedRuleContext(D96Parser.Array_literal_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_multi_demensional_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_demensional_array" ):
                return visitor.visitMulti_demensional_array(self)
            else:
                return visitor.visitChildren(self)




    def multi_demensional_array(self):

        localctx = D96Parser.Multi_demensional_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_multi_demensional_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(D96Parser.ARRAY)
            self.state = 226
            self.match(D96Parser.LP)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ARRAY:
                self.state = 227
                self.array_literal_list()


            self.state = 230
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_listContext(ParserRuleContext):
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
            return D96Parser.RULE_array_literal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_list" ):
                return visitor.visitArray_literal_list(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_list(self):

        localctx = D96Parser.Array_literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_literal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.array_literal()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 233
                self.match(D96Parser.COMMA)
                self.state = 234
                self.array_literal()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
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
            return D96Parser.RULE_type_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = D96Parser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_type_name)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
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

        def INTEGER(self):
            return self.getToken(D96Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTEGER) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
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

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(D96Parser.ARRAY)
            self.state = 248
            self.match(D96Parser.LSB)
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 249
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 250
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 253
            self.match(D96Parser.COMMA)
            self.state = 254
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 255
            self.match(D96Parser.RSB)
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
        self.enterRule(localctx, 42, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StatementContext)
            else:
                return self.getTypedRuleContext(D96Parser.StatementContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(D96Parser.LCB)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.VAR) | (1 << D96Parser.VAL) | (1 << D96Parser.SELF) | (1 << D96Parser.RETURN) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 260
                self.statement()
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 266
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_and_const_declaration(self):
            return self.getTypedRuleContext(D96Parser.Variable_and_const_declarationContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(D96Parser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(D96Parser.If_statementContext,0)


        def foreach_statement(self):
            return self.getTypedRuleContext(D96Parser.Foreach_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(D96Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(D96Parser.Return_statementContext,0)


        def method_invocation_statement(self):
            return self.getTypedRuleContext(D96Parser.Method_invocation_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.variable_and_const_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 271
                self.foreach_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 272
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 273
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 274
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 275
                self.method_invocation_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_and_const_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.number_variable = 0

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def variable_initialization(self):
            return self.getTypedRuleContext(D96Parser.Variable_initializationContext,0)


        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def DOLLAR_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR_ID)
            else:
                return self.getToken(D96Parser.DOLLAR_ID, i)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_and_const_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_and_const_declaration" ):
                return visitor.visitVariable_and_const_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_and_const_declaration(self):

        localctx = D96Parser.Variable_and_const_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_variable_and_const_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAR or _la==D96Parser.VAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 279
            self.match(D96Parser.ID)
            self.getInvokingContext(24).number_variable+=1
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 281
                self.match(D96Parser.COMMA)
                self.state = 282
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.getInvokingContext(24).number_variable+=1
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 289
            self.match(D96Parser.COLON)
            self.state = 290
            self.type_name()
            self.state = 291
            self.variable_initialization()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def variable_initialization_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_initialization_listContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_initialization" ):
                return visitor.visitVariable_initialization(self)
            else:
                return visitor.visitChildren(self)




    def variable_initialization(self):

        localctx = D96Parser.Variable_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_variable_initialization)
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(D96Parser.ASSIGN)
                self.state = 294
                self.variable_initialization_list()
                pass
            elif token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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


    class Variable_initialization_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_initialization_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_initialization_list" ):
                return visitor.visitVariable_initialization_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_initialization_list(self):

        localctx = D96Parser.Variable_initialization_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_variable_initialization_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.expression()
            self.getInvokingContext(24).number_variable -= 1
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 300
                    if not self.getInvokingContext(24).number_variable > 0:
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$variable_and_const_declaration::number_variable > 0")
                    self.state = 301
                    self.match(D96Parser.COMMA)
                    self.state = 302
                    self.expression()
                    self.getInvokingContext(24).number_variable -= 1 
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 310
            if not self.getInvokingContext(24).number_variable == 0:
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "$variable_and_const_declaration::number_variable == 0")
            self.state = 311
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_hand_side(self):
            return self.getTypedRuleContext(D96Parser.Left_hand_sideContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.left_hand_side()
            self.state = 314
            self.match(D96Parser.ASSIGN)
            self.state = 315
            self.expression()
            self.state = 316
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_hand_sideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def member_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Member_access_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_left_hand_side

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_hand_side" ):
                return visitor.visitLeft_hand_side(self)
            else:
                return visitor.visitChildren(self)




    def left_hand_side(self):

        localctx = D96Parser.Left_hand_sideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_left_hand_side)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                self.index_expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 321
                self.member_access_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def elseif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Elseif_statementContext)
            else:
                return self.getTypedRuleContext(D96Parser.Elseif_statementContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.match(D96Parser.IF)
                self.state = 325
                self.match(D96Parser.LP)
                self.state = 326
                self.expression()
                self.state = 327
                self.match(D96Parser.RP)
                self.state = 328
                self.block_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(D96Parser.IF)
                self.state = 331
                self.match(D96Parser.LP)
                self.state = 332
                self.expression()
                self.state = 333
                self.match(D96Parser.RP)
                self.state = 334
                self.block_statement()
                self.state = 335
                self.else_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
                self.match(D96Parser.IF)
                self.state = 338
                self.match(D96Parser.LP)
                self.state = 339
                self.expression()
                self.state = 340
                self.match(D96Parser.RP)
                self.state = 341
                self.block_statement()
                self.state = 343 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 342
                    self.elseif_statement()
                    self.state = 345 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.ELSEIF):
                        break

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 347
                self.match(D96Parser.IF)
                self.state = 348
                self.match(D96Parser.LP)
                self.state = 349
                self.expression()
                self.state = 350
                self.match(D96Parser.RP)
                self.state = 351
                self.block_statement()
                self.state = 353 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 352
                    self.elseif_statement()
                    self.state = 355 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==D96Parser.ELSEIF):
                        break

                self.state = 357
                self.else_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_statement" ):
                return visitor.visitElseif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elseif_statement(self):

        localctx = D96Parser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(D96Parser.ELSEIF)
            self.state = 362
            self.match(D96Parser.LP)
            self.state = 363
            self.expression()
            self.state = 364
            self.match(D96Parser.RP)
            self.state = 365
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = D96Parser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(D96Parser.ELSE)
            self.state = 368
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foreach_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def DOUBLE_DOT(self):
            return self.getToken(D96Parser.DOUBLE_DOT, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_foreach_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach_statement" ):
                return visitor.visitForeach_statement(self)
            else:
                return visitor.visitChildren(self)




    def foreach_statement(self):

        localctx = D96Parser.Foreach_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_foreach_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(D96Parser.FOREACH)
            self.state = 371
            self.match(D96Parser.LP)
            self.state = 372
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 373
            self.match(D96Parser.IN)
            self.state = 374
            self.expression()
            self.state = 375
            self.match(D96Parser.DOUBLE_DOT)
            self.state = 376
            self.expression()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 377
                self.match(D96Parser.BY)
                self.state = 378
                self.expression()


            self.state = 381
            self.match(D96Parser.RP)
            self.state = 382
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(D96Parser.BREAK)
            self.state = 385
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(D96Parser.CONTINUE)
            self.state = 388
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_return_statement)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(D96Parser.RETURN)
                self.state = 391
                self.expression()
                self.state = 392
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(D96Parser.RETURN)
                self.state = 395
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Member_access_expressionContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_statement" ):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.member_access_expression(0)
            self.state = 399
            self.match(D96Parser.SEMI)
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

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invocation" ):
                return visitor.visitInstance_method_invocation(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invocation(self):

        localctx = D96Parser.Instance_method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_instance_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.expression()
            self.state = 402
            self.match(D96Parser.DOT)
            self.state = 403
            self.match(D96Parser.ID)
            self.state = 404
            self.match(D96Parser.LP)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 405
                self.list_of_expressions()


            self.state = 408
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expression(self):
            return self.getTypedRuleContext(D96Parser.String_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.string_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relation_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Relation_expressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.Relation_expressionContext,i)


        def STRING_ADD(self):
            return self.getToken(D96Parser.STRING_ADD, 0)

        def STRING_EQUAL(self):
            return self.getToken(D96Parser.STRING_EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_string_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expression" ):
                return visitor.visitString_expression(self)
            else:
                return visitor.visitChildren(self)




    def string_expression(self):

        localctx = D96Parser.String_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_string_expression)
        self._la = 0 # Token type
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.relation_expression()
                self.state = 413
                _la = self._input.LA(1)
                if not(_la==D96Parser.STRING_EQUAL or _la==D96Parser.STRING_ADD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 414
                self.relation_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.relation_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relation_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Logical_expressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.Logical_expressionContext,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relation_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_expression" ):
                return visitor.visitRelation_expression(self)
            else:
                return visitor.visitChildren(self)




    def relation_expression(self):

        localctx = D96Parser.Relation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_relation_expression)
        self._la = 0 # Token type
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.logical_expression(0)
                self.state = 420
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LT) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.GTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 421
                self.logical_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.logical_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expression(self):
            return self.getTypedRuleContext(D96Parser.Adding_expressionContext,0)


        def logical_expression(self):
            return self.getTypedRuleContext(D96Parser.Logical_expressionContext,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_logical_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expression" ):
                return visitor.visitLogical_expression(self)
            else:
                return visitor.visitChildren(self)



    def logical_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Logical_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_logical_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 434
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 429
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 430
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 431
                    self.adding_expression(0) 
                self.state = 436
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expression(self):
            return self.getTypedRuleContext(D96Parser.Multiplying_expressionContext,0)


        def adding_expression(self):
            return self.getTypedRuleContext(D96Parser.Adding_expressionContext,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_adding_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expression" ):
                return visitor.visitAdding_expression(self)
            else:
                return visitor.visitChildren(self)



    def adding_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Adding_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_adding_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 445
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Adding_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                    self.state = 440
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 441
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 442
                    self.multiplying_expression(0) 
                self.state = 447
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negative_expression(self):
            return self.getTypedRuleContext(D96Parser.Negative_expressionContext,0)


        def multiplying_expression(self):
            return self.getTypedRuleContext(D96Parser.Multiplying_expressionContext,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multiplying_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expression" ):
                return visitor.visitMultiplying_expression(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Multiplying_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_multiplying_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.negative_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 456
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Multiplying_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                    self.state = 451
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 452
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 453
                    self.negative_expression() 
                self.state = 458
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Negative_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def negative_expression(self):
            return self.getTypedRuleContext(D96Parser.Negative_expressionContext,0)


        def sign_expression(self):
            return self.getTypedRuleContext(D96Parser.Sign_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_negative_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegative_expression" ):
                return visitor.visitNegative_expression(self)
            else:
                return visitor.visitChildren(self)




    def negative_expression(self):

        localctx = D96Parser.Negative_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_negative_expression)
        try:
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.match(D96Parser.NOT)
                self.state = 460
                self.negative_expression()
                pass
            elif token in [D96Parser.SELF, D96Parser.NEW, D96Parser.NULL, D96Parser.ARRAY, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.SUB, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.sign_expression()
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


    class Sign_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def sign_expression(self):
            return self.getTypedRuleContext(D96Parser.Sign_expressionContext,0)


        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def member_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Member_access_expressionContext,0)


        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_sign_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expression" ):
                return visitor.visitSign_expression(self)
            else:
                return visitor.visitChildren(self)




    def sign_expression(self):

        localctx = D96Parser.Sign_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_sign_expression)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.match(D96Parser.SUB)
                self.state = 465
                self.sign_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.index_expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
                self.member_access_expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 468
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Member_access_expressionContext,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def index_expression(self):
            return self.getTypedRuleContext(D96Parser.Index_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression" ):
                return visitor.visitIndex_expression(self)
            else:
                return visitor.visitChildren(self)



    def index_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_index_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 472
                self.member_access_expression(0)
                self.state = 473
                self.match(D96Parser.LSB)
                self.state = 474
                self.expression()
                self.state = 475
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.state = 477
                self.match(D96Parser.ID)
                self.state = 478
                self.match(D96Parser.LSB)
                self.state = 479
                self.expression()
                self.state = 480
                self.match(D96Parser.RSB)
                pass

            elif la_ == 3:
                self.state = 482
                self.match(D96Parser.DOLLAR_ID)
                self.state = 483
                self.match(D96Parser.LSB)
                self.state = 484
                self.expression()
                self.state = 485
                self.match(D96Parser.RSB)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 496
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expression)
                    self.state = 489
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 490
                    self.match(D96Parser.LSB)
                    self.state = 491
                    self.expression()
                    self.state = 492
                    self.match(D96Parser.RSB) 
                self.state = 498
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Member_access_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def self_method_call(self):
            return self.getTypedRuleContext(D96Parser.Self_method_callContext,0)


        def member_access_expression(self):
            return self.getTypedRuleContext(D96Parser.Member_access_expressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_access_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access_expression" ):
                return visitor.visitMember_access_expression(self)
            else:
                return visitor.visitChildren(self)



    def member_access_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Member_access_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_member_access_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 500
                self.match(D96Parser.ID)
                self.state = 501
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 502
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 2:
                self.state = 503
                self.match(D96Parser.ID)
                self.state = 504
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 505
                self.match(D96Parser.DOLLAR_ID)
                self.state = 506
                self.match(D96Parser.LP)
                self.state = 508
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                    self.state = 507
                    self.list_of_expressions()


                self.state = 510
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.state = 511
                _la = self._input.LA(1)
                if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 512
                self.match(D96Parser.DOT)
                self.state = 513
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                self.state = 514
                _la = self._input.LA(1)
                if not(_la==D96Parser.SELF or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 515
                self.match(D96Parser.DOT)
                self.state = 516
                self.match(D96Parser.ID)
                self.state = 517
                self.match(D96Parser.LP)
                self.state = 519
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                    self.state = 518
                    self.list_of_expressions()


                self.state = 521
                self.match(D96Parser.RP)
                pass

            elif la_ == 5:
                self.state = 522
                self.self_method_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 538
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 536
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Member_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expression)
                        self.state = 525
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 526
                        self.match(D96Parser.DOT)
                        self.state = 527
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Member_access_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expression)
                        self.state = 528
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 529
                        self.match(D96Parser.DOT)
                        self.state = 530
                        self.match(D96Parser.ID)
                        self.state = 531
                        self.match(D96Parser.LP)
                        self.state = 533
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                            self.state = 532
                            self.list_of_expressions()


                        self.state = 535
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 540
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Self_method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_self_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelf_method_call" ):
                return visitor.visitSelf_method_call(self)
            else:
                return visitor.visitChildren(self)




    def self_method_call(self):

        localctx = D96Parser.Self_method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_self_method_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 542
            self.match(D96Parser.LP)
            self.state = 544
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 543
                self.list_of_expressions()


            self.state = 546
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_creation_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_expressions(self):
            return self.getTypedRuleContext(D96Parser.List_of_expressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_object_creation_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_creation_expression" ):
                return visitor.visitObject_creation_expression(self)
            else:
                return visitor.visitChildren(self)




    def object_creation_expression(self):

        localctx = D96Parser.Object_creation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_object_creation_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(D96Parser.NEW)
            self.state = 549
            self.match(D96Parser.ID)
            self.state = 550
            self.match(D96Parser.LP)
            self.state = 552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.NULL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID))) != 0):
                self.state = 551
                self.list_of_expressions()


            self.state = 554
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_creation_expression(self):
            return self.getTypedRuleContext(D96Parser.Object_creation_expressionContext,0)


        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_operand)
        try:
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.object_creation_expression()
                pass
            elif token in [D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
                self.match(D96Parser.DOLLAR_ID)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 558
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 559
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.ARRAY, D96Parser.INTEGER_LITERAL, D96Parser.STRING_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 560
                self.literal()
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 561
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 7)
                self.state = 562
                self.match(D96Parser.LP)
                self.state = 563
                self.expression()
                self.state = 564
                self.match(D96Parser.RP)
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


    class List_of_expressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_of_expressions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_expressions" ):
                return visitor.visitList_of_expressions(self)
            else:
                return visitor.visitChildren(self)




    def list_of_expressions(self):

        localctx = D96Parser.List_of_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_list_of_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.expression()
            self.state = 573
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 569
                self.match(D96Parser.COMMA)
                self.state = 570
                self.expression()
                self.state = 575
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self._predicates[6] = self.attribute_initialization_list_sempred
        self._predicates[26] = self.variable_initialization_list_sempred
        self._predicates[41] = self.logical_expression_sempred
        self._predicates[42] = self.adding_expression_sempred
        self._predicates[43] = self.multiplying_expression_sempred
        self._predicates[46] = self.index_expression_sempred
        self._predicates[47] = self.member_access_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def attribute_initialization_list_sempred(self, localctx:Attribute_initialization_listContext, predIndex:int):
            if predIndex == 0:
                return self.getInvokingContext(4).number_attribute > 0
         

            if predIndex == 1:
                return self.getInvokingContext(4).number_attribute == 0
         

    def variable_initialization_list_sempred(self, localctx:Variable_initialization_listContext, predIndex:int):
            if predIndex == 2:
                return self.getInvokingContext(24).number_variable > 0
         

            if predIndex == 3:
                return self.getInvokingContext(24).number_variable == 0
         

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def index_expression_sempred(self, localctx:Index_expressionContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

    def member_access_expression_sempred(self, localctx:Member_access_expressionContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 6)
         





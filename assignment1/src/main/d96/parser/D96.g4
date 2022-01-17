// ID: 1910409
grammar D96;

@lexer::header {
from lexererr import *
import re
}

options {
	language = Python3;
}

// program: mptype 'main' LB RB LP body? RP EOF;
program: exp* stmt* EOF;



// *****************************CLASS STRUCTURE*****************************
class_declare: CLASS (ID) (COLON ID)? LP body_class RP;

body_class: (constructor_declare | destructor_declare | method_declare | attribute_declare)*;

constructor_declare: CONSTRUCTOR LB params_list? RB block_stmt;
params_list: params_declare (SEMI params_declare)*;
params_declare: id_list COLON type_data;
id_list: ID (COMMA ID)*;
type_data: primitive_type | array_type | class_type;
primitive_type: 'asd';
array_type: 'asfrth';
class_type: 'fd';

destructor_declare: 'asdadsasdasdas';

method_declare: 'sadadsaas';

attribute_declare: 'nhanv';
// *****************************END CLASS STRUCTURE*****************************




// *****************************STATEMENT*****************************
block_stmt: LP stmt* RP;
stmt:   variable_and_constant_stmt | assignment_stmt | if_stmt | for_in_stmt | break_stmt | 
        continue_stmt | return_stmt | method_invocation_stmt;

variable_and_constant_stmt: 'hjahaa';

// có thể còn member access exp
assignment_stmt: (ID | STATIC_ID | index_exp) EQUAL exp SEMI;

if_stmt:    IF LB exp RB block_stmt       
            | IF LB exp RB block_stmt (ELSEIF LB exp RB block_stmt)+        
            | IF LB exp RB block_stmt (ELSEIF LB exp RB block_stmt)+ (ELSE block_stmt)
            | IF LB exp RB block_stmt (ELSE block_stmt);

for_in_stmt: FOREACH LB (ID | STATIC_ID) IN exp DOUBLE_DOT exp (BY exp)? RB block_stmt;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN exp? SEMI;

method_invocation_stmt: 'hahah';
// *****************************END STATEMENT*****************************



// *****************************EXPRESSION*****************************
exp: exp1 (ADD_STR | IS_EQUAL_STR) exp1 | exp1;
exp1: exp2 (IS_EQUAL | NOT_EQUAL | LT | GT | LTE | GTE) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MULTIPLY | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: '-' exp6 | exp7;
exp7: exp7 index_operator | exp8;
exp8: exp8 (DOT | DOUBLE_COLON) exp9 | exp9;
exp9: NEW exp9 | operands;

operands: ID | STATIC_ID | LB exp RB | literals;
literals: INT_LIT | FLOAT_LIT | STRING_LIT | boolean_literal;
boolean_literal: TRUE | FALSE;

index_operator: LSB exp RSB | LSB exp RSB index_operator;
index_exp:   ID LSB exp RSB | STATIC_ID LSB exp RSB |
                    index_exp LSB exp RSB;
// *****************************END EXPRESSION*****************************












fragment UPPERCASE: [A-Z];
fragment LOWERCASE: [a-z];
fragment UNDERSCORE: '_';
fragment DIGIT: [0-9];
fragment LETTER: UPPERCASE | LOWERCASE;
fragment DOUBLE_HASHTAG: '##';
fragment DOLLAR: '$';

// Block comment
COMMENT: DOUBLE_HASHTAG .*? DOUBLE_HASHTAG -> skip;

mptype: INTTYPE | VOIDTYPE;

body: funcall SEMI;

// exp: funcall | INTLIT;
// exp: funcall | INT_LIT;     // myself

funcall: ID LB exp? RB;

INTTYPE: 'int';

VOIDTYPE: 'void';



// *****************************KEYWORDS*****************************
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
INT: 'Int';
NULL: 'Null';
VAR: 'Var';
VAL: 'Val';
ARRAY: 'Array';
SELF: 'Self';
RETURN: 'Return';
NEW: 'New';
IN: 'In';
CLASS: 'Class';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
BY: 'By';
// *****************************END KEYWORDS*****************************




// *****************************SEPERATORS*****************************
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
DOUBLE_DOT: '..';
DOT: '.';
COMMA: ',';
SEMI: ';';
LP: '{';
RP: '}';
DOUBLE_COLON: '::';
COLON: ':';
// *****************************END SEPERATORS*****************************




// *****************************LITERALS*****************************
STRING_LIT:'"' CHAR* '"'
{
    self.text = self.text[1:-1]
}
;

// fix lại: chỉ có underscore ở integer_part
// underscore only between digits, not start and after, only 1 underscore
fragment E: [eE];
fragment SIGN: [+-];
fragment INTEGER_PART: [0-9] ('_'? [0-9])*;
fragment DEC_PART: DOT DIGIT*;
fragment EXPONENT_PART: E SIGN? DIGIT+;
FLOAT_LIT: (INTEGER_PART DEC_PART EXPONENT_PART
            | INTEGER_PART DEC_PART
            | INTEGER_PART EXPONENT_PART
            | DEC_PART EXPONENT_PART)
{
    self.text = re.sub('_','',self.text)
};

// nhập nhằng: 0002.123 --> fix lại cho được luôn
// underscore 3 part và remove
// không cho vụ .123
// fragment DEC_PART: DOT DIGIT*;
// fragment INTEGER_PART: [0-9] ('_'*[0-9])*;
// fragment DEC_PART: DOT INTEGER_PART?;
// fragment EXPONENT_PART: E SIGN? INTEGER_PART;
// FLOAT_LIT: 	(INT_DECIMAL DEC_PART EXPONENT_PART
// 			| INT_DECIMAL DEC_PART //33.
// 			| INT_DECIMAL EXPONENT_PART	//33e10
//             | DEC_PART EXPONENT_PART
//             | DEC_PART
//             ) 
// {
//             self.text = re.sub('_','',self.text)
// };
// FLOAT_LIT: 	(INTEGER_PART DEC_PART EXPONENT_PART
// 			| INTEGER_PART DEC_PART //33.
// 			| INTEGER_PART EXPONENT_PART	//33e10
//             | DEC_PART EXPONENT_PART
//             //| DEC_PART
//             ) 
// {
//             self.text = re.sub('_','',self.text)
// };

// fix lại: underscore trong INT_DECIMAL ---> underscore nằm ở cuối ko được, còn cái cũ thì được và
// sẽ remove underscore ở cuối (cái cũ)
fragment X: [xX];
fragment B: [bB];
// fragment INT_OCT: '0' [1-7][0-7]*;
fragment INT_OCT: '0' [0-7]+;
// fragment INT_DECIMAL: [1-9][_0-9]* | '0';
// fragment INT_DECIMAL: [1-9]('_'* [0-9])* | '0';
fragment INT_DECIMAL: [1-9]('_'? [0-9])* | '0';
// fragment INT_HEXA: '0' X [1-9a-fA-F] [0-9a-fA-F]*;
// fragment INT_HEXA: '0' X [0-9a-fA-F]*;
fragment INT_HEXA: '0' X [0-9A-F]+;
fragment INT_BINARY: '0' B [01]+;
INT_LIT: (INT_DECIMAL | INT_HEXA | INT_OCT | INT_BINARY) {
    self.text = re.sub('_','',self.text)
}
;

BOOLEAN_LIT: TRUE | FALSE;
// fragment INT_LIST: INT_LIT (COMMA INT_LIT)*;
// ARRAY_LIT: 'Array' '(' INT_LIST ')';
// *****************************END LITERALS*****************************





// *****************************OPERATORS*****************************
NOT: '!';
AND: '&&';
OR: '||';
IS_EQUAL: '==';         // not float
NOT_EQUAL: '!=';        // not float

ADD: '+';
SUB: '-';
MULTIPLY: '*';
DIV: '/';       // not float
MOD: '%';       // not gloat
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';

ADD_STR: '+.';
IS_EQUAL_STR: '==.';

EQUAL: '=';     // for assignment
// *****************************END OPERATORS*****************************




WS: [ \t\b\r\n\f]+ -> skip; // skip spaces, tabs, newlines
ID: (UNDERSCORE | LETTER) (LETTER | UNDERSCORE | DIGIT)*;
// STATIC_ID: DOLLAR ID;
STATIC_ID: DOLLAR [_a-zA-Z0-9]+;



// fragment CHAR : ~[\b\t\f\r\n\\"'] | ESCAPE;
fragment CHAR : ~[\r\n\\"'] | ESCAPE;
fragment ESCAPE: '\\' [btnfr'\\] | ('\'' '"');
fragment ILL_ESC: '\\'~[btrfn\\'] | '\''~'"'  ;

// UNTERMINATED_COMMENT: '##' ('#'~'#' | ~'#')* EOF
// {
//     raise UnterminatedComment()
// }
// ;

ILLEGAL_ESCAPE: '"' CHAR* ILL_ESC
{
    string_to_illegal = str(self.text)
    raise IllegalEscape(string_to_illegal[1:])
};
UNCLOSE_STRING:'"' CHAR*
{
    raise UncloseString(self.text[1:])
};
ERROR_CHAR: .
{
    raise ErrorToken(self.text)
};

// UNCLOSE_STRING:'"' CHAR* ([\r\n] | EOF)
// {
//     text = str(self.text)
//     error_sequence =['\r','\n']
//     if(text[-1] in error_sequence):
//         raise UncloseString(text[1:-1])
//     else:
//         raise UncloseString(text[1:])
// };
// UNCLOSE_STRING:'"' CHAR*
// {
//     text = str(self.text)
//     error_sequence =['\r','\n']
//     if(text[-1] in error_sequence):
//         raise UncloseString(text[1:-1])
//     else:
//         raise UncloseString(text[1:])
// }
// ;
// UNCLOSE_STRING:'"' CHAR*
// {
//     text = str(self.text)
//     error_sequence = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
//     if(text[-1] in error_sequence):
//         raise UncloseString(text[1:-1])
//     else:
//         raise UncloseString(text[1:])
// }
// ;
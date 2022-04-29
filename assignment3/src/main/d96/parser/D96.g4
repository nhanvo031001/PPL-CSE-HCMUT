// grammar D96;

// @lexer::header {
// from lexererr import *
// }

// options {
// 	language = Python3;
// }

// program: EOF;

// WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

// ERROR_CHAR: .;
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;


// ID: 1910409
grammar D96;

@lexer::header {
from lexererr import *
import re
}

options {
	language = Python3;
}


program: class_declare+ EOF;
// program: test_declare EOF;




// *****************************CLASS STRUCTURE*****************************
class_declare: CLASS name_class (COLON ID)? LP body_class RP;
name_class: ID;
body_class: mem_class_declare*;
mem_class_declare: constructor_declare | destructor_declare | method_declare | attribute_declare;

constructor_declare: CONSTRUCTOR LB params_list? RB block_stmt;
params_list: params_declare (SEMI params_declare)*;
params_declare: id_list COLON type_data;
id_list: ID (COMMA ID)*;
type_data: primitive_type | array_type | class_type;
primitive_type: BOOLEAN | INT | FLOAT | STRING;
array_type: ARRAY LSB element_type COMMA size RSB;
element_type: primitive_type | array_type;
size: INT_LIT;
class_type: ID;

destructor_declare: DESTRUCTOR LB RB block_stmt;

method_declare: (ID | STATIC_ID) LB params_list? RB block_stmt;

attribute_declare: (VAR | VAL) variable_name_list COLON type_data (EQUAL value_list[$variable_name_list.count] ({$value_list.count_after == 0}? SEMI) | SEMI);
// variable_name_list returns[count = 0]: (ID | STATIC_ID) {$count+=1} (COMMA (ID | STATIC_ID) {$count+=1})*;
variable_name_list returns[count = 0]: (id_or_staticID) {$count+=1} (COMMA (id_or_staticID) {$count+=1})* ; // 3
id_or_staticID: ID | STATIC_ID;
value_list[count] returns[count_after]:	exp {$count-=1} ({$count > 0}? COMMA exp {$count-=1})* {$count_after = $count} ;
// *****************************END CLASS STRUCTURE*****************************




// *****************************STATEMENT*****************************
block_stmt: LP stmt* RP;
stmt:   variable_and_constant_stmt | assignment_stmt 
        | if_stmt | for_in_stmt | break_stmt 
        | continue_stmt | return_stmt | method_invocation_stmt
        | block_stmt;

// thay doi theo AST
// block_stmt: LP variable_and_constant_stmt* stmt* RP;
// stmt:   assignment_stmt 
//         | if_stmt | for_in_stmt | break_stmt 
//         | continue_stmt | return_stmt | method_invocation_stmt
//         | block_stmt;

variable_and_constant_stmt: (VAR | VAL) variable_name_list_in_method COLON type_data (EQUAL value_list_stmt[$variable_name_list_in_method.count] ({$value_list_stmt.count_after == 0}? SEMI)| SEMI);
variable_name_list_in_method returns[count = 0]: ID {$count+=1} (COMMA ID {$count+=1})*;
value_list_stmt[count] returns[count_after]: exp {$count-=1} ({$count > 0}? COMMA exp {$count-=1})* {$count_after = $count};

assignment_stmt: scalar_variable EQUAL exp SEMI;
scalar_variable: ID // bien thuong  
                | name_class DOUBLE_COLON STATIC_ID // bien dollar
                | exp8 DOT ID // cai cuoi la bien thuong, phia truoc goi ham van duoc
                | index_exp_for_scalar_variable; // index expression
// index_exp_for_scalar_variable:  exp7 LSB exp RSB;
index_exp_for_scalar_variable:  exp8 index_operator;

// if_stmt:    IF LB exp RB block_stmt       
//             | IF LB exp RB block_stmt (ELSEIF LB exp RB block_stmt)+            
//             | IF LB exp RB block_stmt (ELSEIF LB exp RB block_stmt)+ (ELSE block_stmt)
//             | IF LB exp RB block_stmt (ELSE block_stmt);

if_stmt: IF LB exp RB block_stmt elseif_block* else_block?;
elseif_block: ELSEIF LB exp RB block_stmt;
else_block: ELSE block_stmt;

for_in_stmt: FOREACH LB ID IN exp DOUBLE_DOT exp (BY exp)? RB block_stmt;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN exp? SEMI;

// method_invocation_stmt: (static_method_invocation | instance_method_invocation | calling_method_inside_class) SEMI;
method_invocation_stmt: (static_method_invocation | instance_method_invocation) SEMI; // | calling_method_inside_class) SEMI;
static_method_invocation: name_class DOUBLE_COLON STATIC_ID LB exp_list? RB ;
instance_method_invocation: pre_exp DOT ID LB exp_list? RB;
pre_exp: pre_exp DOT ID
        | pre_exp DOT ID LB exp_list? RB
        | exp9;
// *****************************END STATEMENT*****************************




// *****************************EXPRESSION*****************************

// style hard code
// exp: exp1 (ADD_STR | IS_EQUAL_STR) exp1 | exp1;
// exp1: exp2 (IS_EQUAL | NOT_EQUAL | LT | GT | LTE | GTE) exp2 | exp2;
// exp2: exp2 (AND | OR) exp3 | exp3;
// exp3: exp3 (ADD | SUB) exp4 | exp4;
// exp4: exp4 (MULTIPLY | DIV | MOD) exp5 | exp5;
// exp5: NOT exp5 | exp6;
// exp6: '-' exp6 | index_exp | member_access_exp | operands;

// index_exp:      ID index_operator            // arr[1], arr[2+4], arr[a.b], arr[New X()]
//                 | STATIC_ID index_operator      // $arr[1], $arr[2+4], $arr[a.b], $arr[New X()]
//                 | member_access_exp index_operator //; //a.b[i]
//                 | object_creation_exp index_operator
//                 | index_exp index_operator
//                 | LB exp RB;

// index_operator: LSB exp RSB | LSB exp RSB index_operator;


// member_access_exp:  instance_attr_access
//                     | static_attr_access
//                     | instance_method_invocation
//                     | static_method_invocation
//                     | calling_method_inside_class;

// instance_attr_access:   instance_attr_access DOT ID 
//                         | ID
//                         | SELF
//                         | object_creation_exp
//                         | LB exp RB
//                         | static_attr_access
//                         | instance_method_invocation
//                         | static_method_invocation; //

// static_attr_access: ID DOUBLE_COLON STATIC_ID;  // khong goi chaining: Shape::$a::$b ---> No

// instance_method_invocation: instance_method_invocation DOT ID LB exp_list? RB
//                             | instance_method_invocation DOT ID
//                             | ID DOUBLE_COLON STATIC_ID
//                             | ID DOUBLE_COLON STATIC_ID LB exp_list? RB
//                             | ID
//                             | SELF
//                             | object_creation_exp
//                             | LB exp RB
//                             ;

// static_method_invocation: ID DOUBLE_COLON STATIC_ID LB exp_list? RB;

// exp_list: exp (COMMA exp)*;

// operands: ID | STATIC_ID | LB exp RB | literals | object_creation_exp | NULL; // | funccall;
// literals: ZERO_LIT | INT_LIT | FLOAT_LIT | STRING_LIT | boolean_literal | array_literal;
// boolean_literal: TRUE | FALSE;
// array_literal: indexed_array | multidimensional_array;
// indexed_array: ARRAY LB exp_list? RB;
// multidimensional_array: ARRAY LB array_list? RB;
// array_list: array_literal (COMMA array_literal)*;
// // funccall: (ID | STATIC_ID) LB exp_list? RB;
// object_creation_exp: NEW ID LB exp_list? RB;






// style recursion, change according to ver 1.2
// exp: exp1 (ADD_STR | IS_EQUAL_STR) exp1 | exp1;
// exp1: exp2 (IS_EQUAL | NOT_EQUAL | LT | GT | LTE | GTE) exp2 | exp2;
// exp2: exp2 (AND | OR) exp3 | exp3;
// exp3: exp3 (ADD | SUB) exp4 | exp4;
// exp4: exp4 (MULTIPLY | DIV | MOD) exp5 | exp5;
// exp5: NOT exp5 | exp6;
// exp6: '-' exp6 | exp7;
// exp7: exp7 index_operator | exp8;
// exp8: exp8 DOT exp9 | exp9;
// exp9: exp10 DOUBLE_COLON exp10 | exp10;
// exp10: NEW exp10 | operands | calling_method_inside_class;

// operands: ID | STATIC_ID | LB exp RB | literals | SELF | NULL;
// literals: ZERO_LIT | INT_LIT | FLOAT_LIT | STRING_LIT | boolean_literal | array_literal;
// boolean_literal: TRUE | FALSE;
// array_literal: indexed_array | multidimensional_array;
// indexed_array: ARRAY LB exp_list? RB;
// exp_list: exp (COMMA exp)*;
// multidimensional_array: ARRAY LB array_list? RB;
// array_list: array_literal (COMMA array_literal)*;
// // funccall: (ID | STATIC_ID) LB exp_list? RB;

// element_exp: exp index_operator;
// index_operator: LSB exp RSB | LSB exp RSB index_operator;

// member_access_exp:  instance_attr_access
//                     | static_attr_access
//                     | instance_method_invocation
//                     | static_method_invocation
//                     | calling_method_inside_class;
// instance_attr_access:  exp DOT ID;      // Shape.length
// static_attr_access: ID DOUBLE_COLON STATIC_ID;      // Shape::$width
// instance_method_invocation: exp DOT ID LB exp_list? RB;  // obj.getLength()
// static_method_invocation : ID DOUBLE_COLON STATIC_ID LB exp_list? RB; // Shape::$getWidth()

// object_creation_exp: NEW ID LB exp_list? RB;






// change according to ver 1.2, recursive cach khac, doi cach viet member access
// exp: exp1 (ADD_STR | IS_EQUAL_STR) exp1 | exp1;
// exp1: exp2 (IS_EQUAL | NOT_EQUAL | LT | GT | LTE | GTE) exp2 | exp2;
// exp2: exp2 (AND | OR) exp3 | exp3;
// exp3: exp3 (ADD | SUB) exp4 | exp4;
// exp4: exp4 (MULTIPLY | DIV | MOD) exp5 | exp5;
// exp5: NOT exp5 | exp6;
// exp6: SUB exp6 | exp7;
// exp7: exp7 index_operator | exp8;
// exp8:   exp8 DOT ID 
//         | exp8 DOT ID LB exp_list? RB
//         | exp9;
// exp9:   ID DOUBLE_COLON STATIC_ID 
//         | ID DOUBLE_COLON STATIC_ID LB exp_list? RB
//         | exp10;
// exp10: NEW ID LB exp_list? RB | operands;

// operands: ID | STATIC_ID | LB exp RB | literals | SELF | NULL | calling_method_inside_class;
// literals: ZERO_LIT | INT_LIT | FLOAT_LIT | STRING_LIT | boolean_literal | array_literal;
// boolean_literal: TRUE | FALSE;
// array_literal: multidimensional_array | indexed_array;
// multidimensional_array: ARRAY LB array_list? RB;
// indexed_array: ARRAY LB exp_list? RB;
// exp_list: exp (COMMA exp)*;
// array_list: array_literal (COMMA array_literal)*;
// calling_method_inside_class: (ID | STATIC_ID) LB exp_list? RB;

// index_operator: LSB exp RSB | LSB exp RSB index_operator;






// giong cai tren, nhung dieu chinh muc sai sot theo forum
// remove calling_method_inside_class, operands ko co static ID
exp: exp1 (ADD_STR | IS_EQUAL_STR) exp1 | exp1;
exp1: exp2 (IS_EQUAL | NOT_EQUAL | LT | GT | LTE | GTE) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MULTIPLY | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7: exp7 index_operator | exp8;
exp8:   exp8 DOT ID 
        | exp8 DOT ID LB exp_list? RB
        | exp9;
exp9:   ID DOUBLE_COLON STATIC_ID 
        | ID DOUBLE_COLON STATIC_ID LB exp_list? RB
        | exp10;
exp10: NEW ID LB exp_list? RB | operands;

// sua lai tam thoi de test AST
// exp8: operands;
// exp9: 'nhanvo';
operands: ID | LB exp RB | literals | SELF | NULL;
literals: ZERO_LIT | INT_LIT | FLOAT_LIT | STRING_LIT | boolean_literal | array_literal;
boolean_literal: TRUE | FALSE;
array_literal: multidimensional_array | indexed_array;
// multidimensional_array: ARRAY LB array_list? RB;
multidimensional_array: ARRAY LB array_list RB;
array_list: array_literal (COMMA array_literal)*;
indexed_array: ARRAY LB exp_list? RB;
exp_list: exp (COMMA exp)*;

index_operator: LSB exp RSB index_operator | LSB exp RSB;
// sua theo for easy writing AST, write ok
// index_operator: (LSB exp RSB)+;

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

// fix lai: chi co underscore o phan integer_part
// underscore only between digits, not start and after, only 1 underscore
fragment E: [eE];
fragment SIGN: [+-];
// fragment INTEGER_PART: [0-9] ('_'? [0-9])*;
fragment INTEGER_PART: '0' | [1-9] ('_'? [0-9])*;
fragment DEC_PART: DOT DIGIT*;
fragment EXPONENT_PART: E SIGN? DIGIT+;
FLOAT_LIT: (INTEGER_PART DEC_PART EXPONENT_PART
            | INTEGER_PART DEC_PART
            | INTEGER_PART EXPONENT_PART
            | DEC_PART EXPONENT_PART)
{
    self.text = re.sub('_','',self.text)
};


fragment X: [xX];
fragment B: [bB];
fragment INT_OCT: '0' [1-7] ('_'? [0-7])*;
fragment INT_DECIMAL: [1-9]('_'? [0-9])*;
fragment INT_HEXA: '0' X [1-9A-F] ('_'? [0-9A-F])*;
fragment INT_BINARY: '0' B '1' ('_'? [0-1])*;
INT_LIT: (INT_DECIMAL | INT_HEXA | INT_OCT | INT_BINARY) {
    self.text = re.sub('_','',self.text)
};

BOOLEAN_LIT: TRUE | FALSE;

ZERO_LIT: '0' | '0b0' | '0B0' | '0x0' | '0X0' | '00';


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



WS: [ \t\r\n\f]+ -> skip; // skip spaces, tabs, newlines
ID: (UNDERSCORE | LETTER) (LETTER | UNDERSCORE | DIGIT)*;
// STATIC_ID: DOLLAR ID;
STATIC_ID: DOLLAR [_a-zA-Z0-9]+;



// fragment CHAR : ~[\b\t\f\r\n\\"'] | ESCAPE;
fragment CHAR : ~[\b\t\f\r\n\\"] | ESCAPE;
fragment ESCAPE: '\\' [btnfr'\\] | ('\'' '"');
fragment ILL_ESC: '\\'~[btrfn\\'] | '\\';// | '\''~'"' ;

// UNTERMINATED_COMMENT: '##' ('#'~'#' | ~'#')* EOF
// {
//     raise UnterminatedComment()
// }
// ;
// UNCLOSE_STRING:'"' CHAR*
// {
//     raise UncloseString(self.text[1:])
// };

// cach khac
UNCLOSE_STRING:'"' CHAR* ( [\b\t\f\r\n\\"] | EOF )
{
    y = str(self.text)
    error_seq = ['\b', '\t', '\f', '\n', '\r', '"']
    if y[-1] in error_seq:
        raise UncloseString(y[1:-1])
    else:
        raise UncloseString(y[1:])
};

ILLEGAL_ESCAPE: '"' CHAR* ILL_ESC
{
    string_to_illegal = str(self.text)
    raise IllegalEscape(string_to_illegal[1:])
};

ERROR_CHAR: .
{
    raise ErrorToken(self.text)
};


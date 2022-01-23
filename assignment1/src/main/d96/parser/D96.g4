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


// *****************************CLASS STRUCTURE*****************************
class_declare: CLASS name_class (COLON ID)? LP body_class RP;
name_class: ID;
body_class: (constructor_declare | destructor_declare | method_declare | attribute_declare)*;

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

attribute_declare locals[count = 0]: (VAR | VAL) variable_name_list COLON type_data (EQUAL value_list | SEMI);     
variable_name_list: (ID | STATIC_ID) {$attribute_declare::count+=1} (COMMA (ID | STATIC_ID) {$attribute_declare::count+=1} )*;
value_list: exp {$attribute_declare::count-=1}
            ({$attribute_declare::count > 0}? COMMA exp {$attribute_declare::count-=1})*
            ({$attribute_declare::count == 0}? SEMI);
// *****************************END CLASS STRUCTURE*****************************




// *****************************STATEMENT*****************************
block_stmt: LP stmt* RP;
stmt:   variable_and_constant_stmt | assignment_stmt 
        | if_stmt | for_in_stmt | break_stmt 
        | continue_stmt | return_stmt | method_invocation_stmt;

variable_and_constant_stmt locals[count = 0]: (VAR | VAL) variable_name_list_in_method COLON type_data (EQUAL value_list_stmt | SEMI);
variable_name_list_in_method: ID {$variable_and_constant_stmt::count+=1} (COMMA ID {$variable_and_constant_stmt::count+=1})*;
value_list_stmt:    exp {$variable_and_constant_stmt::count-=1}
                    ({$variable_and_constant_stmt::count > 0}? COMMA exp {$variable_and_constant_stmt::count-=1})*
                    ({$variable_and_constant_stmt::count == 0}? SEMI);

// có thể còn member access exp
// assignment_stmt: (ID | STATIC_ID | index_exp | member_access_exp) EQUAL (exp) SEMI; // theo hard code
assignment_stmt: (ID | STATIC_ID | exp7 | exp8 | exp9) EQUAL (exp) SEMI; // theo recursive
// NOTE: exp7 (index_exp), exp8 (DOT access), exp9 (DOUBLE COLON access)

if_stmt:    IF LB exp RB block_stmt       
            | IF LB exp RB block_stmt (ELSEIF LB exp RB block_stmt)+        
            | IF LB exp RB block_stmt (ELSEIF LB exp RB block_stmt)+ (ELSE block_stmt)
            | IF LB exp RB block_stmt (ELSE block_stmt);

for_in_stmt: FOREACH LB (ID | STATIC_ID) IN exp DOUBLE_DOT exp (BY exp)? RB block_stmt;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN exp? SEMI;

// method_invocation_stmt: (static_method_invocation | instance_method_invocation | calling_method_inside_class) SEMI;
method_invocation_stmt: (exp8 | exp9) SEMI;
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

// static_attr_access: ID DOUBLE_COLON STATIC_ID;  // không gọi chaining: Shape::$a::$b ---> không

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







// style recursion, change theo ver 1.2
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





// change theo ver 1.2, recursive cách khác, đổi cách viết member access
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

operands: ID | STATIC_ID | LB exp RB | literals | SELF | NULL | calling_method_inside_class;
literals: ZERO_LIT | INT_LIT | FLOAT_LIT | STRING_LIT | boolean_literal | array_literal;
boolean_literal: TRUE | FALSE;
array_literal: multidimensional_array | indexed_array;
multidimensional_array: ARRAY LB array_list? RB;
indexed_array: ARRAY LB exp_list? RB;
exp_list: exp (COMMA exp)*;
array_list: array_literal (COMMA array_literal)*;
calling_method_inside_class: (ID | STATIC_ID) LB exp_list? RB;

index_operator: LSB exp RSB | LSB exp RSB index_operator;

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

// fix lại: chỉ có underscore ở integer_part
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
fragment INT_BINARY:    '0' B '1' ('_'? [0-1])*;
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

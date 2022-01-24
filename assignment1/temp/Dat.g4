// Student ID: 1910110
// Student Name: Huynh Thanh Dat
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
// ----------------------------------  PARSER  -------------------------------------------
// program structure
program: class_declaration+ EOF; // File không rỗng

/***************************** CLASS ******************************/
class_declaration : CLASS class_name (COLON class_name)? LCB class_body RCB;
class_name: ID;
class_body: (attribute_declaration | method_declaration | constructor_declaration | destructor_declaration)*;

// Check số biến == số khởi tạo --> Dư: trả vị trí dấu , | Thiếu: trả vị trí dấu ;
attribute_declaration
    locals [number_attribute = 0]: 
    (VAR | VAL) (ID | DOLLAR_ID) {$attribute_declaration::number_attribute+=1} 
    (COMMA (ID | DOLLAR_ID) {$attribute_declaration::number_attribute+=1})* 
    COLON type_name attribute_initialization;

attribute_initialization    :   ASSIGN attribute_initialization_list 
                            |   SEMI
                            ;
attribute_initialization_list   :   expression {$attribute_declaration::number_attribute -= 1}  // first expression
                                    ({$attribute_declaration::number_attribute > 0}? COMMA expression {$attribute_declaration::number_attribute -= 1})*   // loop until number_var == 0 or not match
                                    ({$attribute_declaration::number_attribute == 0}? SEMI); // check number_var == 0


method_declaration      :   (ID | DOLLAR_ID) LP list_of_parameters? RP block_statement;
constructor_declaration :   CONSTRUCTOR LP list_of_parameters? RP block_statement;
destructor_declaration  :   DESTRUCTOR LP RP block_statement;

list_of_parameters      :   parameter_declaration(SEMI parameter_declaration)*;
parameter_declaration   :   ID (COMMA ID)* COLON type_name;

/***************************** TYPE ******************************/

type_name       :   primitive_type | array_type | class_type;
primitive_type  :   INTEGER | FLOAT | STRING | BOOLEAN;
array_type      :   ARRAY LSB (primitive_type | array_type) COMMA INTEGER_LITERAL RSB;
class_type      :   ID;

/***************************** LITERAL AND ARRAY ******************************/

literal             :   array_literal | primitive_literal;
primitive_literal   :   ZERO_INTEGER | INTEGER_LITERAL | FLOAT_LITERAL | STRING_LITERAL | BOOLEAN_LITERAL;

array_literal       :   indexed_array
                    |   multi_demensional_array
                    ;
// Phải để trước index để multi dimensional sẽ match multi trước
multi_demensional_array     :   ARRAY LP array_literal_list? RP; 
array_literal_list          :   array_literal (COMMA array_literal)*; 
indexed_array               :   ARRAY LP list_of_expressions? RP;



/*
ARRAY LITERAL CHECK SỐ PHẦN TỬ ARRAY
*/
/*
indexed_array     
    [parent_first_array_size = -1] returns [size = 0]  // -1 tức là không có array nào chứa nó
    locals [list_size = 0]:
    ARRAY LP 
    (array_list_of_expressions[$parent_first_array_size] {$list_size = $array_list_of_expressions.size})? 
    {($parent_first_array_size == -1) | ($list_size == $parent_first_array_size)}? RP {$size = $list_size};


array_list_of_expressions
    [parent_first_array_size = -1]
    returns [size = 0]:
    expression {$size += 1}
    ({($parent_first_array_size == -1) | ($size < $parent_first_array_size)}? COMMA expression {$size += 1})*;
                                      
multi_demensional_array 
    [parent_first_array_size = -1] returns [size = 0]
    locals [list_size = 0]:  
    ARRAY LP 
    (array_literal_list[$parent_first_array_size]  {$list_size = $array_literal_list.size} )? 
    {($parent_first_array_size == -1) | ($list_size == $parent_first_array_size)}? RP  {$size = $list_size};


array_literal_list
    [parent_first_array_size = -1] 
    returns [size = 0]
    locals [first_array_size]:
    (indexed_array [-1]
{
$first_array_size = $indexed_array.size
$size += 1
} 
    | multi_demensional_array[-1] 
{
$first_array_size = $multi_demensional_array.size
$size += 1
})
    ({($parent_first_array_size == -1) | ($size < $parent_first_array_size)}? COMMA (indexed_array[$first_array_size] {$size += 1} | multi_demensional_array[$first_array_size] {$size += 1}))*
	;
*/

/***************************** EXPRESSION ******************************/
list_of_expressions: expression (COMMA expression)*;
expression          :   string_expression;

string_expression   :   relation_expression (STRING_ADD | STRING_EQUAL) relation_expression
                    |   relation_expression
                    ;
relation_expression :   logical_expression (EQUAL | NOT_EQUAL | LT | LTE | GT | GTE) logical_expression
                    |   logical_expression
                    ;

logical_expression  :   logical_expression (AND | OR) adding_expression  
                    |   adding_expression
                    ;

adding_expression   :   adding_expression (ADD | SUB) multiplying_expression
                    |   multiplying_expression
                    ;

multiplying_expression  :   multiplying_expression (MUL | DIV | MOD) negative_expression
                        |   negative_expression
                        ;

negative_expression :   NOT negative_expression
                    |   sign_expression
                    ;

sign_expression     :   SUB sign_expression
                    |   index_expression
                    ;

index_expression    :   index_expression LSB expression RSB
                    |   instance_access_expression
                    ;
instance_access_expression  :   instance_access_expression DOT ID
                            |   instance_access_expression DOT ID LP list_of_expressions? RP
                            |   self_method_call
                            |   static_access_expression
                            ;

static_access_expression    :   ID DOUBLE_COLON DOLLAR_ID
                            |   ID DOUBLE_COLON DOLLAR_ID LP list_of_expressions? RP
                            |   object_creation_expression
                            ;
self_method_call            :   (ID | DOLLAR_ID) LP list_of_expressions? RP; 

object_creation_expression  :   NEW ID LP list_of_expressions? RP
                            |   operand
                            ;

operand :   DOLLAR_ID
        |   ID
        |   SELF
        |   literal
        |   NULL
        |   LP expression RP
        ;

/***************************** STATEMENT ******************************/
block_statement: LCB statement* RCB;
statement   :   variable_and_const_declaration
            |   assign_statement 
            |   if_statement
            |   foreach_statement
            //|     while_statement           
            |   break_statement
            |   continue_statement
            |   return_statement  
            |   method_invocation_statement  
            ;


variable_and_const_declaration 
    locals [number_variable = 0]: 
    (VAR | VAL) ID {$variable_and_const_declaration::number_variable+=1} 
    (COMMA (ID){$variable_and_const_declaration::number_variable+=1})* 
    COLON type_name variable_initialization
    ;

variable_initialization :   ASSIGN variable_initialization_list 
                        |   SEMI
                        ;

variable_initialization_list    :   expression {$variable_and_const_declaration::number_variable -= 1} 
                                    ({$variable_and_const_declaration::number_variable > 0}? COMMA expression {$variable_and_const_declaration::number_variable -= 1})*  
                                    ({$variable_and_const_declaration::number_variable == 0}? SEMI)
                                ;
assign_statement: left_hand_side ASSIGN expression SEMI;

left_hand_side  :   ID 
                |   DOLLAR_ID 
                |   index_expression
                |   instance_access_expression
                |   static_access_expression
                ;
/* 
if_statement: IF LP expression RP block_statement // 1 if
            | IF LP expression RP block_statement else_statement // 1 if 1 else
            | IF LP expression RP block_statement elseif_statement+ // 1 if multi elseif
            | IF LP expression RP block_statement elseif_statement+ else_statement // 1 if multi elseif 1 elseif
            ;
*/
if_statement        :   IF LP expression RP block_statement 
                        elseif_statement* 
                        else_statement?
                    ;

elseif_statement    :   ELSEIF LP expression RP block_statement;
else_statement      :   ELSE block_statement;

foreach_statement   :   FOREACH LP (ID | DOLLAR_ID) IN expression DOUBLE_DOT expression (BY expression)? RP block_statement;
break_statement     :   BREAK SEMI;
continue_statement  :   CONTINUE SEMI;
return_statement    :   RETURN expression SEMI | RETURN SEMI;

method_invocation_statement :   (instance_method_invocation | static_method_invocation) SEMI;
                                //(instance_access_expression | static_access_expression) SEMI;

instance_method_invocation      :   instance_access_expression DOT ID LP list_of_expressions? RP
                                |   self_method_call;
static_method_invocation        :   class_name DOUBLE_COLON DOLLAR_ID LP list_of_expressions? RP;


// ----------------------------------  LEXER  -------------------------------------------
/********************** FRAGMENT ***********************/
//fragment COMMENT_CHAR: ~'#' | '#'~'#';


// Các trường hợp 0 0x0 0b0 00 sẽ được bắt riêng 1 token để check ràng buộc > 0
fragment DEC_INTEGER_LITERAL:  [1-9]('_'?[0-9])*;
fragment OCT_INTEGER_LITERAL: '0' [1-7]('_'?[0-7])*;
fragment BIN_INTEGER_LITERAL: '0'[bB][1]('_'?[0-1])*;
fragment HEX_INTEGER_LITERAL: '0'[xX] [1-9A-F]('_'?[0-9A-F])*;

fragment STRING_CHAR    : ~(["\r\n\\]) 
                        | ESCAPE_SEQUENCE 
                        | DOUBLE_QUOTE_CHAR;
fragment ESCAPE_SEQUENCE: '\\' [btnfr'\\];
fragment DOUBLE_QUOTE_CHAR: '\'"';
fragment ILLEGAL_SEQUENCE   :   '\\' ~[btnfr'\\]  
                        //    |   '\'' ~["] 
                            |   '\\' // Dấu \ đứng một mình
                            ;
fragment SIGN: [+-];
fragment FLOAT_INTEGER_PART: [1-9]('_'?[0-9])* | '0';
fragment FLOAT_DECIMAL_PART: '.' [0-9]*;
fragment FLOAT_EXPONENT_PART: [eE] SIGN? [0-9]+;

/********************** COMMENT ***********************/
COMMENT: '##' .*? '##' -> skip;
/********************* KEY WORDS **********************/
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
fragment TRUE: 'True'; // Đem vào boolean literal
fragment FALSE: 'False';
VAR: 'Var';
VAL: 'Val';
SELF: 'Self';
RETURN: 'Return';
IN: 'In';
BY: 'By';
NEW: 'New';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NULL: 'Null';
/********************* TYPES **********************/
CLASS: 'Class';
ARRAY: 'Array';
INTEGER: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
/********************* LITERALS ***********************/
ZERO_INTEGER: '0' | '00' | '0b0' | '0B0' | '0x0' | '0X0'; // Tách 0 ra để những ràng buộc > 0 ở parser
INTEGER_LITERAL : (
                DEC_INTEGER_LITERAL 
                | OCT_INTEGER_LITERAL 
                | HEX_INTEGER_LITERAL 
                | BIN_INTEGER_LITERAL
) {
    self.text = self.text.translate(str.maketrans('','','_'))
}; // remove _ character


STRING_LITERAL: '"' (STRING_CHAR)* '"' {
	self.text = self.text[1:-1]
}; // remove open and close string
BOOLEAN_LITERAL: TRUE | FALSE;
FLOAT_LITERAL   : (
                FLOAT_INTEGER_PART FLOAT_DECIMAL_PART FLOAT_EXPONENT_PART?
                | FLOAT_INTEGER_PART FLOAT_EXPONENT_PART
                | FLOAT_DECIMAL_PART FLOAT_EXPONENT_PART

) {
    self.text = self.text.translate(str.maketrans('','','_'))
};







/********************* OPERATORS **********************/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
ASSIGN: '=';
NOT_EQUAL: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
STRING_EQUAL: '==.';
STRING_ADD: '+.';

/******************** SEPARATORS **********************/
LP: '(' ;
RP: ')' ;

LSB: '[';
RSB: ']';

DOT: '.';
DOUBLE_DOT: '..';
COMMA: ',';
SEMI: ';';
COLON: ':';
DOUBLE_COLON: '::';

LCB: '{';
RCB: '}';

/******************** IDENTIFIERS *********************/
//_NUMBER is ID, not INTEGER_LITERAL
ID: [_a-zA-Z][_a-zA-Z0-9]*;
DOLLAR_ID: ('$')[_a-zA-Z0-9]+;

/*********************** SKIP *************************/
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines


/*********************** ERRORS *************************/
// NOT(##) = NOT(#) OR # NOT(#)
// 1. ## NOT(##) EOF
// 2. ## NOT(#) #EOF ---- CASE # BEFORE EOF --> NOT(##) EOF CAN'T CATCH
/*UNTERMINATED_COMMENT    : (
                        '##' COMMENT_CHAR* EOF
                        | '##' ~'#'* '#' EOF
)  {
	raise UnterminatedComment()
};
*/

UNCLOSE_STRING: '"' STRING_CHAR* {
    raise UncloseString(self.text[1:]);
};

ILLEGAL_ESCAPE: '"' STRING_CHAR* ILLEGAL_SEQUENCE {
    raise IllegalEscape(self.text[1:])
};
ERROR_TOKEN: . {
    raise ErrorToken(self.text)
};
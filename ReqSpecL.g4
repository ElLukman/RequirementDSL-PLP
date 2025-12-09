grammar ReqSpecL;

// --- Parser Rules ---
program     : definition+ EOF;

definition  : actor_def 
            | var_def       
            | endpoint_def  
            | feature_def;

var_def     : KW_DEF_CTX ID '=' STRING ';';

endpoint_def: KW_DEF_API ID method STRING ';';

method      : 'GET' | 'POST' | 'PUT' | 'DELETE';

actor_def   : KW_ACTOR ID ';';

feature_def : KW_FEATURE ID '{' scenario_def* '}';

scenario_def: KW_SCENARIO STRING '{' 
            given_clause*
            when_clause 
            then_clause* error_clause? 
'}';

given_clause: KW_GIVEN (STRING | ID) ';'; 

when_clause : KW_WHEN STRING ';';
then_clause : KW_THEN STRING ';';
error_clause: KW_ERROR STRING ';';

// --- Lexer Rules ---
KW_ACTOR    : 'def_actor';
KW_FEATURE  : 'def_feature';
KW_DEF_CTX  : 'def_context'; 
KW_DEF_API  : 'def_endpoint'; 
KW_SCENARIO : 'scenario';
KW_GIVEN    : 'given';
KW_WHEN     : 'when';
KW_THEN     : 'then';
KW_ERROR    : 'expect_error'; 

ID          : [a-zA-Z_] [a-zA-Z0-9_]*;
STRING      : '"' (~["])* '"';
WS          : [ \t\r\n]+ -> skip;
SL_COMMENT  : '//' .*? '\n' -> skip;
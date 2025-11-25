grammar ReqSpecL;

// --- Parser Rules (Struktur Kalimat) ---
program     : definition+ EOF;

definition  : actor_def | feature_def;

actor_def   : KW_ACTOR ID ';';

feature_def : KW_FEATURE ID '{' scenario_def* '}';

scenario_def: KW_SCENARIO STRING '{' 
              given_clause*
              when_clause 
              then_clause+ 
              '}';

given_clause: KW_GIVEN STRING ';';
when_clause : KW_WHEN STRING ';';
then_clause : KW_THEN STRING ';';

// --- Lexer Rules (Kosa Kata) ---
KW_ACTOR    : 'def_actor';
KW_FEATURE  : 'def_feature';
KW_SCENARIO : 'scenario';
KW_GIVEN    : 'given';
KW_WHEN     : 'when';
KW_THEN     : 'then';

ID          : [a-zA-Z_] [a-zA-Z0-9_]*;
STRING      : '"' (~["])* '"';
WS          : [ \t\r\n]+ -> skip;
SL_COMMENT  : '//' .*? '\n' -> skip;
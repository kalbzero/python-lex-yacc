
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programAND ASSIGN BREAK CASE CHAR COLON COMMA DECIMAL DEFAULT DIFF DIVIDE DIVIDEEQUALS ELSE EQUALS EXPLAMATION FLOAT ID IF INT LBRACE LPAREN MAIOR MAIOREQUALS MENOR MENOREQUALS MINUS MINUSEQUALS NUMBER OR PLUS RBRACE RPAREN SEMICOLON STRING SUMEQUALS SWITCH TIMES TIMESEQUALSprogram : sequence_declarationsequence_declaration : declaration sequence_declaration \n                            | declarationdeclaration  : type variavel define_end_of_instruction\n                    | statement_if\n                    | statement_switchstatement_if : IF LPAREN expression RPAREN LBRACE declaration RBRACE\n                    | IF LPAREN expression RPAREN LBRACE declaration RBRACE ELSE LBRACE declaration RBRACEstatement_switch : SWITCH LPAREN ID RPAREN LBRACE define_cases define_default RBRACEdefine_cases : CASE value COLON LBRACE declaration define_break RBRACE define_default\n                    | CASE value COLON LBRACE declaration define_break RBRACE define_casesdefine_default : DEFAULT COLON LBRACE declaration define_break RBRACEexpression : condition MAIOR condition\n                  | condition MENOR condition\n                  | condition MAIOREQUALS condition\n                  | condition MENOREQUALS condition\n                  | condition EQUALS condition\n                  | condition DIFF condition\n                  | condition AND condition\n                  | condition OR conditiontype : INT\n            | FLOAT\n            | CHARvalue : NUMBER\n            | DECIMAL\n            | STRINGcondition : type\n                 | valuevariavel : ID\n                | ID COMMA variaveldefine_end_of_instruction : SEMICOLONdefine_break : BREAK define_end_of_instruction'
    
_lr_action_items = {'INT':([0,3,5,6,15,17,18,30,31,32,33,34,35,36,37,39,52,57,60,61,62,66,],[7,7,-5,-6,7,-4,-31,7,7,7,7,7,7,7,7,7,-7,-9,7,7,7,-8,]),'FLOAT':([0,3,5,6,15,17,18,30,31,32,33,34,35,36,37,39,52,57,60,61,62,66,],[8,8,-5,-6,8,-4,-31,8,8,8,8,8,8,8,8,8,-7,-9,8,8,8,-8,]),'CHAR':([0,3,5,6,15,17,18,30,31,32,33,34,35,36,37,39,52,57,60,61,62,66,],[9,9,-5,-6,9,-4,-31,9,9,9,9,9,9,9,9,9,-7,-9,9,9,9,-8,]),'IF':([0,3,5,6,17,18,39,52,57,60,61,62,66,],[10,10,-5,-6,-4,-31,10,-7,-9,10,10,10,-8,]),'SWITCH':([0,3,5,6,17,18,39,52,57,60,61,62,66,],[11,11,-5,-6,-4,-31,11,-7,-9,11,11,11,-8,]),'$end':([1,2,3,5,6,12,17,18,52,57,66,],[0,-1,-3,-5,-6,-2,-4,-31,-7,-9,-8,]),'ID':([4,7,8,9,16,19,],[14,-21,-22,-23,27,14,]),'RBRACE':([5,6,17,18,49,52,53,57,63,66,67,69,70,71,],[-5,-6,-4,-31,52,-7,57,-9,66,-8,70,72,-12,-32,]),'BREAK':([5,6,17,18,52,57,64,65,66,],[-5,-6,-4,-31,-7,-9,68,68,-8,]),'MAIOR':([7,8,9,21,22,23,24,25,26,],[-21,-22,-23,30,-27,-28,-24,-25,-26,]),'MENOR':([7,8,9,21,22,23,24,25,26,],[-21,-22,-23,31,-27,-28,-24,-25,-26,]),'MAIOREQUALS':([7,8,9,21,22,23,24,25,26,],[-21,-22,-23,32,-27,-28,-24,-25,-26,]),'MENOREQUALS':([7,8,9,21,22,23,24,25,26,],[-21,-22,-23,33,-27,-28,-24,-25,-26,]),'EQUALS':([7,8,9,21,22,23,24,25,26,],[-21,-22,-23,34,-27,-28,-24,-25,-26,]),'DIFF':([7,8,9,21,22,23,24,25,26,],[-21,-22,-23,35,-27,-28,-24,-25,-26,]),'AND':([7,8,9,21,22,23,24,25,26,],[-21,-22,-23,36,-27,-28,-24,-25,-26,]),'OR':([7,8,9,21,22,23,24,25,26,],[-21,-22,-23,37,-27,-28,-24,-25,-26,]),'RPAREN':([7,8,9,20,22,23,24,25,26,27,40,41,42,43,44,45,46,47,],[-21,-22,-23,29,-27,-28,-24,-25,-26,38,-13,-14,-15,-16,-17,-18,-19,-20,]),'LPAREN':([10,11,],[15,16,]),'SEMICOLON':([13,14,28,68,],[18,-29,-30,18,]),'COMMA':([14,],[19,]),'NUMBER':([15,30,31,32,33,34,35,36,37,51,],[24,24,24,24,24,24,24,24,24,24,]),'DECIMAL':([15,30,31,32,33,34,35,36,37,51,],[25,25,25,25,25,25,25,25,25,25,]),'STRING':([15,30,31,32,33,34,35,36,37,51,],[26,26,26,26,26,26,26,26,26,26,]),'COLON':([24,25,26,54,55,],[-24,-25,-26,58,59,]),'LBRACE':([29,38,56,58,59,],[39,48,60,61,62,]),'CASE':([48,72,],[51,51,]),'DEFAULT':([50,70,72,73,74,],[54,-12,54,-10,-11,]),'ELSE':([52,],[56,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'sequence_declaration':([0,3,],[2,12,]),'declaration':([0,3,39,60,61,62,],[3,3,49,63,64,65,]),'type':([0,3,15,30,31,32,33,34,35,36,37,39,60,61,62,],[4,4,22,22,22,22,22,22,22,22,22,4,4,4,4,]),'statement_if':([0,3,39,60,61,62,],[5,5,5,5,5,5,]),'statement_switch':([0,3,39,60,61,62,],[6,6,6,6,6,6,]),'variavel':([4,19,],[13,28,]),'define_end_of_instruction':([13,68,],[17,71,]),'expression':([15,],[20,]),'condition':([15,30,31,32,33,34,35,36,37,],[21,40,41,42,43,44,45,46,47,]),'value':([15,30,31,32,33,34,35,36,37,51,],[23,23,23,23,23,23,23,23,23,55,]),'define_cases':([48,72,],[50,74,]),'define_default':([50,72,],[53,73,]),'define_break':([64,65,],[67,69,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> sequence_declaration','program',1,'p_program','etapa2_yacc.py',19),
  ('sequence_declaration -> declaration sequence_declaration','sequence_declaration',2,'p_sequence_declaration','etapa2_yacc.py',23),
  ('sequence_declaration -> declaration','sequence_declaration',1,'p_sequence_declaration','etapa2_yacc.py',24),
  ('declaration -> type variavel define_end_of_instruction','declaration',3,'p_declaration','etapa2_yacc.py',28),
  ('declaration -> statement_if','declaration',1,'p_declaration','etapa2_yacc.py',29),
  ('declaration -> statement_switch','declaration',1,'p_declaration','etapa2_yacc.py',30),
  ('statement_if -> IF LPAREN expression RPAREN LBRACE declaration RBRACE','statement_if',7,'p_statement_if','etapa2_yacc.py',34),
  ('statement_if -> IF LPAREN expression RPAREN LBRACE declaration RBRACE ELSE LBRACE declaration RBRACE','statement_if',11,'p_statement_if','etapa2_yacc.py',35),
  ('statement_switch -> SWITCH LPAREN ID RPAREN LBRACE define_cases define_default RBRACE','statement_switch',8,'p_statement_switch','etapa2_yacc.py',43),
  ('define_cases -> CASE value COLON LBRACE declaration define_break RBRACE define_default','define_cases',8,'p_define_cases','etapa2_yacc.py',47),
  ('define_cases -> CASE value COLON LBRACE declaration define_break RBRACE define_cases','define_cases',8,'p_define_cases','etapa2_yacc.py',48),
  ('define_default -> DEFAULT COLON LBRACE declaration define_break RBRACE','define_default',6,'p_define_default','etapa2_yacc.py',52),
  ('expression -> condition MAIOR condition','expression',3,'p_expression','etapa2_yacc.py',55),
  ('expression -> condition MENOR condition','expression',3,'p_expression','etapa2_yacc.py',56),
  ('expression -> condition MAIOREQUALS condition','expression',3,'p_expression','etapa2_yacc.py',57),
  ('expression -> condition MENOREQUALS condition','expression',3,'p_expression','etapa2_yacc.py',58),
  ('expression -> condition EQUALS condition','expression',3,'p_expression','etapa2_yacc.py',59),
  ('expression -> condition DIFF condition','expression',3,'p_expression','etapa2_yacc.py',60),
  ('expression -> condition AND condition','expression',3,'p_expression','etapa2_yacc.py',61),
  ('expression -> condition OR condition','expression',3,'p_expression','etapa2_yacc.py',62),
  ('type -> INT','type',1,'p_define_type','etapa2_yacc.py',74),
  ('type -> FLOAT','type',1,'p_define_type','etapa2_yacc.py',75),
  ('type -> CHAR','type',1,'p_define_type','etapa2_yacc.py',76),
  ('value -> NUMBER','value',1,'p_define_value','etapa2_yacc.py',80),
  ('value -> DECIMAL','value',1,'p_define_value','etapa2_yacc.py',81),
  ('value -> STRING','value',1,'p_define_value','etapa2_yacc.py',82),
  ('condition -> type','condition',1,'p_define_condition','etapa2_yacc.py',86),
  ('condition -> value','condition',1,'p_define_condition','etapa2_yacc.py',87),
  ('variavel -> ID','variavel',1,'p_variavel','etapa2_yacc.py',91),
  ('variavel -> ID COMMA variavel','variavel',3,'p_variavel','etapa2_yacc.py',92),
  ('define_end_of_instruction -> SEMICOLON','define_end_of_instruction',1,'p_define_end_of_instruction','etapa2_yacc.py',96),
  ('define_break -> BREAK define_end_of_instruction','define_break',2,'p_define_break','etapa2_yacc.py',99),
]

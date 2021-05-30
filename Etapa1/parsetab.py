
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programCHAR COMMA FLOAT ID INT SEMICOLONprogram : sequence_declarationsequence_declaration : declaration sequence_declaration \n                            | declarationdeclaration  : type variavel define_end_of_instructiontype : INT\n            | FLOAT\n            | CHARvariavel : ID\n                | ID COMMA variaveldefine_end_of_instruction : SEMICOLON'
    
_lr_action_items = {'INT':([0,3,11,12,],[5,5,-4,-10,]),'FLOAT':([0,3,11,12,],[6,6,-4,-10,]),'CHAR':([0,3,11,12,],[7,7,-4,-10,]),'$end':([1,2,3,8,11,12,],[0,-1,-3,-2,-4,-10,]),'ID':([4,5,6,7,13,],[10,-5,-6,-7,10,]),'SEMICOLON':([9,10,14,],[12,-8,-9,]),'COMMA':([10,],[13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'sequence_declaration':([0,3,],[2,8,]),'declaration':([0,3,],[3,3,]),'type':([0,3,],[4,4,]),'variavel':([4,13,],[9,14,]),'define_end_of_instruction':([9,],[11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> sequence_declaration','program',1,'p_program','etapa1_yacc.py',18),
  ('sequence_declaration -> declaration sequence_declaration','sequence_declaration',2,'p_sequence_declaration','etapa1_yacc.py',22),
  ('sequence_declaration -> declaration','sequence_declaration',1,'p_sequence_declaration','etapa1_yacc.py',23),
  ('declaration -> type variavel define_end_of_instruction','declaration',3,'p_declaration','etapa1_yacc.py',27),
  ('type -> INT','type',1,'p_define_type','etapa1_yacc.py',31),
  ('type -> FLOAT','type',1,'p_define_type','etapa1_yacc.py',32),
  ('type -> CHAR','type',1,'p_define_type','etapa1_yacc.py',33),
  ('variavel -> ID','variavel',1,'p_variavel','etapa1_yacc.py',37),
  ('variavel -> ID COMMA variavel','variavel',3,'p_variavel','etapa1_yacc.py',38),
  ('define_end_of_instruction -> SEMICOLON','define_end_of_instruction',1,'p_define_end_of_instruction','etapa1_yacc.py',42),
]
# ------------------------------------------------------------
# Etapa 03 - Peso 1.0
# ------------------------------------------------------------
import ply.yacc as yacc
import declarations
from declarations import *
import errors
 
# Get the token map from the lexer.  This is required.
from etapa3_lex import tokens

GLOBAL="GLOBAL"
var_global = Escopo(GLOBAL)

#---------------------------------------
# Regra Inicial (S)
#---------------------------------------
def p_program(t):
    'program : sequence_declaration'
    t[0]=t[1]

def p_sequence_declaration(t):
    '''sequence_declaration : declaration sequence_declaration 
                            | declaration'''
    t[0]=t[1]

def p_declaration(t):
    '''declaration  : type variavel define_end_of_instruction
                    | op_math
                    | statement_if
                    | statement_switch
                    | statement_for
                    | statement_while '''
    t[0]=t[1]

def p_statement_if(t):
    '''statement_if : IF LPAREN expression RPAREN LBRACE declaration RBRACE
                    | IF LPAREN expression RPAREN LBRACE declaration RBRACE ELSE LBRACE declaration RBRACE''' 
    if(t[3]):
        t[0]=t[6]
    else:
        if(len(t)>10): #with else
            t[0]=t[10]

def p_statement_switch(t):
    '''statement_switch : SWITCH LPAREN ID RPAREN LBRACE define_cases define_default RBRACE''' 
    t[0]=t[1]

def p_define_cases(t):
    '''define_cases : CASE value COLON LBRACE declaration define_break RBRACE
                    | CASE value COLON LBRACE declaration define_break RBRACE define_cases''' 
    t[0]=t[1]

def p_define_default(t):
    '''define_default : DEFAULT COLON LBRACE declaration define_break RBRACE'''
    t[0]=t[1]

def p_statement_while(t):
    '''statement_while : WHILE LPAREN expression RPAREN LBRACE declaration RBRACE'''
    t[0]=t[1]

def p_statement_for(t):
    '''statement_for  :  FOR LPAREN condition_for SEMICOLON expression SEMICOLON alter_value RPAREN LBRACE declaration RBRACE'''
    t[0]=t[1]

def p_condition_for(t):
    '''condition_for : INT ID ASSIGN NUMBER define_end_of_instruction expression define_end_of_instruction alter_value define_end_of_instruction'''
    t[0]=t[1]

def p_alter_value(t):
    ''' alter_value : ID PLUS PLUS 
                    | PLUS PLUS ID 
                    | ID MINUS MINUS 
                    | MINUS MINUS ID'''

def p_op_math(t):
    ''' op_math : ID ASSIGN ID PLUS ID define_end_of_instruction op_math
                | ID ASSIGN ID MINUS ID define_end_of_instruction op_math
                | ID ASSIGN ID TIMES ID define_end_of_instruction op_math
                | ID ASSIGN ID DIVIDE ID define_end_of_instruction op_math
                | ID ASSIGN ID PLUS ID define_end_of_instruction
                | ID ASSIGN ID MINUS ID define_end_of_instruction
                | ID ASSIGN ID TIMES ID define_end_of_instruction
                | ID ASSIGN ID DIVIDE ID define_end_of_instruction'''
    if t[4] == PLUS  : t[1] = t[3] + t[5]
    elif t[4] == MINUS : t[1] = t[3] - t[5]
    elif t[4] == DIVIDE : t[1] = t[3] / t[5]
    elif t[4] == TIMES : t[1] = t[3] * t[5]
    else: t[0]=t[1]

def p_expression(t):
    '''expression : condition MAIOR condition
                  | condition MENOR condition
                  | condition MAIOREQUALS condition
                  | condition MENOREQUALS condition
                  | condition EQUALS condition
                  | condition DIFF condition
                  | condition AND condition
                  | condition OR condition'''
    if t[2] == '>'  : t[0] = t[1] > t[3]
    elif t[2] == '<': t[0] = t[1] < t[3]
    elif t[2] == '>=': t[0] = t[1] >= t[3]
    elif t[2] == '<=': t[0] = t[1] <= t[3]
    elif t[2] == '==': t[0] = t[1] == t[3]
    elif t[2] == '!=': t[0] = t[1] != t[3]
    elif t[2] == '&&': t[0] = t[1] and t[3]
    elif t[2] == '||': t[0] = t[1] or t[3]
    else: errors.unknownSignal(t)

def p_define_type(t):
    '''type : INT
            | FLOAT
            | CHAR'''
    t[0]=t[1]

def p_define_value(t):
    '''value : NUMBER
             | DECIMAL
             | STRING'''
    t[0]=t[1]

def p_define_condition(t):
    '''condition : ID
                 | value'''
    t[0]=t[1]

def p_variavel(t):
    '''variavel : ID
                | ID COMMA variavel
                | ID ASSIGN value
                | ID ASSIGN value COMMA variavel '''
    t[0]=t[1]
    
def p_define_end_of_instruction(p):
    'define_end_of_instruction : SEMICOLON'

def p_define_break(t):
    'define_break : BREAK define_end_of_instruction'
    
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

#---------------------------------------
# Buildar o parser, conferir os arquivos parser.out e parsetab.py
#---------------------------------------
# parser = yacc.yacc()
parser=yacc.yacc(start='program')

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
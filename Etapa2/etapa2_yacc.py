# ------------------------------------------------------------
# Etapa 02 - Peso 1.0
# ------------------------------------------------------------
import ply.yacc as yacc
import declarations
from declarations import *
 
# Get the token map from the lexer.  This is required.
from etapa1_lex import tokens

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
    '''declaration  : type variavel define_end_of_instruction'''
    t[0]=t[1]

def p_define_type(t):
    '''type : INT
            | FLOAT
            | CHAR'''
    t[0]=t[1]

def p_variavel(t):
    '''variavel : ID
                | ID COMMA variavel'''
    t[0] = t[1]
    
def p_define_end_of_instruction(p):
    'define_end_of_instruction : SEMICOLON'

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
# ------------------------------------------------------------
# Trabalho 01 - Peso 0.5
#
# https://www.dabeaz.com/ply/ply.html#ply_nn4
# https://stackoverflow.com/questions/34594597/create-c-parser-with-ply
#
# Apresente a Gramática e os analisadores léxicos e sintáticos para o reconhecimento de
# declaração de variáveis no estilo da Linguagem C (leia com atenção as especificações abaixo,
# não deve ser implementado nem mais, nem menos).
#
# - Devem reconhecer os tipos: char – int – float
# - O char pode ser um caractere ou uma cadeia.
# - As variáveis são apenas declaradas, não sendo possível inicializar
# - Identificadores: de acordo com as regras da Linguagem C
# - Podes ser declarados individualmente ou por uma lista (sendo lista separados por vírgulas).
# - A finalização de cada declaração será por ponto-e-vírgula (;).
# ------------------------------------------------------------
import ply.lex as lex

# Lista do nome dos tokens   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Palavras reservadas
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'do' : 'DO'
}

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
3 + 4 * 10
+ -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
    # print(tok.type, tok.value, tok.lineno, tok.lexpos)
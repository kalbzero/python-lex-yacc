# ------------------------------------------------------------
# Etapa 02 - Peso 1.0
# ------------------------------------------------------------
import ply.lex as lex

# Lista do nome dos tokens
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

# Expressões regulares dos tokens acima
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_CHAR    = r'char'
t_INT     = r'int'
t_FLOAT   = r'float'

# Uma string que tem caracteres ignorados (espacos e tabs)
t_ignore  = ' \t'

# Expressão Regular com algum codigo
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Regra para identificar a quebra de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regra para lidar com erros
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Buildar o lexer
lexer = lex.lex()

# Codigo para testar
data = '''
3 + 4 * 10
+ -20 *2
'''

# Coloque o data na funcao input()
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # Quando termina a leitura
    print(tok)
    # print(tok.type, tok.value, tok.lineno, tok.lexpos)
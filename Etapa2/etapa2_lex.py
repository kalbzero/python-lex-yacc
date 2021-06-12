# ------------------------------------------------------------
# Etapa 01 - Peso 0.5
# ------------------------------------------------------------
import ply.lex as lex

# Lista do nome dos tokens
tokens = (
    'ID',
    'INT',
    'FLOAT',
    'CHAR',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'IF',
    'ELSE',
    'SWITCH',
    'CASE',
    'BREAK',
    'DEFAULT',
    'RPAREN',
    'LPAREN',
    'RBRACE',
    'LBRACE',
    'OR',
    'AND',
    'EXPLAMATION',
    'EQUALS',
    'DIFF',
    'MENOR',
    'MAIOR',
    'MENOREQUALS',
    'MAIOREQUALS',
    'SUMEQUALS',
    'MINUSEQUALS',
    'TIMESEQUALS',
    'DIVIDEEQUALS'
)

# Expressões regulares dos tokens acima
t_ignore        = ' \t'
t_INT           = r'int'
t_FLOAT         = r'float'
t_CHAR          = r'char'
t_COMMA         = r','
t_SEMICOLON     = r';'

t_COLON         = r':'
t_RPAREN        = r'\)'
t_LPAREN        = r'\('
t_RBRACE        = r'\}'
t_LBRACE        = r'\{'

t_OR 			= r'\|\|'
t_AND			= r'&&'
t_EXPLAMATION	= r'!'

t_EQUALS		= r'=='
t_DIFF			= r'!='
t_MENOR			= r'<'
t_MAIOR			= r'>'
t_MENOREQUALS	= r'<='
t_MAIOREQUALS 	= r'>='

t_SUMEQUALS		= r'\+='
t_MINUSEQUALS	= r'-='
t_TIMESEQUALS 	= r'\*='
t_DIVIDEEQUALS	= r'/='

# Palavras reservadas
reserved = {
    'int'    : 'INT',
    'float'  : 'FLOAT',
    'char'   : 'CHAR',
    'if'	 : 'IF',
	'else'	 : 'ELSE',
    'switch' : 'SWITCH',
    'case'   : 'CASE',
    'break'  : 'BREAK',
    'default': 'DEFAULT',
}

# Expressão Regular para identificar ID's
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
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

# Coloque o código a ser testado na variável 'data'

#1 - reconhecer os comandos: if – else – switch
data = '''
if()
'''

#2 - O char pode ser um caractere ou uma cadeia.
# data = '''
# char a;
# char name;
# '''

#3 - As variáveis são apenas declaradas, não sendo possível inicializar.
# data = '''
# float age;
# float money = 25.1;
# '''

#4 - Identificadores: iniciam por letras ou _, depois do segundo caractere pode ser número, letra ou _ e o único caractere especial reconhecido é o _
# data = '''
# int number;
# int _number;
# char p1;
# char pp;
# char p_;
# '''
# data = '''
# int #number;
# int p-age;
# char p.name;
# '''

#5 - Podes ser declarados individualmente ou por uma lista (sendo lista separados por vírgulas)
data = '''
char a;
'''

# Coloque a 'data' na funcao input()
lexer.input(data)

# Tokenize
print('Ex: Token - Valor')
while True:
    tok = lexer.token()
    if not tok: 
        break      # Quando termina a leitura
    # print(tok)
    print(tok.type, tok.value) #tok.lineno, tok.lexpos
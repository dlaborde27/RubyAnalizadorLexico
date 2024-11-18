import ply.lex as lex

palabras_reservadas = {
#INICIO DARIO LABORDE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO DARIO LABORDE
    # Palabras reservadas
    'begin': 'BEGIN',
    'break': 'BREAK',
    'case': 'CASE',
    'class': 'CLASS',
    'def': 'DEF',
    'do': 'DO',
    'end': 'END',
    'elsif': 'ELSIF',
    'else': 'ELSE',
    'for': 'FOR',
    'if': 'IF',
    'in': 'IN',
    'module': 'MODULE',
    'return': 'RETURN',
    'self': 'SELF',
    'unless': 'UNLESS',
    'until': 'UNTIL',
    'when': 'WHEN',
    'while': 'WHILE',
    'and': 'AND_RESERVED',
    'or': 'OR_RESERVED',
    'then': 'THEN',
    'Set' : 'SET',
    'Proc' : 'PROC',
    'call' : 'CALL',
#FIN DARIO LABORDE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DARIO LABORDE
#INICIO JORDAN SALINAS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO JORDAN SALINAS
    # Otros términos o métodos comunes
    'array': 'ARRAY',
    'chomp': 'CHOMP',
    'defined?': 'DEFINED',
    'gets': 'GETS',
    'new': 'NEW',
    'puts': 'PUTS',
    'redo': 'REDO',
    'to_f': 'TO_F',
    'to_i': 'TO_I'
#FIN JORDAN SALINAS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN JORDAN SALINAS
}

tokens = (
#INICIO DARIO LABORDE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO DARIO LABORDE
    # Variables / constantes / tipos de dato
    'LOCAL_VARIABLE',
    'INSTANCE_VARIABLE',
    'CLASS_VARIABLE',
    'GLOBAL_VARIABLE',
    'CONSTANT',
    'INTEGER',
    'FLOAT',
    'STRING',
    'BOOLEAN',
    'NIL',
    'SYMBOL',

    # Operadores aritméticos
    'DIVIDE',
    'EXPONENT',
    'MINUS',
    'MODULO',
    'MULTIPLY',
    'PLUS',

    # Operadores de comparación
    'CASE_EQUAL',
    'EQUAL',
    'GREATER_THAN',
    'GREATER_THAN_EQUAL',
    'LESS_THAN',
    'LESS_THAN_EQUAL',
    'NOT_EQUAL',
    'SPACESHIP',
#FIN DARIO LABORDE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DARIO LABORDE
#INICIO JORDAN SALINAS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO JORDAN SALINAS
    # Puntuación y operadores de separación
    'COLON',
    'COMMA',
    'DOT',
    'HASH',
    'PERCENT_W',
    'LEFT_PAR',
    'RIGHT_PAR',
    'LEFT_COR',
    'RIGHT_COR',

    # Operadores de asignación
    'ASSIGN',
    'DIVIDE_ASSIGN',
    'MODULO_ASSIGN',
    'MULTIPLY_ASSIGN',
    'PLUS_ASSIGN',
    'EXPONENT_ASSIGN',
    'MINUS_ASSIGN',

    # Operadores lógicos y de bits
    'AND',
    'NOT',
    'OR',
    'AMPERSAND',
    'PIPE',

    # Caracteres especiales y de escape
    'BACKSLASH',
    'NEWLINE',
    'SPACE',
    'TAB',
    'DOUBLE_QUOTE',

    # Rango y otros operadores especiales
    'RANGE_EX',
    'RANGE_IN',
#FIN JORDAN SALINAS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN JORDAN SALINAS
) + tuple(palabras_reservadas.values())

#INICIO DARIO LABORDE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO DARIO LABORDE
# Variables / constantes / tipos de dato
t_INSTANCE_VARIABLE = r'@[a-z_A-Z]\w*'
t_CLASS_VARIABLE = r'@{2}[a-z_A-Z]\w*'
t_GLOBAL_VARIABLE = r'\$[a-z_A-Z]\w*'
t_CONSTANT = r'[A-Z]\w*'
t_STRING = r'"[^"]*"'
t_BOOLEAN = r'\b(true|false)\b'
t_SYMBOL = r':[a-zA-Z_]\w*'

# Operadores aritméticos
t_DIVIDE = r'/'
t_EXPONENT = r'\*\*'
t_MINUS = r'-'
t_MODULO = r'%'
t_MULTIPLY = r'\*'
t_PLUS = r'\+'

# Operadores de comparación
t_CASE_EQUAL = r'==='
t_EQUAL = r'=='
t_GREATER_THAN = r'>'
t_GREATER_THAN_EQUAL = r'>='
t_LESS_THAN = r'<'
t_LESS_THAN_EQUAL = r'<='
t_NOT_EQUAL = r'!='
t_SPACESHIP = r'<=>'
#FIN DARIO LABORDE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DARIO LABORDE

#INICIO JORDAN SALINAS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO JORDAN SALINAS
# Puntuación y operadores de separación
t_COLON = r':'
t_COMMA = r','
t_DOT = r'\.'
t_HASH = r'\{[^{}]*\}'
t_PERCENT_W = r'%\w'
t_LEFT_PAR = r'\('
t_RIGHT_PAR = r'\)'
t_LEFT_COR = r'\['
t_RIGHT_COR = r'\]'

# Operadores de asignación
t_ASSIGN = r'='
t_DIVIDE_ASSIGN = r'/='
t_EXPONENT_ASSIGN = r'\*\*='
t_MINUS_ASSIGN = r'-='
t_MODULO_ASSIGN = r'%='
t_MULTIPLY_ASSIGN = r'\*='
t_PLUS_ASSIGN = r'\+='

# Operadores lógicos y de bits
t_AND = r'&&'
t_AMPERSAND = r'&'
t_PIPE = r'\|'
t_NOT = r'!'
t_OR = r'\|\|'

# Caracteres especiales y de escape
t_SPACE = r'\s'

# Rango y otros operadores especiales
t_RANGE_EX = r'\.\.\.'
t_RANGE_IN = r'\.\.'
#FIN JORDAN SALINAS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN JORDAN SALINAS

#INICIO DARIO LABORDE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO DARIO LABORDE
# Variables y constantes
def t_LOCAL_VARIABLE(t):
    r'[_a-z]\w*'
    if t.value in palabras_reservadas:
        t.type = palabras_reservadas[t.value]
    return t

def t_FLOAT(t):
    r'(\d+\.\d*|\d*\.\d+)'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NIL(t):
    r'\bnil\b'
    t.value = None
    return t

def t_error(t):
    print(f"Token no admitido '{t.value[0]}' en la linea {t.lineno}")
    t.lexer.skip(1)

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'
#FIN DARIO LABORDE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DARIO LABORDE

#INICIO JORDAN SALINAS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO JORDAN SALINAS
def t_COMMENT(t):
    r'\#.*'
    pass

def t_NEWLINE(t):
    r'\\n'
    t.value = '\n'
    return t

def t_TAB(t):
    r'\\t'
    t.value = '\t'
    return t

def t_BACKSLASH(t):
    r'\\\\'
    t.value = '\\'
    return t

def t_DOUBLE_QUOTE(t):
    r'\\"'
    t.value = '"'
    return t
#FIN JORDAN SALINAS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN JORDAN SALINAS
def llamada_lexer():
    lexer = lex.lex()
#INICIO DARIO LABORDE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO DARIO LABORDE
def ejecutarAnalizador(algoritmo_ruby, usuario_github, fecha_hora):
    lexer = lex.lex()
    lexer.input(algoritmo_ruby)
    tokens = []
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)
        tokens.append(token)

    filename = f"./logs/lexico/lexico-{usuario_github}-{fecha_hora.strftime('%d%m%Y-%Hh%M')}.txt"

    with open(filename, "w") as file:
        for token in tokens:
            file.write(str(token) + "\n")
#FIN DARIO LABORDE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DARIO LABORDE
reserved={'Hasta': 'UNTIL', 'Cuando': 'WHEN', 
'DEFAULT': 'DEFAULT', 'EnTons': 'THEN', 'Desde':'FROM',
'Haga' : 'DO', 'SiNo': 'IFNOT', 'Inicio': 'START',
'Repita': 'REPEAT', 'Final': 'END', 'Ini': 'INI',
'Fin_EnCaso': 'ENDINCASE', 'Proc': 'PROCEDURE',
'EnCaso': 'INCASE', 'Fin_Desde': 'ENDSINCE', 'Inc': 'INC',
'Rellene': 'FILL', 'DiagonalD': 'DIAGR', 
'HastaEncontrar': 'TOFIND', 'DCL': 'DECLARE', 
'DiagonalI': 'DIAGL', 'Llamar': 'CALL', 'Punto': 'DOT'
}

tokens = [
    'ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE','CONDITION',
    'LPAREN','RPAREN','LBRACKET','RBRACKET','SEMICOLON']+list(reserved.values())

#'CONDITIONAL',
# Tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'  
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\{'
t_RBRACKET  = r'\}'
t_SEMICOLON = r';'
# Ignored characters space and taps
t_ignore = " \t"

def t_CONDITION(t):
    r'<>|>=|<=|=|<|>'
    return t

def t_NUMBER(t):
	r'\d+'
	try:
		t.value = int(t.value)
	except ValueError:
		print("Integer value too large %d", t.value)
		t.value = 0

	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if(t.value in reserved):
        t.type = reserved.get(t.value)    # Check for reserved words
    return t

# Build the lexer
import ply.lex as lex
lexer = lex.lex()



reserved={'Hasta': 'UNTIL', 'Cuando': 'WHEN', 
'DEFAULT': 'DEFAULT', 'EnTons': 'THEN', 'Desde':'FROM',
'Haga' : 'DO', 'SiNo': 'IFNOT', 'Inicio': 'START',
'Repita': 'REPEAT', 'Final': 'END', 'Ini': 'INITIALIZE',
'Fin_EnCaso': 'ENDINCASE', 'Proc': 'PROCEDURE',
'EnCaso': 'INCASE', 'Fin_Desde': 'ENDFROM', 'Inc': 'INCREASE',
'Rellene': 'FILL', 'DiagonalD': 'DIAGR','Dec':'DECREASE',
'HastaEncontrar': 'TOFIND', 'DCL': 'DECLARE',
'DiagonalI': 'DIAGL', 'Llamar': 'CALL', 'Punto': 'DOT'
}
tokens = [
    'ID','NUMBER','CONDITION','LPAREN','RPAREN','LBRACKET',
    'RBRACKET','SEMICOLON','COMMA','COLOR','COLON']+list(reserved.values())



# Tokens
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\{'
t_RBRACKET  = r'\}'
t_COLON     = r'\:'
t_COMMA     = r','
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
    if(t.value=='Azul' or t.value=='Rojo'):
        t.type = 'COLOR'    # Check for reserved words
    if(t.value in reserved):
        t.type = reserved.get(t.value)    # Check for reserved words
    return t

# Build the lexer
import ply.lex as lex
lexer = lex.lex()



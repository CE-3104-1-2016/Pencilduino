import ply.yacc as yacc
import lex_Duino as lex

tokens=lex.tokens
names = { }

"""

'Hasta': 'UNTIL', 'Cuando': 'WHEN', 
'DEFAULT': 'DEFAULT', 'EnTons': 'THEN', 
'Haga': 'DO', 'SiNo': 'IFNOT', 'Inicio': 'START',
'Repita': 'REPEAT', 'Final': 'END', 'Ini': 'INI',
'Fin_EnCaso': 'ENDINCASE', 'Proc': 'PROCEDURE',
'EnCaso': 'INCASE', 'Fin_Desde': 'ENDSINCE', 'Inc': 'INC',
'Rellene': 'FILL', 'DiagonalD': 'DIAGR', 
'HastaEncontrar': 'TOFIND', 'DCL': 'DECLARE', 
'DiagonalI': 'DIAGL', 'Llamar': 'CALL', 'Punto': 'DOT',
'ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE','CONDITION',
'LPAREN','RPAREN','LBRACKET','RBRACKET','SEMICOLON'
 
 """
start='expresion'

def p_expresion(p):
	'''expresion : declare
				 | inCase
				 | repeat'''
	pass

def p_declare(p):
	'''declare : DECLARE ID SEMICOLON
			   | DECLARE ID DEFAULT NUMBER SEMICOLON'''
	pass

def p_inCase(p):
	'''inCase : INCASE  when1 ifnot ENDINCASE SEMICOLON
			  | INCASE ID when2 ifnot ENDINCASE SEMICOLON'''
	pass

def p_when1(p):
	'''when1 : WHEN ID CONDITION sentence THEN LBRACKET expresion RBRACKET when1
			 | empty'''
	pass

def p_ifnot(p):
	'''ifnot : IFNOT LBRACKET expresion RBRACKET'''
	pass

def p_when2(p):
	'''when2 : WHEN CONDITION sentence THEN LBRACKET expresion RBRACKET when2
			 | empty'''
	pass

def p_sentence(p):
	'''sentence : ID
				| NUMBER'''
	pass

def p_repeat(p):
	'repeat : '


def p_empty(p):
    'empty : '
    pass 

def p_error(p):
	print("ERROR during parsing",p)


yacc.yacc()
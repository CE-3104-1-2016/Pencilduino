"""
import guiPencil as gui
win=gui.myWindow()
win.run()
"""
data="EnCaso\n Cuando Valor1 < 12 EnTons {\n  DCL L3 DEFAULT 5;}"#\n Cuando Valor2 = Val3 EnTons {\n  DCL UL2;}\n Cuando tf >= uno EnTons {\n  DCL T23 DEFAULT 100;}"


import lex_Duino as lexer
lexer.lex.input(data)
for tok in lexer.lexer:
	print(tok)

import yacc_Duino 
result = yacc_Duino.yacc.parse(data)
print(data)
print(result)

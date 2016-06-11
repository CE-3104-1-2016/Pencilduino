
import guiPencil as gui
win=gui.myWindow()
win.run()
"""
#data="EnCaso\n Cuando Valor1 < 12 EnTons\n  h DCL L3 DEFAULT 5;}\n SiNo { DCL L3;} \nFin_EnCaso"#\n Cuando Valor2 = Val3 EnTons {\n  DCL UL2;}\n Cuando tf >= uno EnTons {\n  DCL T23 DEFAULT 100;}"
#data="DCL dedo DEFAULT 7;"
data = "Repita{\n DCL r;\n DCL qwe;\n} F>Fd ;"

import lex_Duino as lexer
lexer.lex.input(data)
for tok in lexer.lexer:
	print(tok)

import yacc_Duino 
result = yacc_Duino.yacc.parse(data)
print(data)
print(result)
"""

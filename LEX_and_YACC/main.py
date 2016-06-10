
#data="EnCaso\n Cuando Valor1 < 12 EnTons\n { h DCL L3 DEFAULT 5;}\n SiNo { DCL L3;} \nFin_EnCaso"#\n Cuando Valor2 = Val3 EnTons {\n  DCL UL2;}\n Cuando tf >= uno EnTons {\n  DCL T23 DEFAULT 100;}"
#data="DCL dedo DEFAULT 7;"
#data = "DCL val23; \nDCL delta DEFAULT 7; \nEnCaso delta\n Cuando < val23 EnTons {\n  DCL L2 DEFAULT 3;}\n SiNo{\n  Repita{\n   DCL ReD;}\n  HastaEncontrar ReD = 0\nFin_EnCaso;"
#data = "Desde DCL i DEFAULT 7; Hasta < 100 Haga\n DCL d1;\n DCL d2;\n DCL d3;\nFin_Desde;"
#data = "DCL Cont DEFAULT 2;\nEnCaso cont\n Cuando < 1 EnTons{\n  DCL dot;\n  Punto(12,dot,Rojo);}\n SiNo{\n  Repita\n   Rellene(7);\n  HastaEncontrar cont <> 2;}   \nFin_EnCaso;"
#data = "DCL R;\nDiagonalD(R);\nDiagonalI(12);\nRellene(2);"
#data = "Proc suma(a,b,c,d,e,f)\n DCL d;\nInicio:\n Rellene(8);\n Punto(2,2,Azul);\nFinal;\nProc Float(lista_2,indice)\n DCL find;\nInicio:\n Rellene(8);\n Punto(1,2,Azul);\nFinal;\nProc Hallar_X()\n DCL Raw;\nInicio:\nPunto(1,2,Azul);\nFinal;"
data = "Proc Suma(a,b)\n DCL resultado;\nInicio:\n Punto(1,2,Azul);\nFinal;\nLlamar suma(1,2);"

    
import yacc_Duino
# Build the lexer
"""
yacc_Duino.lex.lexer.input(data)
for t in yacc_Duino.lex.lexer:
    print(t)
"""
try:
    result = yacc_Duino.yacc.parse(data)
except SyntaxError as Sy:
    print("Error de Syntaxis:",Sy)
except ValueError as Va:
    print("Error valor erroneo:",Va)
except NameError as Na:
    print("Undifined Name:",Na)
finally:
    print(data)

#"""
        

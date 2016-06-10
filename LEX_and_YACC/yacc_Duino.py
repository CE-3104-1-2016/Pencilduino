

import ply.yacc as yacc
import lex_Duino as lex

tokens=lex.tokens

Variables={}
Functions={}
matrix_size=15
syntax_flag=True
temp_list={}
stack_call={}



start='expression'

def in2(name,dic):
    find_flag=False
    for i in dic:
        if(i.lower()==name.lower()):
            find_flag=True
    return find_flag


def get_value(name,dic):
    value="none"
    i = 0
    while(i < len(dic)):

        if(str(i).lower()==name.lower()):
            value=dic[i]
        i = i + 1
    return value

def p_expression(p):
    '''expression : declare expression
                | inCase expression
                | repeat expression
                | since expression
                | dot expression
                | initialize expression
                | fill expression
                | increase expression
                | decrease expression
                | diagonal_right expression
                | diagonal_left expression
                | procedure expression
                | call expression
                | empty'''
    pass

def p_declare(p):
        '''declare : DECLARE ID SEMICOLON
                   | DECLARE ID DEFAULT NUMBER SEMICOLON'''
        if(len(p)==4):
                Variables[p[2]]=0
        elif(len(p)==6):
                Variables[p[2]]=p[4]
        pass

def p_inCase(p):
        '''inCase : INCASE  when1 ifnot ENDINCASE SEMICOLON
                  | INCASE ID when2 ifnot ENDINCASE SEMICOLON'''

        if (len(p)==7 and not in2(p.slice[2].value,Variables)):
            error_value(p,"Please define before use the variable",NameError)
        pass

def p_when1(p):
    '''when1 : WHEN ID CONDITION sentence THEN LBRACKET expression RBRACKET when1
             | empty'''

    if(len(p)==10 and not in2(p.slice[2].value,Variables)):
        error_value(p,"Please define before use the variable",NameError)

    pass

def p_when2(p):
    '''when2 : WHEN CONDITION sentence THEN LBRACKET expression RBRACKET when2
             | empty
    '''

def p_ifnot(p):
    '''ifnot : IFNOT LBRACKET expression RBRACKET'''

    pass

def p_sentence(p):
    '''sentence : ID
                | NUMBER'''

    if(p.slice[1].type=="ID"):
        if(not in2(p.slice[1].value,Variables)):
            error_value(p,"Please define before use the variable",NameError)
    pass

def p_repeat(p):
    '''repeat : REPEAT expression until_find SEMICOLON '''
    #print("Hola")

def p_until_find(p):
    '''until_find : TOFIND sentence CONDITION sentence'''
    # i=10
    # while(i>0):
    #     print("haciendo perro 2")
    #     i-=1
    # print("terminar")

def p_since(p):
    '''since : FROM declare UNTIL CONDITION sentence DO expression ENDFROM SEMICOLON'''


def p_dot(p):
    '''dot : DOT LPAREN sentence COMMA sentence COMMA COLOR RPAREN SEMICOLON '''

def p_increase(p):
    '''increase : INCREASE LPAREN ID COMMA sentence RPAREN SEMICOLON'''
    if(not in2(p[3],Variables)):
        error_value(p,"Please define before use the variable",NameError)

def p_decrease(p):
    '''decrease : DECREASE LPAREN ID COMMA sentence RPAREN SEMICOLON'''
    if(not in2(p[3],Variables)):
        error_value(p,"Please define before use the variable",NameError)

def p_initialize(p):
    '''initialize : INITIALIZE LPAREN ID RPAREN SEMICOLON'''
    if(not in2(p[3],Variables)):
        error_value(p,"Please define before use the variable",NameError)

def p_fill(p):
    '''fill : FILL LPAREN fillSentence RPAREN SEMICOLON'''

def p_fillSentence(p):
    '''fillSentence : ID
                    | NUMBER'''
    size=0
    if(p.slice[1].type=="ID"):
        if(not in2(p.slice[1].value,Variables)):
            error_value(p,"Please define before use the variable",NameError)
        else:
            size=Variables[p.slice[1].value]

    elif(p.slice[1].type=="NUMBER"):
        size=p.slice[1].value

    if(size>matrix_size):
        msg="Value error size exceded the limits of the matrix"
        error_value(p,"Please define before use the variable",ValueError)

    pass

def p_digonalleft(p):
  '''diagonal_left : DIAGL LPAREN sentence RPAREN SEMICOLON'''

def p_digonalright(p):
  '''diagonal_right : DIAGR LPAREN sentence RPAREN SEMICOLON'''

def p_empty(p):
    '''empty : '''
    pass


###Statments for Procedures

def save_procedure():
    indice_p = 0
    indice_v = 0
    list_param=[]
    list_variable=[]
    name=""
    print(list_variable)
    for i in temp_list:
        if(temp_list[i]=="param" and i != None):
            list_param.insert(indice_p,i)
        elif(len(temp_list[i])==2):
            tupla=temp_list[i]
            list_variable.insert(indice_v,tupla)
        elif(temp_list[i]=="procedure"):
            name=i
        indice_p+=1
        indice_v+=1

    Functions[name]=[list_param.copy(),list_variable.copy()]
    list_param.clear()
    list_variable.clear()


def p_localDeclare(p):
    """localDeclare : DECLARE ID SEMICOLON
                    | DECLARE ID DEFAULT NUMBER SEMICOLON """
    tupla=()
    print("p es:",p[2])
    if(len(p)==4):
                tupla=(p[2],0)
    elif(len(p)==6):
                tupla=(p[2],p[4])
    print(tupla)
    temp_list[p[2]]=tupla
    pass

def p_localExpression(p):
    '''localExpression : inCase localExpression
                | repeat localExpression
                | since localExpression
                | dot localExpression
                | initialize localExpression
                | fill localExpression
                | increase localExpression
                | decrease localExpression
                | diagonal_right localExpression
                | diagonal_left localExpression
                | procedure localExpression
                | empty'''
    pass

def p_params(p):
    '''params : oneParam
                | moreParam
                | empty'''

def p_oneParam(p):
    '''oneParam : ID params'''
    temp_list[p.slice[1].value]="param"


def p_moreParam(p):
    '''moreParam : COMMA ID params'''
    temp_list[p.slice[2].value]="param"



def p_procedure(p):
    """ procedure : PROCEDURE ID LPAREN params RPAREN localDeclare START COLON localExpression END SEMICOLON"""
    temp_list[p.slice[2].value]="procedure"
    save_procedure()
    temp_list.clear()

# CALL rules
def p_params_call(p):
    '''params_call : oneParam_call
                    | moreParam_call
                    | empty'''

def p_oneParam_call(p):
    '''oneParam_call : ID params_call
                    | NUMBER params_call'''
    stack_call[p[1]]="argument"

def p_moreParam_call(p):
    '''moreParam_call : COMMA ID params_call
                    | COMMA NUMBER params_call'''
    stack_call[p[2]]="argument"

def p_call(p):
    '''call : CALL ID LPAREN params_call RPAREN SEMICOLON'''
    stack_call[p[2]]="procedure"
    verify_Call()

def verify_Call():
    name=""
    list_arguments=[]
    print(stack_call)
    for i in stack_call:
        if(stack_call[i]=="procedure"):
            name=i
        elif(stack_call[i]=="argument"):
            print(i)
            list_arguments.append(i)
    print("*****")
    print(name,list_arguments)
    print(Functions)
    print("*****")
    if(not in2(name,Functions)):
        error_value("vacio","Function '"+name+"' is not declared",NameError)

    else:
        valid_arguments=get_value(name,Functions)
        if(len(valid_arguments)!=len(list_arguments)):
            error_value("vacio","Function '"+name+"' recive "+str(len(valid_arguments))+" and "+str(len(list_arguments))+" were given",ValueError)



def p_error(p):
    if(p!=None):
        raise SyntaxError ("Problems in: "+str(p))
    else:
        raise SyntaxError ("missing ';'")

def error_value(p,msg,Type):
    if(p=="vacio"):
        raise Type(msg)
    else:
        raise Type(msg+str(p.slice))



yacc.yacc()

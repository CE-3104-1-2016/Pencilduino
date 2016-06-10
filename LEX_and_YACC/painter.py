
""" FILL
    Val is the amount of times that rellena will work
"""
def painter_fill(val):
    print("Sending mesage to the printer")
"""PAramre
    val1: is the position on X
    val2: is the position on Y
"""
""" DOT
    Val1 is the position on  x
    val2 is the positio  on  y
"""
def painter_dot(val1,val2):
    print("Sending message to the  printer")
"""
d: Right
    val >= 0 : go up
    val < 0 :go down
"""
def painter_diagonalD(val):
    print("Sending message to the  printer")
#-------------------------------interprete_<functions>--------------------------
""" painter_diagonalI
 I: Left
    val >= 0 : go up
    val < 0 :go down
"""
def painter_diagonalI(val):
    print("Sending message to the  printer")

""" interprete_when
    val1 is a number
    val2 is  number
    condition is  a number with the following meaning:
        0: less than
        1: more than
        2: equal
        3: less or equal than
        4: more or equal than
"""
def interprete_when(val1,val2,condition):
    print("compare val1 with val2")
    if (condition == 0):
        return (val1 < val2)
    elif (condition == 1 ):
        return (val1 > val2)
    elif (condition == 2):
        return (val1 == val2)
    elif(condition == 3):
        return (val1 <= val2)
    else:
        return (val1 >= val2 )

""" interprete_expre
    Format of the expression array
"""
def interprete_expre(expre):
    return 1

""" interprete_incase
    when_list:  when_expression_list
    Example of this list:
                        [
                            [val1,val2,cond,[exp0,exp1,exp2...,expn]] ,
                            [val1,val2,cond,[exp0,exp1,exp2...,expn]],
                                        ...,
                            [val1,val2,cond,[exp0,exp1,exp2...,expn]]
                        ]
    else_element: when no one of the elements on when_expression_list are invalid
"""
def interprete_incase(when_list,else_element):
    #starts the counter on 0 to look for the ec
    i = 0
    while (i < len(when_list)):
        #get the i-th when, the two values and the comparison symbol
        temp_val1 = when_list[i][0] # the first value
        temp_val2 = when_list[i][1] # the second value
        temp_condition = when_list[i][2] #the comparison value
        if (interprete_when(temp_val1,temp_val2,temp_condition)):
            #time to do all the expressions
            j = 0
            while (j < len(when_list)):
                tmp_expre = when_list[i][3][j]
                interprete_expre(temp_expre)



""" interprete_repeat_to_find
"""
def interprete_repeat_to_find(expressions_list,condition_to_continue):
    while(interprete_when(condition_to_continue)):
        i = 0
        while(i < len(expressions_list)):
            result = interprete_expre(expressions_list[i])
            #update the data to vary(result,condition_to_continue)
            i = i + 1

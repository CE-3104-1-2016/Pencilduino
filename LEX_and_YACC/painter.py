names_variables={}
new_Stack={}
index=0
class Expression:
    def __init__(self):
        self.lista_expresion=[]
    def add_expresseion(self,expression):
        self.lista_expresion+=expression
    def run(self,tipo):
        self.tipo=tipo
class ID:
    def __init__(self,name):
        self.name=name
        self.consume["ID"]
    def run(self):
        return names_variables[self.name]
class Sentence_Object:
    def __init__(self,lex_token):
        self.value=0
        if(lex_token.type=="NUMBER"):
            self.value=lex_token.value
        else:
            self.value=names_variables[token.value]


    def run(self):
        value=None
        if(isinstance(self.data,str)):
            value = names_variables[self.data]
        else:
            value = data
        return value
class declare:
    def __init__(self,list_lex_token):
        self.ID=list_lex_token
    def run(self):
        print("Declaring something... ")
        pass
class when_Object:
    def __init__(self,list_lex_token):
        self.ID=names_variables[list_lex_token[2].value]
        self.Condition=list_lex_token[3].value
        self.sentence=new_Stack[0]
        new_Stack.remove(new_Stack[0])

    def check_when(self):
        return self.Condition.evaluate()

    def run(self):
        for i in self.list_Expresion:
            i.run()
class ifnot:
    def __init__(self,list_lex_token):
        self.list_expression=list_Expression
        self.consume=["ifnot"]
    def run(self):
        for i in self.list_expression:
            i.run()
class inCase_syntax1_Object:
    def __init__(self,token4):
        self.list_when = list_when
        self.ifnot = ifnot
    def run(self):
        flag=False
        for i in self.list_when:
            if (i.check_when()):
                flag = True
        if(not flag):
            self.ifnot.run()

def constructor(list_code):
    Type=list_code
    Object=None
    if(Type=="sentence"):
        Object=Sentence_Object(list_code[1])

    elif(Type=="when1"):
        Object=when_Object(list_code[1:])

    elif(Type=="ifnot"):
        Object=ifnot(list_code[1:])

    elif(Type=="declare"):
        Object=declare("declare")

    elif(Type == "inCase"):
        Object = inCase_syntax1_Object(list_code[1:])

    new_Stack =[Object]+new_Stack
    #new_Stack[0].run()
    new_Stack.remove(new_Stack[0])

def define_name(dictionary):
    names_variables=dictionary
    print(names_variables)

def Interpreter(code_tree):
    for_intance=[]
    temp=[]
    for i in code_tree:
        #print("i:",i,"value:",code_tree[i])
        print("nombre",code_tree[i][0])

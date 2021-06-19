class Escopo(object):
    """docstring for Escopo."""
    names = {}

    def __init__(self, name):
        super(Escopo, self).__init__()
        self.name=name

    def add(self, value):
        try: #if value is iterable
            for element in value:
                try:
                    self.names[element] #has a declaration with this name
                    print("Same Name Variavel Error "+ str(element))
                    return
                except:
                    self.names[element]= value[element]
        except:
            try:

                self.names[value.name] #has a declaration with this name
                print("Same Name Variavel Error2" + str(element))
                return
            except:
                self.names[value.name]= value

    def show(self, d):
        try:
            return self.names[d].value
        except:
            for element in self.names:

                    try:
                        return self.names[element].escopo.show(d)
                    except:
                        continue
        return None

    def change(self, v, value):
        self.names[v].value=value

    def all(self):
        return self.names

    def __str__(self):
        tmp=self.name+"\n"
        tmp+="____________________________________________________________\n"
        for element in self.names:
            tmp+=str(self.names[element])+"\n"

        return tmp

    def name(self):
        return str(self.names)
        
class Declaration(object):
    """docstring for Declaration."""
    name=''

    def __init__(self):
        super(Declaration, self).__init__()

    def __str__(self):
     return self.name

    def name(self):
        return self.name

class Variable(Declaration):
    """Exclusive class for control variables"""
    """docstring for Variable."""
    name=''
    type=''
    value=None

    def __init__(self, name, type, value):
        super(Variable, self).__init__()
        self.name = name
        self.type = type
        self.value = value
        self.def_type(type)


    def def_type(self, type):
        self.type=type
        if(self.value==None):
            if(type=="int"):
                self.value=0
            elif(type=="float"):
                self.value=0.0
            elif(type=="char"):
                self.value=''

    def __str__(self):
        return "Variable: "+self.name+ "\n\tType: " + str(self.type) + "\n\tValue: " + str(self.value)

    def __repr__(self):
        return "|"+self.name+ "," + str(self.type) + "," + str(self.value)+"|"
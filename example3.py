class ModelField:
    def __init__(self,default=None):
        self.name = None
        self.default = default

    def __set_name__(self,owner,name):
        self.name = name


    def __get__(self,instance,owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name,self.default) 

    def __set__(self,instance,value):
        instance.__dict__[self.name] = value




class CharField(ModelField):
    def __init__(self,max_length=None,default=""):
        super().__init__(default)
        self.max_length = max_length

    def __set__(self,instance,value):
        if not isinstance(value,str):
            raise TypeError("Value must be string")
        if self.max_length and len(value) > self.max_length:
            raise ValueError(f"string cannot be longer than {self.max_length} characters")
        instance.__dict__[self.name] = value



class User:
    name = CharField(max_length=100)
    surname = CharField(max_length=100,default="unwritten")


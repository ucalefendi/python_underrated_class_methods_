class PositiveNumber:
    def __init__(self):
        self.name = None


    def __set_name__(self,owner,name):
        self.name = name
        print(name)

    def __get__(self,instance,owner):
        return instance.__dict__.get(self.name,0)

    def __set__(self,instance,value):
        if value < 0 :
            raise  ValueError(f"{self.name} must be positive") 
        instance.__dict__[self.name] = value


class Product:
    price = PositiveNumber()                      
    quantity = PositiveNumber()     


    def __init__(self,price,quantity):
        self.price = price
        self.quantity = quantity



p = Product(8,9)
print(p.price)
print(p.quantity)

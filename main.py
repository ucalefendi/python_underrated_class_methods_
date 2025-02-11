class Product:
    def __init__(self):
        self._price = 0
        self._quantity = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be neqative")

    @property
    def quantity(self):
        return self._quantity 

    @quantity.setter
    def quantity(self,value):
        if isinstance(value,int):
            self._quantity = value
        else:
            raise TypeError('quantity must be an integer')   



# p = Product()
# print(p.set_price(12)) 
# price = p.get_price() 
# print(price)    


p = Product()
# p.price = -45
# print(p.price)
# p._price = 5

print(p._price)






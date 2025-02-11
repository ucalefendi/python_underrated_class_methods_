from functools import cached_property

class Product:
    def __init__(self,name,price,cost):
        self._name = name
        self._price = price
        self._cost = cost
        self._reviews = []

    @property
    def name(self):
        return self._name    

    @name.setter
    def name(self,value):
        self._name = value


    @name.deleter
    def name(self):
        print('Deleting name....')
        self._name = "eldar Mansurov"


    #Read only property
    @property
    def profit_margin(self):
        return self._price - self._cost  


    @cached_property
    def average_review(self):
        print("calculating average")
        if not self._reviews:
            return 0
        return sum(self._reviews) / len(self._reviews)  




notebook = Product("Acer",450,600)  

# print(notebook.name)
# notebook.name = "HP"
# print(notebook.name)
# del notebook.name
# print(notebook.name)
# print(notebook.name)
# print(notebook.profit_margin)
# notebook.profit_margin = 45
# print(notebook.profit_margin)
notebook._reviews = [5,6,8,9,87]
# print(notebook.average_review)
del notebook.average_review
print(notebook.average_review)



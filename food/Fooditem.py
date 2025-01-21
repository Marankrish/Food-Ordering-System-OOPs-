from .Abstract import Abstractitems
class Fooditem(Abstractitems):
    
    def __init__(self,name,rating,price,description):
        super().__init__(name,rating)
        self.Price = price
        self.Description = description
from .Abstract import Abstractitems
from .Fooditem import Fooditem
class Foodmenu(Abstractitems):
    
    def __init__(self,name):
        super().__init__(name)
        self.__Fooditems = []

    @property    
    def Fooditems(self):
        return self.__Fooditems
    
    @Fooditems.setter
    def Fooditems(self,items):
        for item in items:
            if not isinstance(item,Fooditem):
                print("invalid fooditem")
        
        self.__Fooditems = items
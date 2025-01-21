from food.Foodmenu import Foodmenu
class Restaurant:
    def __init__(self,name,rating,location,offer):
        self.Name = name
        self.Rating = rating
        self.Location = location
        self.Offer = offer
        self.__Foodmenus = []

    @property    
    def Foodmenus(self):
        return self.__Foodmenus
    
    @Foodmenus.setter
    def Foodmenus(self,items):
        for item in items:
            if not isinstance(item,Foodmenu):
                print("invalid fooditem")
        
        self.__Foodmenus = items
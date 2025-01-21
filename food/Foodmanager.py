from .Restaurant import Restaurant
from .Fooditem import Fooditem
from .Foodmenu import Foodmenu
class Foodmanager:

    def __init__(self):
        self.Restaurants = self.__preparerestaurant()
    
    def __preparefood(self):
        item1 = Fooditem(name="vegbri",rating=4,price=100,description="***")
        item2 = Fooditem(name="chirice",rating=4.5,price=150,description="***")
        item3 = Fooditem(name="chibri",rating=3.8,price=200,description="***")
        item4 = Fooditem(name="parotta",rating=4.2,price=30,description="***")
        return [item1,item2,item3,item4]
    def __preparefoodmenu(self):
        Fooditems = self.__preparefood()
        menu1 = Foodmenu("veg")
        menu1.Fooditems = [Fooditems[0],Fooditems[3]]
        menu2 = Foodmenu("non-veg")
        menu2.Fooditems = [Fooditems[2]]
        menu3 = Foodmenu("Chinese")
        menu3.Fooditems = [Fooditems[1]]
        return [menu1,menu2,menu3]

    def __preparerestaurant(self):
        Foodmenus = self.__preparefoodmenu()
        res1= Restaurant(name="a2b",rating=5,location="chennai",offer=10)
        res1.Foodmenus = [Foodmenus[0]]
        res2 = Restaurant(name="pallava",rating=4,location="pondy",offer=20)
        res2.Foodmenus = [Foodmenus[1]]
        res3 = Restaurant(name="kfc",rating=4.5,location="cudd",offer=7)
        res3.Foodmenus = [Foodmenus[2]]

        return [res1,res2,res3]
    
    def findres(self,resname):
        for res in self.Restaurants:
            if res.Name == resname:
                return res

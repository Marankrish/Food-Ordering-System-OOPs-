from .Foodmanager import Foodmanager
from .Cart import Cart
from .Payment import Payment

class Mainmenu:
    __options = {1:"show restaurants", 2:"show fooditems", 3:"search restaurant", 4:"search fooditem"}
    def __init__(self):
        self.__Foodmanager = Foodmanager()

    def showrestaurants(self):
        for res in self.__Foodmanager.Restaurants:
            print(f"{res.Name} -> Rating: {res.Rating}")
        choice = int(input("please enter the restaurant: "))
        res = self.__Foodmanager.Restaurants[choice-1]
        self.showfoodmenus(res.Foodmenus)
    
    def searchrestaurant(self):
        resname = input("Enter restaurant name: ")
        res = self.__Foodmanager.findres(resname)
        if res is not None:
            print("Restaurant found.....")
            print(f"{res.Name} -> Rating : {res.Rating}")
            self.showfoodmenus(res.Foodmenus)
        else:
            print("no restaurant found")

    def showfooditems(self,foodit=None):
        if foodit is not None:
            if not hasattr(self,'cart'):
                self.cart = None
            while True:
                for i,food in enumerate(foodit,1):
                    print(f"{i}. {food.Name}",end=" ")
                choices = list(map(int,input("enter the food: ").split(",")))
                if 0 in choices:
                    break
                try:
                    if self.cart is None:
                        cart = Cart(foodit,choices)
                        cart.UpdateTotal(foodit)
                    else:
                        new_choices = {}

                        for choice in choices:
                            if choice not in self.cart.Foodit:
                                # Add new items to both Foodit and new_choices
                                self.cart.Foodit[choice] = 1
                                new_choices[choice] = 1
                            else:
                                # Increment existing items
                                self.cart.Foodit[choice] += 1
                                new_choices[choice]= 1
                        self.cart.UpdateTotalForNewItems(foodit, new_choices)

                except KeyError:
                    print("invalid selection, Try again")

            cart.Processorder(foodit)
            self.payment = Payment()
            self.payment.process()



        else:
            ls = []
            for res in self.__Foodmanager.Restaurants:
                for menu in res.Foodmenus:
                    for food in menu.Fooditems:
                        ls.append(food)    
            if not hasattr(self,'cart'):
                self.cart = None
        
            
            while True:
                for i,food in enumerate(ls,1):
                    print(f"{i}. {food.Name} -> {food.Price}")
                choices = list(map(int,input("enter the food: ").split(",")))
                if 0 in choices:
                    break
                try:
                    if self.cart is None:
                        self.cart = Cart(ls,choices)
                        self.cart.UpdateTotal(ls)
                    else:
                        new_choices = {}

                        for choice in choices:
                            if choice not in self.cart.Foodit:
                                # Add new items to both Foodit and new_choices
                                self.cart.Foodit[choice] = 1
                                new_choices[choice] = 1
                            else:
                                # Increment existing items
                                self.cart.Foodit[choice] += 1
                                new_choices[choice]= 1

                        # Update total for only the new additions
                        self.cart.UpdateTotalForNewItems(ls, new_choices)
                except KeyError:
                    print("invalid selection, Try again")

            self.cart.Processorder(ls)
            self.payment = Payment()
            self.payment.process()

            
                        



    def searchfooditem(self):
        food_name = input("Enter the food item name: ").strip().lower()
        found_items = []  # To store matching food items along with their restaurant

    # Traverse through restaurants and their menus to find matching food items
        for res in self.__Foodmanager.Restaurants:
            for menu in res.Foodmenus:
                for food in menu.Fooditems:
                    if food_name in food.Name.lower():  # Case-insensitive search
                        found_items.append((food, res.Name))  # Store food and its restaurant

    # Display the search results
        if found_items:
            print("Food items found:")
            for i, (food, restaurant) in enumerate(found_items, 1):
                print(f"{i}. {food.Name} -> Price: {food.Price} (Restaurant: {restaurant})")
        
        # Allow the user to add items to the cart
            choices = list(map(int, input("Enter the numbers of the food items to add to cart (comma-separated, 0 to exit): ").split(",")))
            if 0 not in choices:
                try:
                    if not hasattr(self, 'cart') or self.cart is None:
                        self.cart = Cart([item[0] for item in found_items], choices)
                        self.cart.UpdateTotal([item[0] for item in found_items])
                    else:
                        new_choices = {}
                        for choice in choices:
                            food = found_items[choice - 1][0]
                            if food not in self.cart.Foodit:
                                self.cart.Foodit[food] = 1
                                new_choices[food] = 1
                            else:
                                self.cart.Foodit[food] += 1
                                new_choices[food] = 1
                        self.cart.UpdateTotalForNewItems([item[0] for item in found_items], new_choices)
                except (KeyError, IndexError):
                    print("Invalid selection. Try again.")
                self.cart.Processorder([item[0] for item in found_items])
                self.payment = Payment()
                self.payment.process()
        else:
            print("No food items found matching your search.")

    def showfoodmenus(self,menus):
        for i,menu in enumerate(menus,1):
            print(f"{i}. {menu.Name}")
        choice = int(input("please enter your preferred menu: "))
        foodit = menus[choice-1].Fooditems
        self.showfooditems(foodit)
        


    def start(self):
        while True:
            for option in Mainmenu.__options:
                print(f"{option}.{Mainmenu.__options[option]}",end=" ")
            print()
            try:
                choice = int(input("value: "))
                if choice ==0:
                    break
                value = Mainmenu.__options[choice].replace(" ","")
                getattr(self,value)()
            except (KeyError,ValueError):
                print("please enter the valid input")


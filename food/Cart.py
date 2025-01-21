
class Cart:
    def __init__(self,foodit,choices):
        self.Choices = choices
        self.Foodit = self.Addtocart(foodit)
        self.total = 0

    def Addtocart(self,foodit):
        foodic = {}
        for choice in self.Choices:
            if choice > len(foodit):
                raise KeyError
            if choice in foodic:
                foodic[choice]+=1
            else:
                foodic[choice] = 1
        return foodic
    
    def Processorder(self,foodit):
        for item in self.Foodit:
            price = self.Foodit[item]*foodit[item-1].Price
            print(f"{foodit[item-1].Name} x {self.Foodit[item]} = {price}")
        print(f"Total amount: {self.total}")
    
    def UpdateTotal(self,foodit):
        for item in self.Foodit:
            self.total+= self.Foodit[item] * foodit[item-1].Price
        print(f"current total: {self.total}")
    
    def UpdateTotalForNewItems(self, foodit, new_choices):
        """
        Update the total cost only for the newly added items.
        """
        for item in new_choices:
            self.total += new_choices[item] * foodit[item - 1].Price
        print(f"Current total: {self.total}")

  

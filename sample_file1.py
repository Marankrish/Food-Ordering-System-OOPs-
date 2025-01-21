from userdetails import User
from userstorage import Userstorage
from food.controls import Mainmenu

class Loginsystem:

    def login(self):
        mail = input("Mail: ")
        password = input("Password: ")

        user1 = Userstorage.finduser(mail,password)
        if user1 is not None:
            print("login successful")
            menu = Mainmenu()
            menu.start()
        else:
            print("invalid mail ID or password")

    def register(self):
        name = input("Name: ")
        mobile = int(input("Mobile: "))
        mail = input("Mail: ")
        password = input("Password: ")

        user = User(name,mobile,mail,password)
        Userstorage.adduser(user)

    def guest(self):
        print("You have been entered as a guest")
        menu = Mainmenu()
        menu.start()


    def validate(self,choice):
        if choice == 1:
            self.login()
        elif choice == 2:
            self.register()
        elif choice == 3:
            self.guest()
        elif choice == 4:
            print("thank you")
            exit()
        else:
            print("invalid input")



class Foodapp:
    mainpage = {1:"login",2:"register",3:"guest", 4:"exit"}
    @staticmethod
    def init():
        print("food delivery")
        loginsystem = Loginsystem()
        while True:
            for choice in Foodapp.mainpage:
                print(f"{choice}.{Foodapp.mainpage[choice]}",end=" ")
            print()
            try:
                choice = int(input("value: "))
                loginsystem.validate(choice)
            except (KeyError,ValueError):
                print("please enter the valid input")



Foodapp.init()
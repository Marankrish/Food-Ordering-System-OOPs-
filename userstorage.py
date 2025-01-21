from userdetails import User
class Userstorage:
    __details = []

    @classmethod
    def adduser(cls,user):
        if isinstance(user,User):
            cls.__details.append(user)
            print("registration successful")
    
    @classmethod
    def finduser(cls,mail,password):
        for user in cls.__details:
            if user.Mail == mail and user.Password == password:
                return user
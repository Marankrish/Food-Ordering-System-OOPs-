class Payment:
    __names = {1:"UPI",2:"COD",3:"netbanking"}

    def UPI(self):
        while True:
            upi = input("enter the upi id:")
            if upi.isalnum():
                print("Thank You!!! your order has been taken and will be delivered soon")
                break
            else:
                print("enter the correct upi id")
    def netbanking(self):
        while True:
            acc = input("enter the acc no: ")
            mpin = int(input("enter your mpin: "))
            if acc.isalnum():
                print("Thank You!!! your order has been taken and will be delivered soon")
                break
            else:
                print("enter your correct account number or mpin")

    def COD(self):
        print("Thank You!!! your order has been taken and will be delivered soon")                


    def process(self):
        print("select the payment method")
        for i in Payment.__names:
            print(f"{i}. {Payment.__names[i]}")
        num = int(input("enter the payment method: "))
        value = Payment.__names[num]
        getattr(self,value)()

            
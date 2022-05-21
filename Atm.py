class   Atm(object):
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
       

    def balanceinquiry(self):
        print("your balance is 1000 rupees")

    def cashwidthdrawal(self,amount):
        new_amount = 1000-amount
        print("you withdrawed:"+str(amount) + "your remaining balance is:" +str(new_amount))
        
        
    def cashdeposit(self,amount):
        new_amount = 1000+amount
        print("you withdrawed:"+str(amount) + "your remaining balance is:" +str(new_amount))
        

def inquiry():
        name=input("Hello what is your name:")
        print("welcome,"+name)
        cardnumber = input("Please insert your card number:")
        pin = input("Please insert your 4 digit pin:")
        new_user = Atm(cardnumber,pin)
        print("how can i help you")
        print("please choose your activity")
        print("Type 1 for Balance Inquiry")
        print("type 2 for cash withdrawl")
        print("type 3 for cash deposit")
        activity=int(input("enter the activity:"))
        if (activity == 1):
            new_user.balanceinquiry()
        elif(activity == 2):
            amount = int(input("Enter The amount:"))
            new_user.cashwidthdrawal(amount)
        elif(activity == 3):
            amount = int(input("Enter The Amount:"))
            new_user.cashdeposit(amount)
        else:
            print("enter a valid number")



        



inquiry()


        
class Atm(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber  = pinNumber

    def withdrawel(self):
        return print("Amount of ₹2,000 succesfully withdrawed from Acc:",self.cardNumber)  

    def amountremaining(self):
        return print("Balance account is of ₹40,000")

User1 = Atm(180060815891,202084)

User1.withdrawel()
User1.amountremaining()
        
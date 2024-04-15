class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 10
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance
    
    def deposite(self, amount):
        if(amount>10):
            self.balance += amount
        else:
            print("oh you think you are peter russel")
    
    def withdraw(self, amount):
        if(amount>=self.min_withdraw and amount<=self.max_withdraw):
            self.balance -= amount + amount * 0.4
            print(f'ok! new balance - {self.balance}')
        elif(amount<self.min_withdraw):
            print('fuck you! poor m***f**r')
        elif(amount>self.max_withdraw):
            print("whoa whoa whoa! hold your horses Ironman. We are not as rich as you are")

brac = Bank(150000)
brac.deposite(12)
print(brac.balance) 
brac.deposite(1)
brac.withdraw(112)
brac.withdraw(9)
brac.withdraw(100909090909)


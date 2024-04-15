class Calc:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
    
    def rem(self):
        return self.a % self.b
    
    def ab(self, x):
        if(x>0):
            return x
        elif(x<0):
            return -1*x
        else:
            return 0
        
a = int(input("just fuck of and enter A: "))
b = int(input("just fuck of and enter B: "))
obj = Calc(a, b)
choice = 3
while(choice!=False):
    print("0. Exit")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Remainder")
    print("6. Absolute value")
    choice = int(input("fuckoff: "))
    if(choice==1):
        print("Result: ", obj.add())
    elif(choice==2):
        print("Result: ", obj.sub())
    elif(choice==3):
        print("Result: ", obj.mul())
    elif(choice==4):
        print("Result: ", obj.div())
    elif(choice==5):
        print("Result: ", obj.rem())
    elif(choice==6):
        c = int(input("piss offf: "))
        print("Result: ", obj.ab(c))
    else:
        print("Invalid choice")
    


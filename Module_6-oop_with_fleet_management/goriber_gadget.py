# base class=parent class=common attribute + functionality class 
# derived class=child class=uncommon attribute + functionality class

class Device:
    def __init__(self,name, brand, price, color) -> None:
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        return f"Running {self.name} : {self.brand}"

    def music(self):
        return f"Playing music on {self.brand} {self.name}"

class Laptop(Device):
    def __init__(self,name ,brand, price,color, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd
        super().__init__(name ,brand, price,color)

    def coding(self):
        return f"learning python"
    

class Phone(Device):
    def __init__(self,name ,brand, price,color, dual_sim, call) -> None:
      self.dual_sim = dual_sim
      self.call = call
      super().__init__(name ,brand, price,color)
    
  

# inheritance
my_phone = Phone('mobile',"Iphone",123000,'red',True, "I love you ")
print(my_phone.run())
print(my_phone.music())
print(my_phone.name)
my_laptop = Laptop("laptop", 'hp',1212124, 'grey',3223,512)
print(my_laptop.run())
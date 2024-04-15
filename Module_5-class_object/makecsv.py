import csv

class Std_info:
    stdlst = []
    def __init__(self):
        self.stdlst = []
    def add(self, name, age, cls, section, roll):
        std = {
            "name":name,
            "age" :age,
            "cls" :cls,
            "section":section,
            "roll": roll
        }
        self.stdlst.append(std)
    
    def getlst(self):
        return self.stdlst

class1 = Std_info()

on = 1
while(on):
    name = input("Name: ")
    age = int(input("Age: "))
    cls = int(input("Class: "))
    section = input("Section: ")
    roll = input("Roll: ")

    class1.add(name, age, cls, section, roll)
    on = int(input("should go?:(1/0) "))







class1lst = class1.getlst()
keys = class1lst[0].keys()
with open('student_info.csv', 'w',newline='') as csvfile:
    dict_writer = csv.DictWriter(csvfile, keys)
    dict_writer.writeheader()
    dict_writer.writerows(class1lst)
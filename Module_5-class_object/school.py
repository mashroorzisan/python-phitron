class Student:
    def __init__(self, name, curr_class, id):
        self.name = name
        self.id  = id
        self.curr_class = curr_class
    
    def __repr__(self)->str:
        return f'Student with name: {self.name}\nclass: {self.curr_class}\nid: {self.id}'
    
class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.id  = id
        self.subject = subject
    
    def __repr__(self)->str:
        return f'Teacher with name: {self.name}\nsubject: {self.subject}\nid: {self.id}'
    


alia = Student('Alia', 5, 12323)
print(alia)

salauddin = Teacher("saladdin", "vugul",1212)
print(salauddin)
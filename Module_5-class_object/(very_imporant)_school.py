import csv

class Student:
    def __init__(self, name, curr_class, id):
        self.name = name
        self.id  = id
        self.curr_class = curr_class
    
    # representation
    def __repr__(self)->str:
        return f'Student with name: {self.name}\nclass: {self.curr_class}\nid: {self.id}'
   
    def add_to(self, stdlst):
        self.student = {
            "name":self.name,
            "class":self.curr_class,
            "id":self.id
        }
        stdlst.append(self.student)

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.id  = id
        self.subject = subject

    
    def __repr__(self)->str:
        return f'Teacher with name: {self.name}\nsubject: {self.subject}\nid: {self.id}'
    
    def add_to(self, tchrlst):
        self.teacher = {
            "name":self.name,
            "subject":self.subject,
            "id":self.id
        }
        tchrlst.append(self.teacher)



class School:
    def __init__(self, name) -> None:
        self.name  = name
        self.teachers = []
        self.students = []

    
    def recruit(self, name, subject):
        id = len(self.teachers) + 2001
        teacher = Teacher(name, subject, id)
        teacher.add_to(self.teachers)
    
    def enroll(self, name, fee):
        if(fee<6500):
            return "not enough"
        else:
            id = len(self.students)+1
            student = Student(name, 12, id)
            student.add_to(self.students)
            print( f"{name} is enrolled with id:{id}")

    def get_students(self):
        return self.students
    
    def get_teachers(self):
        return self.teachers


phitron = School("Phitron")
phitron.enroll('alia', 5300)
phitron.enroll('kalia', 6500)
phitron.enroll('dalia', 6500)
phitron.enroll('nalia', 6500)
phitron.enroll('opalia', 6500)
phitron.enroll('lalia', 6500)

phitron.recruit('tia', "physics")
phitron.recruit('tlia', "chemistry")
phitron.recruit('tlia', "Biology")
phitron.recruit('tlia', "physics")
phitron.recruit('talia', "math")
phitron.recruit('tlia', "math")



studentDB = phitron.get_students()
teacherDB = phitron.get_teachers()

keyst = studentDB[0].keys()
keyt = teacherDB[0].keys()

with open("school-std.csv", 'w')as stdfile:
    dict_writer = csv.DictWriter(stdfile, keyst)
    dict_writer.writeheader()
    dict_writer.writerows(studentDB)

with open("school-tchr.csv", 'w')as tchrfile:
    dict_writer = csv.DictWriter(tchrfile, keyt)
    dict_writer.writeheader()
    dict_writer.writerows(teacherDB)
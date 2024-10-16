class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,grade,student_id):
        super().__init__(name,age)
        self.grade = grade
        self.student_id = student_id
        
    def display_info(self):
        print(self.grade,self.student_id)


class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary
        
    def display_info(self):  
            print(self.subject,self.salary)



# n = Student("ali",17,"diplima",333)
# m = Teacher("abbas",33,"english_teacher",20000000)
# n.display_info()
# m.display_info()
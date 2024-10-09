class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info():
        print(self.name,self.age)

    class Student(Person):
        def __init__(self,geade,student_id):
            super().__init__(self.name,self.age)
            self.student = student
            self.student_id = student_id
        
        def display_info(self,student,student_id):
            super().display_info(self.name,self.age)
            print(self.name,self.age,self.student,self.student_id)


    class Teacher(Person):
        def __init__(self,subject,salary):
            super().__init__(self.name,self.age)
            self.subject = subject
            self.salary = salary
        
        def display_info(self,subject,salary):
            super().display_info(self.name,self.age)  
            print(self.name,self.age,self.subject,self.salary)
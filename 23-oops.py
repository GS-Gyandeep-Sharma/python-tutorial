#OOPs Methods 
# Abstraction   = Hiding unnecessory details from users through class, methods
# Encaptulation = Restrict access to certain attributes or methods to protect data and enforce controlled areas 
# Inharitance   = Allows one class to reuse the properties and method of another class (parent)
# Polimorphism  = Same method in Parent and Child class but no inharitance (different behaviour of objects)

class Student:#Class Parent class
    def __init__(self,name,grade,percentage):#method
        self.name       = name #attribute
        self.grade      = grade #attribute
        self.__percentage = percentage #attribute (__ represent encapsulation)

    def getPercentage(self): # use to get access of private attribute
        return self.__percentage

    def studentDetails(self): # method abstration
        print(f"{self.name} is in {self.grade} class with {self.getPercentage()}%.") # hidden from user


student1 = Student("Madhav",10,67)
student2 = Student("Keshav",12,76)

print(student1.name,student1.grade)
print(student2.name,student2.grade)

student1.studentDetails()
student2.studentDetails()

print(student1.__dict__) #fetch full object

#modify attribute/property of object
print(student1.grade)
student1.grade = 2
print(student1.grade)

#remove attribute/property of object
print(student1.__dict__)
del student1.grade
print(student1.__dict__)

#remove object
print(student1.__dict__)
del student1
# print(student1.__dict__)

class GraduateStudent(Student): #Child class of parent Inharitance
    def __init__(self,name,grade,percentage,stream):# paramters from parent class and new from child class 
        super().__init__(name,grade,percentage) # call parent calss init
        self.stream = stream # new attribute from child class
    
    def studentDetails(self):
        super().studentDetails()#remove this and this become Polimorphism
        print(f"Stream is {self.stream}")

GradStudent1 = GraduateStudent("Ram",10,78,"PCM")
print(GradStudent1.stream)
GradStudent1.studentDetails()



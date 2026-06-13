## Inhertance
# One class acquires propertis and methods of another class
# Parent ---> Child
# without Inheritance
# class Dog:
#     def sound(self):
#         return "ooohh"
# class Cat:
#     def sound(self):
#         return "ooohh"
# D = Dog()
# C = Cat()
# print(D.sound())
# print(C.sound())
# repeated code 
# class Animals:
#     def sound(self):
#         return "ooohh"
# class Dog(Animals):
#     pass
# class Cat(Animals):
#     pass
# d = Dog()
# c = Cat()
# print(d.sound())
# print(c.sound())
#--------------------------------------------
# Practice 1
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def display_name(self):
#         print(self.name)
# class Student(Person):
#     def study(self):
#         print("Studying...:(")
# s1 = Student("Bhanu")
# s1.display_name()
# s1.study()

# Practice 2
# class Vehicle:
#     def start(self):
#         print("Vehicle Started")
# class Car(Vehicle):
#     def drive(self):
#         print("Car is Driving")
# c1 = Car()
# c1.start()
# c1.drive()

# Practice 3
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")
# class Manager(Employee):
#     def manage_team(self):
#         print("Managing Team...:)")
# m1 = Manager("Bhanu", 50000)
# m1.display()
# m1.manage_team()
#------------------------------------------------
# Advanced Inheritance
# super keyword, also with Method overriding condition:
# class Manager:
#     def __init__(self, name):
#         self.name = name
#     def work(self):
#         print("Manager is Managing Team.")
# class Employee(Manager):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary
#     def work(self):
#         print("Employee is doing his best.")
# e1 = Employee("Bhanu",25000)
# e1.work()
#-------------------------------------------------
# Practice 1
class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"Person Name: {self.name}")
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def teach(self):
        print("Teaching Python")
    def display(self):
        print(f"Teacher Name: {self.name}")
        print(f"Subject: {self.subject}")
t1 = Teacher("Bhanu", "Python")
t1.display()

# Practice 2
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def show_brand(self):
        print(f"Brand: {self.brand}")
class Bike(Vehicle):
    def __init__(self, brand, cc):
        super().__init__(brand)
        self.cc = cc
    def show_brand(self):
        print(f"Brand: {self.brand}")
        print(f"CC: {self.cc}")
    def ride(self):
        print("Bike is riding")
b1 = Bike("YAMAHA",150)
b1.show_brand()
b1.ride()
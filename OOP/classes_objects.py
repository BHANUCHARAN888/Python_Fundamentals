# TODO:-
# Class: It is blueprint or template used to create objects
# -------structure---------
# class class_name:
#     pass

# Object: instance for a class
# -------structure---------
# class class_name:
#     pass

# s1 = class_name()
# print(s1)

# Attribute / Instance variable: Ex: self.attribute = attribute

# self

# Instance variable - Belongs to only particular method
# class variable - Belongs to entire class
#------------------------------------------------------------------
# Adding attributes to class and object
# class Student:
#     pass
# s1 = Student()
# s1.name = "Bhanu"
# s1.age = 20
# s1.branch = "CSD"
# print(s1.name)
# print(s1.age)
# TODO:Problem here for many students we have to create many slots to avoid this
# we must use constructor(__init__)
# also self which used to perform actions with object attributes
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s1 = Student("Bhanu", 20)
# print(s1.name)
# print(s1.age)
# # output: Bhanu 20\n
#--------------------------------------------------------------------
# Practice: 1
# class car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#     def display(self):
#         print("Brand :",self.brand)
#         print("Model :",self.model)
#         print("Price :",self.price)
#         print("------------------")
# car1 = car("BMW", "X3", 5000000)
# car2 = car("BENZ", "S-class", 7000000)
# car1.display()
# car2.display()
#------------
# Practice: 2
# class BankAccount:
#     def __init__(self, account_holder, account_number, balance):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.balance = balance
#     def display(self):
#         print("A/c Holder: ", self.account_holder)
#         print("A/c Number: ", self.account_number)
#         print("Balance: ", self.balance)
#         print("---------------------------")
#     def deposit(self, amount):
#         self.balance += amount
#         print(amount,"Successfully deposited.")
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient Funds..")
#         self.balance -= amount
# AC1 = BankAccount("KALLA BHANU CHARAN",662398453200001,50000)
# AC2 = BankAccount("KALLA TULASI RAO",662398453200002,500000)

# AC1.display()
# AC2.display()

# AC1.deposit(20000)
# AC2.deposit(100000)

# AC1.withdraw(1)
# AC2.withdraw(1)

# AC1.display()
# AC2.display()
#------------
# Practice: 3
# class Student:
#     def __init__(self, name, id_no, marks):
#         self.name = name
#         self.id_no = id_no
#         self.marks = marks
#     def display(self):
#         print("Name: ", self.name)
#         print("ID: ", self.id_no)
#         print("Marks: ", self.marks)
#         print("------------------------")
#     def update_marks(self, new_marks):
#         a = []
#         a.append(self.marks)
#         self.marks = new_marks
#         print("Marks updated.")
#     def check_result(self):
#         if self.marks >= 40:
#             print("PASS")
#         else:
#             print("FAIL")
# s1 = Student("Bhanu",4420,60)
# s2 = Student("Anil",4438,80)

# s1.display()
# s2.display()
# s1.update_marks(80)
# s1.check_result()
# s2.check_result()

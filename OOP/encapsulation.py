## Encapsulation
# Encapsulation = Bundling data and methods together and controlling access to the data.
# till now we have done this classes and objects but we have not controlled the access to the data.
# What problem without Encapsulation
# class Car:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def display(self):
#         print(f"{self.name}:{self.price}")
# c1 = Car("BMW",5000000)
# c1.display()

# c1.name = "TATA"  # data changed
# c1.display()
# Encapsulation solves this, now we change important data using methods not with variables also we use private variables
# class Car:
#     def __init__(self, name, price):
#         self.__name = name
#         self.__price = price
#     def display(self):
#         print(f"{self.__name}: {self.__price}" )
# c1 = Car("AUDI",10000000)
# c1.display()

# c1.__name = "BENZ"  # data not changed
# c1.display()
#-------------------------------------------------------------------------------------------------------------
# Practice 1: 
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self, marks):
#         if 0 <= marks <= 100:
#            self.__marks = marks
#         else:
#             return "Not a valid marks"
# s1 = Student("Bhanu",100)
# print(s1.get_marks())
# s1.set_marks(98)
# print(s1.get_marks())
# fixed the idea : private variable + get + set-------->Encapsulation
#-------------------------------
# Practice 2:
# TODO:Mobile Phone Battery system 
# class MobilePhone:
#     def __init__(self, battery):
#         self.__battery = battery

#     def get_battery(self):
#         return self.__battery
    
#     def charge_battery(self, charge):
#         if self.__battery >= 100:
#             print("Unplug charge, Battery is Full.")
#             return
#         if self.__battery + charge > 100:
#             print("Battery cannot excced 100%")
#             return
#         self.__battery += charge
#         print("Battery Charged.")
#     def use_phone(self, hours):
#         # Assuming 1 hour = 10% battery consumption
#         if (hours*10) >= self.__battery:
#             self.__battery = 0
#             print(f"Mobile used {hours}hrs ,Not enough battery.")
#             return
#         else:
#             self.__battery -= (hours*10)
#             return self.__battery
#     def display(self):
#         print(f"Battery: {self.__battery}%")
#         print("--------------------------")
# phone1 = MobilePhone(40)
# phone1.charge_battery(10)
# phone1.use_phone(7)
# phone1.display()
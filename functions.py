### FUNCTIONS ###
# TODO:Structure
# def add(parameter):
#     # code
#     return
#---------------------
## Parameters
# def greet(name):
#     return f"Hello, {name}"

# print(greet("Bhanu"))
# Multiple parameters
# def Casio(a, b):
#     print(f"{a}+{b}={a+b}")
#     print(f"{a}-{b}={a-b}")
#     print(f"{a}*{b}={a*b}")
#     print(f"{a}//{b}={a//b}")
#     print(f"{a}%{b}={a%b}")
#     print(f"{a}**{b}={a**b}")
#     return 
# Casio(2, 3)
#--------------------------------
## Scope
# Local Variable
# def test():
#     x = 10
#     print(x)
# test()
# print(x) X--- error rise

# Global Variable
# x = 20
# def test():
#     print(x)
#     return
# test()
#------------------------------------------------
## TODO:Lambda function (one-line function)
# square = lambda x: x*x
# print(square(2))

# TODO: Custom function
# def add(a, b):
#     return a + b

# def isEven_Odd(n):
#     return n%2 == 0
# print(isEven_Odd(3))

# def largest(a, b):
#     return a if a>b else b
# print(largest(2,4))

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact
# print(factorial(5))

# def Rev_str(str):
#     return str[::-1]
# print(Rev_str("JDR"))

# def Count_Vowel(text):
#     vowels = "AEIOUaeiou"
#     count = 0
#     for ch in text:
#         if ch in vowels:
#             count += 1
#     return f"Count of vawels:{count}"
# print(Count_Vowel("IRON MAN"))
#-----------------------------------------------

# TODO:Build Project 1: Unit Converter
# def km_to_miles(km):
#     return km * 0.6213

# def miles_to_km(mile):
#     return mile * 1.6093

# km = float(input("Enter KM: "))
# print("Miles:", km_to_miles(km))

# mile = float(input("Enter MILE: "))
# print("Kilometer:", miles_to_km(mile))
#--------------------------------------------------

# TODO:Build Project 2: Expense Calculator
# def Total_Expense_Cal(expense):
#     return sum(expense)
# expense = []
# for i in range(5):
#     amount = float(input("Expense: "))
#     expense.append(amount)
# print("Total Expense: ", Total_Expense_Cal(expense))
#-----------------------------------------------------
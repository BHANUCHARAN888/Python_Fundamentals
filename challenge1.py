# ---------(LEVEL 1)---------
# Greeting program 
# name = str(input("Enter your name: "))
# age = int(input("Enter your age: "))
# lang = str(input("Enter your favorite comp. language: "))

# print(f"Hello {name}..")
# print(f"You are {age} years old.")
# print(f"My favorite language is {lang}.")

# -------(LEVEL 2)----------
# Arithmetic Practice
# Sum of numbers
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))

# print(f"Sum of num1 & num2: {num1+num2}")
# print(f"Sum of num1,num2,num3: {num1+num2+num3}")

# Rectangle Area,perimeter
# length = int(input("Enter length (cm): "))
# width = int(input("Enter width (cm): "))
# print(f"Area of Rectangle: {length * width}")
# print(f"Perimeter of Rectangle: {2*(length+width)}")

# Circle Area
# pi = 3.14159
# radius = int(input("Enter the Radius: "))
# print(f"Area of Circle: {pi*(radius**2)}")

# ---------(LEVEL 3)----------
# Type Conversion
# # Add Two Inputs
# input1 = input("Enter input 1: ")
# input2 = input("Enter input 2: ")
# sum_inputs = int(input1) + int(input2)
# print(f"{input1} + {input2} = {sum_inputs}")

# Temperature Converter
# F = float(input("Enter Fahrenheit(F): "))
# C = float(input("Enter Celsius(C): "))

# print(f"Celsius--->Fahrenheit : {(C * 9/5) + 32}")
# print(f"Fahrenheit--->Celsius : {(F - 32) * 5/9}")

# Minutes to Hours
# minute = int(input("Enter Minutes: "))
# hour = minute//60
# print(f"{minute} ----- {hour}hr")

# ---------(LEVEL 4)----------
# BMI Calculator
# weight = int(input("Enter weight(KG): "))
# height = int(input("Enter height(m): "))
# BMI = weight / (height**2)
# print(f"BMI : {BMI}")

# Simple Interest
# principle = int(input("Enter Principle : "))
# rate = int(input("Enter rate : "))
# time = int(input("Enter time : "))
# SI = (principle * time * rate)/100
# print(f"Simple Interest : {SI}")

# ---------(LEVEL 5)----------
# swaping number
# a = 10 
# b = 20
# temp = a
# a = b
# b = temp
# print(a)
# print(b)

# Second Converter
# seconds = int(input("Enter Seconds: "))
# hours = seconds // 3600
# remaining_sec = seconds % 3600
# minute = remaining_sec // 60
# seconds = remaining_sec % 60
# print(f"{hours} hour")
# print(f"{minute} minutes")
# print(f"{seconds} seconds")

# Student Marksheet
# print("Total 100 marks for each subject")
# sub1 = int(input("Enter English marks: "))
# sub2 = int(input("Enter Math marks: "))
# sub3 = int(input("Enter General Awareness marks: "))
# sub4 = int(input("Enter Reasoning marks: "))

# total = sub1 + sub2 + sub3 + sub4
# avg = total / 4
# print(f"Total marks: {total}")
# print(f"Average : {avg}")
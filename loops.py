#-------------LOOPS---------------
# range(start, stop, step)

## For loop
# for i in range(1,11):
#     print(i)

## While loop
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

## break
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

## continue
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

#### PRACTICE
# problem 1: Print numbers from 1 to 20.
# for i in range(1, 21):
#     print(i, end=" ")

# problem 2: Print even numbers from 1 to 50.
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i, end = " ")

# problem 3: Print odd numbers from 1 to 50.
# for i in range(1, 51):
#     if i % 2 != 0:
#         print(i, end = " ")

# problem 4: Find the sum of numbers from 1 to 100.
# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(sum)

# problem 5: Print squares of numbers from 1 to 10.
# for i in range(1, 11):
#     print(i**2, end = " ")

# problem 6: Print cubes of numbers from 1 to 10.
# for i in range(1, 11):
#     print(i**3, end = " ")

# problem 7: Print table of any number.
# num = int(input("Enter number: "))
# for i in range(1, 13):
#     value = num * i
#     print(f"{num} * {i} = {value}")

# problem 8: Count backwards from 10 to 1.
# for i in range(10, 0, -1):
#     print(i, end = " ") 

# problem 9: Print all numbers divisible by 3 from 1 to 50.
# for i in range(1, 51):
#     if i % 3 == 0:
#         print(i, end = " ")

# problem 10: Count how many numbers from 1 to 100 are divisible by 7.
# for i in range(1, 101):
#     if i % 7 == 0:
#         print(i, end = " ")


### mini challenge

## Number Guessing Game
# import random
# secret = random.randint(1, 10)
# print("'Guess the number between 1 - 10'")
# count = 0
# while True:
#     guess = int(input("Enter the number: "))
#     count = count + 1
#     if guess == secret:
#         print(f"Perfect!, you guessed the number in {count} chances.")
#         break
#     else:
#         print("Try again")

## Pattern Printing
# for i in range(5):
#     print("$" * 4)

# for i in range(1, 6):
#     print("$" * i)
# for i in range(6, 0, -1):
#     print("$" * i)

# for i in range(1, 5):
#     print(" " * (5-i)+ "*" * (2*i-1))

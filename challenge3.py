# --------------------LEVEL 1-----------------------
## print 1-10
# for i in range(1,11):
#     print(i, end = " ")

## print 10-1
# for i in range(10, 0, -1):
#     print(i, end = " ")

## Print even numbers up to 20
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i, end = " ")

## Print even numbers up to 20
# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i, end = " ")

## sum 1-50
# sum = 0
# for i in range(1, 51):
#     sum = sum + i
# print(sum)

## Sum even numbers up to 50
# sum = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         sum = sum + i
# print(sum)

## sum of odd numbers up to 50
# sum = 0
# for i in range(1, 51):
#     if i % 2 != 0:
#         sum = sum + i
# print(sum)

# ----------------------LEVEL 2-------------------------
## TODO:Factorial of a number
# num = int(input("Enter number: "))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i
# print(f"Factorial of {num} is : {factorial}")

## TODO: Reverse a number
# num = int(input("Enter number: "))
# reversed_num = 0
# while num > 0:
#     digit = num % 10
#     reversed_num = (reversed_num*10) + digit
#     num = num // 10
# print(reversed_num)

## Count digits in a number
# num = int(input("Enter number: "))
# count = 0
# while num > 0:
#     digit = num % 10
#     count = count + 1
#     num = num // 10
# print(f"Count of digits are {count}.")

## Sum digits of a number
# num = int(input("Enter number: "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10
# print(f"Sum of digits in numbers: {sum}.")

## TODO:Check palindrome number
# num = int(input("Enter number: "))
# reverse_num = 0
# original_num = num
# while num > 0:
#     digit = num % 10
#     reverse_num = (reverse_num*10) + digit
#     num = num // 10
# if original_num == reverse_num:
#     print("Number is Palindrome.")
# else:
#     print("Not a Palindrome")

## TODO:Check Armstrong number
# num = int(input("Enter the number: "))
# og = num
# len_num = len(str(num))
# armstrong = 0
# while num > 0:
#     digit = num % 10
#     armstrong = armstrong + (digit**len_num)
#     num = num // 10
# if og == armstrong:
#     print(f"Number is an Armstrong number")
# else:
#     print("Not an Armstrong number")

## TODO: Fibonacci series
# term = int(input("Enter the term: "))
# a = 0
# b = 1
# for i in range(term):
#     print(a, end = " ")
#     a, b = b, a+b

## TODO:largest digit
# max = 0
# num = int(input("Enter number: "))
# num = abs(num)
# while num > 0:
#     digit = num % 10
#     if digit > max:
#         max = digit
#     num = num // 10
# print(f"Largest digit in the number is: {max}")

## TODO:smallest digit
# num = int(input("Enter the number: "))
# num = abs(num)
# min = num % 10
# if num == 0:
#     min = 0
# while num > 0:
#     digit = num % 10
#     if digit < min:
#         min = digit
#     num = num // 10
# print(f"Smallest digit in the number is: {min}")

## TODO:vowels in string
# string = str(input("Enter string: "))
# vowels = "aeiouAEIOU"
# count = 0
# for char in string:
#     if char in vowels:
#         count = count + 1
# print(f"Number of vowels in the string is: {count}")

# --------------------------LEVEL 3-------------------------
## TODO:Prime number check
# num = int(input("Enter number to check for Prime: "))
# if num <= 1:
#     print("num is not a Prime number")
# else:
#     isPrime = True
#     Limit = int(num**0.5) + 1
#     for i in range(2, Limit):
#         if num % i == 0:
#             isPrime = False
#             break
#     if isPrime:
#         print(f"{num} is Prime")
#     else:
#         print(f"{num} is not Prime")

## TODO:Print primes from 1–100
# for i in range(1, 101):
#     num = i
#     if num > 1:
#         isPrime = True
#         limit = int(num**0.5)+1
#         for i in range(2, limit):
#             if num % i == 0:
#                 isPrime = False
#                 break
#         if isPrime:
#             print(num, end = " ")

## TODO:Pyramid pattern

# UPWARD
for i in range(1, 5):
    print(" "*(5-i)+"*"*(2*i-1))

# COMPLETE
for i in range(1, 5):
    print(" "*(5-i)+"*"*(2*i-1))
for i in range(5, 0, -1):
    print(" "*(5-i)+"*"*(2*i-1))

# DOWNWARD
for i in range(4, 0, -1):
    print(" "*(5-i)+"*"*(2*i-1))
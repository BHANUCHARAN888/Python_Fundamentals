# -------Function Practice Problems---------
# ===========================================

# -----EASY------

## Create a greeting function.
# def greet(name, info, date, venue):
#     return f"""
# Hi {name},
# {info}
# {date}
# Please Visit
# {venue}"""
# print(greet("Bhanu", "College fest", "15th August, 2026", "XYZ University."))

## Square & Cube of a number
# Square = lambda x: x*x
# print(Square(3))
# Cube = lambda x: x*x*x
# print(Cube(3))

## Check even/odd
# def isEven(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#     return
# num = int(input("Enter number to check even/odd: "))
# print(isEven(num))

## Reverse a string
# def Rev_str(text):
#     return text[::-1]
# print(Rev_str("elgooG"))

## Count vowels
# def Count_Vowels(txt):
#     vowels = "AEIOUaeiou"
#     count = 0
#     for ch in txt:
#         if ch in vowels:
#             count += 1
#     return f"Count is: {count}"
# print(Count_Vowels("Hello, I am Bhanu Charan aspiring AI-Assisted irreplaceable."))

# -------------MEDIUM---------------

## Factorial Number
# def Factorial(num):
#     if num < 1:
#         print("Factorial not defined.")
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     return f"Factorial of {num} is: {fact}"
# num = int(input("Enter number to get its factorial: "))
# print(Factorial(num))

## Prime Number
# def isPrime(num):
#     if num <= 1:
#         print("Not a Prime Number")
#     for i in range(2, num):
#         if num % i == 0:
#             return f"{num} is not an Prime number"
#         else:
#             return f"{num} is a Prime number"
#     return ""
# num = int(input("Enter a number to check Prime: "))
# print(isPrime(num))

## Fibonacci function
# def Fibonacci(term):
#     a, b = 0, 1
#     list_series = []
#     for i in range(term):
#         list_series.append(a)
#         a, b = b, a+b
#     return list_series
# term = int(input("Enter the Term: "))
# print(Fibonacci(term))

## Sum of digits
# def Sum_digits(num):
#     sum = 0
#     og = num
#     while num > 0:
#         digit = num % 10
#         sum = sum + digit
#         num = num // 10
#     return f"Sum of digits in {og} is {sum}."
# num = int(input("Enter number: "))
# print(Sum_digits(num))

## Palindrome checker
# def Palindrome(num):
#     rev = 0
#     og = num
#     while num > 0:
#         digit = num % 10
#         rev = rev*10 + digit
#         num = num // 10
#     if og == rev:
#         return True
#     return False
# num = int(input("Enter the number: "))
# print(Palindrome(num))

## Count words in sentence
# def Count_Words(txt):
#     words = txt.split()
#     return len(words)
# txt = str(input("Enter the Sentense: "))
# print(Count_Words(txt))

# -------------------CHALLENGING-----------------------

## Mini Project: Bank account simulator (deposit, withdraw, balance).

# def show_menu():
#     print("\n---BANK ACCOUNT SIMULATOR---")
#     print("1. A/C Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Exit")
# def Balance_Check(balance):
#     print(f"\nYour current balance is: {balance:.2f}")
# def Deposit(balance, amount):
#     if amount > 0:
#         balance += amount
#         print(f"\nSuccessfully deposited ₹{balance:.2f}")
#     else:
#         print("Invalid Amount!!")
#     return balance
# def Withdraw(balance, amount):
#     if amount > balance:
#         print("\nTransaction Denied: Insufficient funds!")
#     elif amount <= 0:
#         print("Invalid Amount!!")
#     else:
#         balance -= amount
#         print(f"\nSuccessfully withdrew ₹{amount:.2f}")
#     return balance
# def Start_App():
#     account_balance = 0.0
#     while True:
#         show_menu()
#         choice = input("Enter your choice(1-4): ")
#         if choice == "1":
#             Balance_Check(account_balance)
#         elif choice == "2":
#             amount = float(input("Enter deposit amount: ₹"))
#             account_balance = Deposit(account_balance, amount)
#         elif choice == "3":
#             amount = float(input("Enter withdrawal amount: ₹"))
#             account_balance = Withdraw(account_balance, amount)
#         elif choice == "4":
#             print("\nThank you for banking with us. Goodbye!")
#             break
#         else:
#             print("\nInvalid choice! Please select an option between 1 and 4.")
# Start_App()

# ----------
## Mini Project: Expense Tracker

# def show_menu():
#     print("\n---Expense Tracker---")
#     print("1. Balance")
#     print("2. Enter Budget")
#     print("3. Enter Expense")
#     print("4. Exit")
# def Balance_Check(balance):
#     print(f"Current Balance: ₹{balance:.2f}")
# def Enter_Budget(balance, Budget):
#     if Budget > 0:
#         balance += Budget
#         return balance
#     else:
#         return "Invalid Budget"
# def Enter_Expense(balance, Expense):
#     balance -= Expense
#     return balance

# def Tracker_App():
#     balance = 0.0
#     while True:
#         show_menu()
#         choice = input("\nEnter your choice: ")
#         if choice == '1':
#             Balance_Check(balance)
#         elif choice == '2':
#             Budget = float(input("\nEnter your Budget: ₹"))
#             balance = Enter_Budget(balance, Budget)
#             print(f"Budget Entered Successfully! of ₹{Budget}")
#         elif choice == '3':
#             Expense = float(input("Enter your Expense : ₹"))
#             balance = Enter_Expense(balance, Expense)
#             print(f"Remaining: ₹{balance:.2f}")
#         elif choice == '4':
#             print("Thank you for choosing our platform..Good bye.")
#             break
#         else:
#             print("\nInvalid choice!")
# Tracker_App()

#---------------
## Mini Project: Student Grade Calculator

# def S_Total(m1, m2, m3, m4, m5):
#     total = m1 + m2 + m3 + m4 + m5
#     return total
# def S_Percentage(total):
#     percent = (total/500)*100
#     return percent
# def S_Grade(percent):
#     if percent >= 90:
#         return "A+"
#     elif percent >= 80 and percent < 90:
#         return "A"
#     elif percent >= 70 and percent < 80:
#         return "B"
#     elif percent >= 60 and percent < 70:
#         return "C"
#     elif percent >= 50 and percent < 60:
#         return "D"
#     elif percent < 50:
#         return "F"
#     else:
#         return "NOT FOUND!"
# def Display():
#     print("---STUDENT GRADE CALCULATOR---")
#     m1 = float(input("Enter Marks Subject 1: "))
#     m2 = float(input("Enter Marks Subject 2: "))
#     m3 = float(input("Enter Marks Subject 3: "))
#     m4 = float(input("Enter Marks Subject 4: "))
#     m5 = float(input("Enter Marks Subject 5: "))
#     total = S_Total(m1, m2, m3, m4, m5)
#     print(f"Total: {total:.2f}")
#     percentage = S_Percentage(total)
#     print(f"Percentage: {percentage:.2f}%")
#     grade = S_Grade(percentage)
#     print(f"Grade: {grade}")
# Display()

#----------------
## Mini Project: Password Strength Checker

# Mini Project: Password Strength Checker

# def check_length(password):
#     return len(password) >= 8
# def has_digit(password):
#     for ch in password:
#         if ch.isdigit():
#             return True
#     return False
# def has_uppercase(password):
#     for ch in password:
#         if ch.isupper():
#             return True
#     return False
# def password_strength(password):
#     length_ok = check_length(password)
#     digit_ok = has_digit(password)
#     upper_ok = has_uppercase(password)
#     if not length_ok:
#         return "Weak"
#     if length_ok and digit_ok and upper_ok:
#         return "Strong"
#     if length_ok and digit_ok:
#         return "Moderate"
#     return "Weak"
# def password_checker():
#     password = input("Enter your password: ")
#     strength = password_strength(password)
#     print(f"Password Strength: {strength}")
# password_checker()
    

    


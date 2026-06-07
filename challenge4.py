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

## Bank account simulator (deposit, withdraw, balance).

def show_menu():
    print("\n---BANK ACCOUNT SIMULATOR---")
    print("1. A/C Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
def Balance_Check(balance):
    print(f"\nYour current balance is: {balance:.2f}")
def Deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"\nSuccessfully deposited ₹{balance:.2f}")
    else:
        print("Invalid Amount!!")
    return balance
def Withdraw(balance, amount):
    if amount > balance:
        print("\nTransaction Denied: Insufficient funds!")
    elif amount <= 0:
        print("Invalid Amount!!")
    else:
        balance -= amount
        print(f"\nSuccessfully withdrew ₹{amount:.2f}")
    return balance
def Start_App():
    account_balance = 0.0
    while True:
        show_menu()
        choice = input("Enter your choice(1-4): ")
        if choice == "1":
            Balance_Check(account_balance)
        elif choice == "2":
            amount = float(input("Enter deposit amount: ₹"))
            account_balance = Deposit(account_balance, amount)
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: ₹"))
            account_balance = Withdraw(account_balance, amount)
        elif choice == "4":
            print("\nThank you for banking with us. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select an option between 1 and 4.")
Start_App()

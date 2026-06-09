# Lists : A list stores multiple values and can be changed.
# duplicate allow - mutable
# names = ["BANU", "CHARAN", "ANIL"]
# print(names[0])
# names.append("TULASI")
# print(names)
#----------------------------------------------------------
# operations:
# def menu():
#     print("---Name Jar---")
#     print("1. Get list")
#     print("2. Enter name")
#     print("3. Exit")
# def jar():
#     name = []
#     while True:
#         menu()
#         choice = str(input("\nEnter your choice: "))
#         if choice == "1": 
#             print(f"Names: {name}")
#         elif choice == "2":
#             names = str(input("Enter names: "))
#             name.append(names)
#             print(f"{names} Entered successfully!")
#         elif choice == "3":
#             print("Byee!")
#             break
#         else:
#             print("\nEnter correct choice")
# jar()
#-----------------------

### Practice
# TODO:----List: [append, insert, remove, pop, del, sort, reverse, clear, count, index, copy]
## Add item
# numbers = [1,2,3,4,5,3,3,3]
# print(numbers)
# numbers.append(100)
# print(numbers)
# numbers.insert(0,10)
# print(numbers)
# numbers.remove(10)
# print(numbers)
# numbers.pop()
# print(numbers)
# del numbers
# print(numbers)
# numbers[0] = 20
# numbers[1] = 30
# print(numbers)
# numbers.sort()
# print(numbers)
# print(20 in numbers)
# numbers.reverse()
# print(numbers)
# print(numbers.count(3))
# print(numbers.index(5))
# a = numbers.copy()
# print(a)
#----------------------------------------

# mini tasks
## Find the largest number in a list.
# def max(nums):
#     max = nums[0]
#     for i in nums:
#         if i > max:
#            max = i
#     return max
# a = max([10,30,90,60,80,20])
# print(f"Largest number is {a}.")
#-----------
## Find the smallest number in a list.
# def min(nums):
#     min = nums[0]
#     for i in nums:
#         if i < min:
#            min = i
#     return min
# b = min([10,30,90,60,80,20])
# print(f"Smallest number is {b}.")
#-----------
## Count how many times a number appears.
# def CountRepeatNum(num, target):
#     count = 0
#     for i in num:
#         if i == target:
#             count += 1
#     return f"{target} repeat '{count}' times."
# print(CountRepeatNum([1,2,2,3,2,4], 2))
#------------
## Reverse a list.
# def Rev(num):
#     new = []
#     for i in range(len(num)-1, -1, -1):
#         new.append(num[i])
#     return new
# print(Rev([1,2,3,4]))

# # Another approach
# def Rev(num):
#     new = []
#     for i in num:
#         new.insert(0, i)
#     return new
# print(Rev([1,2,3,4]))
#--------------

## Sort a list in descending order
# def Largest(nums):
#     nums = nums.copy()
#     new = []
#     while len(nums)>0:
#         large = nums[0]
#         for i in nums:
#            if i > large:
#               large = i
#         new.append(large)
#         nums.remove(large)
#     return new
# print(Largest([10,30,20,50]))
#----------------

## Check if a name exists in a list, use the in operator.
# def check_name(names, search):
#     for i in names:
#         if i == search:
#             return "Found"
#     return "Not Found"
# print(check_name(["Bhanu", "Charan", "Anil"], "Charan"))

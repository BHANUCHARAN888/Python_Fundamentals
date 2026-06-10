# Sets: A set stores unique values.
# Duplicates automatically removed
# nums = {1, 2, 2, 3, 3, 4}
# print(nums)
# operation: (Add, Remove, len, union, intersection, difference, symmetric_difference)
# names = {'Tony','Steeve','Banner','Thor'}
# names.add('Vision')
# print(names)
# names.remove('Vision')
# print(names)
# print("Tony" in names)
# a = {'B','A','C'}
# b = {'A','D','C'}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
##-------------------------------------------------------
# Dictionaries: stores data in key-value pair
# student = {
#     "name": "Bhanu",
#     "age": 18,
#     "skill": "Python"
# }
# print(student["name"])
# student["City"] = "Vizag"
# # print(student)
# student["age"]=19
# print(student)
#---------------
# print(student.get("name"))
#---------------
# loops
# for key in student:
#     print(key)
# for value in student.values():
#     print(value)
# for key,value in student.items():
#     print(f"{key}: {value}")
# ================================================>
# Practice
# Set

## Remove duplicates from a list.
# def R_Duplicate(nums):
#     return list(set(nums))
# print(R_Duplicate([1, 2, 2, 3, 3, 4, 5, 5]))
# another approach
# def R_Duplicate(nums):
#     unique = set()
#     for i in nums:
#         unique.add(i)
#     return list(unique)
# print(R_Duplicate([1, 2, 2, 3, 3, 4, 5, 5]))

## Union of 2 Sets
# def union_set(a, b):
#     return a.union(b)
# print(union_set({1,2,3},{3,4,5}))

## Intersection of 2 Sets
# def intersection_set(a, b):
#     return a.intersection(b)
# print(intersection_set({1,2,3},{3,4,5}))

## Difference of 2 sets
# def difference_set(a, b):
#     return a.difference(b)
# print(difference_set({1,2,3},{3,4,5}))

## Check for value
# def check_value(s, target):
#     return target in s
# print(check_value({1,2,3,4,5}, 3))
#----------------------------------------------------
# Dictionaries
# # <---------creation--------->
# student = {
#     "name": "Bhanu",
#     "age" : 18,
#     "skill": "Python"
# }
# # <---------Addition---------->
# student["city"] = "Vizag"
# # <---------Update---------->
# student["age"] = 19
# # <---------Delete---------->
# del student["skill"]
# # <---------Accessing---------->
# print(student)

# # Check key exist 
# print("name" in student)
#---------------------------------------------------

## Challenge Problems
# TODO: Contact Search
# contacts = {
#     "Bhanu": "9876543210",
#     "Charan": "9123456789"
# }
# def Contact_Search(contact, search):
#         if search in contact:
#             print("Found")
#             return contact[search]
#         return "Contact Not Found"
# name = input("Enter name:")
# print(Contact_Search(contacts,name))

# TODO: Word Counter
# def Word_Counter(word):
#     seen = {}
#     for l in word:
#         if l in seen:
#            seen[l] += 1
#         else:
#             seen[l] = 1
#     return seen
# print(Word_Counter("Banana"))
#----------------------------------------------------
# Mini Project: Contact Book
def menu():
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View Contacts")
    print("4. Delete Contact")
    print("5. Exit") 
def Contact_book():
    contacts = {}
    while True:
          menu()
          choice = input("Enter Choice: ")
          if choice == "1":
             name = input("Enter Name: ")
             number = input("Enter Number: ")
             contacts[name] = number
             print("Contact Added")
          elif choice == "2":
              search = input("Enter Name: ")
              if search in contacts:
                  print("Phone: ", contacts[name])
              else:
                  print("Not Found")
          elif choice == '3':
               for name,number in contacts.items():
                   print(name,"-",number)
          elif choice == '4':
               name = input("Delete Name: ")
               if name in contacts:
                   del contacts[name]
                   print("Deleted")
               else:
                   print("Not Found")
          elif choice == '5':
               print("Thank you")
               break
          else:
              print("Invalid Choice!!")
Contact_book()
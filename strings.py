# String
# name = "RDJ"
# print(len(name))
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[0:2])
# print(name[0:3])
# print(name[::-1])
# Methods: upper, lower, title, capitalize, count, find, replace, split, join, strip, join, startswith, endswith.
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize())
# print(name.count("D"))
# print(name.find("D"))
# print(name.replace("D", "X"))
# print(name.split())
# print(" ".join(name))
# print(name.strip("R"))
# Title = "  IronMan   "
# print(Title.split())
# print(Title.strip())
# print(Title.startswith(' '))
# print(Title.endswith(' '))
#-----------------------------

## Reverse String
# def rev(str):
#     return str[::-1]
# print(rev("Bhanu"))

## Count Vowels
# def Count_Vowel(str):
#     vowels = "AaEeIiOoUu"
#     count = 0
#     for ch in str:
#         if ch in vowels:
#             count += 1
#     return count
# print(Count_Vowel("banana"))

## Palindrome Check
# def Palindrome(str):
#     str = str.lower()
#     if str == str[::-1]:
#         return "Palindrome"
#     return "Not a Palindrome"
# print(Palindrome("Madam"))

## Remove Duplicate
# def remove_duplicate(str):
#     seen = {}
#     string = ""
#     for i in str:
#         if i in seen:
#             pass
#         else:
#             seen[i] = 1
#             string += i
#     return string
# print(remove_duplicate("programming"))
## Count of String 
# def count_character(str):
#     seen = {}
#     for i in str:
#         if i in seen:
#             seen[i] += 1
#         else:
#             seen[i] = 1
#     return seen
# print(count_character("programming"))


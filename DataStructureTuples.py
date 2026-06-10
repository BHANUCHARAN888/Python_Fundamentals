# Tuples: A Tuple stores multiple values, just like a List.
# duplicate not allowed - Immutable
# names = ("Bhanu", "Charan", "Anil")
# print(names)
# print(names[0])
# print(names[1])
# names[0] = "RDJ"  # Immutable(cant update once created)
# print(names) # TypeError
# operations: (len, count, index)
## Practice
# Create a tuple of 5 numbers and print the third element.
# nums = (1,2,3,4,5)
# a = nums[3]
# print(a)

# Count how many times 10 appears.
# nums = (10, 20, 10, 30, 10)
# target = 10
# count = 0
# for i in nums:
#     if i == target:
#         count += 1
# print(count)

# Find the index of "Python"
# skills = ("Java", "C", "Python", "SQL")
# target = "Python"
# for i in skills:
#     if i == target:
#         index = skills.index(target)
# print(index)

# Use tuple unpacking.
# student = ("Bhanu", 18, "Python")
# name, age, skill = student
# print(name)
# print(age)
# print(skill)

# Convert: tuple-->list
# letters = ("A", "B", "C")
# L = list(letters)
# print(L)
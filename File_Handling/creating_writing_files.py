# Creating and Writing Files 
# file - is a place on one computer where data is stored permanently
# example: (.txt, .csv, .pdf)
# It will store after the file closes 
# Structure====================>
# with open("Data.txt", "w") as file:
#     file.write("I am a GoodBoy")
    # write only accepts strings.
    # with helps to close automatically
# ------------------------------------

# Practice:
# Problem 1: create name.txt, store Bhanu Charan
with open("name.txt", "w") as file:
    file.write("Bhanu Charan")

# Problem 2: create skills.txt, store some skills
with open("skills.txt", 'w') as file:
    file.write("Python\nDSA\nSQL\nFILE handling")

# Problem 3: create student.txt, store some data 
name = input("Enter name: ")
age = input("Enter age: ")
skills = input("Enter skills: ")
goal = input("Enter Goal: ")

with open("student.txt", "w") as file:
    file.write(f"Name: {name}")
    file.write(f"\nAge: {age}")
    file.write(f"\nSkills: {skills}")
    file.write(f"\nGoal: {goal}")
    file.close()

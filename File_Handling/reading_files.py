### All about reading file ###
# with open("student.txt", "r") as file:
#     data = file.read()
# print(data) # gives data because file already created 

# with open("abc.txt", "r") as file:
#     data = file.read()
#     print(data) # FileNotFoundError

FILES =[
    "Data.txt",
    "name.txt",
    "skills.txt",
    "student.txt"
]
for f in FILES:
    with open(f, "r") as file:
        data = file.read()
    print(data)
    print("-------------------")

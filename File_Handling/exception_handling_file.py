# with open("abc.txt", "r") as file:
#     file.read()
#     #TODO: file does'nt exist here so, FileNotFoundError appears
#     #TODO: to handle this we use try-except method
## --------Practice---------
# 1
# try:
#     with open("abc.txt", "r") as file:
#         file.read()
# except:
#     print("File doesnt exist")
# 2
# try:
#     a = int(input("First: "))
#     b = int(input("Second: "))
#     print(a/b) 
# except ValueError:
#     print("Invalid Input")
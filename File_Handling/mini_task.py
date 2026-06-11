# File Handling Mini Project
# <----------Contact Book------------->
def menu():
    print("<---Contact Book--->")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Exit")
def add_contact(name, number):
    with open("Contact.txt", "a") as file:
        file.write(f"\n{name}: {number}")
    return "Contact added successfully"
def view_contact():
    print("<---Contact Data--->")
    with open("Contact.txt", "r") as file:
        data = file.read()
    return data
def contact_book():
    while True:
          menu()
          choice = input("Enter your Choice: ")
          if choice == "1":
             name = input("Enter name: ")
             number = input("Enter number: ")
             add = add_contact(name,number)
             print(add)
          elif choice == "2":
               data = view_contact()
               if data:
                  print(data)
               else:
                   print("No Contact Saved")
          elif choice == "3":
               print("Contact Book is closing...")
               break
          else:
              print("Invalid Choice!")
contact_book()

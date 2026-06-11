# File Handling Mini Project
# CRUD - Contact book v2
def menu():
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
def add_contact(name, number):
    with open("Contact.txt", "a") as file:
        file.write(f"{name}: {number}\n")
    print("\nContact Added Successfully")
def view_contact():
    with open("Contact.txt", "r") as file:
        data = file.read()
    if data:
        print(data)
    else:
        print("\nNo Contact Found")
def search_contact(search):
    with open("Contact.txt", "r") as file:
        contacts = file.readlines()
    found = False
    for contact in contacts:
        if contact.startswith(search):
            print(contact)
            found = True
    if found == False:
        print("\nContact not found")
def delete_contact(name):
    with open("Contact.txt", "r") as file:
        contacts = file.readlines()
    with open("Contact.txt", "w") as file:
        deleted = False
        for contact in contacts:
            if not contact.startswith(name):
                file.write(contact)
            else:
                deleted = True
    if deleted:
        print("\nDeleted Successfully")
    else:
        print("\nContact not found")
def update_contact(name, new_num):
    with open("Contact.txt", "r") as file:
        contacts = file.readlines()
    with open("Contact.txt", "w") as file:
        updated = False
        for contact in contacts:
            old_name = contact.split(":")[0]
            if old_name == name:
                file.write(f"{name}: {new_num}\n")
                updated = True
            else:
                file.write(contact)
    if updated:
        print("\nUpdated Successfully")
    else:
        print("\nContact not found")
def contact_book():
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == "1":
            print("\n---Adding new Contact---")
            name = input("Enter name: ")
            number = input("Enter number: ")
            add_contact(name, number)
            print("--------------------------")
        elif choice == "2":
            print("--------------------------")
            view_contact()
            print("--------------------------")
        elif choice == "3":
            print("--------------------------")
            search = input("Search Input: ")
            search_contact(search)
            print("--------------------------")
        elif choice == "4":
             print("--------------------------")
             name = input("Enter name: ")
             new_num = input("Enter number: ")
             update_contact(name, new_num)
             print("--------------------------")
        elif choice == "5":
            print("--------------------------")
            name = input("Enter name: ")
            delete_contact(name)
            print("--------------------------")
        elif choice == "6":
            print("\nContact book v2 is closing...")
            break
        else:
            print("\nInvalid choice")
contact_book()
            

    
    

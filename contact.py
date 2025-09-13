contacts = []
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, c in enumerate(contacts, 1):
            print(f"{i}. {c['name']} - {c['phone']}")
def search_contact():
    keyword = input("Enter name or phone to search: ")
    found = False
    for c in contacts:
        if keyword.lower() in c['name'].lower() or keyword in c['phone']:
            print(f"Found: {c['name']} | {c['phone']} | {c['email']} | {c['address']}")
            found = True
    if not found:
        print("No contact found.")
def update_contact():
    name = input("Enter the name of the contact to update: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = input("Enter new Phone: ")
            c['email'] = input("Enter new Email: ")
            c['address'] = input("Enter new Address: ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    choice = input("Choose an option:")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")

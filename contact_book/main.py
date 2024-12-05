from contact_manager import add_contact, view_contacts, remove_contact, search_contacts
from storage import load_contacts

# Load contacts at the start of the program
contacts = load_contacts()

while True:
    print("\n\nWelcome to Contact Book Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contacts (Bonus)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        name = input("Enter contact name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        add_contact(name, email, phone, address, contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        phone = input("Enter the phone number of the contact to remove: ")
        remove_contact(phone, contacts)
    elif choice == "4":
        query = input("Enter the name, email, or phone to search: ")
        search_contacts(query, contacts)
    elif choice == "5":
        print("Exiting Contact Book Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

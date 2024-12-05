from storage import save_contacts

def add_contact(name, email, phone, address, contacts):
    """Add a new contact if the phone number is unique."""
    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return
    if any(contact['phone'] == phone for contact in contacts):
        print("Error: Phone number already exists.")
        return
    new_contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
    }
    contacts.append(new_contact)
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, "
                  f"Phone: {contact['phone']}, Address: {contact['address']}")

def remove_contact(phone, contacts):
    """Remove a contact by phone number."""
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Contact with phone number {phone} removed successfully.")
            return
    print("Error: Contact not found.")

def search_contacts(query, contacts):
    """Search contacts by name, email, or phone."""
    results = [
        contact for contact in contacts
        if query.lower() in contact['name'].lower()
        or query.lower() in contact['email'].lower()
        or query in contact['phone']
    ]
    if results:
        print("\nSearch Results:")
        for i, contact in enumerate(results, start=1):
            print(f"{i}. Name: {contact['name']}, Email: {contact['email']}, "
                  f"Phone: {contact['phone']}, Address: {contact['address']}")
    else:
        print("No contacts found matching the query.")

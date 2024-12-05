import json
import os

FILE_PATH = "contacts.txt"

def load_contacts():
    """Load contacts from a file."""
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_contacts(contacts):
    """Save contacts to a file."""
    with open(FILE_PATH, "w") as file:
        json.dump(contacts, file, indent=4)

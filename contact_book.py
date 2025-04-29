import json
import logging
import os

# Configure logging
logging.basicConfig(filename='contacts.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

db_file = 'contacts.json'

# Ensure the contacts file exists
def initialize_storage():
    if not os.path.exists(db_file):
        with open(db_file, 'w') as f:
            json.dump([], f)

# Load contacts from JSON
def load_contacts():
    with open(db_file, 'r') as f:
        return json.load(f)

# Save contacts to JSON
def save_contacts(contacts):
    with open(db_file, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    logging.info(f'Added contact: {name}, {phone}, {email}')
    print("Contact added successfully!")

# Update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            save_contacts(contacts)
            logging.info(f'Updated contact: {contact}')
            print("Contact updated successfully!")
            return
    print("Contact not found!")

# Delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    save_contacts(contacts)
    logging.info(f'Deleted contact: {name}')
    print("Contact deleted successfully!")

# Search for a contact
def search_contact():
    name = input("Enter the name to search: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return
    print("Contact not found!")

# Main menu
def main_menu():
    initialize_storage()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            update_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()

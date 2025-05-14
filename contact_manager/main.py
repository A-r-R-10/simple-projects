"""
Contact Management System
------------------------
A simple command-line application to manage contacts with features:
- Add contacts with name, phone number, and optional email and address
- Delete contacts by ID
- Display all contacts
- Edit contact information
- Search contacts by name, phone, or email
"""

from contact_manager import ContactManager
from check_user_inputs import check_fullname, check_phone_number, check_email, check_address, check_id


def show_menu():
    """Display the menu options and get user's choice."""
    print("\n===== Contact Management System =====")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Show contacts")
    print("4. Edit contact")
    print("5. Search contact")
    print("6. Exit")
    print("===================================")

    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def add_contact(contact_manager):
    """Handle the add contact flow."""
    print("\n----- Add Contact -----")
    fullname = check_fullname()
    phone_number = check_phone_number()

    email = None
    if input("Do you want to add email? (y/n): ").lower() == "y":
        email = check_email()

    address = None
    if input("Do you want to add address? (y/n): ").lower() == "y":
        address = check_address()

    result = contact_manager.add_contact(fullname, phone_number, email, address)

    contact_manager.save_to_file()


def delete_contact(contact_manager):
    """Handle the delete contact flow."""
    print("\n----- Delete Contact -----")
    contact_id = check_id()
    result = contact_manager.delete_contact(contact_id)
    contact_manager.save_to_file()


def show_contacts(contact_manager):
    """Display all contacts."""
    print("\n----- All Contacts -----")
    contact_manager.show_all_contacts()


def edit_contact(contact_manager):
    """Handle the edit contact flow."""
    print("\n----- Edit Contact -----")
    contact_id = check_id()

    print("What do you want to edit?")
    print("f - Fullname")
    print("p - Phone number")
    print("e - Email")
    print("a - Address")

    option = input("Enter your choice (f/p/e/a): ").lower()

    if option == "f":
        fullname = check_fullname()
        contact_manager.edit_contact(contact_id, fullname=fullname)
    elif option == "p":
        phone_number = check_phone_number()
        contact_manager.edit_contact(contact_id, phone_number=phone_number)
    elif option == "e":
        email = check_email()
        contact_manager.edit_contact(contact_id, email=email)
    elif option == "a":
        address = check_address()
        contact_manager.edit_contact(contact_id, address=address)
    else:
        print("Invalid choice!")
        return
    contact_manager.save_to_file()


def search_contacts(contact_manager):
    """Handle the search contacts flow."""
    print("\n----- Search Contacts -----")
    print("Search by:")
    print("f - Fullname")
    print("p - Phone number")
    print("e - Email")

    option = input("Enter your choice (f/p/e): ").lower()

    if option == "f":
        fullname = check_fullname()
        contact_manager.search_contacts(fullname=fullname)
    elif option == "p":
        phone_number = check_phone_number()
        contact_manager.search_contacts(phone_number=phone_number)
    elif option == "e":
        email = check_email()
        contact_manager.search_contacts(email=email)
    else:
        print("Invalid choice!")
        return


def main():
    """Main function to run the contact management system."""
    contact_manager = ContactManager()

    while True:
        choice = show_menu()

        if choice == 1:
            add_contact(contact_manager)
        elif choice == 2:
            delete_contact(contact_manager)
        elif choice == 3:
            show_contacts(contact_manager)
        elif choice == 4:
            edit_contact(contact_manager)
        elif choice == 5:
            search_contacts(contact_manager)
        elif choice == 6:
            print("\nThank you for using Contact Manager. Goodbye!")
            break


if __name__ == "__main__":
    main()

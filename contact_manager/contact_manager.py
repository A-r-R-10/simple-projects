from contact import Contact
from json import dump, load, JSONDecodeError
from os import makedirs, path
from create_log import log_creator


class ContactManager:
    """
    A class to manage contacts, providing functionalities to add, delete, edit, display, and search contacts.
    Contacts are stored in and loaded from a JSON file.
    """

    def __init__(self):
        """
        Initializes an empty list of contacts and loads existing contacts from a file.
        """
        self.contacts: list[Contact] = []
        self.load_from_file()

    def add_contact(self, fullname: str, phone_number: str, email: str, address: str):
        """
        Adds a new contact to the contact list.
        :param fullname: Full name of the contact
        :param phone_number: Phone number of the contact
        :param email: Email address of the contact
        :param address: Physical address of the contact
        """
        contact = Contact(fullname, phone_number, email, address)
        self.contacts.append(contact)
        log_creator(contact.id, self.add_contact.__name__)
        print(f"Contact with ID {contact.id} added...")

    def delete_contact(self, contact_id: int):
        """
        Deletes a contact based on its ID.
        :param contact_id: ID of the contact to delete
        """
        for index, contact in enumerate(self.contacts):
            if contact.id == contact_id:
                self.contacts.pop(index)
                log_creator(contact.id, self.delete_contact.__name__)
                print(f"Contact with ID: {contact.id} deleted")
                return
        print(f"Contact with ID: {contact_id} not found!")

    def edit_contact(
            self, contact_id: int, fullname: str = None,
            phone_number: str = None, email: str = None,
            address: str = None
    ):
        """
        Edits a contact's information based on its ID.
        :param contact_id: ID of the contact to edit
        :param fullname: New full name (optional)
        :param phone_number: New phone number (optional)
        :param email: New email address (optional)
        :param address: New physical address (optional)
        """
        for contact in self.contacts:
            if contact.id == contact_id:
                if fullname:
                    contact.fullname = fullname
                if phone_number and phone_number.isdigit():
                    contact.phone_number = phone_number
                if email:
                    contact.email = email
                if address:
                    contact.address = address
                log_creator(contact.id, self.edit_contact.__name__)
                print(f"Contact with ID: {contact_id} updated")
                return
        print(f"Contact with ID: {contact_id} not found")

    def show_all_contacts(self):
        """
        Displays all contacts with numbering.
        """
        for index, contact in enumerate(self.contacts, 1):
            print(f"{index}. {contact.__str__()}")

    def search_contacts(self, fullname: str = None, phone_number: str = None, email: str = None):
        """
        Searches for contacts based on name, phone number, or email.
        :param fullname: Name to search for (optional)
        :param phone_number: Phone number to search for (optional)
        :param email: Email to search for (optional)
        """
        result = []
        for contact in self.contacts:
            if (fullname and fullname in contact.fullname) or \
               (phone_number and phone_number in contact.phone_number) or \
               (email and email in contact.email):
                result.append(contact.__str__())
                log_creator(contact.id, self.search_contacts.__name__)
        print(result)

    def save_to_file(self):
        """
        Saves the contact list to a JSON file.
        """
        try:
            makedirs("data", exist_ok=True)
            with open("data/contacts.json", "w") as file:
                dump({"data": [contact.to_dict() for contact in self.contacts]}, file, indent=4)
        except Exception as e:
            print(f"Error saving contacts: {e}")

    def load_from_file(self):
        """
        Loads contacts from a JSON file.
        """
        try:
            if path.exists("data/contacts.json"):
                with open("data/contacts.json") as file:
                    data_contacts = load(file)
                    self.contacts = [Contact(**data) for data in data_contacts["data"]]
            else:
                self.contacts = []
        except (KeyError, JSONDecodeError) as e:
            print(f"Error loading contacts: Invalid JSON format or missing 'data' key - {e}")
            self.contacts = []
        except Exception as e:
            print(f"Error loading contacts: {e}")
            self.contacts = []

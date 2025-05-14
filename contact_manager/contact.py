"""
Contact Class Module
-------------------
This module defines the Contact class used in the contact management system.
"""


class Contact:
    """
    Represents a contact entry with personal information and unique ID.

    Attributes:
        id (int): Unique identifier for the contact
        fullname (str): Full name of the contact
        phone_number (str): Phone number of the contact
        email (str): Email address (optional)
        address (str): Physical address (optional)
    """
    _contact_id = 0  # Class variable to track the last assigned ID

    def __init__(self, fullname, phone_number, email=None, address=None, id=None):
        """
        Initialize a new Contact object.

        Args:
            fullname (str): Full name of the contact
            phone_number (str): Phone number of the contact
            email (str, optional): Email-address
            address (str, optional): Physical address
            id (int, optional): Specific ID to assign. If None, auto-generated.
        """
        if id is None:
            self.id = self.generate_id()
        else:
            self.id = id
            # Update the class counter if necessary
            if id >= Contact._contact_id:
                Contact._contact_id = id + 1

        self.fullname = fullname
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        """Return a string representation of the contact."""
        result = f"ID: {self.id} | Name: {self.fullname} | Phone: {self.phone_number}"

        if self.email:
            result += f" | Email: {self.email}"

        if self.address:
            result += f" | Address: {self.address}"

        return result

    @classmethod
    def generate_id(cls):
        """
        Generate a unique ID for a new contact.

        Returns:
            int: A unique identifier
        """
        cls._contact_id += 1
        return cls._contact_id

    def to_dict(self):
        """
        Convert the contact to a dictionary representation.

        Returns:
            dict: Dictionary containing all contact attributes
        """
        return {
            "id": self.id,
            "fullname": self.fullname,
            "phone_number": self.phone_number,
            "email": self.email,
            "address": self.address
        }

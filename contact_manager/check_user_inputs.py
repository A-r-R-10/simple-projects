"""
Input Validation Module
---------------------
This module provides functions to validate and sanitize user inputs for the contact management system.
"""

import re


def check_fullname():
    """
    Prompt and validate user input for full name.

    Returns:
        str: Valid full name
    """
    while True:
        fullname = input("Enter full name: ").strip()
        if fullname:
            return fullname
        print("Invalid input! Name cannot be empty.")


def check_phone_number():
    """
    Prompt and validate user input for phone number.

    Returns:
        str: Valid phone number (digits only)
    """
    while True:
        phone_number = input("Enter phone number (digits only): ").strip()
        if phone_number and phone_number.isdigit():
            return phone_number
        print("Invalid input! Phone number must contain only digits.")


def check_email():
    """
    Prompt and validate user input for email address.

    Returns:
        str: Valid email address
    """
    while True:
        email = input("Enter email address: ").strip()
        # Basic email validation using regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if email and re.match(pattern, email):
            return email
        print("Invalid email format! Please enter a valid email address.")


def check_address():
    """
    Prompt and validate user input for address.

    Returns:
        str: Valid address
    """
    while True:
        address = input("Enter address: ").strip()
        if address:
            return address
        print("Invalid input! Address cannot be empty.")


def check_id():
    """
    Prompt and validate user input for contact ID.

    Returns:
        int: Valid contact ID
    """
    while True:
        try:
            contact_id = int(input("Enter contact ID: "))
            if contact_id > 0:
                return contact_id
            print("ID must be a positive number.")
        except ValueError:
            print("Invalid input! Please enter a numeric ID.")

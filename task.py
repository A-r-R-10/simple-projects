"""
task.py
This file defines the Task class, which represents an individual task with a title, description, and status.
"""

class Task:
    """
    Task class
    Represents a single task with attributes for title, description, and status.
    """
    def __init__(self, title, description, status):
        """
        __init__ method
        Initializes a new Task object with the given title, description, and status.
        Args:
            title (str): The title of the task
            description (str): The description of the task
            status (str): The status of the task (e.g., 'pending', 'done')
        """
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        """
        __str__ method
        Returns a string representation of the task for display purposes.
        Returns:
            str: A formatted string with title, description, and status
        """
        return f"title: {self.title} description: {self.description} status: {self.status}"

    def to_dict(self):
        """
        to_dict method
        Converts the task object to a dictionary for JSON serialization.
        Returns:
            dict: A dictionary containing title, description, and status
        """
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

"""
task_manager.py
This file defines the TaskManager class, which manages a collection of tasks.
It supports adding, deleting, updating, displaying tasks, and saving/loading them to/from a JSON file.
"""

from task import Task
from json import dump, load, JSONDecodeError
from os import path, makedirs


class TaskManager:
    """
    TaskManager class
    Manages a list of tasks with operations to add, delete, update, display, and persist tasks to a JSON file.
    """
    def __init__(self):
        """
        __init__ method
        Initializes an empty list to store tasks and loads existing tasks from the JSON file.
        """
        self.tasks = list()
        self.load_from_file()

    def add_task(self, title, description, status):
        """
        add_task method
        Adds a new task to the list if all inputs are valid, then saves the updated list to the file.
        Args:
            title (str): The title of the task
            description (str): The description of the task
            status (str): The status of the task
        Returns:
            str: Success message or error message if inputs are invalid
        """
        if (
                title.rstrip() and
                description.rstrip() and
                status.rstrip() and
                title is not None and
                description is not None and
                status is not None):
            task = Task(title, description, status)
            self.tasks.append(task)
            self.save_to_file()
            return "task added successfully"
        return "error: please provide valid values for all fields"

    def delete_task(self, title):
        """
        delete_task method
        Deletes a task by its title and saves the updated list to the file.
        Args:
            title (str): The title of the task to delete
        Returns:
            str: Success message, error if task not found, or error if title is invalid
        """
        if title.rstrip() and title is not None:
            for index, value in enumerate(self.tasks):
                if value.title == title:
                    self.tasks.pop(index)
                    self.save_to_file()
                    return f"the task with title: {title} deleted successfully..."
            return f"the task with title {title} not found!"
        return "the value of title is not valid"

    def update_task(self, title, description=None, status=None):
        """
        update_task method
        Updates the description and/or status of a task by its title, then saves the updated list to the file.
        Args:
            title (str): The title of the task to update
            description (str, optional): The new description
            status (str, optional): The new status
        Returns:
            str: Success message, error if task not found, or error if inputs are invalid
        """
        if title.rstrip() and title is not None:
            for task in self.tasks:
                if task.title == title:
                    updated = False
                    if (
                            description and description.rstrip() and
                            description is not None and task.description != description):

                        task.description = description
                        updated = True

                    if status and status.rstrip() and status is not None and task.status != status:
                        task.status = status
                        updated = True
                    if updated:
                        self.save_to_file()
                        return "task updated"
                    return "no changes made to the task"
            return f"the task with title {title} not found"
        return "the value is not valid"

    def show_all_tasks(self):
        """
        show_all_tasks method
        Returns a list of formatted strings representing all tasks with their indices.
        Returns:
            list: A list of strings, each describing a task
        """
        return [
            f"{index + 1}: {task.__str__()}"
            for index, task in enumerate(self.tasks)
        ]

    def save_to_file(self):
        """
        save_to_file method
        Saves the list of tasks to a JSON file in the 'data' directory with a 'data' key.
        Creates the 'data' directory if it doesn't exist.
        """
        try:
            makedirs("data", exist_ok=True)
            with open("data/tasks.json", "w") as file:
                dump({"data": [task.to_dict() for task in self.tasks]}, file, indent=4)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_from_file(self):
        """
        load_from_file method
        Loads tasks from the JSON file into the tasks list.
         Initializes an empty list if the file doesn't exist or is invalid.
        """
        try:
            if path.exists("data/tasks.json"):
                with open("data/tasks.json") as file:
                    data_tasks = load(file)
                    self.tasks = [Task(**data) for data in data_tasks["data"]]
            else:
                self.tasks = []
        except (KeyError, JSONDecodeError) as e:
            print(f"Error loading tasks: Invalid JSON format or missing 'data' key - {e}")
            self.tasks = []
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []

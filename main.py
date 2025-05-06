"""
main.py
This file provides a command-line interface to interact with the TaskManager class.
It presents a menu for users to add, delete, update, display tasks, or exit the program.
"""

from task_manager import TaskManager


def show_menu():
    """
    show_menu function
    Displays the menu options and returns the user's choice.
    Returns:
        str: The user's menu choice
    """
    print("\n=== Task Manager Menu ===")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. Update a task")
    print("4. Show all tasks")
    print("5. Exit")
    return input("Enter your choice (1-5): ")


def main():
    """
    main function
    Runs the main loop of the program, handling user interactions with the TaskManager.
    """
    manager = TaskManager()

    while True:
        choice = show_menu()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            status = input("Enter task status (e.g., pending, done): ")
            print(manager.add_task(title, description, status))

        elif choice == "2":
            title = input("Enter the title of the task to delete: ")
            print(manager.delete_task(title))

        elif choice == "3":
            title = input("Enter the title of the task to update: ")
            description = input("Enter new description (or press Enter to skip): ") or None
            status = input("Enter new status (or press Enter to skip): ") or None
            print(manager.update_task(title, description, status))

        elif choice == "4":
            tasks = manager.show_all_tasks()
            if tasks:
                print("\n=== All Tasks ===")
                for task in tasks:
                    print(task)
            else:
                print("No tasks available!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    """
    Entry point
    Runs the main function when the script is executed directly.
    """
    main()

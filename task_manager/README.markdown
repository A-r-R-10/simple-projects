## Task Manager

A simple command-line task management system built with Python. This application allows users to create, delete, update, and view tasks, with persistent storage in a JSON file.

## Features

- Add new tasks with a title, description, and status.
- Delete tasks by title.
- Update task descriptions or statuses.
- Display all tasks with their details.
- Save tasks to a JSON file (`data/tasks.json`) for persistence.
- Load tasks from the JSON file when the program starts.

## Requirements

- Python 3.6 or higher
- No external libraries required (uses standard `json` and `os` modules)

## Installation

1. Clone or download the project files to your local machine.

2. Ensure you have Python installed. You can check this by running:

   ```bash
   python --version
   ```

3. Place the following files in your project directory:

   - `task.py` (contains the `Task` class)
   - `task_manager.py` (contains the `TaskManager` class)
   - `main.py` (main script to run the application)

## Usage

1. Navigate to the project directory in your terminal.

2. Run the main script:

   ```bash
   python main.py
   ```

3. Follow the interactive menu to:

   - Add a new task
   - Delete a task by title
   - Update a task's description or status
   - View all tasks
   - Exit the program

Tasks are automatically saved to `data/tasks.json` after each operation (add, delete, update).

## File Structure

- `task.py`: Defines the `Task` class for representing individual tasks.
- `task_manager.py`: Defines the `TaskManager` class for managing tasks and file operations.
- `main.py`: The main script to interact with the user.
- `data/tasks.json`: Auto-generated file to store tasks (created in the `data` directory).

## Example JSON File

The `data/tasks.json` file will look like this:

```json
{
    "data": [
        {
            "title": "Write report",
            "description": "Complete the project report",
            "status": "pending"
        },
        {
            "title": "Meeting",
            "description": "Team sync at 2 PM",
            "status": "done"
        }
    ]
}
```

## Notes

- The program validates inputs to ensure no empty or invalid values are added.
- If the JSON file is corrupted or missing, the program will initialize an empty task list and print an error.
- The `data` directory is automatically created when saving tasks.

## Future Improvements

- Add a command-line interface (CLI) with `argparse` for non-interactive use.
- Support task categories or priorities.
- Add a GUI using `tkinter` or a web interface.

## License

This project is open-source and available under the MIT License.
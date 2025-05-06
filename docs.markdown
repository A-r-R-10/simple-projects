## Task Manager Documentation

This document provides detailed information about the classes, methods, and functionality of the Task Manager application.

## Overview

The Task Manager is a Python-based application for managing tasks. It uses two main classes: `Task` for representing individual tasks and `TaskManager` for handling task operations and persistence.

## Classes

### `Task`

Represents a single task with a title, description, and status.

#### Attributes

- `title` (str): The title of the task.
- `description` (str): A brief description of the task.
- `status` (str): The status of the task (e.g., "pending", "done").

#### Methods

- `__init__(self, title, description, status)`: Initializes a new task with the given title, description, and status.
- `__str__(self)`: Returns a string representation of the task in the format: `title: <title> description: <description> status: <status>`.
- `to_dict(self)`: Converts the task to a dictionary for JSON serialization. Returns a dictionary with keys `"title"`, `"description"`, and `"status"`.

### `TaskManager`

Manages a collection of tasks, including adding, deleting, updating, displaying, and persisting tasks to a JSON file.

#### Attributes

- `tasks` (list): A list of `Task` objects.

#### Methods

- `__init__(self)`: Initializes an empty task list.
- `add_task(self, title, description, status)`:
  - Adds a new task to the list if all inputs are valid (non-empty and not None).
  - Returns: `"task added successfully"` on success, or an error message if inputs are invalid.
- `delete_task(self, title)`:
  - Deletes a task by its title.
  - Saves changes to the JSON file.
  - Returns: A success message if deleted, or an error message if the task is not found or the title is invalid.
- `update_task(self, title, description=None, status=None)`:
  - Updates the description and/or status of a task by its title.
  - Saves changes to the JSON file.
  - Returns: `"task updated"` on success, or an error message if the task is not found or inputs are invalid.
- `show_all_tasks(self)`:
  - Returns a list of strings, each representing a task with an index (e.g., `1: title: <title> description: <description> status: <status>`).
- `save_to_file(self)`:
  - Saves the task list to `data/tasks.json` in the format: `{"data": [{task1}, {task2}, ...]}`.
  - Creates the `data` directory if it doesn't exist.
- `load_from_file(self)`:
  - Loads tasks from `data/tasks.json` into the `tasks` list.
  - Handles errors like missing files, invalid JSON, or missing `"data"` key by initializing an empty task list.

## Error Handling

- **Input Validation**: Methods like `add_task`, `delete_task`, and `update_task` check for empty or None inputs using `rstrip()` and `is not None`.
- **File Operations**:
  - `save_to_file`: Creates the `data` directory if needed.
  - `load_from_file`: Catches `KeyError` (missing `"data"` key), `JSONDecodeError` (invalid JSON), and other exceptions, initializing an empty task list in case of errors.

## Usage Example

```python
from task_manager import TaskManager

# Create a TaskManager instance
manager = TaskManager()

# Add a task
manager.add_task("Write code", "Finish Python project", "pending")

# Update task status
manager.update_task("Write code", status="done")

# Show all tasks
print(manager.show_all_tasks())

# Delete a task
manager.delete_task("Write code")
```

## File Storage

Tasks are stored in `data/tasks.json` with the following structure:

```json
{
    "data": [
        {
            "title": "string",
            "description": "string",
            "status": "string"
        }
    ]
}
```

## Dependencies

- Python standard library:
  - `json` for JSON serialization/deserialization.
  - `os` for directory creation.
  - `os.path` for file existence checks.

## Notes

- The `load_from_file` method is not automatically called in `__init__`. You may want to add `self.load_from_file()` to `__init__` for automatic loading.
- The `show_all_tasks` method uses the `__str__` method of the `Task` class for consistent task formatting.
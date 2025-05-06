from task import Task
from json import dump, load, JSONDecodeError
from os import path, makedirs


class TaskManager:
    def __init__(self):
        self.tasks = list()

    def add_task(self, title, description, status):
        if (
                title.rstrip() and
                description.rstrip() and
                status.rstrip() and
                title is not None and
                description is not None and
                status is not None):

            task = Task(title, description, status)
            self.tasks.append(task)
            return "task added successfully"
        return "error!..: not a valid value for somthing please fill all the arguments with correct value"

    def delete_task(self, title):
        if title.rstrip() and title is not None:
            for index, value in enumerate(self.tasks):
                if value.title == title:
                    self.tasks.pop(index)
                    self.save_to_file()
                    return f"the task with title: {title} deleted successfully..."

            return f"the task with title {title} not found!"

        return "the value of title is not valid"

    def update_task(self, title, description=None, status=None):
        if title.rstrip() and title is not None:
            for task in self.tasks:
                if task.title == title:
                    if description.rstrip() and description is not None:
                        task.description = description
                    if status.rstrip() and status is not None:
                        task.status = status
                    self.save_to_file()
                    return "task updated"

            return f"the task with title {title} not found"
        return "the value is not valid"

    def show_all_tasks(self):
        return [
            f"{indent + 1}: " + task.__str__()
            for indent, task in enumerate(self.tasks)
        ]

    def save_to_file(self):
        makedirs("data", exist_ok=True)
        with open("data/tasks.json", "w") as file:
            dump({"data": [task.to_dict() for task in self.tasks]}, file, indent=4)

    def load_from_file(self):
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

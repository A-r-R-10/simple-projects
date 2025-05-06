from task_manager import TaskManager

if __name__ == "__main__":
    task = TaskManager()
    task.add_task(title="practice", description="a", status="text..")
    task.add_task(title="sleep", description="have to sleep at the time", status="some text..")
    # print(task.delete_task(title="practice"))
    print(task.update_task(title="practice", description="daily typing exersice", status="done"))
    task.load_from_file()
    task.save_to_file()
    print(task.show_all_tasks())

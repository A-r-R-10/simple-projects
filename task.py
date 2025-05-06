class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"title: {self.title} description: {self.description} status: {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

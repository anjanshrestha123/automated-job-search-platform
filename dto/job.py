class Job:
    def __init__(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status

    def __repr__(self):
        return f"Job(id={self.id}, description={self.description}, status={self.status})"

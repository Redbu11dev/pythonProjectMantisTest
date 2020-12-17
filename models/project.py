class Project:
    def __init__(self, name=None, status=None, view_status=None, description=None):
        self.name = name
        self.status = status
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, o) -> bool:
        return self.name == o.name

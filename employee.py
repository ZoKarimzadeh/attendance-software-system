class Employee:
    def __init__(self, first_name, last_name, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return f"Employee(emp_id={self.id}, first_name={self.first_name}, last_name={self.last_name})"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return (self.id == other.id and
                    self.first_name == other.first_name and
                    self.last_name == other.last_name)
        return False

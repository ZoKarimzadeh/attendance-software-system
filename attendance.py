class Attendance:
    def __init__(self, emp_id, status, time):
        self.emp_id = emp_id
        self.status = status
        self.time = time

    def __repr__(self):
        return f"Attendance(emp_id={self.emp_id}, status={self.status}, time={self.time})"

    def __eq__(self, other):
        if isinstance(other, Attendance):
            return (self.emp_id == other.emp_id and
                    self.status == other.status and
                    self.time == other.time)
        return False

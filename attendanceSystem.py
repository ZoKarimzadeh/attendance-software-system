from employee import Employee
from attendance import Attendance
from datetime import datetime


class AttendanceSystem:
    def __init__(self, repository):
        self.repository = repository

    def add_employee(self, employee):
        self.repository.insert_employee(employee)

    def record_attendance(self, emp_id, status):
        self.record_attendance_time(emp_id, status, self.get_current_time())

    def record_attendance_time(self, emp_id, status, time):
        new_attendance = Attendance(emp_id, status, time)
        self.repository.insert_attendance(new_attendance)

    def new_employee_from_user(self):
        first_name = input("Enter first name of the employee: ")
        last_name = input("Enter last name of the employee: ")
        new_employee = Employee(first_name, last_name)
        self.add_employee(new_employee)

    def new_attendance_from_user(self):
        emp_id = input("Enter employee id: ")
        status = input("Enter status (A- Arrival, D- Departure): ")
        self.record_attendance(emp_id, status)

    def get_employee_attendance(self):
        emp_id = input("Enter employee id: ")
        return self.repository.get_employee_attendance(emp_id)

    def get_all_employees(self):
        return self.repository.get_all_employees()

    @staticmethod
    def get_current_time():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

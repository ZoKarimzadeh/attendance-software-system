from attendanceSystem import AttendanceSystem
from repository import Repository


class Main:
    """Employee Attendance Management Application."""

    def __init__(self):
        """Start the Employee Attendance system with a repository."""
        self.repository = Repository("employees.db")
        self.attendance_system = AttendanceSystem(self.repository)

    @staticmethod
    def print_menu():
        """Menu options."""
        menu = """
        >>> Employee Attendance Menu <<<
        1. Add Employee
        2. View All Employees
        3. Record Attendance
        4. View Employee Attendance
        5. Exit
        """
        print(menu)

    def add_employee(self):
        """Prompt user to add a new employee and add to the system."""
        print("Add Employee")
        self.attendance_system.new_employee_from_user()
        print("Employee has been successfully added.")

    def view_all_employees(self):
        """Display all employees in the system."""
        print("All Employees")
        employees = self.attendance_system.get_all_employees()
        for employee in employees:
            print(employee)

    def record_attendance(self):
        """Prompt user to record attendance for an employee."""
        print("Record Attendance")
        self.attendance_system.new_attendance_from_user()
        print("Attendance has been successfully recorded.")

    def view_employee_attendance(self):
        """Display attendance records for a specific employee."""
        print("Employee Attendance")
        attendance_records = self.attendance_system.get_employee_attendance()
        for record in attendance_records:
            print(record)

    def run(self):
        """Execute the main application loop to handle user inputs."""
        actions = {
            "1": self.add_employee,
            "2": self.view_all_employees,
            "3": self.record_attendance,
            "4": self.view_employee_attendance,
            "5": exit,
        }

        while True:
            self.print_menu()
            choice = input("Please enter your choice (1-5): ")
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main = Main()
    main.run()

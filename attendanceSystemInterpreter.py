from attendanceSystem import AttendanceSystem
from repository import Repository
from employee import Employee


class AttendanceSystemInterpreter:
    def __init__(self):
        self.repository = Repository("employees.db")
        self.attendance_system = AttendanceSystem(self.repository)

    def interpret_dsl_file(self, file_path):
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    self.execute_action(line)

    def execute_action(self, action_line):
        if ":" in action_line:
            action, data = action_line.split(":", 1)
            action = action.strip()
            args = eval(data.strip())
        else:
            action = action_line.strip()
            args = []

        if action == "Add Employee":
            first_name, last_name = args
            new_employee = Employee(first_name, last_name)
            self.attendance_system.add_employee(new_employee)
            print("Employee added successfully!")
        elif action == "Record Attendance":
            emp_id, status = args
            self.attendance_system.record_attendance(emp_id, status)
            print("Attendance recorded successfully!")
        elif action == "View All Employees":
            all_employees = self.attendance_system.get_all_employees()
            for employee in all_employees:
                print(employee)
        elif action == "View Employee Attendance":
            emp_id = args[0]
            employee_attendance = (self.attendance_system
                                   .get_employee_attendance(emp_id))
            for attendance in employee_attendance:
                print(attendance)
        else:
            print("Invalid action.")


if __name__ == "__main__":
    interpreter = AttendanceSystemInterpreter()
    interpreter.interpret_dsl_file("AttendanceSystemDSL.dsl")

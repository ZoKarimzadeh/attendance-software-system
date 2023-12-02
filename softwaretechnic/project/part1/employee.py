class Employee:
    def __init__(self, emp_id, first_name, last_name):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.attendance = []

    def record_attendance(self, status):
        # Implement the method to record attendance (e.g., 'present' or 'absent')
        pass
    
  

class AttendanceSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        # Implement the method to add an employee to the system
        pass

    def record_attendance(self, emp_id, status):
        # Implement the method to record attendance for a specific employee
        pass

    def generate_attendance_report(self):
        # Implement the method to generate and display attendance report
        pass

    def main():
    # Create an instance of the AttendanceSystem
    attendance_system = AttendanceSystem()

    # Example: Add employees to the system
    emp1 = Employee(1, "John", "Doe")
    emp2 = Employee(2, "Jane", "Smith")

    attendance_system.add_employee(emp1)
    attendance_system.add_employee(emp2)

    # Example: Record attendance
    attendance_system.record_attendance(emp1.emp_id, "present")
    attendance_system.record_attendance(emp2.emp_id, "absent")

    # Example: Generate and display attendance report
    attendance_system.generate_attendance_report()

if __name__ == "__main__":
    main()
import unittest
from unittest.mock import MagicMock, patch
from attendanceSystem import AttendanceSystem, Employee, Attendance


class TestAttendanceSystem(unittest.TestCase):
    def setUp(self):
        self.repository = MagicMock()
        self.attendance_system = AttendanceSystem(self.repository)

    def test_add_employee(self):
        # Arrange
        employee = Employee("John", "Doe")

        # Act
        self.attendance_system.add_employee(employee)

        # Assert
        self.repository.insert_employee.assert_called_once_with(employee)

    @patch("builtins.input", side_effect=["John", "Doe"])
    def test_new_employee_from_user(self, mock_input):
        # Arrange
        mock_employee = Employee("John", "Doe")
        self.attendance_system.add_employee = MagicMock()

        # Act
        self.attendance_system.new_employee_from_user()

        # Assert
        self.attendance_system.add_employee.assert_called_once()
        called_employee = self.attendance_system.add_employee.call_args[0][0]
        self.assertEqual(called_employee.first_name, mock_employee.first_name)
        self.assertEqual(called_employee.last_name, mock_employee.last_name)
        self.assertIsNone(called_employee.id)

    @patch("builtins.input", side_effect=["123", "A"])
    def test_new_attendance_from_user(self, mock_input):
        # Act
        self.attendance_system.record_attendance = MagicMock()
        self.attendance_system.new_attendance_from_user()

        # Assert
        (self.attendance_system.record_attendance.
         assert_called_once_with("123", "A"))

    @patch("attendanceSystem.datetime")
    def test_record_attendance(self, mock_datetime):
        # Arrange
        emp_id = "123"
        status = "A"
        expected_time = "2024-05-17 09:00:00"
        mock_datetime.now.return_value.strftime.return_value = expected_time
        self.attendance_system.record_attendance_time = MagicMock()

        # Act
        self.attendance_system.record_attendance(emp_id, status)

        # Assert
        self.attendance_system.record_attendance_time.assert_called_once_with(
            emp_id, status, expected_time
        )

    @patch("builtins.input", side_effect=["123"])
    def test_get_employee_attendance(self, mock_input):
        # Arrange
        self.repository.get_employee_attendance.return_value = [
            Attendance("123", "A", "2024-05-17 09:00:00"),
            Attendance("123", "D", "2024-05-17 18:00:00"),
        ]

        # Act
        result = self.attendance_system.get_employee_attendance()

        # Assert
        self.assertEqual(
            result,
            [
                Attendance("123", "A", "2024-05-17 09:00:00"),
                Attendance("123", "D", "2024-05-17 18:00:00"),
            ],
        )

    def test_get_all_employees(self):
        # Arrange
        self.repository.get_all_employees.return_value = [
            Employee("John", "Doe"),
            Employee("Jane", "Smith"),
        ]

        # Act
        result = self.attendance_system.get_all_employees()

        # Assert
        self.assertEqual(result,
                         [Employee("John", "Doe"),
                          Employee("Jane", "Smith")])


if __name__ == "__main__":
    unittest.main()

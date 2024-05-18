import sqlite3
from employee import Employee
from attendance import Attendance

class Repository:
    def __init__(self, repo_name):
        self.repo_name = repo_name
        self.conn = sqlite3.connect(repo_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                            id INTEGER PRIMARY KEY,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL
                        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
                            id INTEGER PRIMARY KEY,
                            emp_id INTEGER NOT NULL,
                            status TEXT NOT NULL,
                            time TEXT NOT NULL
                        )''')
        self.conn.commit()

    def insert_employee(self, employee):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO employees (first_name, last_name) VALUES (?, ?)''',
                       (employee.first_name, employee.last_name))
        self.conn.commit()

    def insert_attendance(self, attendance):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO attendance (emp_id, status, time) VALUES (?, ?, ?)''',
                       (attendance.emp_id, attendance.status, attendance.time))
        self.conn.commit()

    def get_all_employees(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM employees''')
        rows = cursor.fetchall()
        employees = [Employee(id=row[0], first_name=row[1], last_name=row[2]) for row in rows]
        return employees

    def get_employee_attendance(self, emp_id):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT emp_id, status, time FROM attendance WHERE emp_id = ?''', (emp_id,))
        rows = cursor.fetchall()
        attendance_list = [Attendance(emp_id=row[0], status=row[1], time=row[2]) for row in rows]
        return attendance_list

    def close(self):
        self.conn.close()

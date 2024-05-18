# Advanced Software Engineering/ Zoha Karimzadeh

Welcome to my project repository! This repository contains the files for my Advanced Software Engineering project. Below, you'll find a detailed description of the project, along with software engineering metrics and other relevant information.

## Project Description

My project is a simple employee attendance system, consisting of four main classes: **Attendance**, **AttendanceSystem**, **Employee**, and **Repository**. The project allows users to perform various functions such as inserting employees, recording attendance, viewing all employees, and viewing employee attendance lists.

## Technologies Used

- **Programming Language:** Python
- **Database:** SQLite3
- **Code Analysis:** SonarCloud
- **CI/CD:** GitHub Actions

## 1. Git/Github

I used Git and GitHub for version control, allowing me to track changes, manage branches, and collaborate with others effectively. Branches were used for feature development and bug fixes, with regular merging to the master branch. Tags were utilized for versioning.

## 2. UML Diagrams

For this project, I created four UML diagrams to visualize the system's architecture and behavior:
1. [Use Case Diagram](https://github.com/ZoKarimzadeh/attendance-software-system/blob/main/resources/Usecase_Diagram.png): Provides a graphical overview of system functionality in terms of actors, goals, and dependencies.
2. [Sequence Diagram](https://github.com/ZoKarimzadeh/attendance-software-system/blob/main/resources/Sequence_Diagram.png): Illustrates how processes interact and operate with one another in sequence.
3. [Class Diagram](https://github.com/ZoKarimzadeh/attendance-software-system/blob/main/resources/Class_Diagram.png): Displays the structure of the system, including classes, attributes, operations, and relationships.
4. [Activity Diagram](https://github.com/ZoKarimzadeh/attendance-software-system/blob/main/resources/Activity_Diagram.png): Shows the flow between different activities within the system.

## 3. DDD

A Domain-Driven Design (DDD) session was conducted to identify and map domains within the project. The project's context mapping diagram can be found [here](https://github.com/ZoKarimzadeh/attendance-software-system/blob/main/resources/Core_Domain_Chart.png).

## 4. Metrics

SonarCloud was used for code analysis and monitoring software quality. The project's SonarCloud dashboard can be accessed [here](https://sonarcloud.io/component_measures?id=ZoKarimzadeh_attendance-software-system). Additionally, linting was employed to check code style and adherence to standards.

## 5. Clean Code Development

To ensure clean code practices, the following principles were followed:

### Separated Methods for Each Action
Each action, such as add_employee, view_all_employees, record_attendance, and view_employee_attendance, is contained within its own method. This modular approach enhances readability by isolating each action's logic.

### Action Dictionary
An action dictionary was introduced to map user choices directly to their corresponding methods. This simplifies the run method and enhances code readability, eliminating the need for multiple if-elif conditions.

### Single Responsibility Principle (SRP)
The code follows the Single Responsibility Principle by assigning each method a specific responsibility. For example, the print_menu method is responsible for menu display, while other methods handle individual actions.

### Modularity
The codebase was refactored to enhance modularity. Separate methods were created for each action, resulting in a more organized and maintainable code structure.

### Readability
Descriptive method names were chosen to improve code readability. Additionally, the use of an action dictionary makes it easier to understand how user choices correspond to specific actions, enhancing code comprehension.

### Encapsulation
The logic for each action is encapsulated within its respective method, promoting encapsulation and improving code maintainability.

### Magic Numbers
The use of magic numbers was minimized by employing a dictionary to map user choices to methods. This approach eliminates hardcoded values, making the code more flexible and easier to maintain.

### DRY (Don't Repeat Yourself)
Repetitive code was eliminated by creating a print_menu method to handle menu display and utilizing a dictionary for action handling. This reduces duplication and improves code maintainability.

### Comments and Documentation
Meaningful method names and docstrings were utilized to provide clear explanations of each method's purpose and functionality. This enhances code readability and understanding for future maintenance.

## 6 and 7: Build Management and CI/CD

GitHub Actions was used for build management and CI/CD pipeline [Workflow yml file](https://github.com/ZoKarimzadeh/attendance-software-system/blob/main/.github/workflows/python-app.yml). The workflow includes:
- Build step: Installing requirements, checking code with lint, and running tests.
- Deploy step: Deploying the application after successful build and test completion. [Sample workflow](https://github.com/ZoKarimzadeh/attendance-software-system/actions/runs/9139057392).

## 8. Unit Tests

Python unittest module was used for unit testing. Tests were implemented to verify the functionality of classes, methods, and the database.

## 9. IDE

IntelliJ IDEA was chosen as the IDE for its robust features and productivity enhancements. Here are the top 5 important shortcuts for working with Python in IntelliJ IDEA:
- **Ctrl + Space**: Auto-complete code
- **Ctrl + B**: Go to declaration
- **Ctrl + Alt + B**: Go to implementation(s)
- **Ctrl + Shift + R**: Replace in path
- **Ctrl + Shift + F7**: Highlight usages in file

## 10. Domain Specific Language (DSL)
In this phase dedicated to Domain Specific Language (DSL), our project comprises two essential files: the Interpreter and the DSL file. The Interpreter, meticulously crafted, serves to interpret and execute commands defined within the DSL file.

Its primary role is to orchestrate actions within our employee attendance application seamlessly. These actions encompass fundamental functionalities such as Add Employee, Record Attendance, View All Employees and View Employee Attendance.

In the DSL file, each line corresponds to a distinct action within the employee attendance Application. This succinct yet potent structure ensures clarity and precision in command representation, facilitating efficient communication with the Interpreter.

For further reference, here is the link to access the Interpreter [Interpreter](https://github.com/ZoKarimzadeh/attendance-software-system/blob/main/attendanceSystemInterpreter.py) , and here is the link to explore the DSL file [DSL File](https://github.com/ZoKarimzadeh/attendance-software-system/blob/main/AttendanceSystemDSL.dsl).

## 11. Functional Programming

Functional programming concepts were integrated into the project.

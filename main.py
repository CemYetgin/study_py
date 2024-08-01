from database import Database
from user import User
from employee import Employee
from file_actions import FileOperations
from graph import Graph
from action import Action

def main():
    db = Database()
    user = User(db)
    employee = Employee(db)
    file_ops = FileOperations(db)
    graph = Graph(db)
    action = Action(db)

    print("1. Register")
    print("2. Login")
    choice = input("Your choice: ")

    if choice == '1':
        username = input("Username: ")
        password = input("Password: ")
        user.register(username, password)
        print("Registration successful!")
    elif choice == '2':
        username = input("Username: ")
        password = input("Password: ")
        if user.login(username, password):
            print("Login successful!")
            while True:
                print("1. Add New Employee")
                print("2. Delete Employee")
                print("3. Update Employee")
                print("4. List Employees")
                print("5. Import Data from Excel")
                print("6. Generate Graph")
                print("7. List Actions")
                print("8. Exit")
                action_choice = input("Your choice: ")

                if action_choice == '1':
                    employee_id = input("Employee ID: ")
                    first_name = input("First Name: ")
                    last_name = input("Last Name: ")
                    gender = input("Gender: ")
                    occupation = input("Occupation: ")
                    salary = float(input("Salary: "))
                    employee.add_employee(employee_id, first_name, last_name, gender, occupation, salary)
                    action.log_action("New employee added")
                elif action_choice == '2':
                    condition = input("Delete Criteria (employee_id, gender, occupation): ")
                    value = input(f"Delete Value ({condition}): ")
                    employee.delete_employee(condition, value)
                    action.log_action("Employee deleted")
                elif action_choice == '3':
                    condition = input("Update Criteria (employee_id, salary): ")
                    value = input(f"Employee ID to be updated ({condition}): ")
                    updates = {}
                    while True:
                        field = input("Field to update (employee_id, first_name, last_name, gender, occupation, salary, finish): ")
                        if field == "finish":
                            break
                        new_value = input(f"New Value ({field}): ")
                        updates[field] = new_value
                    employee.update_employee(condition, value, updates)
                    action.log_action("Employee updated")
                elif action_choice == '4':
                    condition = input("List Filter (employee_id, gender, occupation, list): ")
                    if condition == 'list':
                        employee.list_employees()
                    else:
                        value = input(f"List Value ({condition}): ")
                        employee.list_employees(condition, value)
                elif action_choice == '5':
                    file_ops.import_from_excel()
                    action.log_action("Data imported from Excel")
                elif action_choice == '6':
                    print("1. Pie Chart of Occupation and Gender")
                    print("2. Salary Histogram")
                    print("3. Salary Scatter Plot")
                    graph_choice = input("Your choice: ")
                    if graph_choice == '1':
                        graph.pie_chart()
                    elif graph_choice == '2':
                        graph.histogram()
                    elif graph_choice == '3':
                        graph.scatter_plot()
                elif action_choice == '7':
                    actions = action.list_actions()
                    for act in actions:
                        print(f"Operation: {act['operation']}, Date: {act['datetime']}")
                elif action_choice == '8':
                    break
        else:
            print("Login failed.")

if __name__ == "__main__":
    main()

from tabulate import tabulate

class Employee:
    def __init__(self, db):
        self.db = db

    def add_employee(self, employee_id, first_name, last_name, gender, occupation, salary):
        self.db.execute_query(
            "INSERT INTO employees (employee_id, first_name, last_name, gender, occupation, salary) VALUES (%s, %s, %s, %s, %s, %s)",
            (employee_id, first_name, last_name, gender, occupation, salary)
        )

    def delete_employee(self, condition, value):
        self.db.execute_query(f"DELETE FROM employees WHERE {condition} = %s", (value,))

    def update_employee(self, condition, value, updates):
        set_clause = ", ".join([f"{key} = %s" for key in updates.keys()])
        params = list(updates.values()) + [value]
        self.db.execute_query(f"UPDATE employees SET {set_clause} WHERE {condition} = %s", params)

    def list_employees(self, condition=None, value=None):
        if condition and value:
            result = self.db.fetch_all(f"SELECT employee_id, first_name, last_name, gender, occupation, salary FROM employees WHERE {condition} = %s", (value,))
        else:
            result = self.db.fetch_all("SELECT employee_id, first_name, last_name, gender, occupation, salary FROM employees")

        if result:
            headers = ["Employee ID", "First Name", "Last Name", "Gender", "Occupation", "Salary"]
            print(tabulate(result, headers=headers, tablefmt="pretty"))
        else:
            print("No data found.")

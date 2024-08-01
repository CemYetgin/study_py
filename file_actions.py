class FileOperations:
    def __init__(self, db):
        self.db = db

    def import_from_excel(self):
        file_path = r"C:\Users\hp\Desktop\py\factory_automation\employees.xlsx"
        try:
            import pandas as pd
            df = pd.read_excel(file_path)

            for _, row in df.iterrows():
                employee_id = row['employee_id']
                first_name = row['first_name']
                last_name = row['last_name']
                gender = row['gender']
                occupation = row['occupation']
                salary = row['salary']

                # Check if the record has already been added
                existing_record = self.db.fetch_one(
                    "SELECT COUNT(*) FROM employees WHERE employee_id = %s", (employee_id,)
                )[0]

                if existing_record == 0:
                    self.db.execute_query(
                        "INSERT INTO employees (employee_id, first_name, last_name, gender, occupation, salary) VALUES (%s, %s, %s, %s, %s, %s)",
                        (employee_id, first_name, last_name, gender, occupation, salary)
                    )
            print("Data successfully imported.")
        except Exception as e:
            print(f"Error: {e}")

from datetime import datetime

class Action:
    def __init__(self, db):
        self.db = db

    def log_action(self, description):
        # Get and format the current date and time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Add a new action record to the database
        self.db.execute_query(
            "INSERT INTO actions (operation, datetime) VALUES (%s, %s)",
            (description, timestamp)
        )

    def list_actions(self):
        # Prepare a query to get all action records
        query = "SELECT operation, datetime FROM actions"
        # Execute the query and get the result
        result = self.db.fetch_all(query)
        
        # If the result is not null, process the result into a list
        if result is not None:
            actions = [{"operation": row[0], "datetime": row[1]} for row in result]
            return actions
        else:
            # If the result is empty, return an empty list
            return []

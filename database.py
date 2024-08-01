import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='factory',
                user='root',
                password=''
            )
            if connection.is_connected():
                print('Database connection successful')
            return connection
        except Error as e:
            print(f'Error: Could not connect to the database: {e}')
            return None

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print('Query executed successfully')
        except Error as e:
            print(f'Error: Could not execute the query: {e}')
        finally:
            cursor.close()  # Close the cursor to clean up the result

    def fetch_all(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f'Error: Could not fetch data: {e}')
            return None
        finally:
            cursor.close()  # Close the cursor to clean up the result

    def fetch_one(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchone()
        except Error as e:
            print(f'Error: Could not fetch data: {e}')
            return None
        finally:
            cursor.close()  # Close the cursor to clean up the result

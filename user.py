import hashlib

class User:
    def __init__(self, db):
        self.db = db

    def register(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.db.execute_query(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, hashed_password)
        )

    def login(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        result = self.db.fetch_all(
            "SELECT * FROM users WHERE username = %s AND password = %s",
            (username, hashed_password)
        )
        return result

import mysql.connector

class DbClass:
    def __init__(self):
        self.db = mysql.connector.connect(
        auth_plugin="mysql_native_password",
        host="localhost",
        user="newuser",
        password="csci4830!",
        database="yardTracks"
        )
        self.cursor = self.db.cursor()
        # pandas df of testYard table in db

    def providetrackstable(self):
        # SHOW TABLE FOR TESTING
        table = []
        self.cursor.execute("SELECT * FROM testYard")
        for x in self.cursor:
            table.append(x)
        return table

    def providecarstable(self):
        # SHOW TABLE FOR TESTING
        table = []
        self.cursor.execute("SELECT * FROM testCars")
        for x in self.cursor:
            table.append(x)
        return table

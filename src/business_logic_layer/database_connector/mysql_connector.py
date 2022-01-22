
import mysql.connector


class MySQLConnector():

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="giang123",
            database='bachelor_project'
        )
        print(self.db)
        
        # test
        cursor = self.db.cursor()
        query = 'select * from Student'
        cursor.execute(query)

        for row in cursor:
            print(row)

    def get_user_info(self, username, password):
        cursor = self.db.cursor()
        query = 'select * from Student where email = %s and pwd = %s'

        cursor.execute(query, (username, password))
        
        user = {}
        for row in cursor:
            print(row)
            user['mssv'] = row[0]
            user['name'] = row[1]
            user['username'] = row[2]
            user['password'] = row[3]
        print(user)
        if user == {}:
            return None
        return user
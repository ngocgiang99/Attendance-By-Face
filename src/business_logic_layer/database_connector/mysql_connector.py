
import mysql.connector
import datetime

from business_logic_layer.utilities.singleton_meta import SingletonMeta

class MySQLConnector(metaclass=SingletonMeta):

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
        cursor.close()
        if user == {}:
            return None
        return user

    def insert_attendance(self, mssv):
        cursor = self.db.cursor()

        # '2011-12-18 13:17:17'
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(date_time)
        print(type(date_time))

        query = """insert into Attendance_History values (%s, %s, %s);"""
        print(query)
        val = (None, str(mssv), date_time)
        cursor.execute(query, val)

        self.db.commit()
        print(cursor.rowcount, "record inserted.")
        cursor.close()

    def get_histories(self, mssv):

        cursor = self.db.cursor()
        query = 'select * from Attendance_History where mssv = %s ORDER BY time_attend DESC'

        val = (str(mssv),)

        cursor.execute(query, val)
        
        res = []
        for row in cursor:
            res.append(row)
        cursor.close()
        return res


    def get_student_info(self, mssv):
        cursor = self.db.cursor()
        query = 'select * from Student where MSSV = %s'

        val = (str(mssv), )
        cursor.execute(query, val)       
        user = {}
        for row in cursor:
            print(row)
            user['mssv'] = row[0]
            user['name'] = row[1]
            user['email'] = row[2]
            user['password'] = row[3]
        print(user)
        cursor.close()
        if user == {}:
            return None
        return user

    def get_history(self, mssv, time):
        cursor = self.db.cursor()
        query = 'select * from Attendance_History where (MSSV = %s) and (time_attend >= %s);'

        time = time.strftime("%Y-%m-%d %H:%M:%S")
        val = (str(mssv), time)
        cursor.execute(query, val)       
        user = {}
        for row in cursor:
            print(row)
            user['id'] = row[0]
            user['mssv'] = row[1]
            user['time_attend'] = row[2].strftime("%Y-%m-%d %H:%M:%S")
        
        print(time)
        print(user)
        cursor.close()
        if user == {}:
            return None
        return user
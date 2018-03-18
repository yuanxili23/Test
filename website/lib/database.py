import pymysql
import pymysql.cursors

hostname = "localhost"
username = "root"
password = "love0906"
database = "sys"

class Database:
    connection = None

    def __init__(self):
        self.connect()

    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(host=hostname, user=username, passwd=password, db=database)

    def insert_users(self, user, passwd):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `users` (`user`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, (user, passwd))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
        finally:
            self.connection.close()

    def insert_thread(self, thread, created_date):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `threads` (`subject`, created_date) VALUES (%s, %s)"
                cursor.execute(sql, (thread, created_date))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
        finally:
            self.connection.close()



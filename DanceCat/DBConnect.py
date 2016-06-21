from DanceCat import Constants
import mysql.connector
import pymssql


class DBConnect:
    def __init__(self, connection_type, config):
        self.type = connection_type
        self.config = config
        self.connection = None

    def connect(self):
        if self.type == Constants.MYSQL:
            self.connection = mysql.connector.connect(**self.config)
        elif self.type == Constants.SQLSERVER:
            self.connection = pymssql.connect(**self.config)

    def connection_test(self):
        try:
            self.connect()
            return not not self.connection
        except:
            return False

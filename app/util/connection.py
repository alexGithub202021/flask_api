import mysql.connector
import configparser

class Connection:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('conf.ini')
        
    def connect(self):
        return mysql.connector.connect(
                host=self.config['MYSQL']['host'],
                user=self.config['MYSQL']['user'],
                password=self.config['MYSQL']['pwd'],
                database=self.config['MYSQL']['db_name']                                           
            )
from util.connection import Connection
from flask import request

connection = Connection().connect()

# Define a class that contains the user API methods
class UserController:

    # Constructor
    def __init__(self, userMysqlRepository):
        self.connection = connection
        self.cursor = connection.cursor()
        self.userMysqlRepository = userMysqlRepository

    def getUsers(self):
        return self.userMysqlRepository.getUsers()

    def getUserByName(self, name):
        return self.userMysqlRepository.getUserByName(name)

    # def getCmdByUser(self, name, date):
        # return self.userMysqlRepository.getCmdByUser(name, date)

    def createUser(self):
        return self.userMysqlRepository.createUser()

    def replaceUser(self, name):
        return self.userMysqlRepository.replaceUser(name)

    def updateUser(self, name):
        return self.userMysqlRepository.updateUser(name)

    def delUser(self, name):
        return self.userMysqlRepository.delUser(name)

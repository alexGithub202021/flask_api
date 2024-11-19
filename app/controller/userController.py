from util.connection import Connection
from flask import request
from service.mysql.userMysqlService import UserMysqlService

connection = Connection().connect()

# Define a class that contains the user API methods
class User:

    # Constructor
    def __init__(self):
        self.connection = connection
        self.cursor = connection.cursor()
        self.userMysqlService = UserMysqlService()

    def getUsers(self):
        return self.userMysqlService.getUsers()

    def getUserByName(self, name):
        return self.userMysqlService.getUserByName(name)

    # def getCmdByUser(self, name, date):
        # return self.userMysqlService.getCmdByUser(name, date)

    def createUser(self):
        return self.userMysqlService.createUser()

    def replaceUser(self, name):
        return self.userMysqlService.replaceUser(name)

    def updateUser(self, name):
        return self.userMysqlService.updateUser(name)

    def delUser(self, name):
        return self.userMysqlService.delUser(name)

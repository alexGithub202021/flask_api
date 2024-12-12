from util.functions import Functions
from util.logger import Logger
from flask import make_response, jsonify

class UserController:

    def __init__(self, userMysqlRepository):
        self.functions = Functions()
        self.logger = Logger().getLoger()
        self.userMysqlRepository = userMysqlRepository
        self.errorMsgToUsers = 'please contact the administrator.'

    def getUsers(self):
        return self.operation1()

    def getUserByName(self, name):
        return self.operation1(name)

    # def getCmdByUser(self, name, date):
        # return self.userMysqlRepository.getCmdByUser(name, date)

    def createUser(self):
        return self.operation2("createUser")

    def replaceUser(self, name):
        return self.operation2("replaceUser", name)

    def updateUser(self, name):
        return self.operation2("updateUser", name)

    def delUser(self, name):
        return self.operation2("delUser", name)
        
    def operation1(self, name=None):   
        if name is None:     
            res = self.userMysqlRepository.getUsers()
        else:
            res = self.userMysqlRepository.getUserByName(name)
        
        if type(res).__name__ == "CMySQLCursor":
            response = self.functions.convert_to_json(res)
        else:
            self.logger.error(res)
            response = make_response(jsonify({'error': self.errorMsgToUsers}), 404) 
            
        return response  
    
    def operation2(self, methodName, name=None):
        if name is None:
            res = self.userMysqlRepository.createUser()
        elif "updateUser" == methodName:
            res = self.userMysqlRepository.updateUser(name)
        elif "replaceUser" == methodName:
            res = self.userMysqlRepository.replaceUser(name)
        elif "delUser" == methodName:
            res = self.userMysqlRepository.delUser(name)
        
        if str(res[0]).startswith("200"):
            return res[1]
        else:
            self.logger.error(res[1])
            return make_response(jsonify({'error': self.errorMsgToUsers}), 404) 

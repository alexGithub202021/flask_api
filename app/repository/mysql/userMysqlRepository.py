from util.functions import Functions
from flask import request

class UserMysqlRepository:
    
    def __init__(self, connection):
        self.functions = Functions()
        self.connection = connection
        self.cursor = self.connection.cursor()   
    
    def getUsers(self):
        query = "SELECT * FROM user"
        self.cursor.execute(query)
        return self.functions.convert_to_json(self.cursor)

    def getUserByName(self, name):
        if isinstance(name, str): #todo: upd test
            query = """
                SELECT * FROM user where name = %s
            """
            self.cursor.execute(query, (name,))
            return self.functions.convert_to_json(self.cursor)
        else:
            return f'The name of the user must only contains characters or digit.' 
    
    def createUser(self):
        # todo: check inputs
        data = request.json
        name = data.get('name')
        idcity = data.get('idcity')
        create_time = data.get('create_time')
        update_time = data.get('update_time')
        
        if isinstance(name, str) and isinstance(idcity, int) and isinstance(create_time, str) and isinstance(update_time, str): #todo: upd test
            create_time = self.functions.parse_datetime(create_time)
            update_time = self.functions.parse_datetime(update_time)
            query = """
                INSERT INTO `user` (`name`, `idcity`, `create_time`, `update_time`) VALUES (%s, %s, %s, %s)
            """
            try:
                self.cursor.execute(query, (name, idcity, create_time, update_time))
                self.connection.commit()
                return f'New user {name} created'
            except:
                self.connection.rollback()
                return "user {name} creation failed"
            
        else:
            #if no valid inputs
            return f'data inputs are not valid'
        
    # def getCmdByUser(self, name, date):
    #     if isinstance(name, str) and isinstance(date, str): #todo: upd test
    #         query ="""
    #             SELECT c.idcommand_product, u.name, c.create_time, p.label
    #             from user u
    #             join command_product c on u.iduser = c.iduser
    #             join product p on c.idproduct = p.idproduct
    #             where u.name like %s and c.create_time like %s
    #         """
    #         self.cursor.execute(query, (name, f"{date}%"))
    #         # passing query to execute as above:
    #         # + readabl + prevents sql inj°
    #         return self.functions.convert_to_json(self.cursor)
    #     else:
    #         return f'The name of the user must only contains characters or digit.'        
        
    def replaceUser(self, name):
        #todo: validate inputs
        data = request.json
        name2 = data.get('name')
        idcity = data.get('idcity')
        create_time = data.get('create_time')
        update_time = data.get('update_time')
        
        if isinstance(name, str) and isinstance(idcity, int) and isinstance(create_time, str) and isinstance(update_time, str): #todo: upd test
            create_time = self.functions.parse_datetime(create_time)
            update_time = self.functions.parse_datetime(update_time)
            query = """
                UPDATE `user` set `name` = %s, `idcity` = %s, `create_time` = %s, `update_time` = %s where name = %s
            """
            
            try:
                self.cursor.execute(query, (name2, idcity, create_time, update_time, name))
                self.connection.commit()
                return f'User {name} replaced by user {name2}'                
            except:
                self.connection.rollback()
                return "user {name} replacement failed"
        else:
            #if no valid inputs
            return f'data inputs are not valid'
        
    def updateUser(self, name):
        #todo: validate inputs
        data = request.json
        idcity = data.get('idcity')
        create_time = data.get('create_time')
        update_time = data.get('update_time')
        
        if isinstance(name, str) and isinstance(idcity, int) and isinstance(create_time, str) and isinstance(update_time, str): #todo: upd test
            create_time = self.functions.parse_datetime(create_time)
            update_time = self.functions.parse_datetime(update_time)
            query="""
                UPDATE `user` set `idcity` = %s, `create_time` = %s, `update_time` = %s where name = %s
            """

            try:
                self.cursor.execute(query, (idcity, create_time, update_time, name))
                self.connection.commit()
                return f'User {name} updated'                          
            except:
                self.connection.rollback()
                return "user {name} update failed"        
        else:
            #if no valid inputs 
            return f'data inputs are not valid' 
            
    def delUser (self, name):
        if isinstance(name, str): #todo: upd test
            query = """
                DELETE FROM `user` WHERE name LIKE %s
            """
            self.cursor.execute(query, (name,))
            return f'User {name} deleted !'
        else:
            #if no valid inputs
            return f'data inputs are not valid'       
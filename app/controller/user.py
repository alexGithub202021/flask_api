import json
import mysql.connector
import configparser

from flask import Flask, request
from datetime import datetime as dt

config = configparser.ConfigParser()
config.read('conf.ini')

app = Flask(__name__)   
connection = mysql.connector.connect(
                host=config['MYSQL']['host'],
                user=config['MYSQL']['user'],
                password=config['MYSQL']['pwd'],
                database=config['MYSQL']['db_name']                                           
            )

# Define a class that contains the user API methods
class User:
    
    # Constructor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    def __init__(self):
        self.app = app
        self.connection = connection
        self.cursor = connection.cursor()
        
    # @api {get} /api/user Get all users    
    def get_users(self):
        query = "SELECT * FROM user"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return self.convert_to_json(results)
    
    # @api {get} /api/user/:name/:date Get user's command filtering on command's date    
    def get_cmd_by_user(self, name, date):
        if isinstance(name, str) and isinstance(date, str): #todo: upd test
            query ="""
                SELECT c.idcommand_product, u.name, c.create_time, p.label
                from user u
                join command_product c on u.iduser = c.iduser
                join product p on c.idproduct = p.idproduct
                where u.name = %s and c.create_time like %s
            """
            self.cursor.execute(query, (name, f"{date}%"))
            # passing query to execute as above:
            # + readabl + prevents sql inj°
            result = self.cursor.fetchall()
            return self.convert_to_json(result)
        else:
            return f'The name of the user must only contains characters or digit.'

    # @api {get} /api/use/:name Get user by name
    def get_user_by_name(self, name):
        if isinstance(name, str): #todo: upd test
            query = """
                SELECT * FROM user where name = %s
            """
            self.cursor.execute(query, (name,))
            result = self.cursor.fetchall()
            return self.convert_to_json(result)
        else:
            return f'The name of the user must only contains characters or digit.'
    
    # @api {post} /api/user Create a new user
    def create_user(self):
        #validate inputs
        data = request.json
        name = data.get('name')
        idcity = data.get('idcity')
        create_time = data.get('create_time')
        update_time = data.get('update_time')
        
        if isinstance(name, str) and isinstance(idcity, int) and isinstance(create_time, str) and isinstance(update_time, str): #todo: upd test
            #insert
            create_time = self.parse_datetime(create_time)
            update_time = self.parse_datetime(update_time)
            query = """
                INSERT INTO `user` (`name`, `idcity`, `create_time`, `update_time`) VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (name, idcity, create_time, update_time))
            return f'New user {name} created'
        else:
            #if no valid inputs
            return f'data inputs are not valid'
    
    # @api {put} /api/user/:name Replace user by name
    def replace_user(self, name):
        #validate inputs
        data = request.json
        name2 = data.get('name')
        idcity = data.get('idcity')
        create_time = data.get('create_time')
        update_time = data.get('update_time')
        
        if isinstance(name, str) and isinstance(idcity, int) and isinstance(create_time, str) and isinstance(update_time, str): #todo: upd test
            #insert
            create_time = self.parse_datetime(create_time)
            update_time = self.parse_datetime(update_time)
            query = """
                UPDATE `user` set `name` = %s, `idcity` = %s, `create_time` = %s, `update_time` = %s where name = %s
            """
            self.cursor.execute(query, (name2, idcity, create_time, update_time, name))
            return f'User {name} replaced by user {name2}'
        else:
            #if no valid inputs
            return f'data inputs are not valid'
    
    # @api {patch} /api/user/:name Update user by name
    def update_user(self, name):
        #validate inputs
        data = request.json
        idcity = data.get('idcity')
        create_time = data.get('create_time')
        update_time = data.get('update_time')
        
        if isinstance(name, str) and isinstance(idcity, int) and isinstance(create_time, str) and isinstance(update_time, str): #todo: upd test
            #insert
            create_time = self.parse_datetime(create_time)
            update_time = self.parse_datetime(update_time)
            query="""
                UPDATE `user` set `idcity` = %s, `create_time` = %s, `update_time` = %s where name = %s
            """
            self.cursor.execute(query, (idcity, create_time, update_time, name))
            return f'User {name} updated'
        else:
            #if no valid inputs
            return f'data inputs are not valid'
    
    # @api {delete} /api/user/:name Delete user by name
    def del_user(self, name):
        if isinstance(name, str): #todo: upd test
            query = """
                DELETE FROM `user` WHERE name LIKE %s
            """
            self.cursor.execute(query, (name,))
            return f'User {name} deleted !'
        else:
            #if no valid inputs
            return f'data inputs are not valid'

    def run(self):
        self.app.run(debug=True, use_reloader=False, use_debugger=False, host='0.0.0.0', port=5002);  
        # self.app.run(host='0.0.0.0', port=5002);     
        
    # Convert the query results to a list of dictionaries    
    def convert_to_json(self, results):
        rows = []
        for row in results:
            row_dict = {}
            for idx, value in enumerate(row):
                # Convert datetime objects to string representation
                if isinstance(value, dt):
                    row_dict[self.cursor.column_names[idx]] = value.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    row_dict[self.cursor.column_names[idx]] = value
            rows.append(row_dict)

        # Serialize the list of dictionaries to JSON format
        json_output = json.dumps(rows)
        return json_output;
    
    # Convert the input date string to a datetime object
    def parse_datetime(self, input_datetime):
        # Parse input date string
        parsed_date = dt.strptime(input_datetime, '%d/%m/%Y')
        current_time = dt.now().time()
        combined_datetime = dt.combine(parsed_date, current_time)
        output_datetime = combined_datetime.strftime('%Y-%m-%d %H:%M:%S')
        return output_datetime;
import json
import mysql.connector
from flask import Flask, request, jsonify
from datetime import datetime as dt

app = Flask(__name__)   
connection = mysql.connector.connect(
                host="mysql_python",
                user="root",
                password="pwd",
                database="pydb"
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

    # @api {get} /api/user/:name Get user by name
    def get_user(self, name):
        if isinstance(name, str):
            query = "SELECT * FROM user where name = '{}'".format(name)
            self.cursor.execute(query)
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
        
        if isinstance(name, str) and isinstance(idcity, int) and isinstance(create_time, str) and isinstance(update_time, str):
            #insert
            create_time = self.parse_datetime(create_time)
            update_time = self.parse_datetime(update_time)
            query = "INSERT INTO `user` (`name`, `idcity`, `create_time`, `update_time`) VALUES ('{}', {}, '{}', '{}')".format(name, idcity, create_time, update_time)
            self.cursor.execute(query)
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
        
        if isinstance(name, str) and isinstance(idcity, int) and isinstance(create_time, str) and isinstance(update_time, str):
            #insert
            create_time = self.parse_datetime(create_time)
            update_time = self.parse_datetime(update_time)
            query = "UPDATE `user` set `name` = '{}', `idcity` = {}, `create_time` = '{}', `update_time` = '{}' where name = '{}'".format(name2, idcity, create_time, update_time, name)
            self.cursor.execute(query)
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
        
        if isinstance(name, str) and isinstance(idcity, int) and isinstance(create_time, str) and isinstance(update_time, str):
            #insert
            create_time = self.parse_datetime(create_time)
            update_time = self.parse_datetime(update_time)
            query = "UPDATE `user` set `idcity` = {}, `create_time` = '{}', `update_time` = '{}' where name = '{}'".format(idcity, create_time, update_time, name)
            self.cursor.execute(query)
            return f'User {name} updated'
        else:
            #if no valid inputs
            return f'data inputs are not valid'
    
    # @api {delete} /api/user/:name Delete user by name
    def del_user(self, name):
        if isinstance(name, str):
            query = "DELETE FROM `user` WHERE name LIKE '{}'".format(name)
            self.cursor.execute(query)
            return f'User {name} deleted !'
        else:
            #if no valid inputs
            return f'data inputs are not valid'

    def run(self):
        self.app.run(host='0.0.0.0', port=5002);    
        
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
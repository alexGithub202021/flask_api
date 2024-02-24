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

class User:
    
    def __init__(self):
        self.app = app
        self.connection = connection
        self.cursor = connection.cursor()
        
    def get_users(self):
        query = "SELECT * FROM user"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return self.convert_to_json(results)

    # @app.route('/api/resource/<name>', methods=['GET']) -> only if direct access <> not in a class
    def get_user(self, name):
        if isinstance(name, (str, int)):
            query = "SELECT * FROM user where name = '{}'".format(name)
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return self.convert_to_json(result)
        else:
            return f'The name of the user must only contains characters or digit.'
    
    # @app.route('/api/resource', methods=['POST']) -> only if direct access <> not in a class
    def create_user(self):
        # data = request.json
        # name = data.get('name')
        # return f'New user {name} created'
        return f'New user created'
    
    # @app.route('/api/resource/<name>', methods=['PUT']) -> only if direct access <> not in a class
    def replace_user(self, name):
        return f'User {name} replaced !'
    
    # @app.route('/api/resource/<name>', methods=['PATCH']) -> only if direct access <> not in a class
    def update_user(self, name):
        return f'User {name} updated !'
    
    # @app.route('/api/resource/<name>', methods=['DELETE']) -> only if direct access <> not in a class 
    def del_user(self, name):
        return f'User {name} deleted !'

    def run(self):
        self.app.run(host='0.0.0.0', port=5002);
        
    def convert_to_json(self, results):
        # Convert the query results to a list of dictionaries
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
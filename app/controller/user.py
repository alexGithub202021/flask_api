from flask import Flask, request

app = Flask(__name__)

class User:
    def __init__(self):
        self.app = Flask(__name__)

    # @app.route('/api/resource/<name>', methods=['GET']) -> only if direct access <> not in a class
    def get_resource(self, name):
        return f'Hello user {name}!'
    
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
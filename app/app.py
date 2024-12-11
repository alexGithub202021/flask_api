from controller.userController import UserController
from flask import Flask
from service.container import Container
import debugpy

app = Flask(__name__)   
container = Container()

def expose_api():
    
    debugpy.listen(("0.0.0.0", 5678))  # Port 5678 or any open port
    print("Waiting for debugger to attach...")    
    
    user = container.userController()
    
    app.add_url_rule('/api/users', view_func=user.getUsers, methods=['GET'])
    app.add_url_rule('/api/users/<string:name>', view_func=user.getUserByName, methods=['GET'])
    # app.add_url_rule('/api/users/<name>/commands/<date>', view_func=user.getCmdByUser, methods=['GET'])
    app.add_url_rule('/api/users', view_func=user.createUser, methods=['POST'])
    app.add_url_rule('/api/users/<string:name>', view_func=user.replaceUser, methods=['PUT'])
    app.add_url_rule('/api/users/<string:name>', view_func=user.updateUser, methods=['PATCH'])
    app.add_url_rule('/api/users/<string:name>', view_func=user.delUser, methods=['DELETE'])
    
    # *** other endpoints format:
    # @app.route("/api/users", methods=["POST"])
    # def create_user():
    #     return user.createUser()
    
    # @app.route("/api/users/<string:name>", methods=["GET"])
    # def get_user_by_name(name):
    #     return user.getUserByName(name)      
    
    app.run(debug=True, use_reloader=False, use_debugger=False, host='0.0.0.0', port=5002);  

if __name__ == '__main__':
    expose_api();
from controller.user import User
import debugpy

def expose_api():
    
    debugpy.listen(("0.0.0.0", 5678))  # Port 5678 or any open port
    print("Waiting for debugger to attach...")    
    
    user = User();
    # endpoints path
    user.app.add_url_rule('/api/users', view_func=user.get_users, methods=['GET'])
    user.app.add_url_rule('/api/users/<string:name>', view_func=user.get_user_by_name, methods=['GET'])
    user.app.add_url_rule('/api/users/<name>/commands/<date>', view_func=user.get_cmd_by_user, methods=['GET'])
    user.app.add_url_rule('/api/user', view_func=user.create_user, methods=['POST'])
    user.app.add_url_rule('/api/users/<name>', view_func=user.replace_user, methods=['PUT'])
    user.app.add_url_rule('/api/users/<name>', view_func=user.update_user, methods=['PATCH'])
    user.app.add_url_rule('/api/users/<name>', view_func=user.del_user, methods=['DELETE'])
    
    user.run();

if __name__ == '__main__':
    expose_api();
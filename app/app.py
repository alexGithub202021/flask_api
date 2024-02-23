from controller.user import User

def expose_api():
    user = User();
    user.app.add_url_rule('/api/resource/<name>', view_func=user.get_resource, methods=['GET'])
    user.app.add_url_rule('/api/resource', view_func=user.create_user, methods=['POST'])
    user.app.add_url_rule('/api/resource/<name>', view_func=user.replace_user, methods=['PUT'])
    user.app.add_url_rule('/api/resource/<name>', view_func=user.update_user, methods=['PATCH'])
    user.app.add_url_rule('/api/resource/<name>', view_func=user.del_user, methods=['DELETE'])
    user.run();

if __name__ == '__main__':
    expose_api();
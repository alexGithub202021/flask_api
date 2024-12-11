from dependency_injector import containers, providers
from repository.mysql.userMysqlRepository import UserMysqlRepository
from controller.userController import UserController
from util.connection import Connection

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()
    connection = providers.Singleton(Connection().connect)
    
    userMysqlRepository = providers.Factory(UserMysqlRepository, connection=connection)
    userController = providers.Factory(UserController, userMysqlRepository=userMysqlRepository) 
import pytest
from unittest import mock

class Test_userController:
    
    def test_get_users_with_no_result(mocker):
        # Mock the MySQL connection
        with mock.patch('mysql.connector.connect') as mock_connect:
            mock_connection = mock.Mock()
            mock_connect.return_value = mock_connection
            
            expected ="[]"

            # Mock the repository
            mock_user_repo = mock.Mock()
            mock_user_repo.getUsers.return_value = "[]"
            
            from controller.userController import UserController 

            # Create an instance of UserController with the mocked repository
            user_controller = UserController(mock_user_repo) 

            # Call the getUsers method
            result = user_controller.getUsers()

            # Assert the expected result
            assert result == expected
            
    
    def test_get_users_with_result(mocker):
        # Mock the MySQL connection
        with mock.patch('mysql.connector.connect') as mock_connect:
            mock_connection = mock.Mock()
            mock_connect.return_value = mock_connection
            
            expected = '[{"create_time": "2024-01-31 14:21:59", "idcity": null, "iduser": 1, "name": "user1", "update_time": null }]'

            # Mock the repository
            mock_user_repo = mock.Mock()
            mock_user_repo.getUsers.return_value = '[{"create_time": "2024-01-31 14:21:59", "idcity": null, "iduser": 1, "name": "user1", "update_time": null }]'
            
            from controller.userController import UserController 

            # Create an instance of UserController with the mocked repository
            user_controller = UserController(mock_user_repo) 

            # Call the getUsers method
            result = user_controller.getUsers()

            # Assert the expected result
            assert result == expected

import pytest
import requests
from config.config import Config
from api.users_api_client import UsersApiClient 

@pytest.mark.smoke
@pytest.mark.user
def test_it_checks_user_list():
    users = UsersApiClient.list_users()
    assert users['per_page'] == len(users['data'])

@pytest.mark.regression
@pytest.mark.user
@pytest.mark.negative
def test_it_checks_fail_answer_with_another_method_for_user_list():
    users = UsersApiClient.no_list_users()
    assert users['per_page'] == len(users['data'])

@pytest.mark.regression
@pytest.mark.user
def test_it_checks_user_created():
    user_details = {"name": "morpheus",
                    "job": "leader"
                    }
    user = UsersApiClient.create_user(user_details)
    print(user)
    assert (user['name'] == 'morpheus' and (user['job'] == 'leader'))

@pytest.mark.regression
@pytest.mark.user
@pytest.mark.negative
def test_it_checks_fail_answer_user_created():
    user_details = {"name": "morpheus",
                    "job": "leader"
                    }
    user = UsersApiClient.create_user(user_details)
    print(user)
    assert (user['id'] == 'morpheus')
    
@pytest.mark.regression
@pytest.mark.user
def test_it_checks_update_user():
    user_details = {"name": "morpheus",
                    "job": "zion resident"
                    }
    user = UsersApiClient.update_user(user_details)
    print(user)
    assert (user['name'] == 'morpheus' and (user['job'] == 'zion resident'))

@pytest.mark.regression
@pytest.mark.user
@pytest.mark.negative
def test_it_checks_fail_answear_update_user():
    user_details = {"name": "morpheus",
                    "job": "zion resident"
                    }
    user = UsersApiClient.update_user(user_details)
    print(user)
    assert ((user['job'] == 'leader') and user['name'] == 'morpheus')

@pytest.mark.regression
@pytest.mark.user
def test_it_checks_delete_user():
    user = UsersApiClient.delete_user()
    print(user)
    assert user.get('id') is None
    
@pytest.mark.regression
@pytest.mark.user
@pytest.mark.negative
def test_it_checks_fail_delete_user():
    user = UsersApiClient.delete_user()
    print(user)
    assert user.get('id') is not None    

@pytest.mark.smoke
@pytest.mark.user
def test_it_checks_single_user():
    user = UsersApiClient.single_user()
    assert user.get('data') is not None

@pytest.mark.smoke
@pytest.mark.user
@pytest.mark.negative
def test_it_checks_fail_single_user():
    user = UsersApiClient.single_user()
    assert user.get('data') is None
import requests
from config.config import Config
from endpoints.endpoints import Endpoints

class UsersApiClient():
    
    @staticmethod
    def _prepare_url(url, base_url=Config.BASE_URL):# Подготовка урл, базовая урла берется из конфига
        return base_url + url

    @staticmethod
    def list_users():
        return requests.get(
            url=UsersApiClient._prepare_url(Endpoints.USERS)
        ).json()

    @staticmethod
    def no_list_users():
        return requests.post(
            url=UsersApiClient._prepare_url(Endpoints.USERS)
        ).json()

    @staticmethod
    def create_user(user_details):
        return requests.post(
            url=UsersApiClient._prepare_url(Endpoints.USERS), 
            json=user_details
        ).json()

    @staticmethod
    def update_user(user_details):
        return requests.put(
            url=UsersApiClient._prepare_url(Endpoints.UPDATE_USER), 
            json=user_details
        ).json()

    @staticmethod
    def delete_user():
        return requests.put(
            url=UsersApiClient._prepare_url(Endpoints.DELETE_USER)
        ).json()

    @staticmethod
    def single_user():
        return requests.get(
            url=UsersApiClient._prepare_url(Endpoints.SINGLE_USER)
        ).json()
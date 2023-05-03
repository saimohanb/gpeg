import requests
import unittest
import pprint
pp = pprint.PrettyPrinter(indent=4)
import logging
log = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)


def post(*args, **kwargs):
    return requests.post(*args, **kwargs)


def get(*args, **kwargs):
    return requests.get(*args, **kwargs)


class Actions(unittest.TestCase):

    def successful_login(self, login_url, params):
        response = post(url=login_url, json=params)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], True)
        auth_token = response.json()['login_data'][0]['token']
        return auth_token

    def missing_cred(self, login_url):
        response = post(url=login_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["username"][0], "This field is required.")
        self.assertEqual(response.json()["password"][0], "This field is required.")

    def invalid_token(self, logout_url, invalid_token):
        headers = {'Content-Type': 'application/json', 'Authorization': f'token {invalid_token}'}
        response = get(url=logout_url, headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["detail"], "Invalid token.")

    def successful_logout(self, login_url, params, logout_url):
        auth_token = self.successful_login(login_url, params)
        headers = {'Content-Type': 'application/json', 'Authorization': f'token {auth_token}'}
        response = get(url=logout_url, headers=headers)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], True)

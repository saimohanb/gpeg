import json
from actions import Actions

with open('tc_data.json') as f:
    config = json.load(f)


def log():
    test = Actions()
    test.successful_login(login_url=config['login_url'],
                          params={"username": config['username'], "password": config['password']})
    test.successful_logout(login_url=config['login_url'],
                           params={"username": config['username'], "password": config['password']},
                           logout_url=config['logout_url'])
    test.missing_cred(login_url=config['login_url'])
    test.invalid_token(logout_url=config['logout_url'], invalid_token=config['invalid_token'])


log()

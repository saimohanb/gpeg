import requests

login_url = "http://65.2.51.31:9008/api/login/"
logout_url = "http://65.2.51.31:9008/api/logout/"
wrong_params = {
    "username": "m.roshan@giglabz.com",
    "password": "wirtual@22#"
}

post_response1 = requests.post(url=login_url, json=wrong_params)
print(f"First Post Response: {post_response1.text}\n")
# o/p: First Post Response: {"status_code":"200","status":true,"message":"logged in successfully.","login_data":[{"token":"2124b5551fca720782dc442ac5b06fd2a0d5560a","username":"m.roshan@giglabz.com","first_name":"mohammed","last_name":"roshan","email":"m.roshan@giglabz.com"}],"user_permissions":["ADD_TASK","CHANGE_TASK","DELETE_TASK","VIEW_TASK"],"user_roles":["admin"]}

post_response2 = requests.post(url=login_url)
print(f"Second Post Response: {post_response2.text}\n")  # o/p: Second Post Response: {"username":["This field is required."],"password":["This field is required."]}

get_response1 = requests.get(url=logout_url)
headers = {'Content-Type': 'application/json', 'Authorization': 'token dcd75362d5e26392ba1e747b748ad9ce6aea8d08'}
get_response2 = requests.get(url=logout_url, headers=headers)
print(f"First Get Response: {get_response1.text}\n")  # o/p: First Get Response: {"detail":"Authentication credentials were not provided."}
print(f"Second Get Response: {get_response2.text}\n")  # o/p: Second Get Response: {"status_code":"200","status":true,"message":"logout successfully."}

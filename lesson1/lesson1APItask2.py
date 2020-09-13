import requests

url = 'https://api.vk.com/method/'
get = 'friends.get'
token = '30320cae30320cae30320cae75305e26c13303230320cae6d7e406dd13fd49332ba7b09'
user_id = input("Enter the VK id number:")
params = {'user_id': user_id, 'v': 5.95, 'access_token': token}

response = requests.get(f'{url}{get}', params=params)
if response.ok:
    print(response.text)
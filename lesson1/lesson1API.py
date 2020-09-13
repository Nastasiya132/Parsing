import json
import requests


username = input("Enter the github username:")
response = requests.get('https://api.github.com/users/'+username+'/repos')

if response:
    data = response.json()
    print(response.status_code)


    with open('list_of_reps.json', 'w') as outfile:
        json.dump(data, outfile)
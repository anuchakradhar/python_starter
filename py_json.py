# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#sample JSON
userJSON = '{"first_name": "Anu", "last_name": "Chakradhar", "age": 24}'

#parse to dict
user = json.loads(userJSON)

print(user)

print(user['first_name'])

user1 = {'firstname': 'Sanu', 'last_name': 'Maya', 'age': 22}

carJSON = json.dumps(user1)

print(carJSON)
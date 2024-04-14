# JSON - java script object notation

emp_data = '''
{
    "employees": [
        {
            "name": "John",
            "age": 29,
            "emails": ["john@gmail.com", "john@outlook.com"]
        },
        {
            "name": "Jane",
            "age": 48,
            "emails": null
        }
    ]
}
'''

import json
# To load json string into a python object
json_data = json.loads(emp_data)

'''print(json_data)
print(type(json_data))
print(json_data['employees'])

for emp in json_data["employees"]:
    print(emp["name"])

# Delete the email for each employee and then load it into a json string
for emp in json_data["employees"]:
    del emp["emails"]


print(json_data)

# Convert a python object into a json string
new_string = json.dumps(json_data, indent=2)
print(new_string)
print(type(new_string))'''


# Load JSON data from a file into a python object
with open("states.json", "r") as file_obj:
    data = json.load(file_obj)

# print(data)
# print(type(data))

for state in data["states"]:
    print(state["name"], state["abbreviation"])

    # remove the area code for each state
    del state["area_codes"]

print(data["states"])

# To write json data to a file
with open("new_states.json", "w") as file_obj:
    json.dump(data, file_obj, indent=2)

# API --> Application Programming Interface
"""
Address --> user entered address 16701, recommended address 16701-1234
web application --> USPS Public API --> validate and return appropriate address
"""

"""
Fidelity Investments --> facebook page, twitter handle, linkedin
Facebook API - JSON format
posts, comments, replies, etc..
"""

# import random
#
# random.random()
# random.choice()

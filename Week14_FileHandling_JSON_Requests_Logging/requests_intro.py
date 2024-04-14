from urllib.request import urlopen
import json

with urlopen("https://dummyjson.com/users") as response:
    api_response = response.read()

# print(api_response)

data = json.loads(api_response)
# print(data)

print(json.dumps(data, indent=2))

for user in data["users"]:
    print(user["email"])

with open("user_emails.txt", "w") as email_obj:
    for user in data["users"]:
        email_obj.write(user["email"] + "\n")

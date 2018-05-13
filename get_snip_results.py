import os
import json
import requests

secret = os.environ['SNIP_JWT_SECRET']
email = os.environ['SNIP_API_EMAIL']
password = os.environ['SNIP_API_PASSWORD']
url_base = "http://ec2-35-171-7-34.compute-1.amazonaws.com:8080"

# Login and get JWT
login_res = requests.post(f"{url_base}/login", data=json.dumps(
    {"email": email, "password": password}))
assert login_res.status_code == 201
jwt_token = login_res.json()['token']

# Get JSON data!
res = requests.get(
    f"{url_base}/diseases/pathogenic",
    headers={"Authorization": jwt_token})
json_data = res.json()

# Write JSON data w/ proper indents
with open("23_and_me.json", "w") as fp:
    fp.write(json.dumps(json_data, indent=4))

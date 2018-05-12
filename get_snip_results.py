import os
import json
import requests

secret = os.environ['SNIP_JWT_SECRET']
email = "seanharr11@gmail.com"  # Your Email Here
password = "pycon2018"  # Your password here
url_base = "http://localhost:8080"

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

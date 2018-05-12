import json
import requests
import sys

secret = "pyc0n2o18-open-sp@c3"
email = "seanharr4182@gmail.com"  # Your Email Here
password = "pycon2018"  # Your password here
# url_base = "http://localhost:8080"
url_base = "http://ec2-35-171-7-34.compute-1.amazonaws.com:8080"

# Create User
res = requests.post(f"{url_base}/users", data=json.dumps(
    {"email": email, "password": password}))
assert res.status_code == 201

# Login and get JWT
login_res = requests.post(f"{url_base}/login", data=json.dumps(
    {"email": email, "password": password}))
assert login_res.status_code == 201

# Upload 23&Me Data
input_filename = sys.argv[1]
jwt_token = login_res.json()['token']
with open(input_filename, "r") as fp:
    snp_csv_data = fp.readlines()
    res = requests.post(
        f"{url_base}/upload-snps",
        headers={'Authorization': jwt_token},
        data=json.dumps(
            {"data": {
                "snp_csv": snp_csv_data}}))
    assert res.status_code == 201

# Get JSON data!
res = requests.get(
    f"{url_base}/diseases/pathogenic",
    headers={"Authorization": jwt_token})
json_data = res.json()

# Write JSON data w/ proper indents
with open("23_and_me.json", "w") as fp:
    fp.write(json.dumps(json_data, indent=4))

import requests
import json

url = "https://6rsqbadgd5jm4jj52ezggecgqu0dbnol.lambda-url.us-east-1.on.aws/"

payload = {
    # Your Email Id as it appears in the coursera instruction page.
    "submitterEmail": 'tyy2@illinois.edu',
    # Your token as it appears in the coursera instruction page. This token will only be valid for 30 mins.
    "secret": 'etWr94TCxpGHB6rx',
    # Public IPv4 address which you can find on the EC2 instance home page. Add port number on which your server is running.
    "ipaddress": 'ec2-23-20-48-177.compute-1.amazonaws.com:5000'
}


print("Running the autograder. This might take several seconds...")

r = requests.post(url, data=json.dumps(payload), headers={
                  "Content-Type": "application/json"})

print(r.status_code, r.reason)
print(r.text)

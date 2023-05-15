import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
    'ip_address1':  "18.206.99.196:80",
    'ip_address2':  "100.24.27.52:80",
    'load_balancer':  "lb-838430069.us-east-1.elb.amazonaws.com",
    'submitterEmail':  "tyy2@illinois.edu",
    'secret':  "ImZF27ZNJhXeWQRr"
}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)

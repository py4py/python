import requests

URL = 'http://127.0.0.1:5000/get_users'
PAYLOAD = {}
HEADER = {'content-type' : 'application/json', 
                'accept' : 'application/json'
        }
    
r = requests.post(URL, data=PAYLOAD, headers=HEADER)

print(r.status_code)
print(r.text)
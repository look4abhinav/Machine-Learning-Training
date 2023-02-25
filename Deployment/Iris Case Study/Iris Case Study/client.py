import requests
import json
url="http://localhost:8111/api"
data=json.dumps({'sl':1.2,'sw':3.3,'pl':3.5,'pw':3.1})
r=requests.post(url,data)
print(r.json())

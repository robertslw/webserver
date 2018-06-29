import requests
import json

urlHVAC = "http://localhost:5003/tod/api/v1.0/Aggregatorall"
reqHeader = { "Content-Type":"application/json", "Accept":"application/json","Authorization":""}

r = requests.get(urlHVAC,headers=reqHeader)
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json)



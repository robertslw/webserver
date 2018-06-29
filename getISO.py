import requests
import json

urlHVAC = "http://localhost:5001/tod/api/v1.0/ISO"
reqHeader = { "Content-Type":"application/json", "Accept":"application/json","Authorization":"101"}

r = requests.get(urlHVAC,headers=reqHeader)
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json)



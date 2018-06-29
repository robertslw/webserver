import requests
import json

urlHVAC = "http://localhost:5000/tod/api/v1.0/HVAC"
urlWH = "http://localhost:5000/tod/api/v1.0/WH"
urlES = "http://localhost:5000/tod/api/v1.0/ES"
urlSolar = "http://localhost:5000/tod/api/v1.0/Solar"
reqHeaderHVAC = { "Content-Type":"application/json", "Accept":"application/json","Authorization":"100"}
reqHeaderWH = { "Content-Type":"application/json", "Accept":"application/json","Authorization":"200"}
reqHeaderES = { "Content-Type":"application/json", "Accept":"application/json","Authorization":"300"}
reqHeaderSolar = { "Content-Type":"application/json", "Accept":"application/json","Authorization":"400"}

r = requests.get(urlHVAC,headers=reqHeaderHVAC)
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json)

r = requests.get(urlWH,headers=reqHeaderWH)
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json)

r = requests.get(urlES,headers=reqHeaderES)
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json)

r = requests.get(urlSolar,headers=reqHeaderSolar)
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json)



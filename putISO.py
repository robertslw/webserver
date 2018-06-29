import requests
import json
import time

payload = { "UtilityID": "232",
    "PredictedLoad": {
        "Hour1": "1",
        "Hour2": "2",
        "Hour3": "3",
        "Hour4": "4",
        "Hour5": "5",
        "Hour6": "6",
        "Hour7": "7",
        "Hour8": "8",
        "Hour9": "9",
        "Hour10": "10",
        "Hour11": "11",
        "Hour12": "12",
        "Hour13": "13",
        "Hour14": "14",
        "Hour15": "15",
        "Hour16": "16",
        "Hour17": "17",
        "Hour18": "18",
        "Hour19": "19",
        "Hour20": "20",
        "Hour21": "21",
        "Hour22": "22",
        "Hour23": "23",
        "Hour24": "24"
        }
    }

urlISO = "http://localhost:5001/tod/api/v1.0/ISO"
reqHeader = { "Content-Type":"application/json", "Accept":"application/json","Authorization":"232"}
for UtilityID in range(100,200):
    time.sleep(1)
    print(UtilityID)
    payload["UtilityID"]=str(UtilityID)
    reqHeader["Authorization"]=str(UtilityID)
    r = requests.put(urlISO,headers=reqHeader,data=json.dumps(payload))
    print(r.status_code)




import requests
import json
import time

payloadHVAC = { "DeviceID": "",
   "DeviceType":"HVAC",
   "DeviceConfiguration": "Config1", 
    "HVAC": {
      "SingleSpeed": {
        "Control": {
          "Mode": "Heat", 
          "Schedule": {
            "Cool": {
              "TemperatureScheduleCool1": "1", 
              "TemperatureScheduleCool2": "2", 
              "TemperatureScheduleCool3": "3", 
              "TemperatureScheduleCool4": "4", 
              "TimeScheduleCool1": "1", 
              "TimeScheduleCool2": "2", 
              "TimeScheduleCool3": "3", 
              "TimeScheduleCool4": "4"
            }, 
            "Heat": {
              "TemperatureScheduleHeat1": "1", 
              "TemperatureScheduleHeat2": "2", 
              "TemperatureScheduleHeat3": "3", 
              "TemperatureScheduleHeat4": "4", 
              "TimeScheduleHeat1": "1", 
              "TimeScheduleHeat2": "2", 
              "TimeScheduleHeat3": "3", 
              "TimeScheduleHeat4": "4"
            }
          }, 
          "Setpoints": {
            "Cool": {
              "TempeatureSetpointF": "80"
            }, 
            "Heat": {
              "TempeatureSetpointF": "50"
            }
          }
        }, 
        "Status": {
          "Measurements": {
            "IndoorTempF": "75", 
            "OutdoorTempF": "90"
          }, 
          "Mode": "Cool"
        }
      }
    }
  }

payloadWH = { "DeviceID": "",
    "DeviceType":"WH",
    "DeviceConfiguration":"Config2",
    "WH":{
      "Heatpump":{
        "Control":{
          "Schedule":{
            "Heat":{
              "TimeScheduleHeat1":"1",
              "TemperatureScheduleHeat1":"2",
              "TimeScheduleHeat2":"3",
              "TemperatureScheduleHeat2":"4",
              "TimeScheduleHeat3":"5",
              "TemperatureScheduleHeat3":"6",
              "TimeScheduleHeat4":"7",
              "TemperatureScheduleHeat4":"8"
              }
            },
          "Setpoints":{
            "Heat":{
              "TempeatureSetpointF":"60"
              }
            },
          "Mode":"Mode1"
          },
        "Status":{
          "Measurements":{
            "UpperTankTemp":"50",
            "LowerTankTemp":"50",
            "ExteriorTankTemp":"50",
            },
          "Mode":"Mode2"
          }
        }
      }
    }


payloadES = { "DeviceID": "",
    "DeviceType":"ES",
    "DeviceConfiguration":"Config3",
    "ES":{
    "HomeSystem":{
      "Configuration":{
        "Chemistry":"Chemistry",
        "Capacity":"10",
        "SOCMax":"11",
        "SOCMin":"12",
        "PowerRating":"13"
        },
      "Control":{			
        "Setpoints":{
          "RealPower":"14"
          },
        "Mode":"Mode3"
        },
      "Status":{
        "Measurements":{
          "DCVoltage":"DC1",
          "ACVoltage":"AC1",
          "RealPower":"15",
          "SOC":"16"
          },
        "Mode":"Mode3"
        }
      }
    }
  }


payloadSolar = { "DeviceID": "",
    "DeviceType":"Solar",
    "DeviceConfiguration":"Config4",
    "Solar":{
      "PV":{
        "Configuration":{
          "RatedPower":"17"
          },
        "Control":{			
          "Capacity":"18"
          },
        "Status":{
          "Forecast":{
            "RealPowerHour1":"1",
            "RealPowerHour2":"2",
            "RealPowerHour3":"3",
            "RealPowerHour4":"4",
            "RealPowerHour5":"5",
            "RealPowerHour6":"6",
            "RealPowerHour7":"7",
            "RealPowerHour8":"8",
            "RealPowerHour9":"9",
            "RealPowerHour10":"10",
            "RealPowerHour11":"11",
            "RealPowerHour12":"12",
            "RealPowerHour13":"13",
            "RealPowerHour14":"14",
            "RealPowerHour15":"15",
            "RealPowerHour16":"16",
            "RealPowerHour17":"17",
            "RealPowerHour18":"18",
            "RealPowerHour19":"19",
            "RealPowerHour20":"20",
            "RealPowerHour21":"21",
            "RealPowerHour22":"22",
            "RealPowerHour23":"23",
            "RealPowerHour24":"24",
            },
          "Measurements":{
            "RealPower":"19"
            },
          "Mode":"Mode4"
          }
        }
      }
    }




urlHVAC = "http://localhost:5000/tod/api/v1.0/HVAC"
urlWH = "http://localhost:5000/tod/api/v1.0/WH"
urlES = "http://localhost:5000/tod/api/v1.0/ES"
urlSolar = "http://localhost:5000/tod/api/v1.0/Solar"
reqHeaderHVAC = { "Content-Type":"application/json", "Accept":"application/json","Authorization":""}
reqHeaderWH = { "Content-Type":"application/json", "Accept":"application/json","Authorization":""}
reqHeaderES = { "Content-Type":"application/json", "Accept":"application/json","Authorization":""}
reqHeaderSolar = { "Content-Type":"application/json", "Accept":"application/json","Authorization":""}
for DeviceID in range(100,200):
    time.sleep(1)
    print(DeviceID)
    payloadHVAC["DeviceID"]=str(DeviceID)
    payloadWH["DeviceID"]=str(DeviceID+100)
    payloadES["DeviceID"]=str(DeviceID+200)
    payloadSolar["DeviceID"]=str(DeviceID+300)
    reqHeaderHVAC["Authorization"]=str(DeviceID)
    reqHeaderWH["Authorization"]=str(DeviceID+100)
    reqHeaderES["Authorization"]=str(DeviceID+200)
    reqHeaderSolar["Authorization"]=str(DeviceID+300)
    r1 = requests.put(urlHVAC,headers=reqHeaderHVAC,data=json.dumps(payloadHVAC))
    print(r1.status_code)
    r2 = requests.put(urlWH,headers=reqHeaderWH,data=json.dumps(payloadWH))
    print(r2.status_code)
    r3 = requests.put(urlES,headers=reqHeaderES,data=json.dumps(payloadES))
    print(r3.status_code)
    r4 = requests.put(urlSolar,headers=reqHeaderSolar,data=json.dumps(payloadSolar))
    print(r4.status_code)

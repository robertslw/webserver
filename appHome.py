 #!flask/bin/python
from flask import Flask, jsonify, request
import json

"""
import sys
import requests
import datetime
import logging

import time
import urllib
import json
import os
from pprint import pprint
from Tkinter import *
from time import sleep
import threading
import random
import socket
import math
import httplib, urllib, base64
"""

app = Flask(__name__)


class ESConfiguration():
	def __init__(self):
		self.Chemistry = ""
		self.Capacity = ""
		self.SOCMax = ""
		self.SOCMin = ""
		self.PowerRating = ""

class PVConfiguration():
	def __init__(self):
		self.RatedPower = ""

class HVACSetpoints():
	def __init__(self):
		self.HeatTemp = ""
		self.CoolTemp = ""

class WHSetpoints():
	def __init__(self):
		self.HeatTemp = ""

class ESSetpoints():
	def __init__(self):
		self.RealPower = ""

class HVACSchedule():
	def __init__(self):
		self.HeatTime = ["","","",""]
		self.HeatTemp = ["","","",""]
		self.CoolTime = ["","","",""]
		self.CoolTemp = ["","","",""]

class WHSchedule():
	def __init__(self):
		self.HeatTime = ["","","",""]
		self.HeatTemp = ["","","",""]

class HVACControl():
	def __init__(self):
		self.Schedule = HVACSchedule()
		self.Setpoints = HVACSetpoints()
		self.Mode = ""

class WHControl():
	def __init__(self):
		self.Schedule = WHSchedule()
		self.Setpoints = WHSetpoints()
		self.Mode = ""

class ESControl():
	def __init__(self):
		self.Setpoints = ESSetpoints()
		self.Mode = ""

class PVControl():
	def __init__(self):
		self.Capacity = ""

class HVACMeasurements():
	def __init__(self):
		self.IndoorTemp = ""
		self.OutdoorTemp = ""

class WHMeasurements():
	def __init__(self):
		self.UpperTemp = ""
		self.LowerTemp = ""
		self.ExteriorTemp = ""

class ESMeasurements():
	def __init__(self):
		self.DCVoltage = ""
		self.ACVoltage = ""
		self.RealPower = ""
		self.SOC = ""

class PVMeasurements():
	def __init__(self):
		self.RealPower = ""

class PVForecast():
	def __init__(self):
		self.Power = ["","","","","","","","","","","","","","","","","","","","","","","",""]

class HVACStatus():
	def __init__(self):
		self.Measurements = HVACMeasurements()
		self.Mode = ""

class WHStatus():
	def __init__(self):
		self.Measurements = WHMeasurements()
		self.Mode = ""

class ESStatus():
	def __init__(self):
		self.Measurements = ESMeasurements()
		self.Mode = ""

class PVStatus():
	def __init__(self):
		self.Measurement = PVMeasurements()
		self.Forecast = PVForecast()
		self.Mode = ""

class SingleSpeed():
	def __init__(self):
		self.Control = HVACControl()
		self.Status = HVACStatus()


class Heatpump():
	def __init__(self):
		self.Control = WHControl()
		self.Status = WHStatus()

class HomeSystem():
	def __init__(self):
		self.Configuration = ESConfiguration()		
		self.Control = ESControl()
		self.Status = ESStatus()

class PV():
	def __init__(self):
		self.Configuration = PVConfiguration()		
		self.Control = PVControl()
		self.Status = PVStatus()

class HVAC():
	def __init__(self):
		self.Configuration = ''
		self.SingleSpeed = SingleSpeed()

class WH():
	def __init__(self):
		self.Configuration = ''
		self.Heatpump = Heatpump()

class ES():
	def __init__(self):
		self.Configuration = ''
		self.HomeSystem = HomeSystem()

class Solar():
	def __init__(self):
		self.Configuration = ''
		self.PV = PV()

class Device():
	def __init__(self):
		self.ID = ''
		self.DeviceType = ''
		self.HVAC = HVAC()
		self.WH = WH()
		self.ES = ES()
		self.Solar = Solar()
	

Devices = []
Devices.append(Device())
devicenumber = 0
webmasternumber = 1	
API = {}
DeviceAPI = {}

############# Function for adding new devices ###############
def New_Device():
	global DeviceAPI
	Devices.append(Device())
	#DeviceAPI[devicenumber] = {'DeviceID':Devices[devicenumber].ID}

############# PROVIDES WEB MASTER ACCESS TO SYSTEM ###############
def get_ID():
	return jsonify({'System':DeviceAPI})

def defineHVACAPI(i):
		global API
		API = {'DeviceID':Devices[i].ID,
			'DeviceType':Devices[i].DeviceType,
			'DeviceConfiguration':Devices[i].HVAC.Configuration,
			'HVAC':{
					'SingleSpeed':{
								'Control':{
										'Schedule':{
												'Heat':{
														'TimeScheduleHeat1':Devices[i].HVAC.SingleSpeed.Control.Schedule.HeatTime[0],
														'TemperatureScheduleHeat1':Devices[i].HVAC.SingleSpeed.Control.Schedule.HeatTemp[0],
														'TimeScheduleHeat2':Devices[i].HVAC.SingleSpeed.Control.Schedule.HeatTime[1],
														'TemperatureScheduleHeat2':Devices[i].HVAC.SingleSpeed.Control.Schedule.HeatTemp[1],
														'TimeScheduleHeat3':Devices[i].HVAC.SingleSpeed.Control.Schedule.HeatTime[2],
														'TemperatureScheduleHeat3':Devices[i].HVAC.SingleSpeed.Control.Schedule.HeatTemp[2],
														'TimeScheduleHeat4':Devices[i].HVAC.SingleSpeed.Control.Schedule.HeatTime[3],
														'TemperatureScheduleHeat4':Devices[i].HVAC.SingleSpeed.Control.Schedule.HeatTemp[3]
														},
												'Cool':{
														'TimeScheduleCool1':Devices[i].HVAC.SingleSpeed.Control.Schedule.CoolTime[0],
														'TemperatureScheduleCool1':Devices[i].HVAC.SingleSpeed.Control.Schedule.CoolTemp[0],
														'TimeScheduleCool2':Devices[i].HVAC.SingleSpeed.Control.Schedule.CoolTime[1],
														'TemperatureScheduleCool2':Devices[i].HVAC.SingleSpeed.Control.Schedule.CoolTemp[1],
														'TimeScheduleCool3':Devices[i].HVAC.SingleSpeed.Control.Schedule.CoolTime[2],
														'TemperatureScheduleCool3':Devices[i].HVAC.SingleSpeed.Control.Schedule.CoolTemp[2],
														'TimeScheduleCool4':Devices[i].HVAC.SingleSpeed.Control.Schedule.CoolTime[3],
														'TemperatureScheduleCool4':Devices[i].HVAC.SingleSpeed.Control.Schedule.CoolTemp[3]
														}
													},
										'Setpoints':{
												'Heat':{
													'TempeatureSetpointF':Devices[i].HVAC.SingleSpeed.Control.Setpoints.HeatTemp
														},
												'Cool':{
													'TempeatureSetpointF':Devices[i].HVAC.SingleSpeed.Control.Setpoints.CoolTemp
														}
													},
												
										'Mode':Devices[i].HVAC.SingleSpeed.Control.Mode
													
											},
								'Status':{
										'Measurements':{
														'IndoorTempF':Devices[i].HVAC.SingleSpeed.Status.Measurements.IndoorTemp,
														'OutdoorTempF':Devices[i].HVAC.SingleSpeed.Status.Measurements.OutdoorTemp
														},
										'Mode':Devices[i].HVAC.SingleSpeed.Status.Mode
									}
						}
				
					}					
		}
		
		#print API[i]
		return API

#######################################################################################################

#######################################################################################################

def defineWHAPI(i):
		global API
		API = {'DeviceID':Devices[i].ID,
			'DeviceType':Devices[i].DeviceType,
			'DeviceConfiguration':Devices[i].WH.Configuration,
			'WH':{
					'Heatpump':{
								'Control':{
										'Schedule':{
												'Heat':{
														'TimeScheduleHeat1':Devices[i].WH.Heatpump.Control.Schedule.HeatTime[0],
														'TemperatureScheduleHeat1':Devices[i].WH.Heatpump.Control.Schedule.HeatTemp[0],
														'TimeScheduleHeat2':Devices[i].WH.Heatpump.Control.Schedule.HeatTime[1],
														'TemperatureScheduleHeat2':Devices[i].WH.Heatpump.Control.Schedule.HeatTemp[1],
														'TimeScheduleHeat3':Devices[i].WH.Heatpump.Control.Schedule.HeatTime[2],
														'TemperatureScheduleHeat3':Devices[i].WH.Heatpump.Control.Schedule.HeatTemp[2],
														'TimeScheduleHeat4':Devices[i].WH.Heatpump.Control.Schedule.HeatTime[3],
														'TemperatureScheduleHeat4':Devices[i].WH.Heatpump.Control.Schedule.HeatTemp[3]
														}
										
													},
										'Setpoints':{
												'Heat':{
													'TempeatureSetpointF':Devices[i].WH.Heatpump.Control.Setpoints.HeatTemp
														}
													},
												
										'Mode':Devices[i].WH.Heatpump.Control.Mode
													
											},
								
								'Status':{
										'Measurements':{
														'UpperTankTemp':Devices[i].WH.Heatpump.Status.Measurements.UpperTemp,
														'LowerTankTemp':Devices[i].WH.Heatpump.Status.Measurements.LowerTemp,
														'ExteriorTankTemp':Devices[i].WH.Heatpump.Status.Measurements.ExteriorTemp
														},
										'Mode':Devices[i].WH.Heatpump.Status.Mode
									}
							}
				
					}					
		}
		
		#print API[i]
		return API

#######################################################################################################

#######################################################################################################

def defineESAPI(i):
		global API
		API = {'DeviceID':Devices[i].ID,
			'DeviceType':Devices[i].DeviceType,
			'DeviceConfiguration':Devices[i].ES.Configuration,
			'ES':{
				'HomeSystem':{
						'Configuration':{
										'Chemistry':Devices[i].ES.HomeSystem.Configuration.Chemistry,
										'Capacity':Devices[i].ES.HomeSystem.Configuration.Capacity,
										'SOCMax':Devices[i].ES.HomeSystem.Configuration.SOCMax,
										'SOCMin':Devices[i].ES.HomeSystem.Configuration.SOCMin,
										'PowerRating':Devices[i].ES.HomeSystem.Configuration.PowerRating
										},
						'Control':	{			
									'Setpoints':{
											'RealPower':Devices[i].ES.HomeSystem.Control.Setpoints.RealPower
												},
									'Mode':Devices[i].ES.HomeSystem.Control.Mode
									},
								
						'Status':{
								'Measurements':{
												'DCVoltage':Devices[i].ES.HomeSystem.Status.Measurements.DCVoltage,
												'ACVoltage':Devices[i].ES.HomeSystem.Status.Measurements.ACVoltage,
												'RealPower':Devices[i].ES.HomeSystem.Status.Measurements.RealPower,
												'SOC':Devices[i].ES.HomeSystem.Status.Measurements.SOC
												},
								'Mode':Devices[i].ES.HomeSystem.Status.Mode
									
								}
				
							}
					}					
				}

		return API

#######################################################################################################

#######################################################################################################

def defineSolarAPI(i):
		global API
		API = {'DeviceID':Devices[i].ID,
			'DeviceType':Devices[i].DeviceType,
			'DeviceConfiguration':Devices[i].Solar.Configuration,
			'Solar':{
					'PV':{
						'Configuration':{
										'RatedPower':Devices[i].Solar.PV.Configuration.RatedPower,
										},
						'Control':	{			
									'Capacity':Devices[i].Solar.PV.Control.Capacity
									},
								
						'Status':	{
									'Forecast':	{
												'RealPowerHour1':Devices[i].Solar.PV.Status.Forecast.Power[0],
												'RealPowerHour2':Devices[i].Solar.PV.Status.Forecast.Power[1],
												'RealPowerHour3':Devices[i].Solar.PV.Status.Forecast.Power[2],
												'RealPowerHour4':Devices[i].Solar.PV.Status.Forecast.Power[3],
												'RealPowerHour5':Devices[i].Solar.PV.Status.Forecast.Power[4],
												'RealPowerHour6':Devices[i].Solar.PV.Status.Forecast.Power[5],
												'RealPowerHour7':Devices[i].Solar.PV.Status.Forecast.Power[6],
												'RealPowerHour8':Devices[i].Solar.PV.Status.Forecast.Power[7],
												'RealPowerHour9':Devices[i].Solar.PV.Status.Forecast.Power[8],
												'RealPowerHour10':Devices[i].Solar.PV.Status.Forecast.Power[9],
												'RealPowerHour11':Devices[i].Solar.PV.Status.Forecast.Power[10],
												'RealPowerHour12':Devices[i].Solar.PV.Status.Forecast.Power[11],
												'RealPowerHour13':Devices[i].Solar.PV.Status.Forecast.Power[12],
												'RealPowerHour14':Devices[i].Solar.PV.Status.Forecast.Power[13],
												'RealPowerHour15':Devices[i].Solar.PV.Status.Forecast.Power[14],
												'RealPowerHour16':Devices[i].Solar.PV.Status.Forecast.Power[15],
												'RealPowerHour17':Devices[i].Solar.PV.Status.Forecast.Power[16],
												'RealPowerHour18':Devices[i].Solar.PV.Status.Forecast.Power[17],
												'RealPowerHour19':Devices[i].Solar.PV.Status.Forecast.Power[18],
												'RealPowerHour20':Devices[i].Solar.PV.Status.Forecast.Power[19],
												'RealPowerHour21':Devices[i].Solar.PV.Status.Forecast.Power[20],
												'RealPowerHour22':Devices[i].Solar.PV.Status.Forecast.Power[21],
												'RealPowerHour23':Devices[i].Solar.PV.Status.Forecast.Power[22],
												'RealPowerHour24':Devices[i].Solar.PV.Status.Forecast.Power[23]
												},

									'Measurements':{
													'RealPower':Devices[i].Solar.PV.Status.Measurement.RealPower
													},
									'Mode':Devices[i].Solar.PV.Status.Mode
									
									}
				
							}	
						}				
				}

		return API

#######################################################################################################

#######################################################################################################

def get_data_HVAC():
	global API
	global Devices

	response = request.headers


	for i in range(0,len(Devices)):
		#print Devices[i].ID
		#print response['Authorization']
		if str(Devices[i].ID) == str(response['Authorization']):
			API = defineHVACAPI(i)
	return jsonify({'HVAC':API})

#######################################################################################################

#######################################################################################################

def get_data_WH():
	global API
	global Devices

	response = request.headers

	for i in range(0,len(Devices)):
		#print Devices[i].ID
		#print response['Authorization']
		if str(Devices[i].ID) == str(response['Authorization']):
			API = defineWHAPI(i)
	return jsonify({'WH':API})

#######################################################################################################

#######################################################################################################

def get_data_ES():
	global API
	global Devices

	response = request.headers

	for i in range(0,len(Devices)):
		#print Devices[i].ID
		#print response['Authorization']
		if str(Devices[i].ID) == str(response['Authorization']):
			API = defineESAPI(i)
	return jsonify({'ES':API})


#######################################################################################################

#######################################################################################################


def get_data_Solar():
	global API
	global Devices

	response = request.headers

	for i in range(0,len(Devices)):
		#print Devices[i].ID
		#print response['Authorization']
		if str(Devices[i].ID) == str(response['Authorization']):
			API = defineSolarAPI(i)
	return jsonify({'Solar':API})

#######################################################################################################

#######################################################################################################

def put_data_HVAC():
	global API
	global Devices
	global devicenumber
	
	response = request.data
	data = json.loads(response)

 
	try:
		# set deviceID to what device is pushed to API
		deviceID = data['DeviceID']

		# initialize usedeviceID
		usedeviceID = ''

		# search device ID within listing of devicIDs
		for i in range(0,len(Devices)):
			if deviceID == Devices[i].ID:
				# if deviceID is found, hold that number
				usedeviceID = deviceID
				holdnumber = i

		# if usedeviceID is still intitialized, no deviceID was found in list
		# add new device to Devices and use hold number 
		if usedeviceID == '':
			Devices[devicenumber].ID = deviceID
			New_Device()
			usedeviceID = deviceID
			holdnumber = devicenumber
			devicenumber = devicenumber + 1

		print('DeviceID:' + deviceID)

		print('All Device list:')
		for i in range(0,len(Devices)):
			print(Devices[i].ID)

	except Exception as e:
		print('%%%%%%%%%%%%%%%%%% ERROR IN JSON PUT HVAC %%%%%%%%%%%%%%')
		print (e)
		#exc_type, exc_obj, exc_tb = sys.exc_info()
		#fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		#print(exc_type,fname,exc_tbl.tb_lineno)


	########################### STATUS ##############################
	try:
		try:
			Devices[holdnumber].ID = data['DeviceID']
		except:
			pass

		try:
			Devices[holdnumber].DeviceType = data['DeviceType']
		except:
			pass

		try:
			Devices[holdnumber].HVAC.Configuration = data['DeviceConfiguration']
		except:
			pass

		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.HeatTime[0]= data['HVAC']['SingleSpeed']['Control']['Schedule']['Heat']['TimeScheduleHeat1']
		except:
			pass

		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.HeatTime[1]= data['HVAC']['SingleSpeed']['Control']['Schedule']['Heat']['TimeScheduleHeat2']
		except:
			pass

		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.HeatTime[2] = data['HVAC']['SingleSpeed']['Control']['Schedule']['Heat']['TimeScheduleHeat3']
		except:
			pass
		
		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.HeatTime[3] = data['HVAC']['SingleSpeed']['Control']['Schedule']['Heat']['TimeScheduleHeat4']
		except:
			pass
		
		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.HeatTemp[0]= data['HVAC']['SingleSpeed']['Control']['Schedule']['Heat']['TemperatureScheduleHeat1']
		except:
			pass
		
		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.HeatTemp[1]= data['HVAC']['SingleSpeed']['Control']['Schedule']['Heat']['TemperatureScheduleHeat2']
		except:
			pass
		
		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.HeatTemp[2]= data['HVAC']['SingleSpeed']['Control']['Schedule']['Heat']['TemperatureScheduleHeat3']
		except:
			pass
		
		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.HeatTemp[3] = data['HVAC']['SingleSpeed']['Control']['Schedule']['Heat']['TemperatureScheduleHeat4']
		except:
			pass

		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.CoolTime[0]= data['HVAC']['SingleSpeed']['Control']['Schedule']['Cool']['TimeScheduleCool1']
		except:
			pass
		
		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.CoolTime[1]= data['HVAC']['SingleSpeed']['Control']['Schedule']['Cool']['TimeScheduleCool2']
		except:
			pass
		
		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.CoolTime[2] = data['HVAC']['SingleSpeed']['Control']['Schedule']['Cool']['TimeScheduleCool3']
		except:
			pass
		
		try: 
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.CoolTime[3]= data['HVAC']['SingleSpeed']['Control']['Schedule']['Cool']['TimeScheduleCool4']
		except:
			pass
		
		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.CoolTemp[0]= data['HVAC']['SingleSpeed']['Control']['Schedule']['Cool']['TemperatureScheduleCool1']
		except:
			pass
		
		try: 
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.CoolTemp[1]= data['HVAC']['SingleSpeed']['Control']['Schedule']['Cool']['TemperatureScheduleCool2']
		except:
			pass
		
		try:
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.CoolTemp[2]= data['HVAC']['SingleSpeed']['Control']['Schedule']['Cool']['TemperatureScheduleCool3']
		except:
			pass
		
		try: 
			Devices[holdnumber].HVAC.SingleSpeed.Control.Schedule.CoolTemp[3] = data['HVAC']['SingleSpeed']['Control']['Schedule']['Cool']['TemperatureScheduleCool4']
		except:
			pass


		try: 
			Devices[holdnumber].HVAC.SingleSpeed.Control.Setpoints.CoolTemp= data['HVAC']['SingleSpeed']['Control']['Setpoints']['Cool']['TempeatureSetpointF']
		except:
			pass

		
		try: 
			Devices[holdnumber].HVAC.SingleSpeed.Control.Setpoints.HeatTemp= data['HVAC']['SingleSpeed']['Control']['Setpoints']['Heat']['TempeatureSetpointF']
		except:
			pass

		try: 
			Devices[holdnumber].HVAC.SingleSpeed.Control.Mode = data['HVAC']['SingleSpeed']['Control']['Mode']
		except:
			pass

		try: 
			Devices[holdnumber].HVAC.SingleSpeed.Status.Measurements.IndoorTemp = data['HVAC']['SingleSpeed']['Status']['Measurements']['IndoorTempF']
		except:
			pass

		try: 
			Devices[holdnumber].HVAC.SingleSpeed.Status.Measurements.OutdoorTemp = data['HVAC']['SingleSpeed']['Status']['Measurements']['OutdoorTempF']
		except:
			pass

		try: 
			Devices[holdnumber].HVAC.SingleSpeed.Status.Mode = data['HVAC']['SingleSpeed']['Status']['Mode']
		except:
			pass

		return '200'
	except:
		print('ERROR IN API CALL')
		return '500'
#######################################################################################################

#######################################################################################################

def put_data_WH():
	global API
	global Devices
	global devicenumber

	response = request.data
	data = json.loads(response)

	try:
		# set deviceID to what device is pushed to API
		deviceID = data['DeviceID']

		# initialize usedeviceID
		usedeviceID = ''

		# search device ID within listing of devicIDs
		for i in range(0,len(Devices)):
			if deviceID == Devices[i].ID:
				# if deviceID is found, hold that number
				usedeviceID = deviceID
				holdnumber = i

		# if usedeviceID is still intitialized, no deviceID was found in list
		# add new device to Devices and use hold number 
		if usedeviceID == '':
			Devices[devicenumber].ID = deviceID
			New_Device()
			usedeviceID = deviceID
			holdnumber = devicenumber
			devicenumber = devicenumber + 1

		print('DeviceID:' + deviceID)
		

		print('All Device list:')
		for i in range(0,len(Devices)):
			print(Devices[i].ID)

	except Exception as e:
		print ('%%%%%%%%%%%%%%%%%% ERROR IN JSON PUT WH %%%%%%%%%%%%%%')
		print (e)
		#exc_type, exc_obj, exc_tb = sys.exc_info()
		#fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		#print(exc_type,fname,exc_tbl.tb_lineno)



	########################### STATUS ##############################
	try:
		try:
			Devices[holdnumber].ID = data['DeviceID']
		except:
			pass

		try:
			Devices[holdnumber].DeviceType = data['DeviceType']
		except:
			pass

		try:
			Devices[holdnumber].WH.Configuration = data['DeviceConfiguration']
		except:
			pass

		try:
			Devices[holdnumber].WH.Heatpump.Control.Schedule.HeatTime[0] = data['WH']['Heatpump']['Control']['Schedule']['Heat']['TimeScheduleHeat1']
		except:
			pass

		try:
			Devices[holdnumber].WH.Heatpump.Control.Schedule.HeatTime[1]= data['WH']['Heatpump']['Control']['Schedule']['Heat']['TimeScheduleHeat2']
		except:
			pass

		try:
			Devices[holdnumber].WH.Heatpump.Control.Schedule.HeatTime[2] = data['WH']['Heatpump']['Control']['Schedule']['Heat']['TimeScheduleHeat3']
		except:
			pass
		
		try:
			Devices[holdnumber].WH.Heatpump.Control.Schedule.HeatTime[3] = data['WH']['Heatpump']['Control']['Schedule']['Heat']['TimeScheduleHeat4']
		except:
			pass
		
		try:
			Devices[holdnumber].WH.Heatpump.Control.Schedule.HeatTemp[0]= data['WH']['Heatpump']['Control']['Schedule']['Heat']['TemperatureScheduleHeat1']
		except:
			pass
		
		try:
			Devices[holdnumber].WH.Heatpump.Control.Schedule.HeatTemp[1]= data['WH']['Heatpump']['Control']['Schedule']['Heat']['TemperatureScheduleHeat2']
		except:
			pass
		
		try:
			Devices[holdnumber].WH.Heatpump.Control.Schedule.HeatTemp[2]= data['WH']['Heatpump']['Control']['Schedule']['Heat']['TemperatureScheduleHeat3']
		except:
			pass
		
		try:
			Devices[holdnumber].WH.Heatpump.Control.Schedule.HeatTemp[3] = data['WH']['Heatpump']['Control']['Schedule']['Heat']['TemperatureScheduleHeat4']
		except:
			pass
		
		try:
			Devices[holdnumber].WH.Heatpump.Control.Setpoints.HeatTemp= data['WH']['Heatpump']['Control']['Setpoints']['Heat']['TempeatureSetpointF']
		except:
			pass
		
		try:
			Devices[holdnumber].WH.Heatpump.Control.Mode = data['WH']['Heatpump']['Control']['Mode']
		except:
			pass
		
		try:
			Devices[holdnumber].WH.Heatpump.Status.Measurements.UpperTemp = data['WH']['Heatpump']['Status']['Measurements']['UpperTankTemp']
		except:
			pass
		
		try:
			Devices[holdnumber].WH.Heatpump.Status.Measurements.LowerTemp = data['WH']['Heatpump']['Status']['Measurements']['LowerTankTemp']
		except:
			pass
		
		try:
			Devices[holdnumber].WH.Heatpump.Status.Measurements.ExteriorTemp = data['WH']['Heatpump']['Status']['Measurements']['ExteriorTankTemp']
		except:
			pass
		
		try:
			Devices[holdnumber].WH.Heatpump.Status.Mode = data['WH']['Heatpump']['Status']['Mode']
		except:
			pass

		return '200'
	except:
		print('ERROR IN API CALL')
		return '500'

#######################################################################################################

#######################################################################################################

def put_data_ES():
	global API
	global Devices
	global devicenumber

	response = request.data
	data = json.loads(response)

	try:
		# set deviceID to what device is pushed to API
		deviceID = data['DeviceID']

		# initialize usedeviceID
		usedeviceID = ''

		# search device ID within listing of devicIDs
		for i in range(0,len(Devices)):
			if deviceID == Devices[i].ID:
				# if deviceID is found, hold that number
				usedeviceID = deviceID
				holdnumber = i

		# if usedeviceID is still intitialized, no deviceID was found in list
		# add new device to Devices and use hold number 
		if usedeviceID == '':
			Devices[devicenumber].ID = deviceID
			New_Device()
			usedeviceID = deviceID
			holdnumber = devicenumber
			devicenumber = devicenumber + 1

		print('DeviceID:' + deviceID)

		print('All Device list:')
		for i in range(0,len(Devices)):
			print(Devices[i].ID)

	except Exception as e:
		print('%%%%%%%%%%%%%%%%%% ERROR IN JSON PUT WH %%%%%%%%%%%%%%')
		print (e)
		#exc_type, exc_obj, exc_tb = sys.exc_info()
		#fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		#print(exc_type,fname,exc_tbl.tb_lineno)



	########################### STATUS ##############################
	try:
		try:
			Devices[holdnumber].ID = data['DeviceID']
		except:
			pass

		try:
			Devices[holdnumber].DeviceType = data['DeviceType']
		except:
			pass

		try:
			Devices[holdnumber].ES.Configuration = data['DeviceConfiguration']
		except:
			pass

		try:
			Devices[holdnumber].ES.HomeSystem.Configuration.Chemistry = data['ES']['HomeSystem']['Configuration']['Chemistry']
		except:
			pass

		try:
			Devices[holdnumber].ES.HomeSystem.Configuration.Capacity = data['ES']['HomeSystem']['Configuration']['Capacity']
		except:
			pass

		try:
			Devices[holdnumber].ES.HomeSystem.Configuration.SOCMax = data['ES']['HomeSystem']['Configuration']['SOCMax']
		except:
			pass
		
		try:
			Devices[holdnumber].ES.HomeSystem.Configuration.SOCMin = data['ES']['HomeSystem']['Configuration']['SOCMin']
		except:
			pass
		
		try:
			Devices[holdnumber].ES.HomeSystem.Configuration.PowerRating = data['ES']['HomeSystem']['Configuration']['PowerRating']
		except:
			pass
		
		try:
			Devices[holdnumber].ES.HomeSystem.Control.Setpoints.RealPower = data['ES']['HomeSystem']['Control']['Setpoints']['RealPower']
		except:
			pass
		
		try:
			Devices[holdnumber].ES.HomeSystem.Control.Mode = data['ES']['HomeSystem']['Control']['Mode']
		except:
			pass
		
		try:
			Devices[holdnumber].ES.HomeSystem.Status.Measurements.DCVoltage = data['ES']['HomeSystem']['Status']['Measurements']['DCVoltage']
		except:
			pass
		
		try:
			Devices[holdnumber].ES.HomeSystem.Status.Measurements.ACVoltage = data['ES']['HomeSystem']['Status']['Measurements']['ACVoltage']
		except:
			pass
		
		try:
			Devices[holdnumber].ES.HomeSystem.Status.Measurements.RealPower = data['ES']['HomeSystem']['Status']['Measurements']['RealPower']
		except:
			pass
		
		try:
			Devices[holdnumber].ES.HomeSystem.Status.Measurements.SOC = data['ES']['HomeSystem']['Status']['Measurements']['SOC']
		except:
			pass
		
		try:
			Devices[holdnumber].ES.HomeSystem.Status.Mode = data['ES']['HomeSystem']['Status']['Mode']
		except:
			pass
		
		return '200'

	except:
		print('ERROR IN API CALL')
		return '500'


#######################################################################################################

#######################################################################################################

def put_data_Solar():
	global API
	global Devices
	global devicenumber

	response = request.data
	data = json.loads(response)
	
	print(data)


	try:
		# set deviceID to what device is pushed to API
		deviceID = data['DeviceID']

		# initialize usedeviceID
		usedeviceID = ''

		# search device ID within listing of devicIDs
		for i in range(0,len(Devices)):
			if deviceID == Devices[i].ID:
				# if deviceID is found, hold that number
				usedeviceID = deviceID
				holdnumber = i

		# if usedeviceID is still intitialized, no deviceID was found in list
		# add new device to Devices and use hold number 
		if usedeviceID == '':
			Devices[devicenumber].ID = deviceID
			New_Device()
			usedeviceID = deviceID
			holdnumber = devicenumber
			devicenumber = devicenumber + 1

		print('DeviceID:' + deviceID)

		print('All Device list:')
		for i in range(0,len(Devices)):
			print(Devices[i].ID)

	except Exception as e:
		print('%%%%%%%%%%%%%%%%%% ERROR IN JSON PUT WH %%%%%%%%%%%%%%')
		print (e)
		#exc_type, exc_obj, exc_tb = sys.exc_info()
		#fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		#print(exc_type,fname,exc_tbl.tb_lineno)

	

	########################### STATUS ##############################
	try:
		try:
			Devices[holdnumber].ID = data['DeviceID']
		except:
			pass

		try:
			Devices[holdnumber].DeviceType = data['DeviceType']
		except:
			pass

		try:
			Devices[holdnumber].Solar.Configuration = data['DeviceConfiguration']
		except:
			pass

		try:
			Devices[holdnumber].Solar.PV.Configuration.RatedPower = data['Solar']['PV']['Configuration']['RatedPower']
		except:
			pass

		try:
			Devices[holdnumber].Solar.PV.Control.Capacity = data['Solar']['PV']['Control']['Capacity']
		except:
			pass

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[0] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour1']
		except:
			pass

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[1] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour2']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[2] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour3']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[3] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour4']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[4] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour5']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[5] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour6']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[6] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour7']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[7] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour8']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[8] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour9']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[9] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour10']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[10] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour11']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[11] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour12']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[12] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour13']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[13] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour14']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[14] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour15']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[15] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour16']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[16] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour17']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[17] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour18']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[18] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour19']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[19] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour20']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[20] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour21']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[21] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour22']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[22] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour23']
		except:
			pass	
		try:
			Devices[holdnumber].Solar.PV.Status.Forecast.Power[23] = data['Solar']['PV']['Status']['Forecast']['RealPowerHour24']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Measurement.RealPower = data['Solar']['PV']['Status']['Measurements']['RealPower']
		except:
			pass	

		try:
			Devices[holdnumber].Solar.PV.Status.Mode = data['Solar']['PV']['Status']['Mode']
		except:
			pass	



		return '200'

	except:
		print('ERROR IN API CALL')
		return '500'


#######################################################################################################

#######################################################################################################


@app.route('/tod/api/v1.0/HVAC', methods=['GET', 'PUT'])
def handle_HVACtasks():
    if request.method == 'GET':
	    returninfo = get_data_HVAC()
    elif request.method == 'PUT':
	    returninfo = put_data_HVAC()
    else:
	    returninfo = "INCORRECT REQUEST"
    return returninfo

@app.route('/tod/api/v1.0/WH', methods=['GET', 'PUT'])
def handle_WHtasks():
    if request.method == 'GET':
	    returninfo = get_data_WH()
    elif request.method == 'PUT':
	    returninfo = put_data_WH()
    else:
	    returninfo = "INCORRECT REQUEST"
    return returninfo

@app.route('/tod/api/v1.0/ES', methods=['GET', 'PUT'])
def handle_EStasks():
    if request.method == 'GET':
	    returninfo = get_data_ES()
    elif request.method == 'PUT':
	    returninfo = put_data_ES()
    else:
	    returninfo = "INCORRECT REQUEST"
    return returninfo

@app.route('/tod/api/v1.0/Solar', methods=['GET', 'PUT'])
def handle_Solartasks():
    if request.method == 'GET':
	    returninfo = get_data_Solar()
    elif request.method == 'PUT':
	    returninfo = put_data_Solar()
    else:
	    returninfo = "INCORRECT REQUEST"
    return returninfo

if __name__ == '__main__':
	app.run(debug=True)




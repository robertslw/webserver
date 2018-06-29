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


class DesiredLoad():
	def __init__(self):
		self.Hour = []
		for i in range(0,24):
			self.Hour.append("")

class Price():
	def __init__(self):
		self.Hour = []
		for i in range(0,24):
			self.Hour.append("")
	
class PredictedLoad():
	def __init__(self):
		self.Hour = []
		for i in range(0,24):
			self.Hour.append("")

class Devicetype():
	def __init__(self):
		self.Devices = [""]

class Home():
	def __init__(self):
		self.ID = ""
		self.NumberofDevices = ""
		self.DeviceType = Devicetype()
		self.PredictedLoad = PredictedLoad()
		self.Price = Price()
		self.DesiredLoad = DesiredLoad()

Homes = []
Homes.append(Home())
API = {}
homenumber = 0
AggregatorAPI = {}

############# Function for adding new devices ###############
def New_Home():
	global API
	Homes.append(Home())

############# PROVIDES WEB MASTER ACCESS TO SYSTEM ###############
def get_Home():
	return jsonify({'Home':API})

def defineHomeAPI(i):
		global API
		API = {'HomeID':Homes[i].ID,
			'NumberofDevices':Homes[i].NumberofDevices,
			'Devicetye':{
					'Devicetype1':Homes[i].DeviceType.Devices[0]
						},
			'PredictedLoad':{
					'Hour1':Homes[i].PredictedLoad.Hour[0],
					'Hour2':Homes[i].PredictedLoad.Hour[1],
					'Hour3':Homes[i].PredictedLoad.Hour[2],
					'Hour4':Homes[i].PredictedLoad.Hour[3],
					'Hour5':Homes[i].PredictedLoad.Hour[4],
					'Hour6':Homes[i].PredictedLoad.Hour[5],
					'Hour7':Homes[i].PredictedLoad.Hour[6],
					'Hour8':Homes[i].PredictedLoad.Hour[7],
					'Hour9':Homes[i].PredictedLoad.Hour[8],
					'Hour10':Homes[i].PredictedLoad.Hour[9],
					'Hour11':Homes[i].PredictedLoad.Hour[10],
					'Hour12':Homes[i].PredictedLoad.Hour[11],
					'Hour13':Homes[i].PredictedLoad.Hour[12],
					'Hour14':Homes[i].PredictedLoad.Hour[13],
					'Hour15':Homes[i].PredictedLoad.Hour[14],
					'Hour16':Homes[i].PredictedLoad.Hour[15],
					'Hour17':Homes[i].PredictedLoad.Hour[16],
					'Hour18':Homes[i].PredictedLoad.Hour[17],
					'Hour19':Homes[i].PredictedLoad.Hour[18],
					'Hour20':Homes[i].PredictedLoad.Hour[19],
					'Hour21':Homes[i].PredictedLoad.Hour[20],
					'Hour22':Homes[i].PredictedLoad.Hour[21],
					'Hour23':Homes[i].PredictedLoad.Hour[22],
					'Hour24':Homes[i].PredictedLoad.Hour[23]
						},
			'Price':{
					'Hour1':Homes[i].Price.Hour[0],
					'Hour2':Homes[i].Price.Hour[1],
					'Hour3':Homes[i].Price.Hour[2],
					'Hour4':Homes[i].Price.Hour[3],
					'Hour5':Homes[i].Price.Hour[4],
					'Hour6':Homes[i].Price.Hour[5],
					'Hour7':Homes[i].Price.Hour[6],
					'Hour8':Homes[i].Price.Hour[7],
					'Hour9':Homes[i].Price.Hour[8],
					'Hour10':Homes[i].Price.Hour[9],
					'Hour11':Homes[i].Price.Hour[10],
					'Hour12':Homes[i].Price.Hour[11],
					'Hour13':Homes[i].Price.Hour[12],
					'Hour14':Homes[i].Price.Hour[13],
					'Hour15':Homes[i].Price.Hour[14],
					'Hour16':Homes[i].Price.Hour[15],
					'Hour17':Homes[i].Price.Hour[16],
					'Hour18':Homes[i].Price.Hour[17],
					'Hour19':Homes[i].Price.Hour[18],
					'Hour20':Homes[i].Price.Hour[19],
					'Hour21':Homes[i].Price.Hour[20],
					'Hour22':Homes[i].Price.Hour[21],
					'Hour23':Homes[i].Price.Hour[22],
					'Hour24':Homes[i].Price.Hour[23]
						},
			'DesiredLoad':{
					'Hour1':Homes[i].DesiredLoad.Hour[0],
					'Hour2':Homes[i].DesiredLoad.Hour[1],
					'Hour3':Homes[i].DesiredLoad.Hour[2],
					'Hour4':Homes[i].DesiredLoad.Hour[3],
					'Hour5':Homes[i].DesiredLoad.Hour[4],
					'Hour6':Homes[i].DesiredLoad.Hour[5],
					'Hour7':Homes[i].DesiredLoad.Hour[6],
					'Hour8':Homes[i].DesiredLoad.Hour[7],
					'Hour9':Homes[i].DesiredLoad.Hour[8],
					'Hour10':Homes[i].DesiredLoad.Hour[9],
					'Hour11':Homes[i].DesiredLoad.Hour[10],
					'Hour12':Homes[i].DesiredLoad.Hour[11],
					'Hour13':Homes[i].DesiredLoad.Hour[12],
					'Hour14':Homes[i].DesiredLoad.Hour[13],
					'Hour15':Homes[i].DesiredLoad.Hour[14],
					'Hour16':Homes[i].DesiredLoad.Hour[15],
					'Hour17':Homes[i].DesiredLoad.Hour[16],
					'Hour18':Homes[i].DesiredLoad.Hour[17],
					'Hour19':Homes[i].DesiredLoad.Hour[18],
					'Hour20':Homes[i].DesiredLoad.Hour[19],
					'Hour21':Homes[i].DesiredLoad.Hour[20],
					'Hour22':Homes[i].DesiredLoad.Hour[21],
					'Hour23':Homes[i].DesiredLoad.Hour[22],
					'Hour24':Homes[i].DesiredLoad.Hour[23]
						}
			
		}
		
		return API

#######################################################################################################

#######################################################################################################

def all_data_Home():
	global API
	global Homes

	response = request.headers
	
	FullAPI = {}
	FullAPI["Aggregator"] = []

	for i in range(0,len(Homes)):
			API = defineHomeAPI(i)
			FullAPI["Aggregator"].append({'Home':API})

	return jsonify(FullAPI)


#######################################################################################################

#######################################################################################################

def get_data_Home():
	global API
	global Homes

	response = request.headers

	for i in range(0,len(Homes)):
		#print Homes[i].ID
		#print response['Authorization']
		if str(Homes[i].ID) == str(response['Authorization']):
			API = defineHomeAPI(i)


	print(API)
	return jsonify({'Home':API})

#######################################################################################################

#######################################################################################################

def put_data_Home():
	global API
	global Homes
	global homenumber
	
	response = request.data
	data = json.loads(response)

	print(data)
	try:
		# set homeid to what device is pushed to API
		homeID = data['HomeID']

		# initialize useHomeID
		useHomeID = ''

		# search Home ID within listing of HomeIDs
		for i in range(0,len(Homes)):
			if homeID == Homes[i].ID:
				# if HomeID is found, hold that number
				useHomeID = homeID
				holdnumber = i

		# if useHomeID is still intitialized, no HomeID was found in list
		# add new Home to Homes and use hold number 
		if useHomeID == '':

			Homes[homenumber].ID = homeID
			New_Home()
			useHomeID = homeID
			holdnumber = homenumber
			homenumber = homenumber + 1

		print('HomeID:' + homeID)

		print('All Home list:')
		for i in range(0,len(Homes)):
			print(Homes[i].ID)

	except Exception as e:
		print('%%%%%%%%%%%%%%%%%% ERROR IN JSON PUT Home %%%%%%%%%%%%%%')
		print (e)
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type,fname,exc_tb.tb_lineno)


	########################### STATUS ##############################
	try:
		try:
			Homes[holdnumber].ID = data['HomeID']
		except:
			pass

		try:
			Homes[holdnumber].NumberofDevices = data['NumberofDevices']
		except:
			pass

		try:
			Homes[holdnumber].Devicetype = data['Devicetype']
		except:
			pass

		try:
			for i in range(0,24):
				try:
					Homes[holdnumber].PredictedLoad.Hour[i] = data['PredictedLoad']['Hour'+str(i+1)]
				except:
					pass
		except:
			pass

		try:
			for i in range(0,24):
				try:
					Homes[holdnumber].Price.Hour[i] = data['Price']['Hour'+str(i+1)]
				except:
					pass
		except:
			pass

		try:
			for i in range(0,24):
				try:
					Homes[holdnumber].DesiredLoad.Hour[i] = data['DesiredLoad']['Hour'+str(i+1)]
				except:
					pass
		except:
			pass


		return '200'

	
	except Exception as e:
		print('ERROR IN API CALL')
		print(e)
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type,fname,exc_tb.tb_lineno)
		return '500'
#######################################################################################################

#######################################################################################################


@app.route('/tod/api/v1.0/Aggregator', methods=['GET', 'PUT'])
def handle_Hometasks():
    if request.method == 'GET':
	    returninfo = get_data_Home()
    elif request.method == 'PUT':
	    returninfo = put_data_Home()
    else:
	    returninfo = "INCORRECT REQUEST"
    return returninfo


@app.route('/tod/api/v1.0/Aggregatorall', methods=['GET', 'PUT'])
def handle_Aggregatortasks():
    if request.method == 'GET':
	    returninfo = all_data_Home()
    #elif request.method == 'PUT':
	    #returninfo = put_data_Home()
    else:
	    returninfo = "INCORRECT REQUEST"
    return returninfo


if __name__ == '__main__':
	app.run(port=5003,debug=True)




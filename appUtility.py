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
	
class PredictedLoad():
	def __init__(self):
		self.Hour = []
		for i in range(0,24):
			self.Hour.append("")

class Devicetype():
	def __init__(self):
		self.Devices = [""]

class Aggregator():
	def __init__(self):
		self.ID = ""
		self.NumberofHomes = ""
		self.PredictedLoad = PredictedLoad()
		self.DesiredLoad = DesiredLoad()

Aggregators = []
Aggregators.append(Aggregator())
API = {}
aggnumber = 0
UtilityAPI = {}

############# Function for adding new devices ###############
def New_Aggregator():
	global API
	Aggregators.append(Aggregator())

############# PROVIDES WEB MASTER ACCESS TO SYSTEM ###############
def get_Aggregator():
	return jsonify({'Home':API})

def defineAggregatorAPI(i):
		global API
		API = {'AggregatorID':Aggregators[i].ID,
			'NumberofHomes':Aggregators[i].NumberofHomes,
			'PredictedLoad':{
					'Hour1':Aggregators[i].PredictedLoad.Hour[0],
					'Hour2':Aggregators[i].PredictedLoad.Hour[1],
					'Hour3':Aggregators[i].PredictedLoad.Hour[2],
					'Hour4':Aggregators[i].PredictedLoad.Hour[3],
					'Hour5':Aggregators[i].PredictedLoad.Hour[4],
					'Hour6':Aggregators[i].PredictedLoad.Hour[5],
					'Hour7':Aggregators[i].PredictedLoad.Hour[6],
					'Hour8':Aggregators[i].PredictedLoad.Hour[7],
					'Hour9':Aggregators[i].PredictedLoad.Hour[8],
					'Hour10':Aggregators[i].PredictedLoad.Hour[9],
					'Hour11':Aggregators[i].PredictedLoad.Hour[10],
					'Hour12':Aggregators[i].PredictedLoad.Hour[11],
					'Hour13':Aggregators[i].PredictedLoad.Hour[12],
					'Hour14':Aggregators[i].PredictedLoad.Hour[13],
					'Hour15':Aggregators[i].PredictedLoad.Hour[14],
					'Hour16':Aggregators[i].PredictedLoad.Hour[15],
					'Hour17':Aggregators[i].PredictedLoad.Hour[16],
					'Hour18':Aggregators[i].PredictedLoad.Hour[17],
					'Hour19':Aggregators[i].PredictedLoad.Hour[18],
					'Hour20':Aggregators[i].PredictedLoad.Hour[19],
					'Hour21':Aggregators[i].PredictedLoad.Hour[20],
					'Hour22':Aggregators[i].PredictedLoad.Hour[21],
					'Hour23':Aggregators[i].PredictedLoad.Hour[22],
					'Hour24':Aggregators[i].PredictedLoad.Hour[23]
						},
			'DesiredLoad':{
					'Hour1':Aggregators[i].DesiredLoad.Hour[0],
					'Hour2':Aggregators[i].DesiredLoad.Hour[1],
					'Hour3':Aggregators[i].DesiredLoad.Hour[2],
					'Hour4':Aggregators[i].DesiredLoad.Hour[3],
					'Hour5':Aggregators[i].DesiredLoad.Hour[4],
					'Hour6':Aggregators[i].DesiredLoad.Hour[5],
					'Hour7':Aggregators[i].DesiredLoad.Hour[6],
					'Hour8':Aggregators[i].DesiredLoad.Hour[7],
					'Hour9':Aggregators[i].DesiredLoad.Hour[8],
					'Hour10':Aggregators[i].DesiredLoad.Hour[9],
					'Hour11':Aggregators[i].DesiredLoad.Hour[10],
					'Hour12':Aggregators[i].DesiredLoad.Hour[11],
					'Hour13':Aggregators[i].DesiredLoad.Hour[12],
					'Hour14':Aggregators[i].DesiredLoad.Hour[13],
					'Hour15':Aggregators[i].DesiredLoad.Hour[14],
					'Hour16':Aggregators[i].DesiredLoad.Hour[15],
					'Hour17':Aggregators[i].DesiredLoad.Hour[16],
					'Hour18':Aggregators[i].DesiredLoad.Hour[17],
					'Hour19':Aggregators[i].DesiredLoad.Hour[18],
					'Hour20':Aggregators[i].DesiredLoad.Hour[19],
					'Hour21':Aggregators[i].DesiredLoad.Hour[20],
					'Hour22':Aggregators[i].DesiredLoad.Hour[21],
					'Hour23':Aggregators[i].DesiredLoad.Hour[22],
					'Hour24':Aggregators[i].DesiredLoad.Hour[23]
						}
			
		}
		
		return API

#######################################################################################################

#######################################################################################################

def all_data_Aggregator():
	global API
	global Aggregators

	response = request.headers
	
	FullAPI = {}
	FullAPI["Utility"] = []

	for i in range(0,len(Aggregators)):
			API = defineAggregatorAPI(i)
			FullAPI["Utility"].append({'Aggregator':API})

	print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FULL UTILITY ########################')
	print(FullAPI)

	return jsonify(FullAPI)


#######################################################################################################

#######################################################################################################

def get_data_Aggregator():
	global API
	global Aggregators

	response = request.headers

	for i in range(0,len(Aggregators)):
		#print Aggregators[i].ID
		#print response['Authorization']
		if str(Aggregators[i].ID) == str(response['Authorization']):
			API = defineAggregatorAPI(i)


	print(API)
	return jsonify({'Aggregator':API})

#######################################################################################################

#######################################################################################################

def put_data_Aggregator():
	global API
	global Aggregators
	global aggnumber
	
	response = request.data
	data = json.loads(response)

	print(data)
	try:
		# set homeid to what device is pushed to API
		aggregatorID = data['AggregatorID']

		# initialize useHomeID
		useAggregatorID = ''

		# search Home ID within listing of HomeIDs
		for i in range(0,len(Aggregators)):
			if aggregatorID == Aggregators[i].ID:
				# if HomeID is found, hold that number
				useAggregatorID = aggregatorID
				aggnumber = i

		# if useHomeID is still intitialized, no HomeID was found in list
		# add new Home to Homes and use hold number 
		if useAggregatorID == '':

			Aggregators[aggnumber].ID = aggregatorID
			New_Aggregator()
			useAggregatorID = aggregatorID
			holdnumber = aggnumber
			aggnumber = aggnumber + 1

		print('AggregatorID:' + aggregatorID)

		print('All Aggregator list:')
		for i in range(0,len(Aggregators)):
			print(Aggregators[i].ID)

	except Exception as e:
		print('%%%%%%%%%%%%%%%%%% ERROR IN JSON PUT Home %%%%%%%%%%%%%%')
		print (e)
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type,fname,exc_tb.tb_lineno)


	########################### STATUS ##############################
	try:
		try:
			Aggregators[holdnumber].ID = data['AggregatorID']
		except:
			pass

		try:
			Aggregators[holdnumber].NumberofHomes = data['NumberofHomes']
		except:
			pass

		try:
			for i in range(0,24):
				try:
					Aggregators[holdnumber].PredictedLoad.Hour[i] = data['PredictedLoad']['Hour'+str(i+1)]
				except:
					pass
		except:
			pass

		try:
			for i in range(0,24):
				try:
					Aggregators[holdnumber].DesiredLoad.Hour[i] = data['DesiredLoad']['Hour'+str(i+1)]
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


@app.route('/tod/api/v1.0/Utility', methods=['GET', 'PUT'])
def handle_Aggregatortasks():
    if request.method == 'GET':
	    returninfo = get_data_Aggregator()
    elif request.method == 'PUT':
	    returninfo = put_data_Aggregator()
    else:
	    returninfo = "INCORRECT REQUEST"
    return returninfo

@app.route('/tod/api/v1.0/Utilityall', methods=['GET', 'PUT'])
def handle_Aggregatoralltasks():
    if request.method == 'GET':
	    returninfo = all_data_Aggregator()
    #elif request.method == 'PUT':
	    #returninfo = put_data_Aggregator()
    else:
	    returninfo = "INCORRECT REQUEST"
    return returninfo


if __name__ == '__main__':
	app.run(port=5002,debug=True)




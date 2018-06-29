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

class PredictedLoad():
	def __init__(self):
		self.Hour = []
		for i in range(0,24):
			self.Hour.append("")

class Utility():
	def __init__(self):
		self.ID = ""
		self.PredictedLoad = PredictedLoad()


Utilities = []
Utilities.append(Utility())
API = {}
utilitynumber = 0
ISOAPI = {}

############# Function for adding new devices ###############
def New_Utility():
	global API
	Utilities.append(Utility())

############# PROVIDES WEB MASTER ACCESS TO SYSTEM ###############
def get_Utilities():
	return jsonify({'Utility':API})

def defineUtilityAPI(i):
		global API
		API = {'UtilityID':Utilities[i].ID,
			'PredictedLoad':{
					'Hour1':Utilities[i].PredictedLoad.Hour[0],
					'Hour2':Utilities[i].PredictedLoad.Hour[1],
					'Hour3':Utilities[i].PredictedLoad.Hour[2],
					'Hour4':Utilities[i].PredictedLoad.Hour[3],
					'Hour5':Utilities[i].PredictedLoad.Hour[4],
					'Hour6':Utilities[i].PredictedLoad.Hour[5],
					'Hour7':Utilities[i].PredictedLoad.Hour[6],
					'Hour8':Utilities[i].PredictedLoad.Hour[7],
					'Hour9':Utilities[i].PredictedLoad.Hour[8],
					'Hour10':Utilities[i].PredictedLoad.Hour[9],
					'Hour11':Utilities[i].PredictedLoad.Hour[10],
					'Hour12':Utilities[i].PredictedLoad.Hour[11],
					'Hour13':Utilities[i].PredictedLoad.Hour[12],
					'Hour14':Utilities[i].PredictedLoad.Hour[13],
					'Hour15':Utilities[i].PredictedLoad.Hour[14],
					'Hour16':Utilities[i].PredictedLoad.Hour[15],
					'Hour17':Utilities[i].PredictedLoad.Hour[16],
					'Hour18':Utilities[i].PredictedLoad.Hour[17],
					'Hour19':Utilities[i].PredictedLoad.Hour[18],
					'Hour20':Utilities[i].PredictedLoad.Hour[19],
					'Hour21':Utilities[i].PredictedLoad.Hour[20],
					'Hour22':Utilities[i].PredictedLoad.Hour[21],
					'Hour23':Utilities[i].PredictedLoad.Hour[22],
					'Hour24':Utilities[i].PredictedLoad.Hour[23]
						}
		}
		
		return API

#######################################################################################################

#######################################################################################################

def get_data_Utility():
	global API
	global Utilties

	response = request.headers

	for i in range(0,len(Utilities)):
		print(Utilities[i].ID)
		print(response['Authorization'])
		if str(Utilities[i].ID) == str(response['Authorization']):
			API = defineUtilityAPI(i)


	print(API)
	return jsonify({'Utility':API})

#######################################################################################################

#######################################################################################################

def put_data_Utility():
	global API
	global Utilities
	global utilitynumber
	
	response = request.data
	data = json.loads(response)

	print(data)
	try:
		# set homeid to what device is pushed to API
		utilityID = data['UtilityID']

		# initialize useHomeID
		useUtilityID = ''

		# search Home ID within listing of HomeIDs
		for i in range(0,len(Utilities)):
			if utilityID == Utilities[i].ID:
				# if HomeID is found, hold that number
				useUtilityID = utilityID
				utilitynumber = i

		# if useHomeID is still intitialized, no HomeID was found in list
		# add new Home to Homes and use hold number 
		if useUtilityID == '':

			Utilities[utilitynumber].ID = useUtilityID
			New_Utility()
			useUtilityID = utilityID
			holdnumber = utilitynumber
			utilitynumber = utilitynumber + 1

		print('UtilityID:' + utilityID)

		print('All Utility list:')
		for i in range(0,len(Utilities)):
			print(Utilities[i].ID)

	except Exception as e:
		print('%%%%%%%%%%%%%%%%%% ERROR IN JSON PUT Home %%%%%%%%%%%%%%')
		print (e)
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type,fname,exc_tb.tb_lineno)


	########################### STATUS ##############################
	try:
		try:
			Utilities[holdnumber].ID = data['UtilityID']
		except:
			pass

		try:
			for i in range(0,24):
				try:
					Utilities[holdnumber].PredictedLoad.Hour[i] = data['PredictedLoad']['Hour'+str(i+1)]
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


@app.route('/tod/api/v1.0/ISO', methods=['GET', 'PUT'])
def handle_Aggregatortasks():
    if request.method == 'GET':
	    returninfo = get_data_Utility()
    elif request.method == 'PUT':
	    returninfo = put_data_Utility()
    else:
	    returninfo = "INCORRECT REQUEST"
    return returninfo


if __name__ == '__main__':
	app.run(port=5001,debug=True)




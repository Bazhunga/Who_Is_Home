import webapp2
import cgi
import urllib
import urllib2
from twilio import twiml
import sys
import os

import json
import keys

class ReceiveText(webapp2.RequestHandler):
	def post(self):
		fromNumber = cgi.escape(self.request.get('From'))
		dataurl = "https://data.sparkfun.com/output/lz994mazZ0tXV13qxQM1.json"
		request = urllib2.Request(dataurl)
		result = urllib2.urlopen(request)
		jsonString = result.read()
		self.getPeopleStatus(self, jsonString)
		# # self.getPeopleStatus(self, jsonString)
		# r = twiml.Response()
		# try:
		# 	r.message("HEY MAN")	
		# except:
		# 	pass

	@staticmethod
	def getPeopleStatus(self, jsonString):
		jsonObj = json.loads(jsonString)
		print jsonObj[0]
		

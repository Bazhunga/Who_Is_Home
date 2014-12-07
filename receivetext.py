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
		people_on = []
		people_on = os.system("WhoIsOnMyWifi.py")

	r = twiml.Response()
	try:
		r.message(people_on)
	except:
		pass


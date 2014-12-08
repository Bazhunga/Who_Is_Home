Who_Is_Home
===========

Who's home? Find out who's at home by checking out which devices are active on your network.


This application consists of 2 parts. The pinging looper that constantly scans for activity of known ip addresses and the twilio application that accesses a database by data.sparkfun 

How to use in your home:

1. Following the format already given, add the people you know as well as their ip addresses to known_peeps.txt. 

2.This application relies on running Constant_Looper.py to constantly ping the ip addresses to see if they have been active. 
Run it by "python Constant_Looper.py". 
The interval has been set to a sweep every 15 seconds assuming that the Constant_Looper.py is always running.
WORD OF WARNING: The code has not been updated to check the time stamp just yet. That's coming soon!

3. Create a stream on data.sparkfun.com and add the known people to it.

4. Create a TwiML application using your twilio account and link it to your number

5. Update the keys in keys.py with your twilio keys and sparkfun keys

6. Using google app engine, deploy the application following the below instructions

NOTES ABOUT THE GOOGLE APP ENGINE DEPLOYMENT
============================================
The application uses twilio to function.
To set it up via LINUX:

Download the Python Google App Engine SDK for Linux and unzip it to get the google_appengine folder. Clone the repository.
Rename APIKeys_template.py to APIKeys.py and fill in your API keys.
Place your info in app.yaml

Install Dependencies

First, cd into the project directory.
Install virtualenv with sudo easy_install pip, then sudo pip install virtualenv
Set up a virtual environment: virtualenv --distribute venv
Activate it: source venv/bin/activate
Install twilio and dateutil: pip install twilio and pip install python-dateutil
Deactivate virtual environment: deactivate
Link dependencies to your project:

ln -s venv/lib/python2.7/site-packages/twilio .
ln -s venv/lib/python2.7/site-packages/httplib2 .
ln -s venv/lib/python2.7/site-packages/six.py .
ln -s venv/lib/python2.7/site-packages/dateutil .
Now, you can run the project locally with ./dev_appserver.py <path_to_project>
or deploy it with ./appcfg.py update <path_to_project>



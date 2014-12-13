__author__ = 'Bazhunga'

# Tested on windows
# Allow usage of windows command line
# Note that devices should be DHCP mode

import shlex
import subprocess
import urllib
import urllib2
from keys import *

def go():
    d_knownpeople = {}
    a_currentusers = []

    d_knownpeople = read_known_people()
    print d_knownpeople

    d_currentusers = find_users(d_knownpeople)
    print d_currentusers

    update_cloud(d_currentusers)

# Read in and create a dictionary of people and their ip addresses
def read_known_people():
    o_knownpeople = open('known_peeps.txt', 'r')
    lineElements = []
    d_knownpeople = {}
    for line in o_knownpeople:
        lineElements = line.split()
        d_knownpeople[lineElements[0]] = lineElements[1]
    return d_knownpeople

def find_users(d_knownpeople):
    users_online = {}
    for peeps in d_knownpeople:
        pingString = "ping -n 1 " + str(d_knownpeople[peeps])
        print pingString

        ping = subprocess.Popen(pingString, stdout=subprocess.PIPE)
        pingResult = ping.stdout.read()
        print pingResult.split()
        if 'unreachable.' not in pingResult.split() and 'timed' not in pingResult.split():
            users_online[peeps] = 1
        else:
            users_online[peeps] = 0
        print
        print

    return users_online

def update_cloud(d_currentusers):
    davidStatus = d_currentusers["David"]
    kevinStatus = d_currentusers["Kevin_Zhu"]
    ruiStatus = d_currentusers["Rui"]
    rahulStatus = d_currentusers["Rahul"]
    url = "http://data.sparkfun.com/input/"+str(pubKey)+"?private_key="+str(privKey)+\
           "&david="+str(davidStatus)+"&kevin="+str(kevinStatus)+"&rui="+str(ruiStatus)+"&rahul="+str(rahulStatus)
    request = urllib2.Request(url)
    result = urllib2.urlopen(request)
    messageReturned = result.read()
    print messageReturned


# def find_mac (userMac):
    # for m in macAddresses:

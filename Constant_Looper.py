__author__ = 'Bazhunga'

#Constantly loops the WhoIsOnMyWifi.py to upload status

import time
import os
from WhoIsOnMyWifi import *
try:
    while True:
        go()
        time.sleep(5)
except KeyboardInterrupt:
    print 'interrupted!'
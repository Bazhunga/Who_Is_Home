__author__ = 'Bazhunga'

# Tested on windows
# Allow usage of windows command line
# Note that devices should be DHCP mode

import shlex
import subprocess

def main():
    d_knownpeople = {}
    a_currentusers = []

    d_knownpeople = read_known_people()
    print d_knownpeople

    a_currentusers = find_users(d_knownpeople)
    print a_currentusers

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
    users_online = []
    for peeps in d_knownpeople:
        pingString = "ping -n 1 " + str(d_knownpeople[peeps])
        print pingString

        ping = subprocess.Popen(pingString, stdout=subprocess.PIPE)
        pingResult = ping.stdout.read()
        print pingResult.split()
        if 'unreachable.' not in pingResult.split() and 'timed' not in pingResult.split():
            users_online.append(peeps)
        print
        print

    return users_online

#Scanning for all ip addresses would take way too long
def scan_ip_addresses():
    pass


# def find_mac (userMac):
    # for m in macAddresses:


if __name__ == "__main__":
    main()
import os
from requests import get

fullPath = os.path.expanduser('~/.ipaddr.txt')

def getIP():
    newIp = get('https://api.ipify.org').content.decode('utf8')
    if os.path.isfile(fullPath):
        with open(fullPath, "r") as ff:
            oldIp = ff.read()
            if oldIp == newIp: return
    return newIp

def writeIpToFile(ipAddr):
    with open(fullPath, "w") as ff:
        ff.write(ipAddr)

def hasIpChanged():
    ipAddr = getIP()
    if ipAddr is not None:
        writeIpToFile(ipAddr)
    return ipAddr

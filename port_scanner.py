#!/bin/python3

#port_scanner
import sys 
import socket
from datetime import datetime

#Define our target
"""print(dir(sys)) yaparak neleri içerdiğini görebilriz."""
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate a host name to IPV4
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()
#Add a pretty banner		
print("-"*50)
print("Scanning target {} ".format(target))
print("Time started: "+str(datetime.now()))
print("-"*50)

try:
	for port in range(1,499 ):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4 and tcp conne+ction
		socket.setdefaulttimeout(2) 
		result = s.connect_ex((target,port)) #returns error indicator
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExitting program.")
	sys.exit()
except socket.gaierror:
	print("Hostname  coult not be resolved. ")
	sys.exit()
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
		

		
				
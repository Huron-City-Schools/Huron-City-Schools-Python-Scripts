#!/usr/bin/env python

"""NetworkCheck.py - Checks to see if we're on the internal school network and sets search and contacts path."""

___author___='Gary Larizza (gary@huronhs.com)'
___version___='0.1'

import sys
sys.path.append('/Library/HuronHS/Python2.5/')
import dsutils
import socket
import os

# Capture all IP Addresses of Network Interfaces
ip = socket.gethostbyname_ex(socket.gethostname())[-1]

# Set 'node' to be the server to which we're bound (IF we're bound)
node = dsutils.GetLDAPServer()

# If we are bound to a server....
if node != "/LDAPv3/":

# Check to see if we're on the HuronHS Network
# If we are, ensure the Search Paths are correct
# If not, strip out Search Paths
	for i in ip:
		octet=i.split('.')
		if octet[0] == '10':
			if octet[1] == '13':
				dsutils.EnsureSearchNodePresent(node)
				dsutils.EnsureContactsNodePresent(node)
				break
			else:
				print('2nd octet doesn\'t match')
				dsutils.DeleteNodeFromSearchPath(node)
				dsutils.DeleteNodeFromContactsPath(node)
		else:
			print('1st octet doesn\'t match')
			dsutils.DeleteNodeFromSearchPath(node)
			dsutils.DeleteNodeFromSearchPath(node)	
else:
	print('We\'re not bound')

import socket 
import time
import re
from bs4 import BeautifulSoup


def serverContact():
	HOST = '10.10.161.129'
	PORT =   4000
	

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.settimeout(30)
	s.connect((HOST, PORT));

	request = b'hello'
	#request = ""
	addr = ("10.10.161.129",4000)
	s.sendto(request,addr)

	#response = s.recv(4096)
	code = ''
	while True:
		data = s.recv(512)
		if(len(data)<1):
			break

		print(data)
		#code = code + str(data)

	s.close()

	

serverContact()
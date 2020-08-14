import socket 
import time
import re
from bs4 import BeautifulSoup

def firstnode():
	HOST = '10.10.4.141'
	PORT =   3010
	

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(30)
	s.connect((HOST, PORT));

	request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % HOST 
	#request = ""
	s.send(request.encode())

	#response = s.recv(4096)
	code = ''
	while True:
		data = s.recv(512)
		if(len(data)<1):
			break

		#print(data)
		code = code + str(data)

	s.close()

	#print(code)
	soup = BeautifulSoup(code, "html.parser")
	port = str(soup.u)
	port = re.sub("[^0-9]","",port)
	#print(port)
	return port


def tempNode(current_PORT):
	HOST = '10.10.4.141'
	PORT = int(current_PORT)
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s2.settimeout(30)
	s2.connect((HOST, PORT));

	request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % HOST 
	#request = ""
	s2.send(request.encode())

	#response = s.recv(4096)
	code = ''
	while True:
		data = s2.recv(512)
		if(len(data)<1):
			break
		data2 = str(data)
		file = open("output.txt" , "a")
		file.write( data2[-17:] + "\n")
		file.close
		#print(data)
		code = code + str(data)
		#code = code + str(data)

	s2.close()
	soup = BeautifulSoup(code, "html.parser")
	print(soup)



number = 0
current_node = None
while True:
	next_node = firstnode()
	if current_node is None:
		current_node = next_node
	elif current_node == next_node:
		time.sleep(0.1)
	else:
		current_node = next_node
		#print(next_node)
		tempNode(current_node)
	

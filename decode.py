import base64

file = open("b64.txt" , 'r' )


data = ""
for line in file:
	data = data + line

for i in range(0,50):
	decrypted = base64.b64decode(data)
	data = decrypted

print(data)

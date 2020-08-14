import re

file = open("output-copy.txt" , "r")

data = ""
number = float(0)
for line in file:
	if "add" in line:
		sections = line.split(' ')
		
		#value = re.sub("[^0-9]","",sections[1])
		value = sections[1]
		number = number + float(value)
		#print(str(float(value)))
		print("add " + sections[1])
	elif "divide" in line:
		sections = line.split(' ')

		#value = re.sub("[^0-9]","",sections[1])
		value = sections[1]
		number = number / float(value)
		#print(str(float(value)))
		print("divide " + sections[1])

	elif "multiply" in line:
		sections = line.split(' ')
		#value = re.sub("[^0-9]","",sections[1])
		value = sections[1]
		#print(str(float(value)))
		number = number * float(value)
		print("multiply " + sections[1])

	elif "minus" in line:
		sections = line.split(' ')
		
		#value = re.sub("[^0-9]","",sections[1])
		value = sections[1]
		number = number - float(value)
		#print(str(float(value)))
		print("minus " + sections[1])

print(number)
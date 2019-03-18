import os
import re

filename = os.path.join("C:\\", "Users", "savid", "Desktop", "malware_analysis", "mypcapcsv.txt")

new_list=[]
ip_list=[]
file = open(filename, "r")
for line in file:
	#input(line)
	line=line.replace(" " ,",")
	new_list.append(line) #captures all lines in csv format
	test = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line) #puts IPs into "test"
	for t in test:
		#print(t)
		if t not in ip_list:
			ip_list.append(t) #appends IPs to "ip_list"
		#print("ip_list:", ip_list)
		
		
ip_list.sort()
print("number of unique IPs: ", len(ip_list))
for x in ip_list:
	print(x)


"""
print("[4] List unique IPs")
selection=input("Selection:")
if selection == "4":
	print("Hi")
"""

#Use pcapper2.py when you need to get the information column

import os
import subprocess
import time

tshark_loc = os.path.join("C:\\", "Program Files", "Wireshark")
os.chdir(tshark_loc)

with open("C:\\users\\savid\\Desktop\\malware_analysis\\output3.txt") as stdout:
	subprocess.Popen("tshark -G column-formats", shell=True, stdout=stdout, stderr=stdout)

tsharkcmd1 = "tshark" 
tsharkcmd1 += " -r c:\\users\\savid\\desktop\\malware_analysis\\homies2.pcap -o "
tsharkcmd1 += "\"gui.column.format:\\"
tsharkcmd1 += "\"Source\\"
tsharkcmd1 += "\",\\\"%s\\\"\""

with open("C:\\users\\savid\\Desktop\\malware_analysis\\output4.txt", "w") as stdout:
	subprocess.Popen(tsharkcmd1, shell=True, stdout=stdout, stderr=stdout)

time.sleep(1)
	
mylist=[]
	
with open("C:\\users\\savid\\Desktop\\malware_analysis\\output4.txt", 'r') as input_file:
	for line in input_file:
		if line not in mylist:
			mylist.append(line)

#with open("C:\\users\\savid\\Desktop\\malware_analysis\\output5.txt", 'w') as output:
for x in mylist:
	x=x.strip(" ")
	x=x.strip("\n")
	print(x)
		

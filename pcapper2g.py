#pcapper2g.py gets dns

import os
import subprocess
import time

tshark_loc = os.path.join("C:\\", "Program Files", "Wireshark")
os.chdir(tshark_loc)

with open("C:\\users\\savid\\Desktop\\malware_analysis\\output3.txt") as stdout:
	subprocess.Popen("tshark -G column-formats", shell=True, stdout=stdout, stderr=stdout)

#the actual command
tsharkcmd1 = "tshark" 
tsharkcmd1 += " -r c:\\users\\savid\\desktop\\malware_analysis\\homies2.pcap -o "
tsharkcmd1 += "\"gui.column.format:\\"
tsharkcmd1 += "\"Information\\"
tsharkcmd1 += "\",\\\"%i\\\"\"" #<= format spot

#the command
with open("C:\\users\\savid\\Desktop\\malware_analysis\\output4.txt", "w") as stdout:
	subprocess.Popen(tsharkcmd1, shell=True, stdout=stdout, stderr=stdout)

time.sleep(1)

#internal de-duplication => clean up => Print
mylist=[]
with open("C:\\users\\savid\\Desktop\\malware_analysis\\output4.txt", 'r') as input_file:
	for line in input_file:
		if "query" in line:
			mylist.append(line)

for x in mylist:
	x=x.strip(" ")
	x=x.strip("\n")
	print(x)
		

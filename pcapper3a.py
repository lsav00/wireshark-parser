"""pcapper3 grabs protocols"""
"""pcapper3a grabs protocols & cleans up with regex"""

import os
import subprocess
import time
import re

tshark_loc = os.path.join("C:\\", "Program Files", "Wireshark")
os.chdir(tshark_loc)

with open("C:\\users\\savid\\Desktop\\malware_analysis\\output3.txt") as stdout:
	subprocess.Popen("tshark -G column-formats", shell=True, stdout=stdout, stderr=stdout)

#tshark -r C:\Users\savid\Desktop\malware_analysis\homies2.pcap -T fields -e frame.protocols | findstr "data"	

"""Don't forget DOUBLE SLASHES"""
tsharkcmd1 = "tshark" 
tsharkcmd1 += " -r C:\\Users\\savid\\Desktop\\malware_analysis\\homies2.pcap -T fields -e frame.protocols"


with open("C:\\users\\savid\\Desktop\\malware_analysis\\output4.txt", "w") as stdout:
	subprocess.Popen(tsharkcmd1, shell=True, stdout=stdout, stderr=stdout)

time.sleep(1)
	
mylist=[]
	
with open("C:\\users\\savid\\Desktop\\malware_analysis\\output4.txt", 'r') as input_file:
	for line in input_file:
		if line not in mylist:
			mylist.append(line)

#with open("C:\\users\\savid\\Desktop\\malware_analysis\\output5.txt", 'w') as output:
newlist=[]

for x in mylist:
	x= re.findall('\w+$' , x)
	#print(x)
	if x not in newlist: 
		newlist.append(x)
print(newlist)
	#input("STOP")
#	abc = 'a, b, c, d'
#letters = re.findall('c', abc)
#for letter in letters:
#	print(letter)
#	x=x.strip("\n")
#for thing in y:

		

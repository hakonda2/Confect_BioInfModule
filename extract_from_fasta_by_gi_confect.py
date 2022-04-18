#!/usr/bin/python


import sys
import re

if (len(sys.argv) < 2):
	print """
make fastafile from list of names

-f fastafile
-i idfile

"""

	sys.exit()
## SET PIPELINES FALSE 

keep=True

if "-f" in sys.argv:
	pos=sys.argv.index("-f")
	fastafile=sys.argv[pos+1]
else:
	sys.exit()
	
if "-i" in sys.argv:
	pos=sys.argv.index("-i")
	idfile=sys.argv[pos+1]
else:
	sys.exit()

if "-r" in sys.argv:
	keep=False


## get IDS
file = open(idfile, "r")
id_list=[]
seen_id={}
for line in file:
	line=line.strip("\n")
	id_list.append(line)
	seen_id[line]=0
#print (id_list)

## PARSE FASTA
file = open(fastafile, "r")
printing=False
for line in file:
	line=line.strip("\n")
	if ">" in line:
		for id in id_list:
			if (keep):
				if "|"+str(id)+"|" in line:
					printing=True
					#sys.stderr.write(line+"\t"+id+"\n")
					break
				else:
					printing=False
			else:
				if id in line:
					printing=False
					break
				else:
					printing=True		
	if (printing):
		print(line)


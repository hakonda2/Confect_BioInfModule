#!/usr/bin/python


import sys


fastafile=sys.argv[1]


file = open(fastafile, "r")
for line in file:
	line=line.strip("\n")
	if ">" in line:
		header=line
	elif (len(line) >= 50):
		print (header)
		print (line)

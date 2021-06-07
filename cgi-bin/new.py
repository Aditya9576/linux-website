#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp

fp = open("/var/www/cgi-bin/mango","r")
x = fp.readline()
fp.close()

if( x == "0"):
	print("yes")
	fp = open("/var/www/cgi-bin/mango","w")
	fp.write("1")
	fp.close()
else:
	print("no")
	fp = open("/var/www/cgi-bin/mango","w")
	fp.write("0")
	fp.close()

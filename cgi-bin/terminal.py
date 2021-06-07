#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess as sp

print('<title>Cloud Shell</title>')
print('<style>body{background:#232729;color:white;font-family:courier;}</style>')


fp = open("/var/www/cgi-bin/mango","r")
flag = fp.readline()
fp.close()
fp = open("/var/www/cgi-bin/mango","w")
fp.write("0")
fp.close()
fip = open("/var/www/cgi-bin/ipaddr.txt","r")
for data in fip:
	ip = data;
if(flag == "0"):
	fp = open("/var/www/cgi-bin/mango","w")
	fp.write("1")
	fp.close()
	fn = open("/var/www/cgi-bin/apple","r")
	print(fn.read())
	fn.close()
	print('<form action="http://{}/cgi-bin/terminal.py">'.format(ip))
	print('<b>[root@localhost]#</b>')
	print('<input type="text" name="a" style="background:#232729;outline:none;color:whitesmoke;font-family:courier;font-weight:bolder;width:50%;border:none;" autofocus>')
	
	print('</form>')
else:
	print('<meta http-equiv="refresh" content="0.5">')
	form = cgi.FieldStorage()
	cmd = form.getvalue("a")
	final = sp.getoutput(cmd)
	if (cmd == "clear"):
		fn = open("/var/www/cgi-bin/apple","w")
		fn.write("")
		fn.close()
	fn = open("/var/www/cgi-bin/apple","a")
	fn.write("[<b>root@localhost]#</b>{}<br>{}<br>".format(cmd,final))
	fn.close()
	fn = open("/var/www/cgi-bin/apple","r")
	print(fn.read())
	fn.close()
	fp = open("/var/www/cgi-bin/mango","w")
	fp.write("0")
	fp.close()


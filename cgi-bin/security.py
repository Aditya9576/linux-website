#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess as sp

form = cgi.FieldStorage()
user = form.getvalue('u')
passwd = form.getvalue('p')


user = "{}\n".format(user)
passwd = "{}\n".format(passwd)

flag1 = 0
flag2 = 0

fu = open("/var/www/cgi-bin/userName.py","r")
fp = open("/var/www/cgi-bin/userPass.py","r")
fip = open("/var/www/cgi-bin/ipaddr.txt","r")

for data in fu:
	if (data == user):
		flag1 = 1

for data in fp:
	if(data == passwd):
		flag2 = 1
for data in fip:
	ip = data
	
fu.close()
fp.close()
fip.close()
if(flag1 == 0):
	print('<script>alert("invalid user name !")</script>')
	#final = sp.getoutput(" /var/www/html/login.html")
	#print(final)
	print('<script>window.open("http://{}/login.html","_self");</script>'.format(ip))
else:
	if(flag2 == 0):
		print('<script>alert("Wrong Password !")</script>')
		#final = sp.getoutput("cat /var/www/html/login.html")
		#print(final)
		print('<script>window.open("http://{}/login.html","_self");</script>'.format(ip))
	else:
		final = sp.getoutput("<script> window.open('http://{}/command_run.html','_self')</script>".format(ip))
		print(final)
	
	


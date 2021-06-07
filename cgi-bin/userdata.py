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

flag= 0

fu = open("/var/www/cgi-bin/userName.py","r")
fip = open("/var/www/cgi-bin/ipaddr.txt","r")
for data in fu:
	if (data == user):
		flag = 1

for data in fip:
	ip = data;

fip.close()
fu.close()

if(flag == 1):
	print('<script>alert("username not available. Try another !")</script>')
	#final = sp.getoutput("cat /var/www/html/signup.html")
	#print(final)
	print('<script>window.open("http://{}/signup.html","_self");</script>'.format(ip));
	
else:
	fu = open("/var/www/cgi-bin/userName.py","a")
	fu.write(user)
	fu.close()
	fp = open("/var/www/cgi-bin/userPass.py","a")
	fp.write(passwd)
	fp.close()
	print('<script>alert("account successfully created !")</script>')
	#final = sp.getoutput("cat /var/www/html/login.html")
	#print(final)
	print('<script>window.open("http://{}/login.html","_self");</script>'.format(ip));



	
	
	
		
	


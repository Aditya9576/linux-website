#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess as sp

a = ["aditya"]
b = ["12345"]

form = cgi.FieldStorage()
user = form.getvalue('u')
passwd = form.getvalue('p')

final = sp.getoutput("cat /var/www/html/login.html")
if(user in a):
	if(passwd in b):
		final = sp.getoutput("cat /var/www/html/command_run.html")
	else:
		print("invalid password")
else:
	print("invalid username")

print(final)

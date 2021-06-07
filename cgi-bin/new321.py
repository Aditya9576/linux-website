#!/usr/bin/python3

print("content-type: text/html")
print()

fp = open("/var/www/cgi-bin/ipaddr","r")
ip = fp.readline()
fp.close()
print('<form action="http://{}/cgi-bin/new123.py">'.format(ip))
print('<input type="text" name="pp" />')
print('<input type="submit" />')
print('</form>')

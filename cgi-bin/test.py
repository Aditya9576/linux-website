#!/usr/bin/python3


print()
import cgi

z = cgi.FieldStorage()
p = z.getvalue('u')
q = z.getvalue('age')
print(p)
print(q)


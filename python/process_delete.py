#!C:\Users\0505z\AppData\Local\Programs\Python\Python36\python.exe
#-*- coding: utf-8 -*-
import sys, os
import codecs
import cgi#common Gateway Interface
import cgitb

#print hangul
cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
pageId = form["pageId"].value
os.remove('data/'+pageId)


#redirection main page
print("Location: index.py")
print()

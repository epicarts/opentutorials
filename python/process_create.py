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
title = form["title"].value
description = form['description'].value


opend_file = open('data/'+title, 'w')
opend_file.write(description)

#
#print("content-type:text/html; charset=UTF-8\n")

#redirection
print("Location: index.py?id="+title)
print()

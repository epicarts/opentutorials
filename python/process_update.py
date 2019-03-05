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
title = form["title"].value
description = form['description'].value

#변경된 파일 저장
opend_file = open('data/'+pageId, 'w')
opend_file.write(description)
opend_file.close()

#파일이름 변경
os.rename('data/'+ pageId, 'data/'+ title)



#print("content-type:text/html; charset=UTF-8\n")

#redirection
print("Location: index.py?id="+title)
print()

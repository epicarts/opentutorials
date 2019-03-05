#!C:\Users\0505z\AppData\Local\Programs\Python\Python36\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import cgi#common Gateway Interface
import cgitb

#print hangul
cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("content-type:text/html; charset=UTF-8\n")


#웹서버가 사용자의 요청에 따라서 파이썬 어플리케이션에 전달하는 여러 데이터
#http://127.0.0.1/cgi_env.py?id=HTML
cgi.test()

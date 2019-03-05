#!C:\Users\0505z\AppData\Local\Programs\Python\Python36\python.exe
#-*- coding: utf-8 -*-
import sys, os
import codecs
import cgi#common Gateway Interface
import cgitb

#print hangul
cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("content-type:text/html; charset=UTF-8\n")

print('\n')
#query string
form = cgi.FieldStorage()
print(form)
print('\n')
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:#without id
    pageId = 'Welcome'
    description = 'Hello web'


files = os.listdir('data')
print(files)
list_str =''
for item in files:
    list_str = list_str + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)


print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>

<body>
  <h1><a href="index.py">WEB</a></h1>
  <ul>
    {list}
  </ul>

  <a href="create.py">create</a>

  <form action="process_update.py" method="post">
      <input type="hidden" name="pageId" value="{form_default_title}">
      <p><input type="text" name="title" placeholder="제목" value={form_default_title}></p>
      <p><textarea rows="4" name="description" placeholder="내용">{form_default_description}</textarea></p>
      <p><input type="submit"></p>
  </form>

  <h2>{title}</h2>
  <p>이페이지는 웹 페이지 입니다</p>
  <p>{desc}</p>
  <p><a href="https://www.w3.org/TR/html52/" title="html5 recommend">링크</a>는 여기로 들어 가세요</p>

  <table>
    <tr>
      <td>head</td>
      <td>98.1%</td>
    </tr>
    <tr>
      <td>body</td>
      <td>97.9</td>
    </tr>
  </table>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/7T7r_oSp0SE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</body>
</html>
'''.format(title=pageId, desc=description, list=list_str, form_default_title=pageId, form_default_description=description))#print end

#!C:\Users\0505z\AppData\Local\Programs\Python\Python36\python.exe
#-*- coding: utf-8 -*-
import sys, os
import codecs
import cgi#common Gateway Interface
import cgitb
import view
import html_sanitizer

sanitizer = html_sanitizer.Sanitizer()


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
    #description secure
    #description = description.replace('<', '&lt;')
    #description = description.replace('<', '&gt;')
    description = sanitizer.sanitize(description)
    #update 값이 있다면 업데이트 링크 생성
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
            <form action="process_delete.py" method="post">
                <input type="hidden" name="pageId" value="{}">
                <input type="submit" value="delete">
            </form>
        '''.format(pageId)
else:#without id
    pageId = 'Welcome'
    description = 'Hello web'
    update_link =''#id 값이 없다면 update 필요없음.
    delete_action =''




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

  {update_link}
  {delete_action}

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
'''.format(title=pageId, desc=description, list=view.getlist(),
           update_link=update_link,delete_action=delete_action))#print end

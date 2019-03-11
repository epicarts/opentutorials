import os
import view
import html_sanitizer


#view list
def getlist():
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('data')
    print(files)
    list_str =''
    for item in files:
        item = sanitizer.sanitize(item)
        list_str = list_str + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return list_str

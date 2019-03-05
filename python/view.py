import os


#view list 
def getlist():
    files = os.listdir('data')
    print(files)
    list_str =''
    for item in files:
        list_str = list_str + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return list_str

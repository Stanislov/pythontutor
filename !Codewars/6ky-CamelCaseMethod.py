''' Заменяем у слов буквы на заглавные, и убираем пробелы. Короткий путь:
return string.title().replace(" ", "")
'''

def camel_case(string):
    string = string.title()

    # убрали пробелы, это можно было сделать и через Replace
    return ''.join(string.split())

a = camel_case('string up len')
print (a)

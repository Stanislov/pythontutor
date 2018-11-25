import requests
import html2text

s=requests.get('http://golos.io')

d = html2text.HTML2Text().handle(s.text)

print(d)

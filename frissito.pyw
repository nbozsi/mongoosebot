import requests
url='https://github.com/nbozsi/mongoosebot/raw/master/test2wild.py'
oldal=requests.get(url)
with open('test2wild.py','wb') as f:
    f.write(oldal.content)

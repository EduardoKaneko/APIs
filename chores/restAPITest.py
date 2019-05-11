import requests

url_test = ['https://rdstation-xerparh.free.beeceptor.com/my/api/path']

for url in url_test:
  r = requests.post(url, data={'welcome': 'Hello, World!'})  
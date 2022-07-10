import urllib, sys
import ssl
import urllib.request

host = 'https://lzagent.market.alicloudapi.com'
path = '/lundroid/agentGet'
method = 'GET'
appcode = '5b6fc19c5281406b9b008c81cb7025ad'
querys = 'targetUrl=http%253A%252F%252F43.226.153.108%252Fcomposite%252Fmytest'
bodys = {}
url = host + path + '?' + querys

request = urllib.request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)
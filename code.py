import json
import getpass
import urllib.request
import urllib.parse

url = "https://its.pku.edu.cn/cas/ITSClient"

headers = [
    ('Host', 'its.pku.edu.cn'),
    ('Content-Type', 'application/x-www-form-urlencoded; charset=utf-8'),
    ('Connection', 'keep-alive'),
    ('Accept', '*/*'),
    ('User-Agent', 'Jipgw'),
    ('Accept-Language', 'zh-Hans-CN;q=1.0'),
    ('Accept-Encoding', 'gzip;q=1.0, compress;q=0.5')
]

openMsg = {
    'app': 'Jipgw1.0',
    'cmd': 'open',
    'ip': '',
    'iprange': 'fee',
    'lang': '',
    'password': '',
    'username': ''
}

closeMsg = {
    'app': 'Jipgw1.0',
    'cmd': 'closeall',
    'lang': '',
    'password': '',
    'username': ''
}

username = input("Your username: ")
password = getpass.getpass("Your password: ")
openMsg['username'] = username
openMsg['password'] = password
closeMsg['username'] = username
closeMsg['password'] = password

select = ''
while True:
    if select == 'o' or select == 'O':
        postData = urllib.parse.urlencode(openMsg).encode('utf-8')
        break
    elif select == 'c' or select == 'C':
        postData = urllib.parse.urlencode(closeMsg).encode('utf-8')
        break
    select = str(input("Open or Close: "))[0]

print("Connecting...", end='', flush=True)

opener = urllib.request.build_opener()
opener.addheaders = headers
ret = opener.open(url, postData)

print("\n\nReturn message: ")
print(json.dumps(json.loads(ret.read().decode('utf-8')),  indent=True, ensure_ascii=False))

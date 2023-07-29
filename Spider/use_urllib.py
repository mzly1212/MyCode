from urllib.request import urlopen

url = 'https://www.bilibili.com/'
response = urlopen(url=url)
print(type(response))
print()
print(response.__dict__)
print()
print(response.headers)
print()

import requests


# raw
r = requests.get('https://api.github.com/events', stream = True)
print(r.raw)
print(r.raw.read(10))

r = requests.get('https://api.github.com/events')

print(r.status_code)
print(r.url)
# print(r.text)
print(r.encoding)
# print(r.json())
# print(r.headers)
print(r.headers.get('content-type'))

# cookies
url = 'https://httpbin.ceshiren.com/cookies'
cookies = {'sla':'vip','nps':'10'}
r = requests.get(url, cookies = cookies)
print(r.text)

# redirects, timeout
r = requests.get('http://www.comm100.com', timeout = 0.1)
print(r.url) # https://www.comm100.com/
print(r.status_code)
print(r.history)
print(r.elapsed)


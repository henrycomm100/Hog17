import requests


# # raw
# r = requests.get('https://api.github.com/events', stream=True)
# # print(r.raw)
# # print(r.raw.read(10))

# # print(r.json())
# print(type(r))
# if type(r) == requests.models.Response:
#     print("yes")

# r = requests.get('https://api.github.com/events')
#
# print(r.status_code)
# print(r.url)
# # print(r.text)
# print(r.encoding)
# # print(r.json())
# # print(r.headers)
# print(r.headers.get('content-type'))
#
# # cookies
# url = 'https://httpbin.ceshiren.com/cookies'
# cookies = {'sla': 'vip', 'nps': '10'}
# r = requests.get(url, cookies=cookies)
# print(r.text)
#
# # redirects, timeout
# r = requests.get('http://www.comm100.com', timeout=0.1)
# print(r.url)  # https://www.comm100.com/
# print(r.status_code)
# print(r.history)
# print(r.elapsed)

# # disallow redirections
# r = requests.get('https://livechat3chatserver.testing.comm100dev.io/bbs.aspx?siteId=10008&planId=c69f3e1a-51f1-42da-a128-38a1c48d1573', allow_redirects=False)
# print(r.request.headers)
# print(r.status_code)
# print(r.headers)
# print(r.history)

# do not specify redirections
r = requests.get('https://livechat3chatserver.testing.comm100dev.io/bbs.aspx?siteId=10008&planId=c69f3e1a-51f1-42da-a128-38a1c48d1573')
print(r.request.headers)
print(r.status_code)
print(r.headers)
print(r.history)


# # allow redirections
# r = requests.get('https://livechat3chatserver.testing.comm100dev.io/bbs.aspx?siteId=10008&planId=c69f3e1a-51f1-42da-a128-38a1c48d1573', allow_redirects=True)
# print(r.request.headers)
# print(r.status_code)
# print(r.headers)
# print(r.history)
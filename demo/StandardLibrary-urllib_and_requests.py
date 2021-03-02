

import urllib.request

# This function always returns an object which can work as a context manager and has the properties url, headers, and status. See urllib.response.addinfourl for more detail on these properties.
# For HTTP and HTTPS URLs, this function returns a http.client.HTTPResponse object slightly modified.
response = urllib.request.urlopen("https://www.baidu.com")
print(response.url)
print(response.headers)
print(response.status)
# print(response.read())



# 更加推荐使用Requests包 https://requests.readthedocs.io/en/master/
import requests

response = requests.get("https://www.baidu.com")
print(response.status_code)
print(response.encoding)
print(response.url)
print(response.request)
print(response.cookies)
print(response.elapsed)

r = requests.post("http://httpbin.org/post", data={'key':'value'})
print(f"this is a POST response with status code {r.status_code}")
print(r.text)
r.encoding = "utf-8"
print(r.text)

# 系统模块
import sys
import os
import time
import re
import random
import json

# 第三方模块, 可以通过 pip install * 来安装
import yaml
import requests

# 自定义模块
# from baidu import search, hello, Person
from baidu import *

search()

hello
print(hello)

Person()

print(dir())  # 找出当前模块定义的对象
print(dir(time))  # 找出当前参数模块的对象

time.sleep(3)

print(sys.path)

print("test commit")

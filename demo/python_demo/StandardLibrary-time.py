import time

print(time.asctime())
print(time.time())  # 返回Unix时间戳
# time.sleep(2)
print(time.localtime())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 将当前的时间戳转换成带格式的时间

# 如何显示两天前的时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime((time.time() - 60 * 60 * 24 * 2))))

now_timestamp = time.time()
twodayago_timestamp = now_timestamp - 60*60*24*2
twodayago_timeTuple = time.localtime(twodayago_timestamp)
print(time.strftime("%Y-%m-%d %H:%M:%S", twodayago_timeTuple))
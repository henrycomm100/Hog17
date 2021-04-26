import time

print(time.asctime())
print(time.time())
# time.sleep(2)
print(time.localtime())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 如何显示两天前的时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime((time.time() - 60 * 60 * 24 * 2))))

now_timestamp = time.time()
twodayago_timestamp = now_timestamp - 60*60*24*2
twodayago_timeTuple = time.localtime(twodayago_timestamp)
print(time.strftime("%Y-%m-%d %H:%M:%S", twodayago_timeTuple))
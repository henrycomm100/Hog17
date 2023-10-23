# using time module
import time
 
# ts stores the time in seconds
ts = time.time()
 
# print the current timestamp
print(ts)

ts_13 = int(round(ts * 1000))
print(ts_13)


def get_current_timestamp():
    return int(round(time.time() * 1000))

print('get function:', get_current_timestamp())
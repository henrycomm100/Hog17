# using time module
import datetime
import time

import pytz
 
# ts stores the time in seconds
ts = time.time()
 
# print the current timestamp
print(ts)

ts_13 = int(round(ts * 1000))
print(ts_13)


def get_current_timestamp():
    return int(round(time.time() * 1000))

print('get function:', get_current_timestamp())

# get current utc time
def get_current_datetime():
    return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

print('get_current_datetime:', get_current_datetime())

print(datetime.datetime.utcnow())
print(datetime.datetime.utcnow().date())
print(datetime.datetime.utcnow().time())
print(datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
print(type(datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')))
# "SubmitTime":"2023-10-24T07:30:00.8744526Z"


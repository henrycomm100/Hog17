import datetime
from faker import Faker

# get current datetime in UTC
# def get_current_datetime():
#
#     return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
#
# print(get_current_datetime())

# print(datetime.datetime.utcnow())

# fake = Faker(locale='zh_CN')
fake = Faker()
# print(fake.street_name())
# print(fake.phone_number())
# print(type(fake.phone_number()))
# print(fake.name())
# print(type(fake.name()))
print(fake.domain_name())
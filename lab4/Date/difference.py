import datetime

a = datetime.datetime.now()
b = datetime.datetime.now().replace(hour=10)

print((a - b).total_seconds())

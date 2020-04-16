import datetime
d1 = datetime.datetime(2020,1,1)
d2 = datetime.datetime(2020,4,1)
diff = d2-d1
print(diff)

d3=d2+datetime.timedelta(days=100)
print(f'日期是{d3}')
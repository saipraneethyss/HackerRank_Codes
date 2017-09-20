import calendar
dateval = list(map(int,input().split()))
print((calendar.day_name[calendar.weekday(dateval[2], dateval[0], dateval[1])]).upper())

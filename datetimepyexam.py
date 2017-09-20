from datetime import datetime
date_format = "%a %d %b %Y %H:%M:%S %z"
for i in range(int(input())):
    print(int(abs((datetime.strptime(input(),date_format)-datetime.strptime(input(),date_format)).total_seconds())))
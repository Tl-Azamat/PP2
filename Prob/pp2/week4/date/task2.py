import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print('Yesterday is : ', yesterday)
print('Today is : ', today)
print('Tomorrow is : ' ,tomorrow)
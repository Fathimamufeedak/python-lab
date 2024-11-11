from datetime import datetime,timedelta
today=datetime.now()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print("yesterday:",yesterday.strftime("%y-%m-%d"))
print("today:",today.strftime("%y-%m-%d"))
print("tomorrow:",tomorrow.strftime("%y-%m-%d"))

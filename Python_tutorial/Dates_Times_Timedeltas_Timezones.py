import datetime

#print a specific date
time = datetime.date(2016, 7, 24)
print(time)

#current today of a week
#weekday() - Monday 0 - Sunday 6
#isoweekday() - Monday 1 - Sunday 7
tday = datetime.date.today()
print(tday.weekday())
print(tday.isoweekday())

#tdelta() for search a date n days before/after today
tdelta = datetime.timedelta(days=7)
#what's the day a week ago
print(tday - tdelta)
#what's the day a week later
print(tday + tdelta)
#How many times passed since the bday
bday = datetime.date(2016, 9, 24)
till_bday = bday - tday
print(till_bday)

#print out a specific element of the date
today = datetime.datetime(2020, 4, 23, 4, 55, 50, 100000)
#year right now
print(today.year)
#hour right now
print(today.hour)

#date of a specific time after a week
dt = datetime.datetime(2023, 2, 20, 4, 58, 45, 100000)
tdelta1 = datetime.timedelta(days=7)
print(dt + tdelta1)

#utc time currently
dt_utc = datetime.datetime.utcnow()
print(dt_utc)

#current time
dt_now = datetime.datetime.now()
print(dt_now)

#time today
dt_today = datetime.datetime.today()
print(dt_today)

#timezone practice
#import pytz
#dt_utcnow = datetime.datetime.now(tz=pytz.UTC)

#current time at Vancouver Canada
#dt_pst = dt_utcnow.astimezone(pytz.timezone(''))
#print(dt_pst)
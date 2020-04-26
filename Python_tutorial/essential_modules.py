#system related like PATH in environment variable
import sys
#current date
import datetime
#calendar related function like isleap() for leap year checkup
import calendar
#mathematic calculation like Pi, rad
import math
#os related function
import os

print(sys.path)

print(math.radians(27))

print(datetime.date.today())

print(calendar.isleap(2020))

print(calendar.isleap(2017))

print(os.getcwd())
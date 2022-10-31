from datetime import datetime, timedelta, timezone
import pytz
from dateutil import tz

dt = datetime.now(tz=timezone.utc)
print("Current UTC time:", dt)

ind_tz = dt.astimezone(pytz.timezone('Asia/Kolkata'))
print("Current IST Time:", ind_tz)
print()

# American current time
# amc_tz = dt.astimezone(pytz.timezone('America/New_York'))
# print(amc_tz)

takeoff_time = input("Enter the Takeoff Time (HH:MM:SS:MS):")
l = takeoff_time.split(':')
# Takeoff time as per IST
takeoff = ind_tz.replace(hour=int(l[0]), minute=int(l[1]), second=int(l[2]), microsecond=int(l[3]))
print("Takeoff Time as per IST:", takeoff)

# Landing Time as per IST
l_dt = takeoff + timedelta(hours=6)
print("Landing Time as per IST:", l_dt)
print()

america_dt = l_dt.astimezone(pytz.timezone('America/New_York'))
print("Landing Time in USA:", america_dt)

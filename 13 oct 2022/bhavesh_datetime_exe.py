from datetime import datetime, timedelta, timezone
from dateutil import tz

current_time = datetime.now()
print("Current Time ", current_time)

utc_dt = datetime.utcnow()
print("Universal Time ", utc_dt)

dt_input = input("Enter the time (HH:MM:SS): ")
l = dt_input.split(':')


amc_dt = tz.gettz('America/New_York')
# takeoff time as per IST
takeoff_time = current_time.replace(hour=int(l[0]),minute=int(l[1]),second=int(l[2]))

# landing time as per IST
lt = takeoff_time + timedelta(hours=6)

print("Takeoff Time: ", takeoff_time)
print("Landing Time: ", lt)

america_dt = lt.astimezone(amc_dt)
print("Landing time in America:", america_dt)



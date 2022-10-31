'''
Exercise 5
Print the date and time together in the form: mm/dd/yyyy hh:mm:ss.
'''
import datetime
date_time = datetime.datetime.now()

result = date_time.strftime("%m/%d/%Y %H:%M:%S")
print(result)
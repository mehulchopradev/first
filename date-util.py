import datetime
from datetime import date
import calendar


# a function that will return only the current date
def date_func():
  return (str(datetime.datetime.today().day))

# a function that will return the current year
def year_func():
  return (str(datetime.datetime.today().year))

# a function that will return the timestamp
def func_timestamp():
  return datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

  

# a function that will return the current month
def month_func():
  return (str(datetime.datetime.today().month))


# a function that will return me the current day of week(sunday-Saturday)
def weekday_func(date.today()):
  my_date=date.today()
  return calendar.day_name[my_date.weekday()] 


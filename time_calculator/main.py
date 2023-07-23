from time_calculator import add_time
from unittest import main

print(add_time("3:00 PM", "3:10"),"# Returns: 6:10 PM")
print(add_time("11:30 AM", "2:32", "Monday"),"# Returns: 2:02 PM, Monday")# Returns: 2:02 PM, Monday
print(add_time("11:43 AM", "00:20"),"# Returns: 12:03 PM")# Returns: 12:03 PM
print(add_time("10:10 PM", "3:30"),"# Returns: 1:40 AM (next day)")# Returns: 1:40 AM (next day)
print(add_time("11:43 PM", "24:20", "tueSday"),"# Returns: 12:03 AM, Thursday (2 days later)")# Returns: 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12"),"# Returns: 7:42 AM (9 days later)")# Returns: 7:42 AM (9 days later)
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("11:40 AM", "0:25"))


#!/usr/bin/env python3

'''
OPS445 Assignment 1 
Program: assignment1.py 
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Author: Bassil Akar
Semester: Fall 2024
Description: 
'''

import sys

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def mon_max(month: int, year: int) -> int:
    "Return the maximum number of days in a given month, accounting for leap years."
    mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        return 29
    return mon_dict[month]

def after(date: str) -> str: 
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function has been tested to work for year after 1582
    '''
    year, mon, day= (int(x) for x in date.split('-'))
    day += 1  # next day

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year
    
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    
    if day > mon_max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{year}-{mon:02}-{day:02}"

def before(date: str) -> str:
    "Return the previous day's date in YYYY-MM-DD format."
    year, mon, day = (int(x) for x in date.split('-'))
    day -= 1 
    if day < 1:
        mon -= 1
        if mon < 1:
            mon = 12
            year -= 1
        day = mon_max(mon, year)
    return f"{year}-{mon:02}-{day:02}"

def usage():
    "Print a usage message to the user and exit."
    print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD division")
    return

def valid_date(date: str) -> bool:
    """Check validity of date"""
    try:
        # Split date string into components
        components = date.split('-')
        if len(components) != 3:
            print("Usage: ./assignment1.py YYYY-MM-DD division")           
            return False  # Ensure the format is strictly YYYY-MM-DD

        year, mon, day = (int(x) for x in components)

        # Validate year range
        if year < 1000 or year > 9999:
            print("Usage: ./assignment1.py YYYY-MM-DD division")
            return False

        # Validate month range
        if mon < 1 or mon > 12:
            print("Error: wrong month entered")
            usage()
            return False  # Prevent usage message duplication

        # Validate the range for day using mon_max
        if day < 1 or day > mon_max(mon, year):
            print("Error: wrong day entered")
            usage()
            return False

    except ValueError:
        # Catch cases where conversion to int fails
        usage()
        return False
    except TypeError:
        usage()
        return False

    # If it passes all checks, the date is valid
    return True

def dbda(start_date: str, days: int) -> str:
    "given a start date and a number of days into the past/future, give date"
    current_date = start_date
    count = 0

    if days > 0:
        while count < days:
            current_date = after(current_date) #go to next day (positive)
            count += 1 #increase count
    elif days < 0:
        while count > days: 
            current_date = before(current_date) 
            count -= 1  # decrease count (negative)

    return current_date



if __name__ == "__main__":
    #make sure there is only 3 command-line arg.
    if len(sys.argv) != 3:
        usage()
        exit()

    start_date = sys.argv[1]   #use first arg for the start_date
    try:
        divisor = int(sys.argv[2])
        if divisor == 0:
            usage()
            exit()
    except ValueError:
        usage()
        exit()

    if not valid_date(start_date):
        exit()  # Exit if date is invalid

    days = round(365 / divisor)
    print(f"A year divided by {divisor} is {days} days.")

    #calculating the past/future date by subtracting and adding days.
    past_date = dbda(start_date, -days)
    future_date = dbda(start_date, days)

    print(f"The date {days} days ago was {past_date}.")
    print(f"The date {days} days from now will be {future_date}.")

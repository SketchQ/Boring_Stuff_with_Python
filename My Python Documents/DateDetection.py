## Date Detection Project from the book
##  DD/MM/YYYY is the date format we're trying to detect
## days : 01-31 months : 01-12 years : 1000-2999 | If the day or month is a single digit it'll have a leading zero
## For invalid dates like 31/02/1990 write an additional program to detect this. 
## April,June,September and November has 30 days, February has 28 days rest are 31 days
## February has 29 day every four years, Leap years are every year evenly divisiable by 4.
## except for years evenly divisable by 100, unless the year is also divisable by 400.
## eg. year 2000 was a leap year, but 1900 1800 and 1700 were not. Becouse they were not divisable by 400. Even when they were divisable by 100 and 4.

import pyperclip,re

pattern = re.compile(r'([0-3]\d)/([01]\d)/([0-2]\d{3})')

text = pyperclip.paste()
valid_dates = []

if pattern.findall(text):
    for day,month,year in pattern.findall(text):

        date = f'{day}/{month}/{year}'
        day,month,year = map(int,[day,month,year])
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 100 and year % 400 == 0)
        r_year = r_month = r_day = str()

        if day not in range(1,31):
            r_day = f'day in this {date} is not valid.'

        if month not in range(1,13):
            r_month = f'month in this {date} is not valid.'
        elif month in [3,6,9,11] and day >30:
            r_month = f'Month in this {date} can not have that many days.'
        elif month == 2:
            if day > 28 and not leap_year:
                r_month = f'February is not leap in {date} and can not have more than 28 days.'
            elif day > 29 and leap_year:
                r_month = f'February is leap in {date} and can not have more than 29 days.'

        if year not in range(1000,3000):
            r_year = f'year in this {date} is out of range.'

        if not (r_year or r_month or r_day):
            print(f'{date} was found and add to your clipboard\n')
            valid_dates.append(date)
        else:
            if r_year:
                print(f'The date {date} was found but is not valid becouse: \n {r_year}\n')
            elif r_month:
                print(f'The date {date} was found but is not valid becouse: \n {r_month}\n')
            elif r_day:
                print(f'The date {date} was found but is not valid becouse: \n {r_day}\n')
    pyperclip.copy('\n'.join(valid_dates))
else:
    print('no Match found...')    

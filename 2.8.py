from datetime import date

year = 2015

mounth = 2
first_date = date(year, mounth, 25).weekday()
print(first_date)
print(date(year, mounth, 1 + abs(first_date-3) + 21).strftime('%d.%m.%y'))

4 + 6
5 + 5
6 + 4
7 + 3
1 + 2
2 + 1
3 + 0
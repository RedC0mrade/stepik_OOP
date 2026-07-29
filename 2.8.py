from datetime import date

year = int(input())

mounth = int(input())
same_date = []
for day in range(1, 32):
    try:
        my_date = date(year, mounth, day)

        if my_date.strftime('%A') == "Thursday":
            same_date.append(my_date)
    except ValueError:
        break

print(same_date[3].strftime('%d.%m.%y'))
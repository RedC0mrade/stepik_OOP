from datetime import date


def last_thursday(year: int, mounth: int) -> str:
    my_date = date(year, mounth, 1)
    first_thursday = (4 - my_date.isoweekday()) % 7
    return date(year, mounth, 1 + first_thursday + 21).strftime("%d.%m.%Y")


print(last_thursday(int(input()), int(input())))

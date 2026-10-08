class HourClock:

    def __init__(self, hours: int):
        
        self._hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if isinstance(hours, int) and 0 < hours < 13:
            self._hours = hours
        else:
            raise ValueError("Некорректное время")
    
    hours = property(get_hours, set_hours)


# INPUT DATA:

# TEST_1:
time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)

# TEST_2:
time = HourClock(7)

try:
    time.hours = 15
except ValueError as e:
    print(e)

# TEST_3:
try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)

# TEST_4:
try:
    HourClock(0)
except ValueError as e:
    print(e)

# TEST_5:
try:
    HourClock('ten o`clock')
except ValueError as e:
    print(e)

# TEST_6:
time = HourClock(1)

print(time.hours)
for _ in range(11):
    time.hours += 1
    print(time.hours)

# TEST_7:
time = HourClock(1)
print(hasattr(HourClock, 'hours'))

import sys

text = [eval(i) for i in sys.stdin]

[print(-90 <= i[0] <= 90 and -180 <= i[1] <= 180) for i in text]

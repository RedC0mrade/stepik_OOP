from math import floor
number = 5

# 1 1 1 1 1
# 1 2 2 2 1
# 1 2 3 2 1
# 1 2 2 2 1
# 1 1 1 1 1

# 1 1 1 1 1 1
# 1 2 2 2 2 1
# 1 2 3 3 2 1
# 1 2 3 3 2 1
# 1 2 2 2 2 1
# 1 1 1 1 1 1

matrix = [[1]*number for _ in range(number)]
max = floor(number / 2)

for i in range(number):
    for j in range(number):
        if j >= matrix[i][j]:
            matrix[i][j] = j+1

print(*matrix, sep="\n")

# 0 1 2 3 4
# 1 2 3 4 5
# 1
# 2
# 3
# 4
# 5
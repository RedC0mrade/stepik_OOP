number = int(input())
matrix = [[0]*number for _ in range(number)]
flag_up = 0
flag_down = number + 1
for i in range(number):
    flag_down -= 1
    for j in range(number):
        if i <= j and i < number - j:
            matrix[i][j] = i + 1
        elif i > j and i < number - 1 - j:
            matrix[i][j] = j + 1
        elif i < j and i > number - 1 - j:
            matrix[i][j] = number - j
        elif i >= j and i >= number - j - 1:
            matrix[i][j] = number - i
    
for i in matrix:
    print(*i, sep=' ')

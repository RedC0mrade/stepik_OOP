n = [["."] * 8 for _ in range(8)]
n[4][5]="N"
for i in range(8):
    for j in range(8):

        print(n[i][j], end=' ')
    print()

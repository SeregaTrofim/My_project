#На вход программе подаются два натуральных числа n и m.
#Программа создает матрицу размером n×m, заполняя её "диагоналями".
s = [int(num) for num in input().split()]
n = s[0]
m = s[1]
matrix = [[0] * m for i in range(n)]

x = -1
c = 1
while x <= n * m:
    x += 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i + j == x and i <= x and j <= x:
                matrix[i][j] = c
                c += 1

for raw in matrix:
    for el in raw:
        print(str(el).ljust(3), end='')
    print()
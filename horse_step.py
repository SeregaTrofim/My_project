matrix = [['.'] * 8 for i in range(8)]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
digits = list(range(1, 9))
Flag = False
print('Введите координаты шахматного поля')
while Flag != True:
    xy = input()
    if xy[0] not in letters or int(xy[1]) not in digits:
        print('Введите корректные координаты шахматного поля')
    else:
        Flag = True

y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])
matrix[y][x] = 'N'

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        inx = (x - j) * (y - i)
        if inx == 2 or inx == -2:
            matrix[i][j] = '*'

for raw in matrix:
    for el in raw:
        print(el, end=' ')
    print()
x = input()
print('Введите 2 целых числа через пробел, а я нарисую числовую змейку')
s = [int(num) for num in input().split()]
n = s[0]
m = s[1]
l = [[0] * m for i in range(n)]

i = 1
x = 0
y = -1
d_row = 0
d_col = 1
while i <= m * n:
    if 0 <= x + d_row < n and 0 <= y + d_col < m and l[x + d_row][y + d_col] == 0:
        x += d_row
        y += d_col
        l[x][y] = i
        i += 1
    else:
        if d_col == 1:
            d_col = 0
            d_row = 1
        elif d_row == 1:
            d_row = 0
            d_col = -1
        elif d_col == -1:

            d_col = 0
            d_row = -1
        elif d_row == -1:
            d_row = 0
            d_col = 1
for i in l:
    print(*i)
x = input()
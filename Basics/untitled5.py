# -*- coding: utf-8 -*-
import random
n = int(input('Введите размер матрицы: '))
arr = [[0 for j in range(n)] for i in range(n)]  
for i in range(0, n):
    for j in range(0, n):
        arr[i][j] = random.choice([-1, 1])
        print(arr[i][j], sep=' ', end=' ')
    print()
p = 1
s = 0
print('Полученная матрица:')
for i in range(0, n):
    for j in range(0, n):
        p = (arr[i][j] * arr[(i + 1) % n][j]) + (arr[i][j] * arr[i][(j + 1) % n])
        print(p, sep=' ', end=' ')
    print()
#print('Значения произведений =', lst)
#print('Неповторяющиеся значения =', set(lst))
for i in set(lst):
    s += i
#print('Сигма =', s)
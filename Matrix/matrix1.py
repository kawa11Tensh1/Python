import random

n = int(input('Введите размер матрицы: '))
m = [-1, 1]
A = [[0 for j in range(n)] for i in range(n)] 
for i in range(0, n):
    for j in range(0, n):
        A[i][j] = random.choice(m)
        print('{:>2d}'.format(A[i][j]), end=' ')
    print()
    
s = 0
B = [[0 for j in range(n)] for i in range(n)] 
print('Полученная матрица: ')
for i in range(0, n):
    for j in range(0, n):
        B[i][j] = (A[i][j] * A[(i + 1) % n][j]) + (A[i][j] * A[i][(j + 1) % n])
        s += B[i][j]
        print('{:>2d}'.format(B[i][j]), end=' ')
    print()
print('Сигма =', s)
import time
import random
import numpy as np
from matplotlib import pyplot as plt

n = int(input('Введите размер матрицы: '))
k = int(input('Введите число итераций: '))
operation = int(input('Шахматная матрица / Однотонная матрица:\n Введите 1 или 2: '))
print('\n')

values = [-1, 1]
T = 0.8

A = np.zeros((n, n))
for i in range(0, n):
    for j in range(0, n):
        A[i][j] = random.choice(values)

# Включить интерактивный режим для анимации
plt.ion()   

for i in range(k):
    print('Итерация:', i + 1, end='\n')
    
    C = A.copy()
    B = A.copy()
    B[random.randint(0, n - 1)][random.randint(0, n - 1)] *= -1
    sum1 = 0
    sum2 = 0
    
    for i in range(n):
        for j in range(n):
            sum1 += A[i][j] * A[(i + 1) % n][j] + A[i][j] * A[i][(j + 1) % n]
            sum2 += B[i][j] * B[(i + 1) % n][j] + B[i][j] * B[i][(j + 1) % n]
    
    if operation == 1:
        dif = sum2 - sum1 
    else:
        dif = sum2 - sum1
        dif = -dif

    if dif <= 0:
        A = B.copy() # Принимаем новую конфигурацию
    else:
        W = np.exp(-dif / T)
        P = random.uniform(0, 1) # Выбрасываем случайное число
        if P > W: 
            A = C.copy() # Возвращаем предыдущую конфигурацию
        elif P <= W:
            A = B.copy() # Принимаем новую конфигурацию
          
    # Очистить текущую фигуру
    plt.clf()

    # Отобразить матрицу
    plt.imshow(A, origin='lower', cmap='plasma', extent=(0, n, 0, n))

    # Следующие два вызова требуются для обновления матрицы
    plt.draw()
    plt.gcf().canvas.flush_events()

    # Задержка перед следующим обновлением
    time.sleep(0.02)
    
# Отключить интерактивный режим по завершению анимации
plt.ioff()

# Нужно, чтобы матрица не закрывалась после завершения анимации
plt.show()
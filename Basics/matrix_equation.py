# Решение системы уравнений

# 2x1 + 3x2 - x3 = 9
# x1 - 2x2 + x3 = 3
# x1 + 2x3 = 2

# (2  3 -1)   (x1)   (9)
# (1 -2  1) * (x2) = (3)
# (1  0  2)   (x3)   (2)

# (4; 0; -1)

import numpy as np
x = np.array([[2, 3, -1], [1, -2, 1], [1, 0, 2]])
y = np.array([9, 3, 2])
deter = round(np.linalg.det(x))
ans = np.linalg.solve(x, y)
print(ans)
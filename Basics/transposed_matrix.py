# Транспонированная матрица

# |2  3 -1|    | 2  1  1|
# |1 -2  1| -> | 3 -2  0|
# |1  0  2|    |-1  1  2|

import numpy as np
x = np.array([[2, 3, -1], [1, -2, 1], [1, 0, 2]])
x_transposed = x.T
print(x_transposed)


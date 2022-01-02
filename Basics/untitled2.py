import random
a, b = map(int, input().split())
c = [[random.randint(0, 101)] * a for i in range(b)]
print(c)
import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = math.isqrt(n)
    if a**2 == n:
        a -= 1

    print(a)
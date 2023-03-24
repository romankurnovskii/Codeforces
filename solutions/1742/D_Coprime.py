import math

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    ss = [-1] * 1001
    for i in range(n):
        ss[s[i]] = i
    res = -1
    for i in range(1, 1001):
        if ss[i] == -1:
            continue
        for j in range(i, 1001):
            if ss[j] != -1 and math.gcd(i, j) == 1:
                res = max(res, ss[i] + ss[j] + 2)
    print(res)

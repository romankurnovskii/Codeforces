def solve():
    n = int(input())
    a = sorted(map(int, input().split()))
    res = float("inf")

    if n == 1:
        res = abs(a[0] - a[1])
    else:
        if n == 2:
            res = min(res, sum(abs(x - 2) for x in a))
        if n % 2 == 0:
            res = min(res, sum(abs(x + 1) for x in a[:-1]) + abs(a[-1] - n))
        res = min(res, sum(abs(x) for x in a))

    print(res)


for _ in range(int(input())):
    solve()

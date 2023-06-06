def solve():
    n, _ = map(int, input().split())

    res = []
    a = [i + 1 for i in range(n // 2)]
    b = [i for i in range(n, n // 2, -1)]

    for i in range(n // 2):
        res.append(b[i])
        res.append(a[i])
    if n % 2:
        res.append(b[-1])
    print(*res)


for _ in range(int(input())):
    solve()

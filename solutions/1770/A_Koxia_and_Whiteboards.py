def solve():
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(m):
        a.sort(reverse=True)
        a = a[: n - 1] + [b[i]]
    print(sum(a))


for _ in range(int(input())):
    solve()

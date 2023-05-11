def solve():
    a, b, c, d = list(map(int, input().split()))
    if d < b or a + d - b - c < 0:
        print(-1)
    else:
        result = d - b + abs(a + d - b - c)
        print(result)


for _ in range(int(input())):
    solve()

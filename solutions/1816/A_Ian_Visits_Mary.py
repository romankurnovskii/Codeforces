def solve():
    a, b = map(int, input().split())
    if a > 0:
        print(2)
        print(a - 1, 1)
        print(a, b)
    else:
        print(2)
        print(1, 1)
        print(a, b)


for _ in range(int(input())):
    solve()

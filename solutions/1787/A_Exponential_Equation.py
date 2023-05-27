def solve():
    n = int(input())
    if n == 2:
        print(1, 1)
    elif n % 2 == 0:
        print(1, n // 2)
    else:
        print(-1)


for _ in range(int(input())):
    solve()

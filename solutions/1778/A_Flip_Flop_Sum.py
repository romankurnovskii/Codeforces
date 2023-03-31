def solve():
    n = int(input())
    ar = list(map(int, input().split()))
    res = sum(ar)

    for i in range(n-1):
        if ar[i] == ar[i+1] == -1:
            print(res + 4)
            return
    if res == n:
        res -= 4
    print(res)

for _ in range(int(input())):
    solve()
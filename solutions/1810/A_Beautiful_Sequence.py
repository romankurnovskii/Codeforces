def solve():
    n = int(input())
    ar = list(map(int, input().split()))
    for i in range(n):
        if ar[i] <= i + 1:
            print("YES")
            return
    print("NO")


for _ in range(int(input())):
    solve()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(0, n, 2):
        if i == n - 1:
            print("YES")
            return
        if i == n - 2:
            if a[i] <= a[i + 1]:
                print("YES")
            else:
                print("NO")
            return

        a[i + 2] -= a[i + 1] - a[i]

    print("YES")


for _ in range(int(input())):
    solve()

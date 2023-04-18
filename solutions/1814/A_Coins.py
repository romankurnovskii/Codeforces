def solve():
    n, k = map(int, input().split())

    if n % 2 == 0:
        print("YES")
    elif n >= k and k % 2 == 1:
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    solve()

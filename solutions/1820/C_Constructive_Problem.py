def solve():
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)
    mex = 0

    for i in b:
        if i == mex:
            mex += 1
        elif i > mex:
            break

    if mex == n:
        print("No")
        return

    L = n
    R = -1

    if mex + 1 not in a:
        print("Yes")
        return

    for i in range(n):
        if a[i] == mex + 1:
            L = min(L, i)
            R = max(R, i)

    b = a[:L] + [mex] + a[R + 1 :]
    b.sort()
    mex2 = 0

    for i in b:
        if i == mex2:
            mex2 += 1
        elif i > mex:
            break

    print("Yes" if mex2 == mex + 1 else "No")


for _ in range(int(input())):
    solve()

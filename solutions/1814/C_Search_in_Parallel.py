def solve():
    n, s1, s2 = map(int, input().split())
    R = list(map(int, input().split()))
    S = sorted(range(n), key=lambda i: -R[i])

    A, B = [], []
    a, b = 0, 0
    for i in S:
        k = R[i]
        if (a + s1) * k <= (b + s2) * k:
            A.append(i + 1)
            a += s1
        else:
            B.append(i + 1)
            b += s2

    print(len(A), *A)
    print(len(B), *B)


for _ in range(int(input())):
    solve()

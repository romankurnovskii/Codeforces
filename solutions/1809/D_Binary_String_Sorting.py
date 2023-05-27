def solve():
    s = input().strip()
    n = len(s)
    c0 = s.count("0")
    c1 = 0
    res = c0 * (10**12 + 1)

    for i in range(n - 1):
        if s[i] == "1":
            c1 += 1
        else:
            c0 -= 1

        if s[i] == "1" and s[i + 1] == "0":
            res = min(res, (c0 + c1 - 2) * (10**12 + 1) + 10**12)
        else:
            res = min(res, (c0 + c1) * (10**12 + 1))

    res = min(res, s.count("1") * (10**12 + 1))
    print(res)


for _ in range(int(input())):
    solve()

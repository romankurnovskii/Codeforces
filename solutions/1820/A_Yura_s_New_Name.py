def solve():
    s = input()
    res = 0

    if len(s) == 1:
        res = 1 if s[0] == '^' else 2
    else:
        if s[0] == '_':
            res += 1

        gap = 0
        for c in s:
            if c == '_':
                gap += 1
            else:
                res += max(0, gap - 1)
                gap = 0

        res += max(0, gap - 1)

        if s[-1] == '_':
            res += 1

    print(res)


for _ in range(int(input())):
    solve()

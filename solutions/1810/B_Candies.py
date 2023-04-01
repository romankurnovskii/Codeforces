def solve():
    n = int(input())

    if n % 2 == 0:
        print(-1)
        return

    res = []
    while n != 1:
        if (n + 1) // 2 % 2 == 1:
            n += 1
            res.append(1)
        else:
            n -= 1
            res.append(2)
        n //= 2

    res.reverse()
    print(len(res))
    print(' '.join(map(str, res)))

for _ in range(int(input())):
    solve()

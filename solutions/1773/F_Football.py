def solve():
    n = int(input())  # number of matches
    a = int(input())  # goals scored
    b = int(input())  # goals conceded

    if n == 1:
        if a == b:
            print(1)
        else:
            print(0)
        print(f"{a}:{b}")
        return

    matches = [[0, 0] for _ in range(n + 1)]
    draw = 0
    match = 1

    while match <= n and a > 0:
        a -= 1
        matches[match] = [1, 0]
        match += 1

    if a > 0:
        matches[1] = [matches[1][0] + a, 0]

    if b > 0:
        if match == n + 1:
            matches[1][0] += 1
            matches[n][0] -= 1
            matches[n][1] = b
        else:
            while match <= n and b > 0:
                b -= 1
                matches[match][1] += 1
                match += 1

            if b > 0:
                matches[n][1] += b

    for i in range(1, n + 1):
        if matches[i][0] == matches[i][1]:
            draw += 1

    print(draw)
    for i in range(1, n + 1):
        print(f"{matches[i][0]}:{matches[i][1]}")


solve()

def solve():
    n = int(input())
    s = input()
    counter = 1
    res = [1]

    for i in range(1, n - 1):
        if s[i] == s[i - 1]:
            counter += 1
        else:
            counter = 1
        res.append(i + 2 - counter)

    print(*res)


for _ in range(int(input())):
    solve()

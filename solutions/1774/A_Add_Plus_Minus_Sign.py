def solve():
    n = int(input())
    s = input()

    num = int(s[0])
    res = []
    for i in range(1, n):
        if num > 0:
            res.append("-")
            num -= int(s[i])
        else:
            res.append("+")
            num += int(s[i])
    print("".join(res))


for _ in range(int(input())):
    solve()

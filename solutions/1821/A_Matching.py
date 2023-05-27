def solve():
    s = input().strip()

    if s[0] == "0":
        print(0)
        return

    res = 1
    for i, char in enumerate(s):
        if char == "?":
            res *= 9 if i == 0 else 10

    print(res)


for _ in range(int(input())):
    solve()

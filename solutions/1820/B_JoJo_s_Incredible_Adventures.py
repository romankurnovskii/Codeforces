import math


def solve():
    s = input()
    n = len(s)

    if "0" not in s:  # If string contains only '1's
        print(n * n)
        return

    s += s  # for cyclic shift handling
    max_group = 0
    curr_group = 0

    for c in s:
        if c == "1":
            curr_group += 1
            max_group = max(max_group, curr_group)
        else:
            curr_group = 0

    max_group += 1
    max_area = math.ceil(max_group / 2) * (max_group // 2)
    print(max_area)


for _ in range(int(input())):
    solve()

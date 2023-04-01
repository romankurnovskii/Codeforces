def luck(n):
    digits = [int(d) for d in str(n)]
    return max(digits) - min(digits)

def solve():
    l, r = map(int, input().split())
    res = l
    max_luck = luck(l)

    for i in range(l + 1, min(r + 1, l + 101)):
        curr_luck = luck(i)
        if curr_luck > max_luck:
            max_luck = curr_luck
            res = i

        if max_luck == 9:
            break

    print(res)

for _ in range(int(input())):
    solve()

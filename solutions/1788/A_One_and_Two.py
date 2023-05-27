def solve(ar):
    twos = ar.count(2)
    if twos % 2 != 0:
        return -1

    passed_twos = 0
    need_twos = twos // 2
    for i, x in enumerate(ar):
        if x == 2:
            passed_twos += 1
        if passed_twos == need_twos:
            return i + 1


t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    print(solve(ar))

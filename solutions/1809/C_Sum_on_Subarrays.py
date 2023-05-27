def solve(n, k):
    res = [-1000] * n
    if k == 0:
        return " ".join(map(str, res))

    for i in range(n):
        possible = (i + 1) * (i + 2) // 2
        res[i] = 2

        if possible == k:
            break

        if k - possible <= i + 1:
            if k - possible == i + 1:
                res[i + 1] = -1
            else:
                x = 2 * (i + 1) + 1
                x -= 2 * (k - possible)
                res[i + 1] = -x

            break

    return " ".join(map(str, res))


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    print(solve(n, k))

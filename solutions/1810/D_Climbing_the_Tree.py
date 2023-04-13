def solve():
    min_range, max_range = 1, 10**18
    results = []

    for _ in range(int(input())):
        operation = list(map(int, input().split()))

        if operation[0] == 1:
            a, b, n = operation[1], operation[2], operation[3]
            curr_min = 1 if n == 1 else (a - b) * (n - 2) + a + 1
            curr_max = (a - b) * (n - 1) + a

            if curr_min <= max_range and curr_max >= min_range:
                results.append(1)
                min_range = max(min_range, curr_min)
                max_range = min(max_range, curr_max)
            else:
                results.append(0)

        else:
            a, b = operation[1], operation[2]
            min_n = max(1, (min_range - a - 1) // (a - b) + 2)
            max_n = max(1, (max_range - a - 1) // (a - b) + 2)

            if max_n > min_n:
                results.append(-1)
            else:
                results.append(min_n)

    print(*results)


for _ in range(int(input())):
    solve()

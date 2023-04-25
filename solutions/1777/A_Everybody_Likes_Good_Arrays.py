def solve():
    n = int(input())
    ar = list(map(int, input().split()))

    # Count the number of times the parity changes in the array
    last_parity = None
    parity_count = 0
    for x in ar:
        if x % 2 != last_parity:
            parity_count += 1
            last_parity = x % 2

    # The result is the difference between the original length and the count of parity changes
    res = n - parity_count
    print(res)


for _ in range(int(input())):
    solve()

t = int(input())

for _ in range(t):
    n = int(input())
    piles = list(map(int, input().split()))

    prefix_sum = [0]
    for pile in piles:
        prefix_sum.append(prefix_sum[-1] + pile)

    left = 1
    right = n

    # Binary search to find the pile with the special stone
    while right > left:
        mid = (right + left) // 2

        query_piles = list(range(left, mid + 1))

        # Send the query and flush the output
        print("?", len(query_piles), *query_piles, flush=True)

        total_weight = int(input())

        # Check which half the special stone is in
        if total_weight == prefix_sum[mid] - prefix_sum[left - 1]:
            left = mid + 1
        else:
            right = mid

    # Output the index of the pile with the special stone
    print("!", (left + right) // 2, flush=True)

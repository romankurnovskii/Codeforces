t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    array = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)

    for i, a in enumerate(array):
        prefix_sum[i + 1] = a + prefix_sum[i]

    results = []
    for _ in range(q):
        l, r, k = map(int, input().split())
        l -= 1
        r -= 1
        sum_modified = (
            prefix_sum[l] + (r - l + 1) * k + prefix_sum[-1] - prefix_sum[r + 1]
        )

        if sum_modified % 2 == 1:
            results.append("YES")
        else:
            results.append("NO")

    print("\n".join(results))

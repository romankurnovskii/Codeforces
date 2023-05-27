from collections import Counter


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    counts = Counter(a)
    zeros = counts[0]
    max_value = max(a)

    if zeros == n:
        print(1)
    elif zeros <= (n + 1) // 2:
        print(0)
    else:
        print(1 if max_value > 1 else 2)


for _ in range(int(input())):
    solve()

from bisect import bisect_left
from math import ceil


def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    max_color_repetitions = ceil(n / k)
    most_frequent_color = a[-1]

    if most_frequent_color > max_color_repetitions:
        print("NO")
        return

    remaining_cells = m - bisect_left(a, most_frequent_color)
    if (
        most_frequent_color == max_color_repetitions
        and n % k
        and remaining_cells > n % k
    ):
        print("NO")
        return

    print("YES")


for _ in range(int(input())):
    solve()

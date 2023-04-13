def solve():
    n, m = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]

    winnings = 0
    for j in range(m):
        sorted_col = sorted(cards[i][j] for i in range(n))
        accumulated_diff = 0
        diff_sum = 0

        for i in range(1, n):
            accumulated_diff += (sorted_col[i] - sorted_col[i - 1]) * i
            diff_sum += accumulated_diff

        winnings += diff_sum

    print(winnings)


for _ in range(int(input())):
    solve()

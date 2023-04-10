def solve():
    n = int(input())
    grid = [[None] * n for _ in range(2)]
    grid[0][0] = n * 2
    grid[-1][-1] = n * 2 - 1

    for i in range(2):
        tmp1 = n * 2 - 2 - i % 2
        tmp2 = (i + 1) % 2 + 1

        for j in range(n):
            if grid[i][j] is None:
                if (i + j) % 2:
                    grid[i][j] = tmp2
                    tmp2 += 2
                else:
                    grid[i][j] = tmp1
                    tmp1 -= 2

    for line in grid:
        print(*line)


for _ in range(int(input())):
    solve()

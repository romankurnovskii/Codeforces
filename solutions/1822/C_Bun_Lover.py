def solve():
    n = int(input())
    total_length = n * 4 + n + (n - 1) * (n - 2)
    print(total_length)


for _ in range(int(input())):
    solve()

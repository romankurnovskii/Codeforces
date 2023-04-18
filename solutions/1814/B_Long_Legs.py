def solve():
        a, b = map(int, input().split())
        ans = float("inf")
        for m in range(1, 10**5):
            jumps_a = (a + m - 1) // m
            jumps_b = (b + m - 1) // m
            ans = min(ans, jumps_a + jumps_b + m - 1)
        print(int(ans))


for _ in range(int(input())):
    solve()

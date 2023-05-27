def solve():
    n = int(input())
    MOD = 10**9 + 7

    # Calculate the total number of inversion pairs in the array
    pairs = n * (n - 1)

    # Find the factorial of n
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i % MOD  # requirement: size n modulo 1000000007(109+7)

    # Calculate the result by multiplying the factorial by the number of inversion pairs
    res = (fact * pairs) % MOD
    print(res)


for _ in range(int(input())):
    solve()

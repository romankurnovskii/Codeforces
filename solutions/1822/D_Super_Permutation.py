def solve():
    n = int(input())

    if n == 1:
        print(1)
    elif n % 2 == 1:
        print(-1)
    else:
        even_numbers = list(range(n, 1, -2))
        odd_numbers = list(range(1, n + 1, 2))
        super_permutation = [None] * n
        super_permutation[::2] = even_numbers
        super_permutation[1::2] = odd_numbers
        print(*super_permutation)


for _ in range(int(input())):
    solve()

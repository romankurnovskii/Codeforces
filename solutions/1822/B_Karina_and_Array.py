def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    # max product among two smallest and two largest numbers
    max_product = max(arr[0] * arr[1], arr[-1] * arr[-2])

    print(max_product)


for _ in range(int(input())):
    solve()

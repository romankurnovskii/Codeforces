def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    l, r = 0, n - 1

    while a[l] == b[l]:
        l += 1
        
    while a[r] == b[r]:
        r -= 1
        
    while r < n - 1 and b[r] <= b[r + 1]:
        r += 1
        
    while l > 0 and b[l - 1] <= b[l]:
        l -= 1
        
    print(l + 1, r + 1)

for _ in range(int(input())):
    solve()

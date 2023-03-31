def solve():
    n, c, d = map(int, input().split())
    ar = list(map(int, input().split()))
    
    l = 0
    r = 0
    
    res = c * n + d
    min_cost = 0

    ar.sort()
    if ar[0] != 1:
        res = min(res, c * n + d)
        
    for i in range(n):
        r = ar[i]
        to_remove = n - i - 1
        
        if l == r:
            min_cost += c
        elif r == l + 1:
            l = r
            min_cost += 0
        else:
            min_cost += d * (max(0, r - l - 1))
            l = r
            
        res = min(res, min_cost + c * to_remove)
        
    print(res)

for _ in range(int(input())):
    solve()

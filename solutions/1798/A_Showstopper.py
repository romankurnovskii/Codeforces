def solve(a,b,n):
    a_max = a[0]

    for i in range(n):
        max_v = max(a[i], b[i])
        min_v = min(a[i], b[i])

        a[i] = max_v
        b[i] = min_v

        a_max = max(a_max, max_v)
    
    if a[-1] >= a_max and b[-1] >= max(b):
        return 'Yes'
    return 'No'


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(solve(a, b, n))
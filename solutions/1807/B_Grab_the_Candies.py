t = int(input())

for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    
    m = 0
    b = 0

    if n == 1:
        print('YES' if ar[0] % 2 == 0 else 'NO')
    else:
        for x in ar:
            if x % 2 == 0:
                m += x
            else:
                b += x
        print('YES' if m > b else 'NO')

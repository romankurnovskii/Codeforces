t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if len(set(arr)) == n else "NO")

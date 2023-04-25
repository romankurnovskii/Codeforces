#  https://romankurnovskii.com/codeforces/problems/1777/

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    res = float("inf")
    l = 0
    cnt = [0] * (m + 1)
    window = 0

    for r in range(n):
        for div in divisors[a[r]]:
            if div > m:
                continue
            cnt[div] += 1
            if cnt[div] == 1:
                window += 1

        while l != n and window == m:
            res = min(res, a[r] - a[l])
            for div in divisors[a[l]]:
                if div > m:
                    continue
                cnt[div] -= 1
                if cnt[div] == 0:
                    window -= 1
            l += 1

    if res != float("inf"):
        print(res)
    else:
        print(-1)


MAX = 100010
divisors = [[] for _ in range(MAX)]
for i in range(1, MAX):
    for j in range(i, MAX, i):
        divisors[j].append(i)


for _ in range(int(input())):
    solve()

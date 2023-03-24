t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = []

    vis = 0
    while a:
        # Find the index of the element with the highest bitwise AND with the complement of visited
        idx = max(range(len(a)), key=lambda i: a[i] & ~vis) 

        if not a[idx] & ~vis:
            break

        res.append(a.pop(idx))
        vis |= res[-1]

    res.extend(a)

    print(" ".join(str(x) for x in res))

t = int(input())


def lower(x, y):
    if any(yi > 0 for yi in y[98:]):
        return True

    if x[97] < y[97] and all(xi == 0 for xi in x[98:]):
        return True

    return False


for _ in range(t):
    q = int(input())
    s = [0] * 128
    t = [0] * 128
    s[ord('a')] = 1
    t[ord('a')] = 1

    for _ in range(q):
        d, k, x = input().split()
        d, k = int(d), int(k)

        if d == 1:
            for c in x:
                s[ord(c)] += k
        else:
            for c in x:
                t[ord(c)] += k

        print("YES" if lower(s, t) else "NO")

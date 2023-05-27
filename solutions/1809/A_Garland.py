def solve(s):
    if all(c == s[0] for c in s):
        return -1
    elif s.count(s[0]) == 3 or s.count(s[1]) == 3:
        return 6
    else:
        return 4


t = int(input())
for _ in range(t):
    s = input()
    print(solve(s))

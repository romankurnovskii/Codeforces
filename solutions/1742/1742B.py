import sys


def inp(): return sys.stdin.readline().rstrip("\r\n")
def inp_int(): return int(inp())


for _ in range(inp_int()):
    n = int(inp_int())
    arr = list(map(int, input().split()))
    print("YES" if len(set(arr)) == n else "NO")

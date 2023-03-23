import sys


def inp(): return sys.stdin.readline().rstrip("\r\n")
def inp_int(): return int(inp())


for _ in range(inp_int()):
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] + arr[1] == arr[2]:
        print("YES")
    else:
        print("NO")

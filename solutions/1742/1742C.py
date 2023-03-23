import sys


def inp(): return sys.stdin.readline().rstrip("\r\n")
def inp_int(): return int(inp())


for _ in range(inp_int()):
    inp()
    grid = [inp() for _ in range(8)]
    for row in grid:
        if all(c == 'R' for c in row):
            print('R')
            break
    print('B')
    break

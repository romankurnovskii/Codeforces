import sys


def input(): return sys.stdin.readline().rstrip('\r\n')


def read_int():
    return int(input())


def check(grid):
    return any(all(ch == 'R' for ch in row) for row in grid)


for _ in range(read_int()):
    input()
    print(['B', 'R'][check([input() for _ in range(8)])])

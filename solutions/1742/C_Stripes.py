t = int(input())

for _ in range(t):
    input()
    grid = [input() for _ in range(8)]
    for row in grid:
        if all(c == 'R' for c in row):
            print('R')
            break
    else:
        print('B')

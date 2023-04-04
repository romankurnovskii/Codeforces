def solve():
    a = input()
    b = input()

    if a[0] == b[0]:
        print('YES')
        print(f'{a[0]}*')
    elif a[-1] == b[-1]:
        print('YES')
        print(f'*{a[-1]}')
    else:
        for i in range(len(a)-1):
            if a[i:i+2] in b:
                print('YES')
                print(f'*{a[i:i+2]}*')
                return
        print('NO')

for _ in range(int(input())):
    solve()

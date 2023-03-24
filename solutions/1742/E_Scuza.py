from bisect import bisect

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    input_numbers = list(map(int, input().split()))
    arr = [0] + input_numbers + [1e9 + 7]  # 1000000007
    b = list(map(int, input().split()))

    _arr = arr.copy()
    for i in range(1, n + 2):
        _arr[i] += _arr[i - 1]
        arr[i] = max(arr[i], arr[i - 1])

    for i in range(q):
        b[i] = _arr[bisect(arr, b[i]) - 1]

    print(' '.join(map(str, b)))

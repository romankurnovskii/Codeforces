def solve():
    n, t = map(int, input().split())
    durations = list(map(int, input().split()))
    values = list(map(int, input().split()))

    max_value = 0  # max entertainment value
    max_index = -1

    # Iterate through the videos
    for i in range(n):
        # If the video can be watched within the lunch break
        if i + durations[i] <= t:
            if values[i] > max_value:
                max_value = values[i]
                max_index = i + 1

    print(max_index)


for _ in range(int(input())):
    solve()

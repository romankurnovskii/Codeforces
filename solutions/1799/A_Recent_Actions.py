def solve():
    n, m = list(map(int, input().split()))
    posts = list(map(int, input().split()))
    tracked_data = [-1] * n

    last = n-1
    used_posts = set()
    for moment, post in enumerate(posts, 1):
        if post not in used_posts:
            if last >= 0:
                tracked_data[last] = moment
                last -= 1
                used_posts.add(post)
    print(*tracked_data)


for _ in range(int(input())):
    solve()

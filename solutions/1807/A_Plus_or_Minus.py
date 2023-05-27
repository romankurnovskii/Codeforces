t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    print("+" if a + b == c else "-")

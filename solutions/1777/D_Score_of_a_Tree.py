from collections import defaultdict

MOD = 10**9 + 7

def dfs(graph, depth):
    stack = [(1, -1, True)]  # node, parent, first_visit
    while stack:
        node, parent, first_visit = stack.pop()

        if first_visit:
            stack.append((node, parent, False))
            for neighbor in graph[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, True))
        else:  # if it's not the first visit, update the depth of the parent node
            if parent != -1:
                depth[parent] = max(depth[parent], depth[node] + 1)

def solve():
    n = int(input())
    graph = defaultdict(list)
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    depth = [1] * (n + 1)
    dfs(graph, depth)

    res = sum(depth[1:])  # sum of depths from the 2nd node to the last node
    print(res * pow(2, n - 1, MOD) % MOD)


for _ in range(int(input())):
    solve()

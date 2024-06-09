
def find_least_passageways(n, h, routes):
    adj_list = [[] for _ in range(n)]
    for a, b in routes:
        adj_list[a].append(b)
        adj_list[b].append(a)

    visited = [False] * n
    visited[h] = True
    queue = [h]
    while queue:
        current = queue.pop(0)
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    needed_passageways = []
    for i in range(n):
        if not visited[i]:
            needed_passageways.append((h, i))

    return len(needed_passageways), needed_passageways

# Input parsing
n, h = map(int, input().split())
routes = [tuple(map(int, input().split())) for _ in range(n-1)]

m, passageways = find_least_passageways(n, h, routes)
print(m)
for a, b in passageways:
    print(a, b)

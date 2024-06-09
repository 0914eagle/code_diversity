
def divide_items(N, items, M, suspicious_pairs):
    graph = {}
    for item in items:
        graph[item] = set()

    for pair in suspicious_pairs:
        item1, item2 = pair.split()
        graph[item1].add(item2)
        graph[item2].add(item1)

    visited = {}
    for item in items:
        visited[item] = False

    def dfs(node, group):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if not dfs(neighbor, 1 - group):
                    return False
            elif visited[neighbor] and group == visited[neighbor]:
                return False
        return True

    for item in items:
        if not visited[item]:
            if not dfs(item, 0):
                return "impossible"

    walter_items = [item for item in items if visited[item] == 0]
    jesse_items = [item for item in items if visited[item] == 1]

    return walter_items, jesse_items

N = int(input())
items = [input() for _ in range(N)]
M = int(input())
suspicious_pairs = [input() for _ in range(M)]

result = divide_items(N, items, M, suspicious_pairs)
if result == "impossible":
    print("impossible")
else:
    walter_items, jesse_items = result
    print(" ".join(walter_items))
    print(" ".join(jesse_items))

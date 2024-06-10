
def check_intersection(seg1, seg2):
    l1, r1 = seg1
    l2, r2 = seg2
    return l1 < r2 and l2 < r1

def build_graph(segments):
    graph = {i: [] for i in range(len(segments))}
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            if check_intersection(segments[i], segments[j]):
                graph[i].append(j)
                graph[j].append(i)
    return graph

def is_tree(graph):
    n = len(graph)
    visited = [False] * n
    stack = [0]
    visited[0] = True
    edges = 0

    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                edges += 1
                stack.append(neighbor)

    return edges == n - 1 and all(visited)

if __name__ == "__main__":
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    graph = build_graph(segments)
    if is_tree(graph):
        print("YES")
    else:
        print("NO")

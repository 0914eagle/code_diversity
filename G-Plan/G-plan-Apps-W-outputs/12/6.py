
def segments_intersect(seg1, seg2):
    return seg1[0] < seg2[1] and seg1[1] > seg2[0]

def build_graph(n, segments):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i+1, n):
            if segments_intersect(segments[i], segments[j]):
                graph[i].append(j)
                graph[j].append(i)
    return graph

def is_tree(n, graph):
    if len(graph) != n:
        return False
    visited = [False] * n
    stack = [0]
    visited[0] = True
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    return all(visited)

if __name__ == "__main__":
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    graph = build_graph(n, segments)
    if is_tree(n, graph):
        print("YES")
    else:
        print("NO")


def check_intersection(seg1, seg2):
    return seg1[0] < seg2[1] and seg1[1] > seg2[0]

def build_graph(segments):
    graph = {i: [] for i in range(len(segments))}
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            if check_intersection(segments[i], segments[j]):
                graph[i].append(j)
                graph[j].append(i)
    return graph

def is_tree(graph):
    visited = [False] * len(graph)
    stack = [0]
    visited[0] = True
    edges = 0
    while stack:
        node = stack.pop()
        edges += len(graph[node])
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    return edges == 2 * (len(graph) - 1)

if __name__ == "__main__":
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    graph = build_graph(segments)
    if is_tree(graph):
        print("YES")
    else:
        print("NO")

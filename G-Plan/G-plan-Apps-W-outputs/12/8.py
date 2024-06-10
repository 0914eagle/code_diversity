
def check_intersection(seg1, seg2):
    l1, r1 = seg1
    l2, r2 = seg2
    return l1 < r2 and l2 < r1

def build_graph(segments):
    graph = {i: [] for i in range(len(segments))}
    for i in range(len(segments)):
        for j in range(i + 1, len(segments)):
            if check_intersection(segments[i], segments[j]):
                graph[i].append(j)
                graph[j].append(i)
    return graph

def is_tree(graph):
    n = len(graph)
    visited = [False] * n

    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    if dfs(0, -1):
        return "NO"
    
    for i in range(n):
        if not visited[i]:
            return "NO"
    
    return "YES"

if __name__ == "__main__":
    n = int(input())
    segments = [tuple(map(int, input().split())) for _ in range(n)]
    graph = build_graph(segments)
    print(is_tree(graph))

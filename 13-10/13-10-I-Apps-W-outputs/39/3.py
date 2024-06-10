
def get_paths(edges, start, end, k):
    paths = []
    for edge in edges:
        if edge[0] == start and edge[1] == end:
            paths.append([start, end])
        elif edge[0] == start:
            for path in get_paths(edges, edge[1], end, k-1):
                paths.append([start, edge[1]] + path)
        elif edge[1] == end:
            for path in get_paths(edges, start, edge[0], k-1):
                paths.append([edge[1], end] + path)
    return paths

def has_path(edges, start, end, k):
    return len(get_paths(edges, start, end, k)) > 0

def add_edge(edges, start, end):
    return edges + [(start, end)]

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    q = int(input())
    for i in range(q):
        x, y, a, b, k = map(int, input().split())
        if has_path(add_edge(edges, x, y), a, b, k):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()


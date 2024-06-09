
def is_harmonious(graph):
    n = len(graph)
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (i, j) in graph and (j, k) in graph and (i, k) not in graph:
                    return False
    return True

def add_edges(graph, m):
    n = len(graph)
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (i, j) in graph and (j, k) in graph and (i, k) not in graph:
                    graph.add((i, k))
                    m -= 1
                    if m == 0:
                        return graph
    return graph

def main():
    n, m = map(int, input().split())
    graph = set()
    for _ in range(m):
        u, v = map(int, input().split())
        graph.add((u, v))
    if is_harmonious(graph):
        print(0)
    else:
        print(add_edges(graph, m))

if __name__ == "__main__":
    main()


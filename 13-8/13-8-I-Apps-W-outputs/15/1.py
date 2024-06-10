
def is_relatively_prime(v, u):
    return gcd(v, u) == 1

def construct_relatively_prime_graph(n, m):
    if m > n * (n - 1) // 2:
        return "Impossible"
    
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    
    edges = []
    for i in range(m):
        v, u = map(int, input().split())
        if v != u and (v, u) not in edges and (u, v) not in edges:
            edges.append((v, u))
            graph[v].append(u)
            graph[u].append(v)
    
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i, j) not in edges and not is_relatively_prime(i, j):
                return "Impossible"
    
    return graph

def main():
    n, m = map(int, input().split())
    graph = construct_relatively_prime_graph(n, m)
    if graph == "Impossible":
        print(graph)
    else:
        print("Possible")
        for edge in graph:
            print(edge[0], edge[1])

if __name__ == '__main__':
    main()


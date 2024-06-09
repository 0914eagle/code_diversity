
def f1(N, K, items):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for i, item in items:
        graph[i].append(item)

    # Check if there is a path from node 0 to node N-1
    return "unique" if graph[0] == [] else "impossible"

def f2(N, K, items, bought_items):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for i, item in items:
        graph[i].append(item)

    # Check if there is a path from node 0 to node N-1
    path = []
    for i in range(N):
        if graph[i] == []:
            continue
        for item in graph[i]:
            if item in bought_items:
                path.append(item)
                break
        else:
            return "impossible"

    # Check if the path is unique
    return "unique" if len(set(path)) == len(path) else "ambiguous"

if __name__ == '__main__':
    N, K = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(K)]
    M = int(input())
    bought_items = [input() for _ in range(M)]
    print(f1(N, K, items))
    print(f2(N, K, items, bought_items))



def read_data():
    n, m = map(int, input().split())
    edges = []
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    queries = list(map(int, input().split()))
    return n, m, edges, queries

def find_paths(edges, q):
    # Initialize a dictionary to store the paths
    paths = {}
    
    # Iterate over the edges and add them to the dictionary
    for edge in edges:
        u, v, w = edge
        if u not in paths:
            paths[u] = {}
        if v not in paths[u]:
            paths[u][v] = w
    
    # Iterate over the queries and find the number of pairs of vertices
    # with a maximum weight of an edge on a simple path between them
    count = 0
    for q in queries:
        for u in paths:
            for v in paths[u]:
                if paths[u][v] <= q:
                    count += 1
    
    return count

def main():
    n, m, edges, queries = read_data()
    print(find_paths(edges, queries))

if __name__ == '__main__':
    main()


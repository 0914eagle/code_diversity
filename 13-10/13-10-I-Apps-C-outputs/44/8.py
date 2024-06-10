
def get_number_of_non_similar_worlds(n, m):
    # Initialize the graph with two vertices, s and t
    graph = {s: set(), t: set()}
    
    # Add the edges for the first n-1 changes
    for i in range(n-1):
        # Add a new vertex w
        w = i+3
        graph[w] = set()
        
        # Add edges (u, w) and (v, w) for each edge (u, v) in the graph
        for u in graph:
            for v in graph:
                if u < v:
                    graph[u].add(w)
                    graph[w].add(v)
    
    # Count the number of non-similar worlds
    number_of_non_similar_worlds = 0
    for u in graph:
        for v in graph:
            if u < v:
                # Check if the minimum cut is at least m
                if len(graph[u].intersection(graph[v])) >= m:
                    number_of_non_similar_worlds += 1
    
    return number_of_non_similar_worlds % 1000000007

def main():
    n, m = map(int, input().split())
    print(get_number_of_non_similar_worlds(n, m))

if __name__ == '__main__':
    main()



def is_good_graph(graph):
    # Check if the graph is a good graph
    # A good graph has no self-loops and no multi-edges
    # Also, vertex 1 and vertex N are not connected
    return not any(graph[i, i] for i in range(1, len(graph))) and not any(graph[i, j] and graph[j, i] for i in range(1, len(graph)) for j in range(i+1, len(graph))) and not graph[1, len(graph)] and not graph[len(graph), 1]

def play_game(graph):
    # Initialize the graph as a good graph
    graph = graph.copy()
    
    # Taro goes first
    while True:
        # Taro chooses two vertices to connect with an edge
        u, v = map(int, input().split())
        
        # Add the edge to the graph
        graph[u, v] = graph[v, u] = 1
        
        # Check if the graph is still a good graph
        if not is_good_graph(graph):
            # If the graph is not a good graph, Taro loses
            return "First"
        
        # Jiro's turn now
        # Jiro chooses two vertices to connect with an edge
        u, v = map(int, input().split())
        
        # Add the edge to the graph
        graph[u, v] = graph[v, u] = 1
        
        # Check if the graph is still a good graph
        if not is_good_graph(graph):
            # If the graph is not a good graph, Jiro loses
            return "Second"

def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate through the test cases
    for _ in range(t):
        # Read the number of vertices and edges
        n, m = map(int, input().split())
        
        # Initialize the graph as an adjacency matrix
        graph = np.zeros((n+1, n+1), dtype=int)
        
        # Read the edges
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u, v] = graph[v, u] = 1
        
        # Play the game
        print(play_game(graph))

if __name__ == '__main__':
    main()


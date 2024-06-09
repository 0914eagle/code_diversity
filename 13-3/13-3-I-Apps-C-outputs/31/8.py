
def is_good_graph(graph):
    # Check if the graph is a good graph
    # A good graph has no self-loops and no multi-edges
    # Also, vertex 1 and vertex N are not connected
    return not any(graph[i][i] for i in range(1, len(graph))) and not any(graph[i][j] and graph[j][i] for i in range(1, len(graph)) for j in range(i+1, len(graph))) and not graph[1][len(graph)]

def play_game(graph):
    # Play the game optimally
    # Taro goes first, then Jiro goes
    while is_good_graph(graph):
        # Taro's turn
        graph = add_edge(graph, 1, 2)
        if not is_good_graph(graph):
            return "First"
        # Jiro's turn
        graph = add_edge(graph, 2, 3)
        if not is_good_graph(graph):
            return "Second"
    return "First" if graph[1][len(graph)] else "Second"

def add_edge(graph, u, v):
    # Add an edge between vertices u and v bidirectionally
    graph[u][v] = graph[v][u] = 1
    return graph

def main():
    num_cases = int(input())
    for case in range(1, num_cases+1):
        n, m = map(int, input().split())
        graph = [[0] * (n+1) for _ in range(n+1)]
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a][b] = graph[b][a] = 1
        print("Case {}: {}".format(case, play_game(graph)))

if __name__ == '__main__':
    main()


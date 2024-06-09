
def is_good_graph(graph):
    # Check if the graph is still a good graph after adding the edge
    # Return True if it is still a good graph, False otherwise
    pass

def add_edge(graph, u, v):
    # Add an edge between vertices u and v to the graph
    # Return the updated graph
    pass

def play_game(graph):
    # Play the game between Taro and Jiro
    # Return True if Taro wins, False otherwise
    pass

if __name__ == '__main__':
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        n, m = map(int, input().split())
        graph = {}
        for i in range(m):
            u, v = map(int, input().split())
            graph[u] = graph.get(u, []) + [v]
            graph[v] = graph.get(v, []) + [u]
        result = "First" if play_game(graph) else "Second"
        print("Case {}: {}".format(case, result))


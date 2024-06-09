
def is_good_graph(graph):
    # Check if the graph is a good graph
    # Return True if it is a good graph, False otherwise
    pass

def add_edge(graph, u, v):
    # Add an edge between vertices u and v to the graph
    # Return the updated graph
    pass

def play_game(graph):
    # Play the game optimally
    # Return the winner of the game (Taro or Jiro)
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
        winner = play_game(graph)
        print("Case {}: {}".format(case, winner))


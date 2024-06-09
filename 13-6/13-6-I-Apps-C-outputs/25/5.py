
def is_good_graph(graph, vertex_1, vertex_2):
    # Check if the graph is still good after adding an edge between vertex_1 and vertex_2
    # Return True if the graph is good, False otherwise
    pass

def taro_wins(graph, vertex_1, vertex_2):
    # Check if Taro the first can win the game by adding an edge between vertex_1 and vertex_2
    # Return True if Taro can win, False otherwise
    pass

def jiro_wins(graph, vertex_1, vertex_2):
    # Check if Jiro the second can win the game by adding an edge between vertex_1 and vertex_2
    # Return True if Jiro can win, False otherwise
    pass

def determine_winner(graph):
    # Determine the winner of the game based on the given graph
    # Return "First" if Taro the first wins, "Second" if Jiro the second wins, and "Draw" if the game ends in a draw
    pass

if __name__ == '__main__':
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        n, m = map(int, input().split())
        graph = {}
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a] = graph.get(a, []) + [b]
            graph[b] = graph.get(b, []) + [a]
        print(determine_winner(graph))


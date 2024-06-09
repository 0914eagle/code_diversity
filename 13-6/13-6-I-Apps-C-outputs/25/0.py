
def is_good_graph(graph):
    # Check if the graph is good
    # A graph is good if vertex 1 and vertex N are not connected, and there are no self-loops and no multi-edges
    return graph[1][0] == 0 and graph[N][0] == 0 and all(graph[i][i] == 0 for i in range(1, N+1)) and all(graph[i][j] == 0 for i in range(1, N+1) for j in range(i+1, N+1))

def play_game(graph):
    # Initialize the game state
    game_state = [True, True]
    
    # Play the game until one player loses
    while game_state[0] and game_state[1]:
        # Taro's turn
        if game_state[0]:
            # Add an edge between two random vertices
            u, v = random.sample(range(1, N+1), 2)
            graph[u][v] = 1
            graph[v][u] = 1
            # Check if the graph is still good
            if not is_good_graph(graph):
                game_state[0] = False
        
        # Jiro's turn
        if game_state[1]:
            # Add an edge between two random vertices
            u, v = random.sample(range(1, N+1), 2)
            graph[u][v] = 1
            graph[v][u] = 1
            # Check if the graph is still good
            if not is_good_graph(graph):
                game_state[1] = False
    
    # Return the winner
    if game_state[0]:
        return "First"
    else:
        return "Second"

def main():
    # Read the input
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        graph = [[0] * (N+1) for _ in range(N+1)]
        for _ in range(M):
            u, v = map(int, input().split())
            graph[u][v] = 1
            graph[v][u] = 1
        # Play the game and print the winner
        print(play_game(graph))

if __name__ == '__main__':
    main()


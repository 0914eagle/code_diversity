
def is_good_graph(graph, n, m):
    # Check if the graph is good
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i][j] == 1 and graph[j][i] == 1:
                return False
    return True


def game(graph, n, m):
    # Initialize the game state
    game_state = [0] * (n + 1)
    game_state[1] = 1
    game_state[n] = -1

    # Play the game
    while True:
        # Taro's turn
        taro_choice = -1
        for i in range(1, n + 1):
            if game_state[i] == 1:
                for j in range(i + 1, n + 1):
                    if graph[i][j] == 1 and game_state[j] == 0:
                        taro_choice = j
                        break
                if taro_choice != -1:
                    break

        # Jiro's turn
        jiro_choice = -1
        for i in range(1, n + 1):
            if game_state[i] == -1:
                for j in range(i + 1, n + 1):
                    if graph[i][j] == 1 and game_state[j] == 0:
                        jiro_choice = j
                        break
                if jiro_choice != -1:
                    break

        # Update the game state
        if taro_choice != -1:
            game_state[taro_choice] = 1
        if jiro_choice != -1:
            game_state[jiro_choice] = -1

        # Check if the game is over
        if taro_choice == -1 and jiro_choice == -1:
            break

    # Determine the winner
    if game_state[1] == 1:
        return "First"
    else:
        return "Second"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        graph = [[0] * (n + 1) for _ in range(n + 1)]
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a][b] = 1
            graph[b][a] = 1
        print(game(graph, n, m))


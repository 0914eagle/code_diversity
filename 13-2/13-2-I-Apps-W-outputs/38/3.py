
def f1(n, k, a):
    # Initialize the game state
    game_state = {i: i for i in range(1, n + 1)}
    game_wins = [0] * n
    game_wins[0] = 1
    game_wins[1] = 1
    winner = 0

    # Play the game
    for i in range(2, n):
        game_wins[i] = 1
        if game_wins[game_state[i]] == k:
            winner = game_state[i]
            break
        game_state[i] = game_state[game_state[i]]

    return winner

def f2(n, k, a):
    # Initialize the game state
    game_state = {i: i for i in range(1, n + 1)}
    game_wins = [0] * n
    game_wins[0] = 1
    game_wins[1] = 1
    winner = 0

    # Play the game
    for i in range(2, n):
        game_wins[i] = 1
        if game_wins[game_state[i]] == k:
            winner = game_state[i]
            break
        game_state[i] = game_state[game_state[i]]

    return winner

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(f1(n, k, a))
    print(f2(n, k, a))


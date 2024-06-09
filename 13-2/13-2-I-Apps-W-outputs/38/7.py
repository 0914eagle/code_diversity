
def f1(n, k, a):
    # Initialize the game state
    game_state = {i: i for i in range(1, n + 1)}
    game_wins = [0] * (n + 1)
    game_wins[1] = 1
    game_wins[2] = 1

    # Play the game
    while len(set(game_state.values())) > 1:
        for i in range(3, n + 1):
            if game_wins[i] < k:
                break
        else:
            break

        winner = i
        loser = game_state[winner]
        game_state[winner] = loser
        game_wins[loser] = 0
        game_wins[winner] += 1

    # Find the winner
    winner_power = a[game_state[1]]
    return winner_power

def f2(n, k, a):
    # Initialize the game state
    game_state = {i: i for i in range(1, n + 1)}
    game_wins = [0] * (n + 1)
    game_wins[1] = 1
    game_wins[2] = 1

    # Play the game
    while len(set(game_state.values())) > 1:
        for i in range(3, n + 1):
            if game_wins[i] < k:
                break
        else:
            break

        winner = i
        loser = game_state[winner]
        game_state[winner] = loser
        game_wins[loser] = 0
        game_wins[winner] += 1

    # Find the winner
    winner_power = a[game_state[1]]
    return winner_power

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(f1(n, k, a))
    print(f2(n, k, a))



def f1(n, k, a):
    # Initialize the game state
    game_state = {i: i for i in range(1, n + 1)}
    game_wins = [0] * (n + 1)
    game_wins[1] = 1
    game_wins[2] = 1

    # Play the game
    while len(set(game_state.values())) > 1:
        for i in range(3, n + 1):
            if game_state[i] != 0:
                winner = game_state[i]
                loser = game_state[i - 1]
                if a[winner - 1] > a[loser - 1]:
                    game_wins[winner] += 1
                    if game_wins[winner] == k:
                        return winner
                else:
                    game_wins[loser] = 0
                    game_state[i] = 0
                    game_state[i - 1] = winner

    return list(game_state.values())[0]

def f2(n, k, a):
    # Initialize the game state
    game_state = {i: i for i in range(1, n + 1)}
    game_wins = [0] * (n + 1)
    game_wins[1] = 1
    game_wins[2] = 1

    # Play the game
    while len(set(game_state.values())) > 1:
        for i in range(3, n + 1):
            if game_state[i] != 0:
                winner = game_state[i]
                loser = game_state[i - 1]
                if a[winner - 1] > a[loser - 1]:
                    game_wins[winner] += 1
                    if game_wins[winner] == k:
                        return winner
                else:
                    game_wins[loser] = 0
                    game_state[i] = 0
                    game_state[i - 1] = winner

    return list(game_state.values())[0]

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(f1(n, k, a))
    print(f2(n, k, a))


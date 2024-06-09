
def f1(N, M, ps):
    # Initialize the probability of Anthony winning
    prob_win = 1

    # Loop through each round
    for i in range(N + M - 1):
        # Calculate the probability of Anthony winning this round
        prob_win_round = ps[i]

        # Calculate the probability of Anthony losing this round
        prob_lose_round = 1 - ps[i]

        # Calculate the probability of Anthony winning the next round
        prob_win_next = prob_win_round * prob_win + prob_lose_round * (1 - prob_win)

        # Update the probability of Anthony winning
        prob_win = prob_win_next

    # Return the probability of Anthony winning the game
    return prob_win

def f2(N, M, ps):
    # Initialize the probability of Anthony winning
    prob_win = 1

    # Loop through each round
    for i in range(N + M - 1):
        # Calculate the probability of Anthony winning this round
        prob_win_round = ps[i]

        # Calculate the probability of Anthony losing this round
        prob_lose_round = 1 - ps[i]

        # Calculate the probability of Anthony winning the next round
        prob_win_next = prob_win_round * prob_win + prob_lose_round * (1 - prob_win)

        # Update the probability of Anthony winning
        prob_win = prob_win_next

        # Calculate the probability of Anthony winning the game
        prob_game_win = prob_win

    # Return the probability of Anthony winning the game
    return prob_game_win

if __name__ == '__main__':
    N, M = map(int, input().split())
    ps = []
    for i in range(N + M - 1):
        ps.append(float(input()))
    print(f1(N, M, ps))
    print(f2(N, M, ps))


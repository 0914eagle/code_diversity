
def f1(N, M, ps):
    # Initialize the probability of Anthony winning
    prob_win = 1

    # Loop through each round
    for i in range(N + M - 1):
        # Calculate the probability of Anthony winning this round
        prob_win_round = ps[i]

        # Update the probability of Anthony winning
        prob_win *= prob_win_round

        # Update the probability of Anthony losing
        prob_lose = 1 - prob_win_round

        # Update the probability of Cora winning
        prob_cora_win = 1 - prob_lose

        # Calculate the probability of Cora winning this round
        prob_cora_win_round = prob_cora_win ** (N + M - i - 2)

        # Update the probability of Cora winning
        prob_cora_win *= prob_cora_win_round

        # Update the probability of Cora losing
        prob_cora_lose = 1 - prob_cora_win_round

        # Update the probability of Anthony losing
        prob_lose *= prob_cora_lose

    # Return the probability of Anthony winning
    return prob_win

def f2(N, M, ps):
    # Initialize the probability of Anthony winning
    prob_win = 1

    # Loop through each round
    for i in range(N + M - 1):
        # Calculate the probability of Anthony winning this round
        prob_win_round = ps[i]

        # Update the probability of Anthony winning
        prob_win *= prob_win_round

        # Update the probability of Anthony losing
        prob_lose = 1 - prob_win_round

        # Update the probability of Cora winning
        prob_cora_win = 1 - prob_lose

        # Calculate the probability of Cora winning this round
        prob_cora_win_round = prob_cora_win ** (N + M - i - 2)

        # Update the probability of Cora winning
        prob_cora_win *= prob_cora_win_round

        # Update the probability of Cora losing
        prob_cora_lose = 1 - prob_cora_win_round

        # Update the probability of Anthony losing
        prob_lose *= prob_cora_lose

    # Return the probability of Anthony winning
    return prob_win

if __name__ == '__main__':
    N, M = map(int, input().split())
    ps = []
    for _ in range(N + M - 1):
        ps.append(float(input()))
    print(f1(N, M, ps))
    print(f2(N, M, ps))


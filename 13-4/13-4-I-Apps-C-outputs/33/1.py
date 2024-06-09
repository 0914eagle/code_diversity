
def f1(N, M, ps):
    # Initialize the probability of Anthony winning
    prob = 1

    # Loop through each round
    for i in range(N + M - 1):
        # Calculate the probability of Anthony winning this round
        prob_win = ps[i]

        # Calculate the probability of Anthony losing this round
        prob_lose = 1 - prob_win

        # Update the probability of Anthony winning
        prob = prob_win * prob + prob_lose * (1 - prob)

    # Return the probability of Anthony winning the game
    return prob

def f2(N, M, ps):
    # Initialize the probability of Anthony winning
    prob = 1

    # Loop through each round
    for i in range(N + M - 1):
        # Calculate the probability of Anthony winning this round
        prob_win = ps[i]

        # Calculate the probability of Anthony losing this round
        prob_lose = 1 - prob_win

        # Update the probability of Anthony winning
        prob = prob_win * prob + prob_lose * (1 - prob)

    # Return the probability of Anthony winning the game
    return prob

if __name__ == '__main__':
    N, M = map(int, input().split())
    ps = []
    for i in range(N + M - 1):
        ps.append(float(input()))
    print(f1(N, M, ps))
    print(f2(N, M, ps))



def solve(N, cards):
    # Initialize the scores of Alice and Bob to 0
    alice_score, bob_score = 0, 0

    # Sort the cards in descending order
    cards.sort(reverse=True)

    # Loop through the cards and assign them to Alice and Bob alternately
    for i in range(N):
        if i % 2 == 0:
            alice_score += cards[i]
        else:
            bob_score += cards[i]

    # Return the difference between Alice's score and Bob's score
    return alice_score - bob_score


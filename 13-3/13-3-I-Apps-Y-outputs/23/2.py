
def get_optimal_score(cards):
    # Sort the cards in descending order
    cards.sort(reverse=True)
    # Initialize the scores of Alice and Bob to 0
    alice_score = 0
    bob_score = 0
    # Loop through the cards and assign them to Alice and Bob alternately
    for i in range(len(cards)):
        if i % 2 == 0:
            alice_score += cards[i]
        else:
            bob_score += cards[i]
    # Return the difference between Alice's score and Bob's score
    return alice_score - bob_score


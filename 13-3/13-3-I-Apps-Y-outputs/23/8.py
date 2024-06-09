
def solve(N, cards):
    # Calculate the sum of the cards
    sum_cards = sum(cards)

    # Calculate the minimum sum that Alice can get
    min_sum = sum_cards // 2

    # Calculate the maximum sum that Alice can get
    max_sum = sum_cards

    # Initialize the optimal score for Alice and Bob
    opt_score_alice, opt_score_bob = 0, 0

    # Loop through all possible scores for Alice
    for alice_score in range(min_sum, max_sum + 1):
        # Calculate the score for Bob
        bob_score = sum_cards - alice_score

        # Check if the current score is optimal
        if alice_score + bob_score == sum_cards:
            # Update the optimal score for Alice and Bob
            opt_score_alice = alice_score
            opt_score_bob = bob_score
            break

    # Return the difference between the optimal score for Alice and Bob
    return opt_score_alice - opt_score_bob


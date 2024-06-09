
def expected_gifts_taken(n):
    # Calculate the expected number of gifts taken out of the bag
    # until the process ends and everyone has gotten their gift
    expected_gifts_taken = 0
    for i in range(n):
        # Probability that the ith person picks their own gift
        prob_pick_own_gift = 1 / n
        # Probability that the ith person picks a gift other than their own
        prob_pick_other_gift = 1 - prob_pick_own_gift
        # Expected number of gifts taken out of the bag by the ith person
        expected_gifts_taken_by_i = prob_pick_own_gift * (i + 1) + prob_pick_other_gift * (n - 1)
        expected_gifts_taken += expected_gifts_taken_by_i
    return expected_gifts_taken


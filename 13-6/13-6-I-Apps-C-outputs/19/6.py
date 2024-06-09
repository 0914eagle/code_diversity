
def expected_gifts(n):
    # Calculate the expected number of gifts taken out of the bag
    # until the process ends and everyone has gotten their gift
    expected_gifts = 0
    for i in range(n):
        # Probability that the ith person picks their own gift is (n-1)/n
        prob_pick_own_gift = (n-1)/n
        # Expected number of gifts taken out of the bag by the ith person
        # is 1 if they pick their own gift, and 0 otherwise
        expected_gifts_taken = 1 if i == 0 else prob_pick_own_gift
        expected_gifts += expected_gifts_taken
    
    return expected_gifts


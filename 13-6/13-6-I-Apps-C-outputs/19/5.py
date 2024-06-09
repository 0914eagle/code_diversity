
def expected_gifts_taken(n):
    # Calculate the probability of the last person picking their own gift
    prob_last_person = 1 / n

    # Calculate the expected number of gifts taken out of the bag for the last person
    expected_gifts_last_person = 0
    for i in range(n):
        expected_gifts_last_person += (i + 1) * prob_last_person

    # Calculate the expected number of gifts taken out of the bag for the first n - 1 people
    expected_gifts_first_n_minus_1 = n * (n - 1) / 2

    # Calculate the total expected number of gifts taken out of the bag
    expected_total_gifts = expected_gifts_first_n_minus_1 + expected_gifts_last_person

    return expected_total_gifts



def expected_gifts(n):
    # Calculate the expected number of gifts taken out of the bag
    # until the process ends and everyone has gotten their gift
    expected_gifts = 0
    for i in range(n):
        # Probability that the last person picks their own gift
        prob = 1 / (n - i)
        # Expected number of gifts taken out of the bag for this person
        expected_gifts += prob * (i + 1)
    return expected_gifts



def expected_gifts_taken(n):
    # Calculate the probability of the last person picking their own gift
    p = 1 / n
    
    # Calculate the expected number of gifts taken out of the bag
    # before the process ends
    expected_gifts = 0
    for i in range(n):
        expected_gifts += i * p * (1 - p) ** (i - 1)
    
    return expected_gifts


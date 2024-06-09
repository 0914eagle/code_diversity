
def expected_gifts_taken(n):
    # Calculate the probability of the last person picking their own gift
    p = 1 / n
    
    # Calculate the expected number of gifts taken out of the bag
    # until the process ends and everyone has gotten their gift
    expected_gifts_taken = 0
    for i in range(n):
        expected_gifts_taken += (i + 1) * p * (1 - p) ** i
    
    return expected_gifts_taken


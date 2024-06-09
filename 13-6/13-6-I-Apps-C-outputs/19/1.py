
def expected_gifts(n):
    # Calculate the expected number of gifts taken out of the bag
    # until the process ends and everyone has gotten their gift
    expected_gifts = 0
    for i in range(1, n+1):
        expected_gifts += (i / n) * (n - i + 1)
    return expected_gifts


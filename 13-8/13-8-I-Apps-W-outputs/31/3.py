
def permutation_happiness(n, m):
    # Calculate the number of framed segments for each permutation
    def count_framed_segments(permutation):
        count = 0
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if permutation[i - 1] <= permutation[j - 1]:
                    count += 1
        return count
    
    # Calculate the sum of happiness for all permutations
    total_happiness = 0
    for permutation in itertools.permutations(range(1, n + 1)):
        total_happiness += count_framed_segments(permutation)
    
    # Return the result modulo m
    return total_happiness % m


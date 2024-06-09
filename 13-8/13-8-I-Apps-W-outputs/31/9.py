
def permutation_happiness(n, m):
    # Calculate the sum of happiness for all permutations of length n
    sum_happiness = 0
    for perm in permutations(range(1, n+1)):
        happiness = 0
        for i in range(1, n+1):
            # Check if [i, i] is a framed segment
            if perm[i-1] == i:
                happiness += 1
            else:
                # Check if [i, n] is a framed segment
                if perm[i-1] == n:
                    happiness += 1
                # Check if [1, i] is a framed segment
                if perm[n-1] == i:
                    happiness += 1
        sum_happiness += happiness
    return sum_happiness % m


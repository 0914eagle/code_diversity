
def solve(N, L):
    # Calculate the sum of the flavors of all apples
    total_flavor = sum(range(L, L+N))
    # Calculate the sum of the flavors of the remaining apples after eating one apple
    remaining_flavor = sum(range(L+1, L+N))
    # Return the difference between the two sums
    return abs(total_flavor - remaining_flavor)


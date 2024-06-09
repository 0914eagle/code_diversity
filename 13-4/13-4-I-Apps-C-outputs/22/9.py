
def solve(n, m, b, mod, a):
    # Calculate the sum of the given numbers
    sum_a = sum(a)
    
    # Initialize a variable to store the result
    result = 0
    
    # Iterate over the given numbers
    for i in range(1, m + 1):
        # Calculate the number of ways to choose i numbers from the given numbers such that their sum is equal to m
        result += comb(n, i) * comb(sum_a, m - i)
    
    # Return the result modulo the given modulo
    return result % mod


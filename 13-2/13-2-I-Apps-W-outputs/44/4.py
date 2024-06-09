
def solve(n, k, a):
    # Calculate the number of possible permutations of the array
    permutations = 1
    for i in range(n):
        permutations *= n - i
    
    # Calculate the number of permutations that result in a sorted array
    sorted_permutations = 1
    for i in range(n - 1):
        sorted_permutations *= n - i
    
    # Calculate the number of permutations that result in a non-sorted array
    non_sorted_permutations = permutations - sorted_permutations
    
    # Calculate the probability that the array is sorted after k operations
    probability = non_sorted_permutations / permutations
    
    # Raise the probability to the kth power
    probability = probability ** k
    
    # Calculate the modular inverse of the probability
    modular_inverse = 1000000007 - probability % 1000000007
    
    # Return the result
    return modular_inverse



def get_happiness(n, m):
    # Calculate the factorial of n
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    
    # Initialize the sum of happiness to 0
    sum_happiness = 0
    
    # Iterate through all permutations of length n
    for permutation in range(1, factorial+1):
        # Convert the permutation to a list of integers
        permutation_list = [int(i) for i in str(permutation)]
        
        # Initialize the happiness of the permutation to 0
        happiness = 0
        
        # Iterate through all subsegments of the permutation
        for l in range(1, n+1):
            for r in range(l, n+1):
                # Check if the subsegment is a framed segment
                if max(permutation_list[l-1:r]) - min(permutation_list[l-1:r]) == r - l:
                    happiness += 1
        
        # Add the happiness of the permutation to the sum
        sum_happiness += happiness
    
    # Return the sum of happiness modulo m
    return sum_happiness % m



def get_happiness(n, m):
    # Calculate the total number of permutations of length n
    total_permutations = 1
    for i in range(2, n+1):
        total_permutations *= i
    
    # Initialize the sum of happiness to 0
    sum_of_happiness = 0
    
    # Iterate through all permutations of length n
    for permutation in range(1, total_permutations+1):
        # Convert the permutation number to a list of digits
        permutation_list = [int(digit) for digit in str(permutation)]
        
        # Initialize the happiness of the permutation to 0
        happiness = 0
        
        # Iterate through all subsegments of the permutation
        for l in range(1, n+1):
            for r in range(l, n+1):
                # Check if the subsegment is a framed segment
                if is_framed_segment(permutation_list, l, r):
                    # Increment the happiness of the permutation
                    happiness += 1
        
        # Add the happiness of the permutation to the sum of happiness
        sum_of_happiness += happiness
    
    # Return the sum of happiness modulo m
    return sum_of_happiness % m

def is_framed_segment(permutation_list, l, r):
    # Check if the subsegment is a valid subsegment
    if l > r or l < 1 or r > len(permutation_list):
        return False
    
    # Initialize the maximum and minimum values in the subsegment
    max_value = permutation_list[l-1]
    min_value = permutation_list[l-1]
    
    # Iterate through the elements in the subsegment
    for i in range(l, r+1):
        # Update the maximum and minimum values
        if permutation_list[i-1] > max_value:
            max_value = permutation_list[i-1]
        if permutation_list[i-1] < min_value:
            min_value = permutation_list[i-1]
    
    # Check if the subsegment is a framed segment
    return max_value - min_value == r - l


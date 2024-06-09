
def solve(n, p, q, s, classical_difficulties, creative_difficulties):
    # Sort the difficulties of the classical and creative problems
    classical_difficulties.sort()
    creative_difficulties.sort()
    
    # Initialize the minimum difference between the difficulties of the two problems as infinity
    min_diff = float('inf')
    
    # Iterate over all possible combinations of classical and creative problems
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the sum of the difficulties of the two problems
            sum_diff = classical_difficulties[i] + creative_difficulties[j]
            
            # If the sum of the difficulties is less than or equal to the given maximum, calculate the difference between the difficulties
            if sum_diff <= s:
                diff = abs(classical_difficulties[i] - creative_difficulties[j])
                
                # Update the minimum difference if it is smaller than the current minimum
                if diff < min_diff:
                    min_diff = diff
    
    # If no combination of problems satisfies the conditions, return -1
    if min_diff == float('inf'):
        return -1
    
    # Otherwise, return the minimum difference
    return min_diff


def get_maximum_score(n, k, sequence):
    # Sort the sequence in non-decreasing order
    sequence.sort()
    
    # Initialize the maximum score to 0
    max_score = 0
    
    # Iterate over each possible partition of the sequence
    for i in range(n - k + 1):
        # Get the current partition of the sequence
        current_partition = sequence[i:i+k]
        
        # Initialize the current score to 0
        current_score = 0
        
        # Iterate over each region in the current partition
        for j in range(k):
            # Get the largest prime number that divides every number in the current region
            prime = get_largest_prime_divisor(current_partition[j])
            
            # If a prime number is found, add it to the current score
            if prime > 0:
                current_score += prime
        
        # Update the maximum score if the current score is greater than the previous maximum score
        if current_score > max_score:
            max_score = current_score
    
    # Return the maximum score
    return max_score

def get_largest_prime_divisor(n):
    # Initialize the largest prime divisor to 0
    largest_prime_divisor = 0
    
    # Iterate over each possible prime number from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If the current prime number divides n, update the largest prime divisor
        if n % i == 0:
            largest_prime_divisor = i
    
    # Return the largest prime divisor
    return largest_prime_divisor


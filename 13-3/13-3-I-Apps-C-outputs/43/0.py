
def get_maximum_score(n, k, sequence):
    # Sort the sequence in non-decreasing order
    sequence.sort()
    
    # Initialize the maximum score to 0
    max_score = 0
    
    # Iterate over the possible partitions of the sequence
    for i in range(k):
        # Get the current partition
        partition = sequence[i::k]
        
        # Initialize the current score to 0
        current_score = 0
        
        # Iterate over the elements in the current partition
        for j in range(len(partition)):
            # Get the current element
            element = partition[j]
            
            # Find the largest prime number that divides the current element
            prime = get_largest_prime_divisor(element)
            
            # If a prime number is found, add it to the current score
            if prime > 0:
                current_score += prime
        
        # Update the maximum score if the current score is greater than the previous maximum score
        max_score = max(max_score, current_score)
    
    # Return the maximum score
    return max_score

def get_largest_prime_divisor(n):
    # Initialize the largest prime divisor to 0
    largest_prime_divisor = 0
    
    # Iterate over the possible prime divisors of n
    for i in range(2, int(n ** 0.5) + 1):
        # If i is a prime divisor of n, update the largest prime divisor
        if n % i == 0:
            largest_prime_divisor = i
    
    # Return the largest prime divisor
    return largest_prime_divisor


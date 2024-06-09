
def get_maximum_score(n, k, sequence):
    # Sort the sequence in non-decreasing order
    sequence.sort()
    
    # Initialize the maximum score to 0
    max_score = 0
    
    # Iterate over each possible partition of the sequence into k regions
    for i in range(k):
        # Get the current region
        current_region = sequence[i::k]
        
        # Initialize the current score to 0
        current_score = 0
        
        # Iterate over each number in the current region
        for num in current_region:
            # Find the largest prime number that divides num
            prime = get_largest_prime_divisor(num)
            
            # If a prime is found, add it to the current score
            if prime > 0:
                current_score += prime
        
        # Update the maximum score if the current score is greater than the previous maximum score
        max_score = max(max_score, current_score)
    
    # Return the maximum score
    return max_score

def get_largest_prime_divisor(n):
    # Initialize the largest prime divisor to 0
    largest_prime = 0
    
    # Iterate over each possible prime factor of n
    for i in range(2, int(n ** 0.5) + 1):
        # If i is a prime factor of n, update the largest prime divisor
        if n % i == 0:
            largest_prime = i
    
    # Return the largest prime divisor
    return largest_prime

n, k = map(int, input().split())
sequence = list(map(int, input().split()))
print(get_maximum_score(n, k, sequence))


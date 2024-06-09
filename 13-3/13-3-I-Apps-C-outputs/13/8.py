
def get_m_numbers(numbers):
    # Initialize a set to store the remainders
    remainders = set()
    
    # Iterate through the given numbers
    for num in numbers:
        # Iterate through the possible divisors
        for div in range(2, num):
            # If the remainder is already in the set, return the current divisor
            if num % div in remainders:
                return div
        # Add the remainder to the set
        remainders.add(num % div)
    
    # If no common remainder is found, return 1
    return 1



def get_m_numbers(numbers):
    # Initialize a set to store the remainders
    remainders = set()
    
    # Iterate through the given numbers
    for num in numbers:
        # Iterate through the possible values of M
        for m in range(2, 100000001):
            # Check if the current remainder is already in the set
            if num % m in remainders:
                # If it is, add it to the set and break the inner loop
                remainders.add(num % m)
                break
    
    # Return the set of all possible M numbers
    return remainders



def find_m(numbers):
    # Initialize a set to store the remainders
    remainders = set()
    
    # Iterate through the numbers
    for num in numbers:
        # Calculate the remainder of each number when divided by M
        for m in range(2, 1000000001):
            if num % m == 0:
                remainders.add(m)
                break
    
    # Return the list of unique remainders
    return list(remainders)


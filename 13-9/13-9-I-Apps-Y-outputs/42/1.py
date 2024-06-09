
def get_common_divisors(a):
    # Convert the list to a set to remove duplicates
    a = set(a)
    # Initialize the number of common divisors to 0
    num_common_divisors = 0
    # Iterate through the list of numbers
    for i in range(1, max(a)):
        # Check if the current number is a divisor of all numbers in the list
        if all(x % i == 0 for x in a):
            # Increment the number of common divisors
            num_common_divisors += 1
    # Return the number of common divisors
    return num_common_divisors


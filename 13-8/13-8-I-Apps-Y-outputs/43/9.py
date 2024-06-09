
def largest_perfect_power(X):
    # Initialize a list to store the perfect powers
    perfect_powers = []

    # Loop through all integers from 1 to X
    for i in range(1, X + 1):
        # Check if the integer is a perfect power
        if is_perfect_power(i):
            # If it is a perfect power, add it to the list
            perfect_powers.append(i)

    # Return the largest perfect power in the list
    return max(perfect_powers)

def is_perfect_power(n):
    # Initialize a variable to store the result
    result = False

    # Loop through all integers from 1 to the square root of n
    for i in range(1, int(n ** 0.5) + 1):
        # Check if i is a factor of n
        if n % i == 0:
            # If it is, return True
            return True

    # If no factor is found, return False
    return result

X = int(input())
print(largest_perfect_power(X))


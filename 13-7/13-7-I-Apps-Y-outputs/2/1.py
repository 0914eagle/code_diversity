
def solve(n):
    # Initialize a set to store the numbers that have already been seen
    seen = set()
    # Initialize a variable to store the minimum number of moves required
    min_moves = 0
    # Loop until the number is 1 or has already been seen
    while n != 1 and n not in seen:
        # If the number is divisible by 2, divide it by 2
        if n % 2 == 0:
            n //= 2
        # If the number is divisible by 3, divide it by 3
        elif n % 3 == 0:
            n //= 3
        # If the number is divisible by 5, divide it by 5
        elif n % 5 == 0:
            n //= 5
        # If the number is not divisible by 2, 3, or 5, it is impossible to obtain 1
        else:
            return -1
        # Add the current number to the set of seen numbers
        seen.add(n)
        # Increment the minimum number of moves required
        min_moves += 1
    # Return the minimum number of moves required
    return min_moves


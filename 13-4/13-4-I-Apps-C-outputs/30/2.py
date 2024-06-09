
def get_badge_numbers(N, L, B, S, D, locks):
    # Initialize a set to store the badge numbers that can pass from S to D
    badge_numbers = set()

    # Iterate through each lock
    for lock in locks:
        # Extract the information from the lock
        a, b, x, y = lock

        # Check if the lock is between S and D
        if a == S and b == D:
            # Add the badge numbers to the set
            badge_numbers |= set(range(x, y + 1))

    # Return the number of badge numbers in the set
    return len(badge_numbers)


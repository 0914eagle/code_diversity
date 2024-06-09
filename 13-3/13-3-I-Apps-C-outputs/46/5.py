
def get_badge_numbers(n, l, b, s, d, locks):
    # Initialize a set to store the badge numbers that can pass from room s to room d
    badge_numbers = set()

    # Iterate through each lock
    for lock in locks:
        # Extract the information from the lock
        a, b, x, y = lock

        # Check if the lock is between the starting and destination rooms
        if a == s and b == d:
            # Add the badge numbers that can pass through the lock to the set
            badge_numbers |= set(range(x, y + 1))

    # Return the number of badge numbers that can pass from room s to room d
    return len(badge_numbers)


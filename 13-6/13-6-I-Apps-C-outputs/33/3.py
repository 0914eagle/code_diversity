
def get_badge_numbers(n, l, b, s, d, locks):
    # Initialize a set to store the badge numbers that can pass from room s to room d
    badge_numbers = set()

    # Loop through each lock
    for a, b, x, y in locks:
        # If the lock is between rooms s and d, add the badge numbers that can pass through the lock to the set
        if a == s and b == d:
            badge_numbers |= set(range(x, y + 1))

    # Return the length of the set, which is the number of badge numbers that can pass from room s to room d
    return len(badge_numbers)



def get_badge_numbers(start, end, locks):
    # Initialize a set to store the badge numbers
    badge_numbers = set()

    # Iterate through the locks
    for lock in locks:
        # Check if the lock is between the start and end rooms
        if lock[0] == start and lock[1] == end:
            # Add the badge numbers to the set
            badge_numbers.update(range(lock[2], lock[3] + 1))

    # Return the length of the set
    return len(badge_numbers)



def get_badge_numbers(start, end, locks):
    # Initialize a set to store the badge numbers that can pass through the locks
    badge_numbers = set()

    # Iterate through the locks
    for lock in locks:
        # If the lock is between the start and end rooms, add the badge numbers to the set
        if lock[0] == start and lock[1] == end:
            badge_numbers.update(range(lock[2], lock[3] + 1))

    # Return the number of badge numbers in the set
    return len(badge_numbers)


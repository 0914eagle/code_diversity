
def get_badge_numbers(start_room, end_room, locks):
    # Initialize a set to store the badge numbers that can pass through the locks
    badge_numbers = set()

    # Iterate through the locks
    for lock in locks:
        # If the lock is between the start and end rooms, add the badge numbers to the set
        if lock[0] == start_room and lock[1] == end_room:
            badge_numbers.update(range(lock[2], lock[3] + 1))

    # Return the length of the set, which is the number of badge numbers that can pass through the locks
    return len(badge_numbers)


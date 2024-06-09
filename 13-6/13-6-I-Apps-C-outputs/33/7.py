
def get_badge_numbers(num_rooms, num_locks, num_badges, start_room, end_room, locks):
    # Initialize a set to store the badge numbers that can pass through the locks
    badge_numbers = set()

    # Iterate through the locks
    for lock in locks:
        # Extract the information from the lock
        room_a, room_b, low, high = lock

        # Check if the lock is between the start and end rooms
        if room_a == start_room and room_b == end_room:
            # Add the badge numbers that can pass through the lock to the set
            badge_numbers |= set(range(low, high + 1))

    # Return the number of badge numbers that can pass through the locks
    return len(badge_numbers)


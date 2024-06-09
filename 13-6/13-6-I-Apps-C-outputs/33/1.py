
def get_badge_numbers(rooms, locks, badges, start_room, end_room):
    # Initialize a set to store the badge numbers that can pass through the locks
    badge_numbers = set()

    # Iterate through the locks
    for lock in locks:
        # Extract the lock details
        room_a, room_b, lower_bound, upper_bound = lock

        # Check if the lock is between the start and end rooms
        if room_a == start_room and room_b == end_room:
            # Add the badge numbers to the set
            badge_numbers.update(range(lower_bound, upper_bound + 1))

    # Return the number of badge numbers that can pass through the locks
    return len(badge_numbers)


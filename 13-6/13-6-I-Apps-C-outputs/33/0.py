
def get_badge_numbers(n_rooms, n_locks, n_badges, start_room, dest_room, locks):
    # Initialize a set to store the badge numbers that can pass through the locks
    badge_numbers = set()

    # Iterate through the locks
    for lock in locks:
        # Extract the lock information
        room_a, room_b, lower_bound, upper_bound = lock

        # Check if the lock is between the start and destination rooms
        if room_a == start_room and room_b == dest_room:
            # Add the badge numbers within the range to the set
            badge_numbers |= set(range(lower_bound, upper_bound + 1))

        # Check if the lock is between the destination and start rooms
        elif room_b == start_room and room_a == dest_room:
            # Add the badge numbers within the range to the set
            badge_numbers |= set(range(lower_bound, upper_bound + 1))

    # Return the length of the set
    return len(badge_numbers)


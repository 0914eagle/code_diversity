
def get_passage_badges(rooms, locks, badges, start_room, end_room):
    # Initialize a set to store the badge numbers that can pass from the start room to the end room
    passage_badges = set()

    # Iterate through the locks
    for lock in locks:
        # Extract the lock details
        lock_from, lock_to, lower_bound, upper_bound = lock

        # Check if the lock is between the start and end rooms
        if lock_from == start_room and lock_to == end_room:
            # Add the badge numbers that are within the range specified by the lock to the passage badges set
            passage_badges.update(range(lower_bound, upper_bound + 1))

    # Return the number of passage badges
    return len(passage_badges)


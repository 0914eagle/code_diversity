
def get_passage_badges(start_room, end_room, locks):
    # Initialize a set to store the badge numbers that can pass from the start room to the end room
    passage_badges = set()

    # Iterate through the locks
    for lock in locks:
        # If the lock is from the start room to the end room, add the badge numbers that can pass through the lock to the set
        if lock[0] == start_room and lock[1] == end_room:
            passage_badges.update(range(lock[2], lock[3] + 1))

    # Return the number of badge numbers in the set
    return len(passage_badges)


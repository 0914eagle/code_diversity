
def is_possible(configuration_senior, configuration_you):
    # Initialize a set to store the rooms visited by the senior student
    visited_rooms_senior = set()
    # Initialize a set to store the rooms visited by you
    visited_rooms_you = set()
    # Initialize a queue to store the rooms to visit
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Dequeue a room from the queue
        current_room = queue.pop(0)
        # If the room is the dormitory, return True
        if current_room == n:
            return True
        # If the room has already been visited by the senior student, skip it
        if current_room in visited_rooms_senior:
            continue
        # If the room has already been visited by you, return False
        if current_room in visited_rooms_you:
            return False
        # Add the current room to the set of visited rooms
        visited_rooms_you.add(current_room)
        # Get the exits of the current room from the configuration
        exits = configuration_you[current_room - 1]
        # If any of the exits is blocked, return False
        if any(exit == 0 for exit in exits):
            return False
        # Add the exits to the queue
        queue.extend(exit for exit in exits if exit not in visited_rooms_you)
    # If the queue is empty and the dormitory has not been visited, return False
    return False


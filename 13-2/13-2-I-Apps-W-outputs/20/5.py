
def is_possible(n, config_senior, config_you):
    # Initialize a set to store the rooms visited by the senior student
    visited_rooms = set()
    # Initialize the current room as the entrance
    current_room = 1
    # Loop through the sequence of instructions given by the senior student
    for instruction in config_senior:
        # If the current room is not blocked and has not been visited before, mark it as visited
        if instruction != 0 and current_room not in visited_rooms:
            visited_rooms.add(current_room)
        # Move to the next room according to the instruction given by the senior student
        current_room = instruction
    # If the senior student reached the dormitory, return True
    if current_room == n:
        return True
    # Initialize a set to store the rooms visited by you
    visited_rooms = set()
    # Initialize the current room as the entrance
    current_room = 1
    # Loop through the sequence of instructions given by you
    for instruction in config_you:
        # If the current room is not blocked and has not been visited before, mark it as visited
        if instruction != 0 and current_room not in visited_rooms:
            visited_rooms.add(current_room)
        # Move to the next room according to the instruction given by you
        current_room = instruction
    # If you reached the dormitory and all the rooms visited by the senior student are also visited by you, return True
    return current_room == n and visited_rooms >= visited_rooms



def is_possible(senior_student_config, your_config):
    # Initialize a set to store the rooms visited by the senior student
    visited_rooms = set()
    # Initialize the current room as the entrance
    current_room = 1
    # Loop through the sequence of instructions given by the senior student
    for instruction in senior_student_config:
        # If the instruction is not blocked, add the room to the set of visited rooms
        if instruction != 0:
            visited_rooms.add(instruction)
        # Set the current room to the next room according to the instruction
        current_room = instruction
    # Loop through the rooms in the configuration you are given
    for room in your_config:
        # If the room is not blocked and is not in the set of visited rooms, return No
        if room != 0 and room not in visited_rooms:
            return "No"
    # If all rooms are visited or blocked, return Yes
    return "Yes"


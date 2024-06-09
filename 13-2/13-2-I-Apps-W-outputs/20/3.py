
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
    # Check if the dormitory is in the set of visited rooms
    if 4 in visited_rooms:
        return "Yes"
    else:
        return "No"


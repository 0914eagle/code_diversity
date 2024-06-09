
def is_possible(senior_student_path, current_path):
    # Initialize a set to store the rooms visited by the senior student
    visited_rooms = set()
    # Initialize a set to store the rooms visited by you
    current_rooms = set()
    # Loop through the senior student's path
    for room in senior_student_path:
        # If the room is not blocked, add it to the set of visited rooms
        if room != 0:
            visited_rooms.add(room)
    # Loop through the current path
    for room in current_path:
        # If the room is not blocked, add it to the set of visited rooms
        if room != 0:
            current_rooms.add(room)
    # Check if the sets of visited rooms are equal
    return visited_rooms == current_rooms


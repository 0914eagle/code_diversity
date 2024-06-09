
def get_min_rooms(notes):
    # Initialize a set to store the unique rooms visited
    rooms_visited = set()
    # Iterate through the notes in the logbook
    for note in notes:
        # If the current note is 0, it means Petya visited a new room
        if note == 0:
            # Add the current room to the set of visited rooms
            rooms_visited.add(len(rooms_visited))
        # If the current note is not 0, it means Petya visited a room before
        else:
            # Add the previous room to the set of visited rooms
            rooms_visited.add(note - 1)
    # Return the length of the set of visited rooms, which is the minimum number of rooms
    return len(rooms_visited)


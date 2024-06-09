
def get_min_rooms(notes):
    # Initialize a set to store the unique rooms visited
    rooms = set()
    # Iterate through the notes
    for note in notes:
        # If the note is 0, it means Petya visited a new room
        if note == 0:
            # Add the room to the set of visited rooms
            rooms.add(len(rooms))
        # If the note is not 0, it means Petya visited a room before
        else:
            # Add the room to the set of visited rooms
            rooms.add(note)
    # Return the length of the set of visited rooms, which is the minimum number of rooms
    return len(rooms)


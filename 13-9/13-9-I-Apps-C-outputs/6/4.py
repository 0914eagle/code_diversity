
def max_rooms_hit(rooms, beam_length):
    # Sort the rooms by their x-coordinate
    sorted_rooms = sorted(rooms, key=lambda x: x[0])

    # Initialize the maximum number of rooms hit to 0
    max_rooms = 0

    # Iterate over the sorted rooms
    for i in range(len(sorted_rooms)):
        # Get the current room
        current_room = sorted_rooms[i]

        # Check if the room is within the beam length
        if current_room[0] + beam_length >= sorted_rooms[i + 1][0]:
            # Increment the maximum number of rooms hit
            max_rooms += 1

    return max_rooms


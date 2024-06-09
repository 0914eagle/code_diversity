
def solve(rooms, beam_length):
    # Sort the rooms by their lower left corner (x1, y1)
    sorted_rooms = sorted(rooms, key=lambda x: (x[0], x[1]))

    # Initialize the maximum number of rooms that can be hit as 0
    max_rooms = 0

    # Iterate through the sorted rooms
    for i in range(len(sorted_rooms)):
        # Get the current room and its coordinates
        room = sorted_rooms[i]
        x1, y1, x2, y2 = room

        # Check if the current room is within the beam length
        if x2 - x1 <= beam_length:
            # If the room is within the beam length, increment the maximum number of rooms that can be hit
            max_rooms += 1

        # Check if the current room is the last room
        if i == len(sorted_rooms) - 1:
            # If the current room is the last room, check if the beam length needs to be adjusted
            if x2 - x1 > beam_length:
                # If the beam length needs to be adjusted, adjust it to the maximum possible length
                beam_length = x2 - x1

    return max_rooms


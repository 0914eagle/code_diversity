
def solve(r, l, rooms):
    # Sort the rooms by their x-coordinates
    sorted_rooms = sorted(rooms, key=lambda x: x[0])

    # Initialize the maximum number of rooms that can be hit
    max_rooms = 0

    # Iterate over the rooms
    for i in range(r):
        # Get the current room
        room = sorted_rooms[i]

        # Check if the room is within the range of the phaser beam
        if room[0] + l >= sorted_rooms[i+1][0]:
            # If the room is within the range, increase the maximum number of rooms that can be hit
            max_rooms += 1

    # Return the maximum number of rooms that can be hit
    return max_rooms


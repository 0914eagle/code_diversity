
def hit_rooms(rooms, beam_length):
    # Sort the rooms by their upper right corner x-coordinate
    sorted_rooms = sorted(rooms, key=lambda x: x[2])

    # Initialize the maximum number of rooms hit to 0
    max_hit_rooms = 0

    # Iterate over the sorted rooms
    for i in range(len(sorted_rooms)):
        # Get the current room
        room = sorted_rooms[i]

        # Get the x-coordinate of the current room's upper right corner
        x2 = room[2]

        # Check if the current room is within the beam's range
        if x2 <= beam_length:
            # Increment the maximum number of rooms hit
            max_hit_rooms += 1

            # Check if the current room is the last room
            if i == len(sorted_rooms) - 1:
                # Break out of the loop
                break

            # Get the next room
            next_room = sorted_rooms[i + 1]

            # Get the x-coordinate of the next room's upper right corner
            next_x2 = next_room[2]

            # Check if the next room is within the beam's range
            if next_x2 <= beam_length:
                # Merge the current room with the next room
                merged_room = [room[0], room[1], next_x2, next_room[3]]

                # Add the merged room to the sorted rooms list
                sorted_rooms.insert(i + 1, merged_room)

                # Remove the next room from the sorted rooms list
                sorted_rooms.pop(i + 2)

    return max_hit_rooms


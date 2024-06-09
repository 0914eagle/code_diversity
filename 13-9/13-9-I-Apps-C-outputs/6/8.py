
def max_rooms_hit(r, l, rooms):
    # Sort the rooms by their area in descending order
    sorted_rooms = sorted(rooms, key=lambda x: (x[2] - x[0]) * (x[3] - x[1]), reverse=True)

    # Initialize the maximum number of rooms hit to 0
    max_rooms = 0

    # Loop through the sorted rooms
    for room in sorted_rooms:
        # Calculate the area of the room
        area = (room[2] - room[0]) * (room[3] - room[1])

        # Check if the area is greater than the length of the phaser beam
        if area > l:
            # Calculate the length of the line segment that intersects the room
            line_segment_length = (room[2] - room[0]) + (room[3] - room[1])

            # Calculate the number of rooms hit by the line segment
            num_rooms = line_segment_length // l

            # Update the maximum number of rooms hit if necessary
            max_rooms = max(max_rooms, num_rooms)

    # Return the maximum number of rooms hit
    return max_rooms


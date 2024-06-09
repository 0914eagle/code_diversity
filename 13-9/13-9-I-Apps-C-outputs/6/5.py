
def solve(r, l, rooms):
    # Sort the rooms by their lower left corner
    sorted_rooms = sorted(rooms, key=lambda x: (x[0], x[1]))

    # Initialize the maximum number of rooms that can be hit
    max_rooms = 0

    # Iterate over each room
    for i in range(r):
        # Get the current room
        room = sorted_rooms[i]

        # Get the center of the room
        cx = (room[0] + room[2]) / 2
        cy = (room[1] + room[3]) / 2

        # Calculate the angle between the center of the room and the beam
        theta = math.atan2(cy - l, cx)

        # Calculate the distance between the center of the room and the beam
        d = math.hypot(cx - l, cy)

        # Calculate the number of rooms that can be hit by the beam
        num_rooms = 0
        for j in range(i, r):
            # Get the next room
            next_room = sorted_rooms[j]

            # Check if the next room is within the beam
            if is_within_beam(next_room, cx, cy, theta, d):
                # Increment the number of rooms that can be hit
                num_rooms += 1

        # Update the maximum number of rooms that can be hit
        max_rooms = max(max_rooms, num_rooms)

    # Return the maximum number of rooms that can be hit
    return max_rooms

# Check if a room is within the beam
def is_within_beam(room, cx, cy, theta, d):
    # Calculate the center of the room
    rx = (room[0] + room[2]) / 2
    ry = (room[1] + room[3]) / 2

    # Calculate the distance between the center of the room and the beam
    rd = math.hypot(rx - cx, ry - cy)

    # Check if the distance is less than or equal to the beam length
    if rd <= d:
        # Calculate the angle between the center of the room and the beam
        rtheta = math.atan2(ry - cy, rx - cx)

        # Check if the angle is within the beam's angle of fire
        if abs(theta - rtheta) <= math.pi / 2:
            return True

    return False


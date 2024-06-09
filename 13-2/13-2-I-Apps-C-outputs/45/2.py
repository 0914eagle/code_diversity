
def get_identical_rooms(maze):
    # Initialize a dictionary to store the rooms and their connections
    rooms = {}
    for i, room in enumerate(maze):
        rooms[i] = set(room[1:])

    # Initialize a set to store the effectively identical rooms
    identical_rooms = set()

    # Loop through each room and its connections
    for room, connections in rooms.items():
        # If the room has already been marked as effectively identical, skip it
        if room in identical_rooms:
            continue

        # Initialize a set to store the rooms that are effectively identical to the current room
        identical_rooms_set = set([room])

        # Loop through each connection and check if it is effectively identical to the current room
        for connection in connections:
            # If the connection is not in the dictionary or it is already marked as effectively identical, skip it
            if connection not in rooms or connection in identical_rooms:
                continue

            # Check if the connection is effectively identical to the current room
            if rooms[connection] == connections:
                identical_rooms_set.add(connection)

        # If the set of effectively identical rooms is not empty, add it to the overall set
        if identical_rooms_set:
            identical_rooms.update(identical_rooms_set)

    return identical_rooms


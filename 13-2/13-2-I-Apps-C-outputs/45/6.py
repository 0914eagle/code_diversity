
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

        # Loop through each connection of the current room
        for connection in connections:
            # If the connection is not already in the set of effectively identical rooms, add it
            if connection not in identical_rooms_set:
                identical_rooms_set.add(connection)

                # Add the connections of the connection to the set
                for connection_connection in rooms[connection]:
                    if connection_connection not in identical_rooms_set:
                        identical_rooms_set.add(connection_connection)

        # Add the set of effectively identical rooms to the overall set
        identical_rooms |= identical_rooms_set

    return identical_rooms


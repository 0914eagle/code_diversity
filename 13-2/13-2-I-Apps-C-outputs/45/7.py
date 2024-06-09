
def get_identical_rooms(maze):
    # Initialize a dictionary to store the room numbers and their connections
    room_connections = {}
    for i, room in enumerate(maze):
        room_connections[i] = set(room[1:])

    # Initialize a set to store the effective identical rooms
    identical_rooms = set()

    # Loop through each room and its connections
    for room, connections in room_connections.items():
        # If the room has no connections, skip it
        if not connections:
            continue
        # If the room is already in the set of effective identical rooms, skip it
        if room in identical_rooms:
            continue
        # Otherwise, add the room to the set and its connections to the dictionary
        identical_rooms.add(room)
        for connection in connections:
            room_connections[connection].add(room)

    # Return the set of effective identical rooms
    return identical_rooms



def get_identical_rooms(maze):
    # Initialize a dictionary to store the room numbers and their connections
    room_connections = {}
    for room in maze:
        room_connections[room[0]] = set(room[1:])

    # Initialize a set to store the effectively identical rooms
    identical_rooms = set()

    # Iterate through the rooms and their connections
    for room, connections in room_connections.items():
        # If the room has already been marked as effectively identical, skip it
        if room in identical_rooms:
            continue
        # If the room has no connections, it is effectively identical to itself
        if not connections:
            identical_rooms.add(room)
            continue
        # If the room has connections, find the effectively identical rooms
        for connection in connections:
            # If the connection is not in the dictionary, it is effectively identical to the current room
            if connection not in room_connections:
                identical_rooms.add(room)
                break
            # If the connection is in the dictionary but has no connections, it is effectively identical to the current room
            elif not room_connections[connection]:
                identical_rooms.add(room)
                break
            # If the connection is in the dictionary and has connections, find the effectively identical rooms recursively
            else:
                recursive_identical_rooms = get_identical_rooms(room_connections[connection])
                identical_rooms.update(recursive_identical_rooms)
                identical_rooms.add(room)
                break

    return identical_rooms


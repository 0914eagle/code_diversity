
def get_identical_rooms(maze):
    # Initialize a dictionary to store the room numbers and their connections
    room_connections = {}
    for room_num, connections in enumerate(maze, start=1):
        room_connections[room_num] = set(connections)

    # Initialize a set to store the effectively identical room sets
    identical_rooms = set()

    # Iterate through the room connections and find pairs of rooms that are effectively identical
    for room_num, connections in room_connections.items():
        for other_room_num in connections:
            if room_num < other_room_num:
                continue
            if room_connections[other_room_num] == connections:
                identical_rooms.add(frozenset({room_num, other_room_num}))

    # Return the set of effectively identical room sets
    return identical_rooms


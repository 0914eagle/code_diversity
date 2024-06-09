
def get_identical_rooms(maze):
    # Initialize a dictionary to store the room numbers and their connections
    room_connections = {}
    for i, room in enumerate(maze):
        room_connections[i] = set(room[1:])

    # Initialize a set to store the effectively identical rooms
    identical_rooms = set()

    # Loop through each room and its connections
    for room, connections in room_connections.items():
        # If the room has already been marked as effectively identical, skip it
        if room in identical_rooms:
            continue
        # If the room has no connections, add it to the set of effectively identical rooms
        if not connections:
            identical_rooms.add(room)
            continue
        # If the room has connections, find the effectively identical rooms by recursively searching the graph
        find_identical_rooms(room, connections, identical_rooms, room_connections)

    return identical_rooms

def find_identical_rooms(room, connections, identical_rooms, room_connections):
    # If the room has already been marked as effectively identical, return
    if room in identical_rooms:
        return
    # If the room has no connections, add it to the set of effectively identical rooms
    if not connections:
        identical_rooms.add(room)
        return
    # Recursively search the graph for effectively identical rooms
    for connection in connections:
        find_identical_rooms(connection, room_connections[connection] - {room}, identical_rooms, room_connections)
    identical_rooms.add(room)

def main():
    maze = [[2, 4], [3, 1, 3, 5], [2, 2, 4], [3, 1, 3, 6], [2, 2, 6], [2, 4, 5], [2, 8, 9], [2, 7, 9], [2, 7, 8], [2, 11, 13], [2, 10, 12], [2, 11, 13], [2, 10, 12]]
    identical_rooms = get_identical_rooms(maze)
    print(identical_rooms)

if __name__ == "__main__":
    main()



def get_connected_rooms(rooms, doors):
    # Initialize a dictionary to store the connected rooms
    connected_rooms = {}

    # Iterate over the doors
    for door in doors:
        # If the door connects to the outside, add it to the dictionary with a key of -1
        if door[0] == -1 or door[1] == -1:
            connected_rooms[-1] = connected_rooms.get(-1, []) + [door[0], door[1]]
        # Otherwise, add it to the dictionary with a key of the smaller room number
        else:
            connected_rooms[min(door[0], door[1])] = connected_rooms.get(min(door[0], door[1]), []) + [max(door[0], door[1])]

    # Return the connected rooms dictionary
    return connected_rooms

def get_protected_rooms(rooms, doors):
    # Get the connected rooms
    connected_rooms = get_connected_rooms(rooms, doors)

    # Initialize a set to store the protected rooms
    protected_rooms = set()

    # Iterate over the connected rooms
    for room, connected_room_list in connected_rooms.items():
        # If the room is not already in the protected rooms set, add it and all of its connected rooms to the set
        if room not in protected_rooms:
            protected_rooms.add(room)
            protected_rooms.update(connected_room_list)

    # Return the protected rooms set
    return protected_rooms

def get_maximum_protected_rooms(rooms, doors):
    # Get the protected rooms
    protected_rooms = get_protected_rooms(rooms, doors)

    # Return the maximum number of protected rooms
    return len(protected_rooms)

def main():
    # Read the number of rooms and doors
    rooms, doors = map(int, input().split())

    # Read the doors
    door_list = []
    for _ in range(doors):
        door_list.append(list(map(int, input().split())))

    # Get the maximum number of protected rooms
    maximum_protected_rooms = get_maximum_protected_rooms(rooms, door_list)

    # Print the maximum number of protected rooms
    print(maximum_protected_rooms)

if __name__ == '__main__':
    main()



def get_connected_rooms(rooms, doors):
    connected_rooms = set()
    for door in doors:
        connected_rooms.add(door[0])
        connected_rooms.add(door[1])
    return connected_rooms

def get_max_protected_rooms(rooms, doors):
    connected_rooms = get_connected_rooms(rooms, doors)
    max_protected_rooms = 0
    for door in doors:
        if door[0] == -1 or door[1] == -1:
            continue
        protected_rooms = connected_rooms - set([door[0], door[1]])
        max_protected_rooms = max(max_protected_rooms, len(protected_rooms))
    return max_protected_rooms

def main():
    rooms, doors = map(int, input().split())
    doors = [tuple(map(int, input().split())) for _ in range(doors)]
    print(get_max_protected_rooms(rooms, doors))

if __name__ == '__main__':
    main()


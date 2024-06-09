
def get_max_protected_rooms(rooms, doors):
    # Initialize a dictionary to store the number of rooms that can be reached from each room
    reachable_rooms = {}
    for room in rooms:
        reachable_rooms[room] = set()

    # Populate the dictionary with the reachable rooms for each room
    for door in doors:
        reachable_rooms[door[0]].add(door[1])
        reachable_rooms[door[1]].add(door[0])

    # Find the door that leads to the maximum number of rooms that can be protected
    max_protected_rooms = 0
    for door in doors:
        if door[0] == -1 or door[1] == -1:
            continue
        protected_rooms = reachable_rooms[door[0]] | reachable_rooms[door[1]]
        if len(protected_rooms) > max_protected_rooms:
            max_protected_rooms = len(protected_rooms)

    return max_protected_rooms

def main():
    rooms = set(range(int(input())))
    doors = []
    for _ in range(int(input())):
        u, v = map(int, input().split())
        doors.append((u, v))
    print(get_max_protected_rooms(rooms, doors))

if __name__ == '__main__':
    main()


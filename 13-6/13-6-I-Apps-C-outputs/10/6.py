
def get_max_protected_rooms(num_rooms, num_doors, doors):
    # Initialize a graph with the given number of rooms
    graph = [[] for _ in range(num_rooms)]

    # Add edges to the graph based on the given doors
    for u, v in doors:
        graph[u].append(v)
        graph[v].append(u)

    # Find the door that connects the most rooms to the outside of the building
    max_protected_rooms = 0
    for door in range(num_doors):
        # Count the number of rooms that can only be reached from the outside of the building through this door
        protected_rooms = 0
        for room in range(num_rooms):
            if room not in graph[door] and -1 not in graph[room]:
                protected_rooms += 1

        # Update the maximum number of protected rooms if necessary
        if protected_rooms > max_protected_rooms:
            max_protected_rooms = protected_rooms

    return max_protected_rooms

def main():
    num_rooms, num_doors = map(int, input().split())
    doors = []
    for _ in range(num_doors):
        u, v = map(int, input().split())
        doors.append((u, v))
    print(get_max_protected_rooms(num_rooms, num_doors, doors))

if __name__ == '__main__':
    main()


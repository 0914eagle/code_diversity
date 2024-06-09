
def get_maximum_protected_rooms(num_rooms, doors):
    # Initialize a graph with the given number of rooms
    graph = [[] for _ in range(num_rooms)]

    # Add edges to the graph based on the given doors
    for u, v in doors:
        graph[u].append(v)
        graph[v].append(u)

    # Find the room that is not connected to the outside
    outside_room = -1
    for i in range(num_rooms):
        if i not in graph[i]:
            outside_room = i
            break

    # Initialize a variable to store the maximum number of protected rooms
    max_protected_rooms = 0

    # Iterate over all possible doors to replace
    for door in range(num_rooms):
        # Skip the door that is already connected to the outside
        if door == outside_room:
            continue

        # Initialize a variable to store the number of protected rooms
        protected_rooms = 0

        # Iterate over all rooms in the graph
        for room in range(num_rooms):
            # If the room is not connected to the outside and is not connected to the current door, increment the number of protected rooms
            if room not in graph[door] and room not in graph[outside_room]:
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
    print(get_maximum_protected_rooms(num_rooms, doors))

if __name__ == '__main__':
    main()


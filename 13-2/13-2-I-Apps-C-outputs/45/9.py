
def get_max_protected_rooms(num_rooms, num_doors, door_list):
    # Initialize a graph with the given number of rooms
    graph = [[] for _ in range(num_rooms)]

    # Add edges to the graph based on the door list
    for u, v in door_list:
        graph[u].append(v)
        graph[v].append(u)

    # Find the door that connects the most rooms to the outside of the building
    max_protected_rooms = 0
    for door in range(num_doors):
        # Count the number of rooms that can only be reached from the outside through this door
        protected_rooms = 0
        for room in range(num_rooms):
            if room != door and graph[door].count(room) == 1:
                protected_rooms += 1

        # Update the maximum number of protected rooms if necessary
        if protected_rooms > max_protected_rooms:
            max_protected_rooms = protected_rooms

    return max_protected_rooms


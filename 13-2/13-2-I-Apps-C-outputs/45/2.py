
def get_max_protected_rooms(num_rooms, num_doors, doors):
    # Initialize a graph with the given number of rooms
    graph = [[] for _ in range(num_rooms)]

    # Add edges to the graph based on the given doors
    for u, v in doors:
        if u != -1:
            graph[u].append(v)
        if v != -1:
            graph[v].append(u)

    # Find the door that connects the most rooms to the outside of the building
    max_protected_rooms = 0
    for u in range(num_rooms):
        if u != -1:
            protected_rooms = 0
            queue = [u]
            while queue:
                node = queue.pop(0)
                if node != -1:
                    protected_rooms += 1
                    queue.extend(graph[node])
            max_protected_rooms = max(max_protected_rooms, protected_rooms)

    return max_protected_rooms


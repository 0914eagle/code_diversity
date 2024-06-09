
def get_max_protected_rooms(N, M, doors):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N)]
    for u, v in doors:
        graph[u].append(v)
        graph[v].append(u)
    
    # Find all rooms that can be reached from the outside of the building
    outside_rooms = []
    for i in range(N):
        if -1 in graph[i]:
            outside_rooms.append(i)
    
    # Find the room that is connected to the maximum number of outside rooms
    max_protected_rooms = 0
    for i in range(N):
        if i in outside_rooms:
            continue
        protected_rooms = 0
        for j in range(N):
            if j in outside_rooms and j in graph[i]:
                protected_rooms += 1
        if protected_rooms > max_protected_rooms:
            max_protected_rooms = protected_rooms
    
    return max_protected_rooms


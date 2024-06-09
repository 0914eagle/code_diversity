
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
    for room in outside_rooms:
        protected_rooms = 0
        for i in range(N):
            if i in graph[room]:
                protected_rooms += 1
        max_protected_rooms = max(max_protected_rooms, protected_rooms)
    
    return max_protected_rooms



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
    max_rooms = 0
    best_room = -1
    for i in range(N):
        if i in outside_rooms:
            continue
        num_rooms = len(set(outside_rooms) & set(graph[i]))
        if num_rooms > max_rooms:
            max_rooms = num_rooms
            best_room = i
    
    return max_rooms


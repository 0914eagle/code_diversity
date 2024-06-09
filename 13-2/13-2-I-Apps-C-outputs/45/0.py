
def get_max_protected_rooms(N, M, doors):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N)]
    for u, v in doors:
        graph[u].append(v)
        graph[v].append(u)
    
    # Find all rooms that can be reached from the outside of the building
    outside_rooms = set()
    for i in range(N):
        if -1 in graph[i]:
            outside_rooms.add(i)
    
    # Find the set of rooms that can only be reached from the outside of the building
    protected_rooms = set()
    for i in range(N):
        if i not in outside_rooms:
            protected_rooms.add(i)
            for j in graph[i]:
                if j in outside_rooms:
                    protected_rooms.add(j)
    
    return len(protected_rooms)


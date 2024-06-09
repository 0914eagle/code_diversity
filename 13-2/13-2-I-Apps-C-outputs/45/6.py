
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
    
    # Initialize a set to store the rooms that are protected by the secure door
    protected_rooms = set()
    
    # Loop through each outside room and find the maximum number of rooms that can be protected
    max_protected_rooms = 0
    for outside_room in outside_rooms:
        # Breadth-first search to find all rooms that can be reached from the outside room
        queue = [outside_room]
        visited = set()
        while queue:
            current_room = queue.pop(0)
            if current_room not in visited:
                visited.add(current_room)
                queue.extend(graph[current_room])
        
        # Add the current room to the set of protected rooms
        protected_rooms.add(outside_room)
        
        # Update the maximum number of protected rooms
        max_protected_rooms = max(max_protected_rooms, len(visited) - 1)
    
    return max_protected_rooms


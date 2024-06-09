
def f1(N, M, doors):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N)]
    for u, v in doors:
        graph[u].append(v)
        graph[v].append(u)
    
    # Find all rooms that can only be reached from the outside of the building
    outside_rooms = set()
    for i in range(N):
        if i not in graph[i]:
            outside_rooms.add(i)
    
    # Find the maximum number of rooms that can be secured by replacing a single door
    max_rooms = 0
    for i in range(N):
        if i in outside_rooms:
            continue
        rooms = set()
        queue = [i]
        while queue:
            node = queue.pop(0)
            rooms.add(node)
            for neighbor in graph[node]:
                if neighbor not in rooms:
                    queue.append(neighbor)
        max_rooms = max(max_rooms, len(rooms))
    
    return max_rooms

def f2(N, M, doors):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N)]
    for u, v in doors:
        graph[u].append(v)
        graph[v].append(u)
    
    # Find all rooms that can only be reached from the outside of the building
    outside_rooms = set()
    for i in range(N):
        if i not in graph[i]:
            outside_rooms.add(i)
    
    # Find the door that leads to the maximum number of rooms that can be secured
    max_rooms = 0
    max_door = None
    for i in range(N):
        if i in outside_rooms:
            continue
        rooms = set()
        queue = [i]
        while queue:
            node = queue.pop(0)
            rooms.add(node)
            for neighbor in graph[node]:
                if neighbor not in rooms:
                    queue.append(neighbor)
        if len(rooms) > max_rooms:
            max_rooms = len(rooms)
            max_door = i
    
    return max_door

if __name__ == '__main__':
    N, M = map(int, input().split())
    doors = []
    for _ in range(M):
        u, v = map(int, input().split())
        doors.append((u, v))
    print(f1(N, M, doors))
    print(f2(N, M, doors))


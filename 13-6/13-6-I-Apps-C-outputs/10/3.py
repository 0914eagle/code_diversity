
def get_input():
    N, M = map(int, input().split())
    doors = []
    for _ in range(M):
        u, v = map(int, input().split())
        doors.append((u, v))
    return N, M, doors

def find_secure_door(N, M, doors):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N)]
    for u, v in doors:
        graph[u].append(v)
        graph[v].append(u)
    
    # Find the door that connects the most rooms to the outside of the building
    max_rooms = 0
    secure_door = None
    for u in range(N):
        if u == -1:
            continue
        rooms = set()
        queue = [u]
        while queue:
            node = queue.pop(0)
            if node == -1:
                continue
            rooms.add(node)
            queue.extend(graph[node])
        if len(rooms) > max_rooms:
            max_rooms = len(rooms)
            secure_door = u
    
    return secure_door

def main():
    N, M, doors = get_input()
    secure_door = find_secure_door(N, M, doors)
    print(secure_door)

if __name__ == '__main__':
    main()


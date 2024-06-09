
def get_max_protected_rooms(num_rooms, doors):
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

    # Initialize a set to store the protected rooms
    protected_rooms = set()

    # DFS to find the maximum number of protected rooms
    def dfs(curr_room):
        nonlocal protected_rooms
        protected_rooms.add(curr_room)
        for neighbor in graph[curr_room]:
            if neighbor != outside_room and neighbor not in protected_rooms:
                dfs(neighbor)

    dfs(outside_room)

    return len(protected_rooms)

def main():
    num_rooms, num_doors = map(int, input().split())
    doors = []
    for _ in range(num_doors):
        u, v = map(int, input().split())
        doors.append((u, v))
    print(get_max_protected_rooms(num_rooms, doors))

if __name__ == '__main__':
    main()



def get_maximum_protected_rooms(number_of_rooms, number_of_doors, door_connections):
    # Initialize a graph with the given number of rooms
    graph = [[] for _ in range(number_of_rooms)]

    # Add edges to the graph based on the door connections
    for u, v in door_connections:
        graph[u].append(v)
        graph[v].append(u)

    # Find the room that is not connected to any other room
    isolated_room = -1
    for i in range(number_of_rooms):
        if not graph[i]:
            isolated_room = i
            break

    # If there is no isolated room, return 0
    if isolated_room == -1:
        return 0

    # Initialize a set to store the protected rooms
    protected_rooms = set()

    # DFS to find the maximum number of protected rooms
    def dfs(node):
        if node == isolated_room:
            return
        protected_rooms.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(isolated_room)

    return len(protected_rooms)

def main():
    number_of_rooms, number_of_doors = map(int, input().split())
    door_connections = []
    for _ in range(number_of_doors):
        u, v = map(int, input().split())
        door_connections.append((u, v))
    print(get_maximum_protected_rooms(number_of_rooms, number_of_doors, door_connections))

if __name__ == '__main__':
    main()


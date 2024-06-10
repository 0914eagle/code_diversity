
def get_rooms(n):
    return [[] for _ in range(n+1)]

def add_corridor(rooms, u, v):
    rooms[u].append(v)
    rooms[v].append(u)

def remove_corridor(rooms, u, v):
    rooms[u].remove(v)
    rooms[v].remove(u)

def get_connected_components(rooms):
    visited = [False] * (len(rooms)+1)
    components = []
    for i in range(1, len(rooms)):
        if not visited[i]:
            component = []
            dfs(rooms, i, visited, component)
            components.append(component)
    return components

def dfs(rooms, i, visited, component):
    visited[i] = True
    component.append(i)
    for j in rooms[i]:
        if not visited[j]:
            dfs(rooms, j, visited, component)

def solve(n, m, corridors):
    rooms = get_rooms(n)
    for u, v in corridors:
        add_corridor(rooms, u, v)
    
    components = get_connected_components(rooms)
    if len(components) == 1:
        return 0, []
    
    removed_corridors = []
    for component in components:
        if len(component) > 1:
            for i in component:
                for j in component:
                    if i != j:
                        remove_corridor(rooms, i, j)
                        removed_corridors.append((i, j))
    
    return len(removed_corridors), removed_corridors

def main():
    n, m = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v = map(int, input().split())
        corridors.append((u, v))
    r, removed_corridors = solve(n, m, corridors)
    print(r)
    for u, v in removed_corridors:
        print(u, v)

if __name__ == '__main__':
    main()


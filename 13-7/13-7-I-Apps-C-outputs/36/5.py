
def get_rooms(n):
    return [[] for _ in range(n+1)]

def add_corridor(rooms, u, v):
    rooms[u].append(v)
    rooms[v].append(u)

def remove_corridor(rooms, u, v):
    rooms[u].remove(v)
    rooms[v].remove(u)

def has_cycle(rooms):
    visited = [False] * (len(rooms)+1)
    def dfs(u):
        if visited[u]:
            return True
        visited[u] = True
        for v in rooms[u]:
            if dfs(v):
                return True
        visited[u] = False
        return False
    return dfs(1)

def remove_cycles(rooms):
    removed = 0
    while has_cycle(rooms):
        for u in range(1, len(rooms)):
            for v in rooms[u]:
                if u < v:
                    remove_corridor(rooms, u, v)
                    removed += 1
                    break
    return removed

def main():
    n, m = map(int, input().split())
    rooms = get_rooms(n)
    for _ in range(m):
        u, v = map(int, input().split())
        add_corridor(rooms, u, v)
    print(remove_cycles(rooms))

if __name__ == '__main__':
    main()


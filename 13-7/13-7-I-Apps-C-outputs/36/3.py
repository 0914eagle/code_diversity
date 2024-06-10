
def get_rooms(n):
    return [set() for _ in range(n + 1)]

def add_corridor(rooms, u, v):
    rooms[u].add(v)
    rooms[v].add(u)

def remove_corridor(rooms, u, v):
    rooms[u].remove(v)
    rooms[v].remove(u)

def is_connected(rooms, u, v):
    return v in rooms[u]

def get_cycles(rooms):
    cycles = []
    for i in range(1, len(rooms)):
        for j in range(i + 1, len(rooms)):
            if is_connected(rooms, i, j):
                cycles.append((i, j))
    return cycles

def get_removable_corridors(rooms, m):
    removable_corridors = []
    for i in range(1, len(rooms)):
        for j in range(i + 1, len(rooms)):
            if is_connected(rooms, i, j) and (i, j) not in removable_corridors:
                removable_corridors.append((i, j))
    return removable_corridors[:m // 2]

def get_output(rooms, m):
    removable_corridors = get_removable_corridors(rooms, m)
    return str(len(removable_corridors)) + '\n' + '\n'.join(str(i) for i, _ in removable_corridors)

def main():
    n, m = map(int, input().split())
    rooms = get_rooms(n)
    for _ in range(m):
        u, v = map(int, input().split())
        add_corridor(rooms, u, v)
    print(get_output(rooms, m))

if __name__ == '__main__':
    main()


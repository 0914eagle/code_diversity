
def get_input():
    n, m = map(int, input().split())
    floorplan = [input() for _ in range(n)]
    return n, m, floorplan

def get_gargoyles(n, m, floorplan):
    gargoyles = []
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] in "VH":
                gargoyles.append((i, j))
    return gargoyles

def get_mirrors(n, m, floorplan):
    mirrors = []
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] in "\\/":
                mirrors.append((i, j))
    return mirrors

def get_obstacles(n, m, floorplan):
    obstacles = []
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] == "#":
                obstacles.append((i, j))
    return obstacles

def is_valid_path(start, end, gargoyles, mirrors, obstacles):
    queue = [(start, [start])]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return True
        for neighbor in [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]:
            if 0 <= neighbor[0] < len(floorplan) and 0 <= neighbor[1] < len(floorplan[0]) and neighbor not in visited and neighbor not in obstacles:
                queue.append((neighbor, path + [neighbor]))
        visited.add(current)
    return False

def get_min_rotations(n, m, floorplan):
    gargoyles = get_gargoyles(n, m, floorplan)
    mirrors = get_mirrors(n, m, floorplan)
    obstacles = get_obstacles(n, m, floorplan)
    min_rotations = float("inf")
    for i in range(len(gargoyles)):
        for j in range(i + 1, len(gargoyles)):
            if is_valid_path(gargoyles[i], gargoyles[j], gargoyles, mirrors, obstacles):
                min_rotations = min(min_rotations, 2)
            for mirror in mirrors:
                if is_valid_path(gargoyles[i], mirror, gargoyles, mirrors, obstacles) and is_valid_path(gargoyles[j], mirror, gargoyles, mirrors, obstacles):
                    min_rotations = min(min_rotations, 1)
    return -1 if min_rotations == float("inf") else min_rotations

if __name__ == '__main__':
    n, m, floorplan = get_input()
    print(get_min_rotations(n, m, floorplan))



def get_gargoyle_positions(n, m, floorplan):
    gargoyle_positions = []
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] == 'V' or floorplan[i][j] == 'H':
                gargoyle_positions.append((i, j))
    return gargoyle_positions

def is_valid_position(n, m, position, gargoyle_positions):
    i, j = position
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    if floorplan[i][j] == '#' or floorplan[i][j] == '/' or floorplan[i][j] == '\\':
        return False
    for gargoyle_position in gargoyle_positions:
        if gargoyle_position == position:
            return False
    return True

def get_neighboring_positions(n, m, position):
    i, j = position
    neighboring_positions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [position for position in neighboring_positions if is_valid_position(n, m, position, gargoyle_positions)]

def bfs(n, m, start_position, goal_position, gargoyle_positions):
    queue = [start_position]
    visited = set()
    step = 0
    while queue:
        position = queue.pop(0)
        if position == goal_position:
            return step
        visited.add(position)
        for neighbor in get_neighboring_positions(n, m, position):
            if neighbor not in visited:
                queue.append(neighbor)
        step += 1
    return -1

def f1(n, m, floorplan):
    gargoyle_positions = get_gargoyle_positions(n, m, floorplan)
    start_position = gargoyle_positions[0]
    goal_position = gargoyle_positions[-1]
    return bfs(n, m, start_position, goal_position, gargoyle_positions)

def f2(...):
    ...

if __name__ == '__main__':
    n, m = map(int, input().split())
    floorplan = [input() for _ in range(n)]
    print(f1(n, m, floorplan))


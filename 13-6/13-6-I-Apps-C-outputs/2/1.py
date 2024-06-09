
def get_gargoyle_positions(floorplan):
    gargoyle_positions = []
    for i, row in enumerate(floorplan):
        for j, char in enumerate(row):
            if char in ["V", "H"]:
                gargoyle_positions.append((i, j))
    return gargoyle_positions

def is_valid_position(position, floorplan):
    i, j = position
    return 0 <= i < len(floorplan) and 0 <= j < len(floorplan[0]) and floorplan[i][j] != "#"

def get_neighbor_positions(position, floorplan):
    i, j = position
    neighbors = []
    if i > 0 and floorplan[i-1][j] != "#":
        neighbors.append((i-1, j))
    if i < len(floorplan)-1 and floorplan[i+1][j] != "#":
        neighbors.append((i+1, j))
    if j > 0 and floorplan[i][j-1] != "#":
        neighbors.append((i, j-1))
    if j < len(floorplan[0])-1 and floorplan[i][j+1] != "#":
        neighbors.append((i, j+1))
    return neighbors

def bfs(start_position, floorplan):
    queue = [start_position]
    visited = set()
    while queue:
        position = queue.pop(0)
        if position not in visited:
            visited.add(position)
            if floorplan[position[0]][position[1]] == ".":
                return True
            for neighbor in get_neighbor_positions(position, floorplan):
                if is_valid_position(neighbor, floorplan):
                    queue.append(neighbor)
    return False

def solve_puzzle(floorplan):
    gargoyle_positions = get_gargoyle_positions(floorplan)
    min_rotations = len(gargoyle_positions)
    for rotation in range(4):
        for position in gargoyle_positions:
            new_position = (position[0] + rotation, position[1] + rotation)
            if is_valid_position(new_position, floorplan) and bfs(new_position, floorplan):
                min_rotations = min(min_rotations, len(gargoyle_positions) - 1)
                break
    return -1 if min_rotations == len(gargoyle_positions) else min_rotations

def main():
    n, m = map(int, input().split())
    floorplan = [input() for _ in range(n)]
    print(solve_puzzle(floorplan))

if __name__ == '__main__':
    main()


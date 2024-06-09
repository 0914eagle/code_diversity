
def is_walkable(row, col, school_map):
    if 0 <= row < len(school_map) and 0 <= col < len(school_map[0]):
        return school_map[row][col] == '.'
    return False

def can_reach_jelly(row, col, school_map, master_paths):
    for master_path in master_paths:
        for master_row, master_col in master_path:
            if row == master_row or col == master_col:
                if row < master_row:
                    for r in range(row, master_row):
                        if not is_walkable(r, col, school_map):
                            return False
                elif row > master_row:
                    for r in range(master_row + 1, row + 1):
                        if not is_walkable(r, col, school_map):
                            return False
                elif col < master_col:
                    for c in range(col, master_col):
                        if not is_walkable(row, c, school_map):
                            return False
                elif col > master_col:
                    for c in range(master_col + 1, col + 1):
                        if not is_walkable(row, c, school_map):
                            return False
    return True

def find_minimum_turns(school_map, start_bed, fridge, master_paths):
    rows, cols = len(school_map), len(school_map[0])
    start_row, start_col = start_bed
    fridge_row, fridge_col = fridge
    
    visited = set()
    queue = [(start_row, start_col, 0)]
    
    while queue:
        row, col, turns = queue.pop(0)
        if (row, col) in visited:
            continue
        
        visited.add((row, col))
        
        if row == fridge_row and col == fridge_col:
            return turns
        
        if can_reach_jelly(row, col, school_map, master_paths):
            return turns
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if is_walkable(new_row, new_col, school_map):
                queue.append((new_row, new_col, turns + 1))
    
    return "IMPOSSIBLE"

# Read input
r, c = map(int, input().split())
start_bed = tuple(map(int, input().strip()[1:-1].split()))
fridge = tuple(map(int, input().strip()[1:-1].split()))
school_map = [input().strip() for _ in range(r)]
p = int(input())
master_paths = [list(map(int, input().strip()[1:-1].split())) for _ in range(p)]

# Find minimum turns
result = find_minimum_turns(school_map, start_bed, fridge, master_paths)
print(result)

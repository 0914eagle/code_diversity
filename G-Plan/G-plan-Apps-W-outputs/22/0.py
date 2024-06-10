djacent(tile1, tile2):
    # Check if two tiles are adjacent
    return abs(ord(tile1[0]) - ord(tile2[0])) <= 1 and abs(ord(tile1[1]) - ord(tile2[1])) <= 1

def find_path(grid, s, path, visited):
    if len(path) == len(s):
        return True
    
    current_tile = path[-1]
    for tile in grid:
        if tile not in visited and is_adjacent(current_tile, tile):
            path.append(tile)
            visited.add(tile)
            if find_path(grid, s, path, visited):
                return True
            path.pop()
            visited.remove(tile)
    
    return False

def generate_grid(s):
    grid = []
    for i in range(2):
        for j in range(13):
            grid.append(chr(ord('A') + i*13 + j))
    
    path = [grid[0]]
    visited = set()
    visited.add(grid[0])
    
    if find_path(grid, s, path, visited):
        return ["".join(path[:13]), "".join(path[13:])]
    else:
        return "Impossible"

if __name__ == "__main__":
    s = input().strip()
    result = generate_grid(s)
    if result == "Impossible":
        print("Impossible")
    else:
        for row in result:
            print(row)

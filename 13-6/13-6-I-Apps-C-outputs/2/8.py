
def read_input():
    n, m = map(int, input().split())
    floorplan = [input() for _ in range(n)]
    return n, m, floorplan

def is_valid_move(gargoyle, direction):
    x, y = gargoyle
    if direction == "L":
        return x > 0 and floorplan[y][x-1] != "#"
    elif direction == "R":
        return x < m-1 and floorplan[y][x+1] != "#"
    elif direction == "U":
        return y > 0 and floorplan[y-1][x] != "#"
    else:
        return y < n-1 and floorplan[y+1][x] != "#"

def move_gargoyle(gargoyle, direction):
    x, y = gargoyle
    if direction == "L":
        return x-1, y
    elif direction == "R":
        return x+1, y
    elif direction == "U":
        return x, y-1
    else:
        return x, y+1

def rotate_gargoyle(gargoyle, direction):
    x, y = gargoyle
    if direction == "L":
        return x, y+1
    elif direction == "R":
        return x, y-1
    elif direction == "U":
        return x+1, y
    else:
        return x-1, y

def find_path(gargoyle1, gargoyle2):
    queue = [(gargoyle1, [])]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == gargoyle2:
            return path
        for direction in ["L", "R", "U", "D"]:
            if is_valid_move(current, direction):
                next_gargoyle = move_gargoyle(current, direction)
                if next_gargoyle not in visited:
                    visited.add(next_gargoyle)
                    queue.append((next_gargoyle, path + [direction]))
    return []

def solve_puzzle(n, m, floorplan):
    gargoyles = []
    for y in range(n):
        for x in range(m):
            if floorplan[y][x] in ["V", "H"]:
                gargoyles.append((x, y))
    for g1 in gargoyles:
        for g2 in gargoyles:
            if g1 != g2:
                path = find_path(g1, g2)
                if path:
                    return len(path)
    return -1

if __name__ == '__main__':
    n, m, floorplan = read_input()
    print(solve_puzzle(n, m, floorplan))


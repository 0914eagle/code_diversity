
def read_input():
    n, m = map(int, input().split())
    floorplan = [input() for _ in range(n)]
    return n, m, floorplan

def is_valid_position(n, m, position):
    i, j = position
    return 0 <= i < n and 0 <= j < m

def is_obstacle(floorplan, position):
    i, j = position
    return floorplan[i][j] == '#'

def is_gargoyle(floorplan, position):
    i, j = position
    return floorplan[i][j] in ['V', 'H']

def is_mirror(floorplan, position):
    i, j = position
    return floorplan[i][j] in ['/', '\\']

def is_top_left_corner(n, m, position):
    i, j = position
    return i == 0 and j == 0

def is_bottom_right_corner(n, m, position):
    i, j = position
    return i == n-1 and j == m-1

def is_path_to_door(n, m, floorplan, position):
    queue = [position]
    visited = set()
    while queue:
        i, j = queue.pop(0)
        if is_obstacle(floorplan, (i, j)):
            continue
        if is_gargoyle(floorplan, (i, j)):
            continue
        if is_mirror(floorplan, (i, j)):
            continue
        if is_bottom_right_corner(n, m, (i, j)):
            return True
        for neighbor in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if is_valid_position(n, m, neighbor) and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return False

def rotate_gargoyle(n, m, floorplan, position):
    i, j = position
    if floorplan[i][j] == 'V':
        floorplan[i][j] = 'H'
    else:
        floorplan[i][j] = 'V'

def find_min_gargoyles_to_unlock_door(n, m, floorplan):
    queue = [(0, 0)]
    visited = set()
    count = 0
    while queue:
        position = queue.pop(0)
        if is_path_to_door(n, m, floorplan, position):
            return count
        if is_gargoyle(floorplan, position):
            rotate_gargoyle(n, m, floorplan, position)
            count += 1
        for neighbor in [(position[0]-1, position[1]), (position[0]+1, position[1]), (position[0], position[1]-1), (position[0], position[1]+1)]:
            if is_valid_position(n, m, neighbor) and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return -1

if __name__ == '__main__':
    n, m, floorplan = read_input()
    print(find_min_gargoyles_to_unlock_door(n, m, floorplan))


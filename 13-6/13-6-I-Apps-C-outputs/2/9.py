
def read_input():
    n, m = map(int, input().split())
    floorplan = [input() for _ in range(n)]
    return n, m, floorplan

def is_valid_position(n, m, x, y):
    return 0 <= x < n and 0 <= y < m

def is_gargoyle(c):
    return c == 'V' or c == 'H'

def is_mirror(c):
    return c == '/' or c == '\\'

def is_obstacle(c):
    return c == '#'

def is_empty(c):
    return c == '.'

def is_face_visible(n, m, x, y, dx, dy):
    if not is_valid_position(n, m, x, y):
        return False
    if is_obstacle(floorplan[x][y]):
        return False
    if is_gargoyle(floorplan[x][y]):
        return True
    if is_mirror(floorplan[x][y]):
        return is_face_visible(n, m, x+dx, y+dy, dx, dy)
    if is_empty(floorplan[x][y]):
        return is_face_visible(n, m, x+dx, y+dy, dx, dy)
    return False

def find_path(n, m, x, y, dx, dy):
    if not is_valid_position(n, m, x, y):
        return False
    if is_obstacle(floorplan[x][y]):
        return False
    if is_gargoyle(floorplan[x][y]):
        return is_face_visible(n, m, x+dx, y+dy, dx, dy)
    if is_mirror(floorplan[x][y]):
        return find_path(n, m, x+dx, y+dy, dx, dy)
    if is_empty(floorplan[x][y]):
        return find_path(n, m, x+dx, y+dy, dx, dy)
    return False

def find_solution(n, m, floorplan):
    for i in range(n):
        for j in range(m):
            if is_gargoyle(floorplan[i][j]):
                for dx in [-1, 1]:
                    for dy in [-1, 1]:
                        if find_path(n, m, i, j, dx, dy):
                            return True
    return False

def main():
    n, m, floorplan = read_input()
    print(find_solution(n, m, floorplan))

if __name__ == '__main__':
    main()


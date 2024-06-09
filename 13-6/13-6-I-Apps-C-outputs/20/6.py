
def is_connected(squares):
    # Check if all the # are connected
    visited = set()
    queue = [0]
    while queue:
        i, j = queue.pop(0)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if squares[i][j] == '#':
            queue.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
    return len(visited) == 6

def is_cube(squares):
    # Check if the connected components can be folded into a cube
    for i in range(6):
        for j in range(6):
            if squares[i][j] == '#':
                # Check if the current square is on the edge of the cube
                if i == 0 or i == 5 or j == 0 or j == 5:
                    return False
                # Check if the current square is connected to the top, bottom, left, and right squares
                if squares[i-1][j] != '#' or squares[i+1][j] != '#' or squares[i][j-1] != '#' or squares[i][j+1] != '#':
                    return False
    return True

def can_fold(squares):
    # Check if the squares can be folded into a cube
    if not is_connected(squares):
        return "cannot fold"
    if is_cube(squares):
        return "can fold"
    return "cannot fold"

if __name__ == '__main__':
    squares = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['#', '#', '#', '#', '#', '#'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]
    print(can_fold(squares))


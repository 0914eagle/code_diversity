
def can_fold(squares):
    # Check if the input is valid
    if len(squares) != 6 or any(len(row) != 6 for row in squares):
        return "invalid input"

    # Count the number of unit squares
    num_unit_squares = sum(row.count("#") for row in squares)
    if num_unit_squares != 6:
        return "cannot fold"

    # Check if the squares form a connected component
    def is_connected(row1, col1, row2, col2):
        return abs(row1 - row2) + abs(col1 - col2) == 1

    visited = set()
    to_visit = [(0, 0)]
    while to_visit:
        row, col = to_visit.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if squares[row][col] == "#":
            to_visit.extend((row+1, col), (row-1, col), (row, col+1), (row, col-1))

    if len(visited) != 6:
        return "cannot fold"

    # Check if the squares can be folded into a cube
    def is_cube(row, col):
        if row < 0 or col < 0 or row >= 6 or col >= 6:
            return False
        if squares[row][col] == ".":
            return False
        return True

    for i in range(6):
        for j in range(6):
            if squares[i][j] == "#" and not (is_cube(i-1, j) and is_cube(i+1, j) and is_cube(i, j-1) and is_cube(i, j+1)):
                return "cannot fold"

    return "can fold"

def get_input():
    return [input() for _ in range(6)]

if __name__ == '__main__':
    squares = get_input()
    print(can_fold(squares))


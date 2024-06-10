
def get_vertical_marks(n, row_specs, col_specs):
    # Initialize the vertical marks as a 2D array of 0s
    vertical_marks = [[0] * (n + 1) for _ in range(n)]

    # Iterate through the rows and columns
    for i in range(n):
        for j in range(n):
            # If the current cell is not marked as a border, skip it
            if not vertical_marks[i][j]:
                continue

            # If the current cell is marked as a border, check if it is part of a group
            if vertical_marks[i][j] == 1:
                # If the current cell is part of a group, mark all cells in the group as 1
                mark_group(vertical_marks, i, j, n)

    return vertical_marks

def get_horizontal_marks(n, row_specs, col_specs):
    # Initialize the horizontal marks as a 2D array of 0s
    horizontal_marks = [[0] * (n) for _ in range(n)]

    # Iterate through the rows and columns
    for i in range(n):
        for j in range(n):
            # If the current cell is not marked as a border, skip it
            if not horizontal_marks[i][j]:
                continue

            # If the current cell is marked as a border, check if it is part of a group
            if horizontal_marks[i][j] == 1:
                # If the current cell is part of a group, mark all cells in the group as 1
                mark_group(horizontal_marks, i, j, n)

    return horizontal_marks

def mark_group(marks, i, j, n):
    # If the current cell is already marked, return
    if marks[i][j] == 1:
        return

    # Mark the current cell as 1
    marks[i][j] = 1

    # If the current cell is not in the last row or column, recurse on the cell below and to the right
    if i < n - 1 and j < n - 1:
        mark_group(marks, i + 1, j + 1, n)

    # If the current cell is not in the first row or column, recurse on the cell above and to the left
    if i > 0 and j > 0:
        mark_group(marks, i - 1, j - 1, n)

if __name__ == '__main__':
    n = int(input())
    row_specs = [list(map(int, input().split())) for _ in range(n)]
    col_specs = [list(map(int, input().split())) for _ in range(n)]

    vertical_marks = get_vertical_marks(n, row_specs, col_specs)
    horizontal_marks = get_horizontal_marks(n, row_specs, col_specs)

    for i in range(n):
        print(''.join(map(str, vertical_marks[i])))

    for i in range(n):
        print(''.join(map(str, horizontal_marks[i])))


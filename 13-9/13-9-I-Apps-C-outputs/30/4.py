
def is_valid_move(grid, row, col, organs, empty_row, empty_col):
    # Check if the move is valid
    if row == empty_row and col == empty_col:
        return True
    if row == empty_row and col == empty_col - 1:
        return True
    if row == empty_row and col == empty_col + 1:
        return True
    if row == empty_row - 1 and col == empty_col:
        return True
    if row == empty_row + 1 and col == empty_col:
        return True
    if row == empty_row - 1 and col == empty_col - 1:
        return True
    if row == empty_row - 1 and col == empty_col + 1:
        return True
    if row == empty_row + 1 and col == empty_col - 1:
        return True
    if row == empty_row + 1 and col == empty_col + 1:
        return True
    return False

def get_empty_cell(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "E":
                return (row, col)
    return None

def get_organs(grid):
    organs = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != "E":
                organs.append(grid[row][col])
    return organs

def get_shortcuts(grid):
    shortcuts = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col].isupper():
                shortcuts[grid[row][col]] = grid[row + 1][col]
    return shortcuts

def expand_shortcuts(sequence, shortcuts):
    expanded_sequence = []
    for move in sequence:
        if move in shortcuts:
            expanded_sequence += shortcuts[move]
        else:
            expanded_sequence.append(move)
    return expanded_sequence

def get_sequence(grid):
    organs = get_organs(grid)
    empty_cell = get_empty_cell(grid)
    empty_row, empty_col = empty_cell
    sequence = []
    for organ in organs:
        row, col = organ
        if is_valid_move(grid, row, col, organs, empty_row, empty_col):
            sequence.append(organ)
    return sequence

def get_shortcut_sequence(grid):
    shortcuts = get_shortcuts(grid)
    sequence = get_sequence(grid)
    return expand_shortcuts(sequence, shortcuts)

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        grid = []
        for _ in range(2 * k + 1):
            grid.append(list(input()))
        if is_valid_move(grid, 0, 0, get_organs(grid), get_empty_cell(grid)[0], get_empty_cell(grid)[1]):
            print("SURGERY COMPLETE")
            print("\n".join(get_shortcut_sequence(grid)))
            print("DONE")
        else:
            print("SURGERY FAILED")

if __name__ == "__main__":
    main()


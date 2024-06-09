
def get_min_moves(n, m, game_field):
    # Initialize variables
    moves = 0
    dwarves = []
    candy_cells = []

    # Parse the game field
    for i in range(n):
        for j in range(m):
            if game_field[i][j] == "G":
                dwarves.append((i, j))
            elif game_field[i][j] == "S":
                candy_cells.append((i, j))

    # Check if the game is solvable
    if len(dwarves) != len(candy_cells):
        return -1

    # Initialize the dwarves' positions
    for dwarf in dwarves:
        dwarf_row, dwarf_col = dwarf
        game_field[dwarf_row][dwarf_col] = "*"

    # Game loop
    while dwarves:
        # Find the dwarves that can move
        moveable_dwarves = []
        for dwarf in dwarves:
            dwarf_row, dwarf_col = dwarf
            if game_field[dwarf_row][dwarf_col + 1] == "*":
                moveable_dwarves.append(dwarf)

        # Move the dwarves
        for dwarf in moveable_dwarves:
            dwarf_row, dwarf_col = dwarf
            game_field[dwarf_row][dwarf_col] = "*"
            game_field[dwarf_row][dwarf_col + 1] = "G"
            dwarf = (dwarf_row, dwarf_col + 1)
            dwarves[dwarves.index(dwarf)] = dwarf

        # Check if the game is over
        for dwarf in dwarves:
            dwarf_row, dwarf_col = dwarf
            if game_field[dwarf_row][dwarf_col] == "S":
                return moves

        # Increment the move count
        moves += 1

    # The game is unsolvable
    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    game_field = []
    for _ in range(n):
        game_field.append(list(input()))
    print(get_min_moves(n, m, game_field))


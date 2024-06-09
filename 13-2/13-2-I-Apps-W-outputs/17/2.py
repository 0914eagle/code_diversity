
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
        dwarf_pos = (dwarf[0], dwarf[1])
        dwarf_next_pos = (dwarf[0], dwarf[1] + 1)
        if dwarf_next_pos[1] == m:
            dwarf_next_pos = (dwarf[0], 0)
        dwarf_positions[dwarf_pos] = dwarf_next_pos

    # Game loop
    while True:
        # Check if all dwarves have reached the candy cells
        if all(dwarf_positions[dwarf] in candy_cells for dwarf in dwarves):
            break

        # Move the dwarves
        for dwarf in dwarves:
            dwarf_pos = dwarf_positions[dwarf]
            dwarf_next_pos = (dwarf_pos[0], dwarf_pos[1] + 1)
            if dwarf_next_pos[1] == m:
                dwarf_next_pos = (dwarf_pos[0], 0)
            dwarf_positions[dwarf] = dwarf_next_pos

        # Update the moves counter
        moves += 1

    return moves

if __name__ == '__main__':
    n, m = map(int, input().split())
    game_field = []
    for _ in range(n):
        game_field.append(input())
    print(get_min_moves(n, m, game_field))


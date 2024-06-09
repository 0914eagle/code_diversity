
def get_min_moves(n, m, game_field):
    # Initialize variables
    moves = 0
    dwarf_positions = []
    candy_positions = []
    
    # Parse the game field
    for i in range(n):
        for j in range(m):
            if game_field[i][j] == "G":
                dwarf_positions.append((i, j))
            elif game_field[i][j] == "S":
                candy_positions.append((i, j))
    
    # Check if the game is solvable
    if len(dwarf_positions) != len(candy_positions):
        return -1
    
    # Solve the game
    while dwarf_positions != candy_positions:
        # Find the closest dwarf to the candy
        min_distance = float("inf")
        for dwarf in dwarf_positions:
            for candy in candy_positions:
                distance = abs(dwarf[0] - candy[0]) + abs(dwarf[1] - candy[1])
                if distance < min_distance:
                    min_distance = distance
                    closest_dwarf = dwarf
                    closest_candy = candy
        
        # Move the closest dwarf to the candy
        dwarf_positions.remove(closest_dwarf)
        candy_positions.remove(closest_candy)
        dwarf_positions.append(closest_candy)
        candy_positions.append(closest_dwarf)
        moves += 1
    
    return moves


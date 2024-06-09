
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
    
    # Initialize the dwarf positions
    for dwarf in dwarf_positions:
        i, j = dwarf
        if j != 0:
            game_field[i][j-1] = "G"
            game_field[i][j] = "*"
    
    # Game loop
    while True:
        # Check if the game is over
        if all(game_field[i][j] == "G" for i, j in candy_positions):
            break
        
        # Move the dwarves
        for dwarf in dwarf_positions:
            i, j = dwarf
            if game_field[i][j] == "G":
                game_field[i][j] = "*"
                if j < m-1:
                    game_field[i][j+1] = "G"
        
        # Update the dwarf positions
        dwarf_positions = []
        for i in range(n):
            for j in range(m):
                if game_field[i][j] == "G":
                    dwarf_positions.append((i, j))
        
        # Update the moves
        moves += 1
    
    # Return the minimum number of moves
    return moves

if __name__ == '__main__':
    n, m = map(int, input().split())
    game_field = [input() for _ in range(n)]
    print(get_min_moves(n, m, game_field))


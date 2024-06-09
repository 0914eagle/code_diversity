
def get_min_moves(n, m, game_field):
    # Initialize variables
    moves = 0
    dwarf_positions = []
    candy_positions = []
    
    # Parse the game field
    for i in range(n):
        for j in range(m):
            if game_field[i][j] == 'G':
                dwarf_positions.append((i, j))
            elif game_field[i][j] == 'S':
                candy_positions.append((i, j))
    
    # Check if the goal can be achieved
    if len(dwarf_positions) == 0 or len(candy_positions) == 0:
        return -1
    
    # Initialize the dwarf positions
    for dwarf in dwarf_positions:
        dwarf_positions[dwarf] = (dwarf[0], dwarf[1] + 1)
    
    # Game loop
    while True:
        # Check if the goal has been reached
        for dwarf in dwarf_positions:
            if dwarf[1] == candy_positions[0][1]:
                return moves
        
        # Move the dwarves
        for dwarf in dwarf_positions:
            dwarf_positions[dwarf] = (dwarf[0], dwarf[1] + 1)
        
        # Increment the move count
        moves += 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    game_field = []
    for i in range(n):
        game_field.append(input())
    print(get_min_moves(n, m, game_field))



def is_valid_move(grid, row, col, direction):
    # Check if the move is valid
    if direction == "u":
        if row == 0:
            return False
        if grid[row - 1][col] != "E":
            return False
    elif direction == "d":
        if row == len(grid) - 1:
            return False
        if grid[row + 1][col] != "E":
            return False
    elif direction == "l":
        if col == 0:
            return False
        if grid[row][col - 1] != "E":
            return False
    elif direction == "r":
        if col == len(grid[0]) - 1:
            return False
        if grid[row][col + 1] != "E":
            return False
    else:
        return False
    
    return True

def make_move(grid, row, col, direction):
    # Make the move
    if direction == "u":
        grid[row - 1][col] = grid[row][col]
        grid[row][col] = "E"
    elif direction == "d":
        grid[row + 1][col] = grid[row][col]
        grid[row][col] = "E"
    elif direction == "l":
        grid[row][col - 1] = grid[row][col]
        grid[row][col] = "E"
    elif direction == "r":
        grid[row][col + 1] = grid[row][col]
        grid[row][col] = "E"
    else:
        return False
    
    return True

def find_shortest_sequence(grid):
    # Initialize the sequence of moves
    sequence = []
    
    # Loop through each row and column
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If the current cell is not empty, skip it
            if grid[row][col] != "E":
                continue
            
            # If the current cell is empty, try to make a move
            for direction in ["u", "d", "l", "r"]:
                if is_valid_move(grid, row, col, direction):
                    make_move(grid, row, col, direction)
                    sequence.append(direction)
                    break
    
    return sequence

def solve(grid):
    # Find the shortest sequence of moves
    sequence = find_shortest_sequence(grid)
    
    # If the sequence is empty, return "SURGERY FAILED"
    if not sequence:
        return "SURGERY FAILED"
    
    # Otherwise, return the sequence of moves
    return "SURGERY COMPLETE\n" + "".join(sequence)

if __name__ == '__main__':
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        print(f"Case #{case}:")
        k = int(input())
        grid = []
        for row in range(2 * k + 1):
            grid.append(list(input()))
        print(solve(grid))


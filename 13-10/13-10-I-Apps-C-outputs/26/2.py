
def find_tour(grid):
    # Initialize a list to store the visited squares
    visited = []
    # Initialize a list to store the sequence of visited squares
    sequence = []
    # Initialize the current position as (0, 0)
    current_position = (0, 0)
    # Add the current position to the visited list
    visited.append(current_position)
    # Add the current position to the sequence
    sequence.append(current_position)
    # Loop until the entire grid is visited
    while len(visited) < len(grid) * len(grid[0]):
        # Get the available moves from the current position
        available_moves = get_available_moves(grid, current_position)
        # If there are no available moves, return -1
        if not available_moves:
            return -1
        # Choose a random move from the available moves
        move = available_moves[0]
        # Update the current position
        current_position = move
        # Add the current position to the visited list
        visited.append(current_position)
        # Add the current position to the sequence
        sequence.append(current_position)
    # Return the sequence of visited squares
    return sequence

def get_available_moves(grid, position):
    # Get the row and column of the current position
    row, col = position
    # Initialize a list to store the available moves
    available_moves = []
    # Check if the move up is available
    if row - 1 >= 0 and grid[row - 1][col] == 0:
        available_moves.append((row - 1, col))
    # Check if the move down is available
    if row + 1 < len(grid) and grid[row + 1][col] == 0:
        available_moves.append((row + 1, col))
    # Check if the move left is available
    if col - 1 >= 0 and grid[row][col - 1] == 0:
        available_moves.append((row, col - 1))
    # Check if the move right is available
    if col + 1 < len(grid[0]) and grid[row][col + 1] == 0:
        available_moves.append((row, col + 1))
    # Return the list of available moves
    return available_moves

def manhattan_distance(p1, p2):
    # Get the row and column of the two positions
    r1, c1 = p1
    r2, c2 = p2
    # Calculate the Manhattan distance
    return abs(r1 - r2) + abs(c1 - c2)

def print_tour(sequence):
    # Loop through the sequence of visited squares
    for i in range(len(sequence)):
        # Get the current position
        current_position = sequence[i]
        # Get the next position
        next_position = sequence[(i + 1) % len(sequence)]
        # Calculate the Manhattan distance between the current and next position
        distance = manhattan_distance(current_position, next_position)
        # Print the current position and the next position
        print(current_position[0], current_position[1], next_position[0], next_position[1])
        # Check if the distance is 2 or 3
        if distance == 2 or distance == 3:
            print()
        else:
            return "Not a valid tour"

if __name__ == '__main__':
    # Read the input grid
    grid = []
    for i in range(int(input())):
        grid.append(list(map(int, input().split())))
    # Find the tour
    sequence = find_tour(grid)
    # Print the tour
    print_tour(sequence)


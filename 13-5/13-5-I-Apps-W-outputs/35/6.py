
def f1(n, m, S_x, S_y):
    # Initialize a list to store the visited cells
    visited = []
    # Initialize the current cell as the starting cell
    current_cell = (S_x, S_y)
    # Add the starting cell to the visited list
    visited.append(current_cell)
    # Loop until all cells have been visited
    while len(visited) < n * m:
        # Generate a list of all possible moves from the current cell
        possible_moves = [(current_cell[0], current_cell[1] + 1), (current_cell[0], current_cell[1] - 1), (current_cell[0] + 1, current_cell[1]), (current_cell[0] - 1, current_cell[1])]
        # Filter out moves that are not valid (i.e. they are not on the grid or have already been visited)
        possible_moves = [move for move in possible_moves if 1 <= move[0] <= n and 1 <= move[1] <= m and move not in visited]
        # If there are no valid moves, return False
        if not possible_moves:
            return False
        # Choose a random move from the list of possible moves
        current_cell = possible_moves[0]
        # Add the current cell to the visited list
        visited.append(current_cell)
    # If all cells have been visited, return the list of visited cells
    return visited

def f2(n, m, S_x, S_y):
    # Initialize a list to store the visited cells
    visited = []
    # Initialize the current cell as the starting cell
    current_cell = (S_x, S_y)
    # Add the starting cell to the visited list
    visited.append(current_cell)
    # Loop until all cells have been visited
    while len(visited) < n * m:
        # Generate a list of all possible moves from the current cell
        possible_moves = [(current_cell[0], current_cell[1] + 1), (current_cell[0], current_cell[1] - 1), (current_cell[0] + 1, current_cell[1]), (current_cell[0] - 1, current_cell[1])]
        # Filter out moves that are not valid (i.e. they are not on the grid or have already been visited)
        possible_moves = [move for move in possible_moves if 1 <= move[0] <= n and 1 <= move[1] <= m and move not in visited]
        # If there are no valid moves, return False
        if not possible_moves:
            return False
        # Choose a random move from the list of possible moves
        current_cell = possible_moves[0]
        # Add the current cell to the visited list
        visited.append(current_cell)
    # If all cells have been visited, return the list of visited cells
    return visited

if __name__ == '__main__':
    n, m, S_x, S_y = map(int, input().split())
    visited = f1(n, m, S_x, S_y)
    for cell in visited:
        print(cell[0], cell[1])


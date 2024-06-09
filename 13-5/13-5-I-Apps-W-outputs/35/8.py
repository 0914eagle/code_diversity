
def f1(n, m, S_x, S_y):
    # Initialize a list to store the visited cells
    visited = []
    # Initialize the current cell as the starting cell
    current_cell = (S_x, S_y)
    # Loop until all cells have been visited
    while len(visited) < n * m:
        # Generate a list of all possible moves from the current cell
        possible_moves = [(current_cell[0], current_cell[1] + 1), (current_cell[0], current_cell[1] - 1), (current_cell[0] + 1, current_cell[1]), (current_cell[0] - 1, current_cell[1])]
        # Filter out moves that are not valid or have already been visited
        possible_moves = [move for move in possible_moves if move[0] >= 1 and move[0] <= n and move[1] >= 1 and move[1] <= m and move not in visited]
        # If there are no valid moves, return False
        if not possible_moves:
            return False
        # Choose a random move from the possible moves
        current_cell = possible_moves[0]
        # Add the current cell to the list of visited cells
        visited.append(current_cell)
    # If all cells have been visited, return the list of visited cells
    return visited

def f2(visited):
    # Initialize an empty list to store the output
    output = []
    # Loop through the list of visited cells
    for cell in visited:
        # Add the cell to the output list
        output.append(cell)
    # Return the output list
    return output

if __name__ == '__main__':
    n, m, S_x, S_y = map(int, input().split())
    visited = f1(n, m, S_x, S_y)
    if visited:
        output = f2(visited)
        for cell in output:
            print(cell[0], cell[1])
    else:
        print("No solution exists.")


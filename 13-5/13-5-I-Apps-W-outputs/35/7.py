
def find_solution(n, m, S_x, S_y):
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
        # Filter out moves that are not valid (i.e. they are not on the grid or they have already been visited)
        valid_moves = []
        for move in possible_moves:
            if move[0] >= 1 and move[0] <= n and move[1] >= 1 and move[1] <= m and move not in visited:
                valid_moves.append(move)
        # If there are no valid moves, return False
        if not valid_moves:
            return False
        # Choose a random valid move
        current_cell = valid_moves[0]
        # Add the current cell to the visited list
        visited.append(current_cell)
    # If all cells have been visited, return the visited list
    return visited

def main():
    n, m, S_x, S_y = map(int, input().split())
    solution = find_solution(n, m, S_x, S_y)
    if solution:
        for cell in solution:
            print(cell[0], cell[1])
    else:
        print("No solution found")

if __name__ == '__main__':
    main()


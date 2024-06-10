
def get_penalty(matrix, k):
    # Initialize the penalty to 0
    penalty = 0
    
    # Loop through each candy
    for candy in range(k):
        # Get the current cell where the candy is placed
        current_cell = (1, 1)
        
        # Loop through each cell in the matrix
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                # If the cell is not empty, skip it
                if matrix[i][j] != 0:
                    continue
                # If the cell is empty, check if it's adjacent to the current cell
                if abs(i - current_cell[0]) + abs(j - current_cell[1]) == 1:
                    # If it's adjacent, add the penalty for the path
                    penalty += 1
                    # Update the current cell to the new cell
                    current_cell = (i, j)
                    break
    
    return penalty

def get_paths(matrix, k):
    # Initialize the paths list
    paths = []
    
    # Loop through each candy
    for candy in range(k):
        # Get the current cell where the candy is placed
        current_cell = (1, 1)
        
        # Initialize the path for the candy
        path = [current_cell]
        
        # Loop through each cell in the matrix
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                # If the cell is not empty, skip it
                if matrix[i][j] != 0:
                    continue
                # If the cell is empty, check if it's adjacent to the current cell
                if abs(i - current_cell[0]) + abs(j - current_cell[1]) == 1:
                    # If it's adjacent, add the cell to the path
                    path.append((i, j))
                    # Update the current cell to the new cell
                    current_cell = (i, j)
                    break
        
        # Add the path to the paths list
        paths.append(path)
    
    return paths

def main():
    # Read the input
    n, m, k = map(int, input().split())
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    
    # Get the penalty
    penalty = get_penalty(matrix, k)
    print(penalty)
    
    # Get the paths
    paths = get_paths(matrix, k)
    
    # Print the paths
    for path in paths:
        print(" ".join(map(str, path)))

if __name__ == '__main__':
    main()


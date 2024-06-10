
def get_penalty(n, m, k):
    # Initialize the matrix with 0s
    matrix = [[0] * m for _ in range(n)]
    
    # Initialize the penalty to 0
    penalty = 0
    
    # Place the candies one by one
    for i in range(k):
        # Find the cell where the candy can be placed
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    matrix[row][col] = i + 1
                    break
        
        # Find the path for the candy
        path = []
        current_row, current_col = 0, 0
        while current_row != row or current_col != col:
            path.append((current_row + 1, current_col + 1))
            if current_row == row:
                current_col += 1
            elif current_col == col:
                current_row += 1
            else:
                current_row, current_col = current_row + 1, current_col + 1
        
        # Add the path to the penalty
        penalty += len(path)
    
    return penalty

def get_paths(n, m, k):
    # Initialize the matrix with 0s
    matrix = [[0] * m for _ in range(n)]
    
    # Initialize the paths to an empty list
    paths = []
    
    # Place the candies one by one
    for i in range(k):
        # Find the cell where the candy can be placed
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    matrix[row][col] = i + 1
                    break
        
        # Find the path for the candy
        path = []
        current_row, current_col = 0, 0
        while current_row != row or current_col != col:
            path.append((current_row + 1, current_col + 1))
            if current_row == row:
                current_col += 1
            elif current_col == col:
                current_row += 1
            else:
                current_row, current_col = current_row + 1, current_col + 1
        
        # Add the path to the list of paths
        paths.append(path)
    
    return paths

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    penalty = get_penalty(n, m, k)
    print(penalty)
    paths = get_paths(n, m, k)
    for path in paths:
        print(*path)



def read_input():
    H, W = map(int, input().split())
    costs = [[int(x) for x in input().split()] for _ in range(10)]
    matrix = [[int(x) for x in input().split()] for _ in range(H)]
    return H, W, costs, matrix

def solve(H, W, costs, matrix):
    # Initialize the minimum total MP required to turn every digit on the wall into 1
    min_mp = float('inf')
    
    # Loop through each row of the matrix
    for i in range(H):
        # Loop through each column of the matrix
        for j in range(W):
            # If the current cell contains a digit
            if matrix[i][j] != -1:
                # Get the cost of turning the current digit into 1
                cost = costs[matrix[i][j]][1]
                
                # If the current cell is not on the edge of the matrix
                if i > 0 and j > 0 and i < H-1 and j < W-1:
                    # Get the cost of turning the current digit into its neighboring digits
                    cost += min(costs[matrix[i-1][j]][matrix[i][j]], costs[matrix[i+1][j]][matrix[i][j]], costs[matrix[i][j-1]][matrix[i][j]], costs[matrix[i][j+1]][matrix[i][j]])
                
                # Update the minimum total MP required
                min_mp = min(min_mp, cost)
    
    # Return the minimum total MP required
    return min_mp

def main():
    H, W, costs, matrix = read_input()
    print(solve(H, W, costs, matrix))

if __name__ == '__main__':
    main()



def read_input():
    H, W = map(int, input().split())
    costs = []
    for i in range(10):
        costs.append(list(map(int, input().split())))
    matrix = []
    for i in range(H):
        matrix.append(list(map(int, input().split())))
    return H, W, costs, matrix

def solve(H, W, costs, matrix):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[costs[matrix[i][j]][1] for j in range(W)] for i in range(H)]
    
    # Iterate through the rows and columns of the matrix
    for i in range(H):
        for j in range(W):
            # If the current cell is not a digit, skip it
            if matrix[i][j] == -1:
                continue
            # If the current cell is already 1, skip it
            if matrix[i][j] == 1:
                continue
            # If the current cell is not 1, check the neighbors and update the dp table
            for k in range(max(0, i-1), min(H, i+2)):
                for l in range(max(0, j-1), min(W, j+2)):
                    # If the neighbor is not a digit or is already 1, skip it
                    if matrix[k][l] == -1 or matrix[k][l] == 1:
                        continue
                    # Update the dp table with the minimum cost of turning the current digit into 1
                    dp[i][j] = min(dp[i][j], dp[k][l] + costs[matrix[i][j]][matrix[k][l]])
    
    # Return the minimum total cost required to turn every digit on the wall into 1
    return min(dp[i][j] for i in range(H) for j in range(W) if matrix[i][j] != -1)

def main():
    H, W, costs, matrix = read_input()
    print(solve(H, W, costs, matrix))

if __name__ == '__main__':
    main()


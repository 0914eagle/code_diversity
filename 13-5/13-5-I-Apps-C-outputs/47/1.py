
def solve(x, y):
    # Initialize the first two rows of the array
    F = [[0, 1], [1, 1]]
    
    # Fill in the remaining rows of the array using the recurrence relation
    for i in range(2, x+1):
        F.append([1, 1])
        for j in range(2, y+1):
            F[i].append(F[i-1][j-1] + F[i][j-1])
    
    # Return the value of F[x, y]
    return F[x][y] % 1000000007


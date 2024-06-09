
def solve(n, m, a, b, roads):
    # Initialize a matrix to store the number of soldiers to move
    moves = [[0] * n for _ in range(n)]
    
    # Loop through each road and update the number of soldiers to move
    for p, q in roads:
        moves[p - 1][q - 1] += 1
        moves[q - 1][p - 1] += 1
    
    # Check if the number of soldiers to move is valid
    for i in range(n):
        if moves[i][i] != 0:
            return "NO"
        for j in range(n):
            if moves[i][j] > a[i] or moves[j][i] > a[j]:
                return "NO"
    
    # If all conditions are met, return the moves
    return "YES"
    for move in moves:
        print(*move)


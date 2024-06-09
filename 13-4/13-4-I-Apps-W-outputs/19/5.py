
def f1(S):
    # f1(S) returns the maximum possible number of moves Aoki has to make
    # given the maze S
    
    # Initialize the maximum number of moves to 0
    max_moves = 0
    
    # Loop through each row of the maze
    for i in range(len(S)):
        # Loop through each column of the maze
        for j in range(len(S[0])):
            # If the current square is a road square
            if S[i][j] == '.':
                # Find the minimum number of moves required to reach the goal square
                # from the current square
                min_moves = f2(S, i, j)
                
                # Update the maximum number of moves if the minimum number of moves
                # is greater than the current maximum number of moves
                if min_moves > max_moves:
                    max_moves = min_moves
    
    # Return the maximum number of moves
    return max_moves

def f2(S, i, j):
    # f2(S, i, j) returns the minimum number of moves required to reach the goal square
    # from the square at row i and column j in the maze S
    
    # If the current square is the goal square, return 0
    if i == len(S) - 1 and j == len(S[0]) - 1:
        return 0
    
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    
    # Loop through the four possible directions to move
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # If the square in the next direction is a road square
        if 0 <= i + di < len(S) and 0 <= j + dj < len(S[0]) and S[i + di][j + dj] == '.':
            # Find the minimum number of moves required to reach the goal square
            # from the square in the next direction
            min_moves = min(min_moves, f2(S, i + di, j + dj) + 1)
    
    # Return the minimum number of moves
    return min_moves

if __name__ == '__main__':
    # Read the input maze from Standard Input
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    
    # Find the maximum possible number of moves Aoki has to make
    max_moves = f1(S)
    
    # Print the maximum possible number of moves
    print(max_moves)


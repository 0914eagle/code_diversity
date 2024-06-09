
def get_min_moves(bombs, n):
    # Initialize a 2D array to represent the matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Place the bombs in the matrix
    for bomb in bombs:
        x, y = bomb
        matrix[x-1][y-1] = 1
    
    # Initialize the minimum number of moves to 0
    min_moves = 0
    
    # Loop through each cell in the matrix
    for i in range(n):
        for j in range(n):
            # If the current cell is a bomb, skip it
            if matrix[i][j] == 1:
                continue
            
            # If the current cell is not a bomb, check if it is adjacent to a bomb
            adjacent_bombs = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    # If the adjacent cell is out of bounds, skip it
                    if k < 0 or k >= n or l < 0 or l >= n:
                        continue
                    
                    # If the adjacent cell is a bomb, increment the number of adjacent bombs
                    if matrix[k][l] == 1:
                        adjacent_bombs += 1
            
            # If the current cell is not adjacent to any bombs, skip it
            if adjacent_bombs == 0:
                continue
            
            # If the current cell is adjacent to one or more bombs, increment the minimum number of moves
            min_moves += adjacent_bombs
    
    return min_moves

def main():
    n, b = map(int, input().split())
    bombs = []
    for _ in range(b):
        x, y = map(int, input().split())
        bombs.append((x, y))
    print(get_min_moves(bombs, n))

if __name__ == '__main__':
    main()


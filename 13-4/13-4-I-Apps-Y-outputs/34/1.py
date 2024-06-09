
def get_min_moves(n):
    # Initialize a 2D array to store the number of moves required to move all figures to a cell
    dp = [[0] * n for _ in range(n)]
    
    # Initialize a 2D array to store the number of figures in each cell
    figures = [[1] * n for _ in range(n)]
    
    # Initialize the minimum number of moves required to move all figures to a cell
    min_moves = 0
    
    # Loop through each cell in the board
    for i in range(n):
        for j in range(n):
            # If the current cell contains no figures, skip it
            if figures[i][j] == 0:
                continue
                
            # Loop through the neighboring cells of the current cell
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    # If the neighboring cell is out of the board, skip it
                    if i + di < 0 or i + di >= n or j + dj < 0 or j + dj >= n:
                        continue
                    
                    # If the neighboring cell contains no figures, skip it
                    if figures[i + di][j + dj] == 0:
                        continue
                    
                    # If the neighboring cell contains figures, update the number of moves required to move all figures to that cell
                    dp[i][j] += 1
                    figures[i + di][j + dj] += figures[i][j]
                    figures[i][j] = 0
    
    # Loop through each cell in the board and find the minimum number of moves required to move all figures to a cell
    for i in range(n):
        for j in range(n):
            if figures[i][j] != 0:
                min_moves += figures[i][j] * dp[i][j]
    
    return min_moves

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(get_min_moves(n))

if __name__ == '__main__':
    main()


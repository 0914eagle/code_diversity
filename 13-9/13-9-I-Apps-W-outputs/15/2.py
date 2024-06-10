
def get_number_of_unattacked_cells(n, m, x, y):
    # Initialize a 2D array to store the state of the board
    board = [[0] * n for _ in range(n)]
    
    # Put the first rook on the board
    board[x - 1][y - 1] = 1
    
    # Count the number of unattacked cells
    unattacked_cells = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                unattacked_cells += 1
    
    return unattacked_cells

def main():
    n, m = map(int, input().split())
    x, y = [], []
    for i in range(m):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    
    result = []
    for i in range(m):
        result.append(get_number_of_unattacked_cells(n, m, x[i], y[i]))
    
    print(*result, sep='\n')

if __name__ == '__main__':
    main()


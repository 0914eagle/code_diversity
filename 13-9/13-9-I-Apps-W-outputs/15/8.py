
def is_cell_under_attack(row, col, n):
    # Check if the cell is under attack
    for i in range(1, n+1):
        if row == i or col == i:
            return True
    return False

def get_unattacked_cells(board, n):
    # Initialize the number of unattacked cells
    unattacked_cells = 0
    
    # Loop through each cell on the board
    for i in range(1, n+1):
        for j in range(1, n+1):
            # Check if the cell is under attack
            if not is_cell_under_attack(i, j, n):
                unattacked_cells += 1
    
    # Return the number of unattacked cells
    return unattacked_cells

def main():
    # Read the input
    n, m = map(int, input().split())
    board = []
    for i in range(m):
        board.append(list(map(int, input().split())))
    
    # Calculate the number of unattacked cells after each rook is placed
    unattacked_cells = [0] * m
    for i in range(m):
        unattacked_cells[i] = get_unattacked_cells(board[:i+1], n)
    
    # Print the number of unattacked cells after each rook is placed
    for i in range(m):
        print(unattacked_cells[i])

if __name__ == '__main__':
    main()


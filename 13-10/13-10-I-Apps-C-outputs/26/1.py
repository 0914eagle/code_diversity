
def get_tour(N, M):
    # Initialize a 2D array to store the tour
    tour = [[0] * M for _ in range(N)]
    
    # Set the starting point of the tour
    tour[0][0] = 1
    
    # Iterate through the remaining squares
    for i in range(1, N*M):
        # Get the current square
        current_row, current_col = get_current_square(tour)
        
        # Find the next square to visit
        next_row, next_col = get_next_square(current_row, current_col, N, M)
        
        # Update the tour
        tour[next_row][next_col] = i + 1
    
    return tour

def get_current_square(tour):
    # Find the current square by finding the first zero in the tour
    for row in tour:
        for col in row:
            if col == 0:
                return row.index(col), row.index(col)

def get_next_square(current_row, current_col, N, M):
    # Find the next square by moving in the direction of the Manhattan distance
    next_row = current_row + (current_col % 2) * (1 if current_row % 2 == 0 else -1)
    next_col = current_col + (1 - current_row % 2) * (1 if current_col % 2 == 0 else -1)
    
    # Wrap around the edges of the grid
    if next_row < 0:
        next_row = N - 1
    elif next_row == N:
        next_row = 0
    if next_col < 0:
        next_col = M - 1
    elif next_col == M:
        next_col = 0
    
    return next_row, next_col

if __name__ == '__main__':
    N, M = map(int, input().split())
    tour = get_tour(N, M)
    for row in tour:
        for col in row:
            print(col, end=" ")
        print()


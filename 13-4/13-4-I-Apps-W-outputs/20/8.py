
def get_min_moves(n, bombs):
    # Initialize a matrix to keep track of the number of bombs at each cell
    matrix = [[0] * n for _ in range(n)]
    for bomb in bombs:
        matrix[bomb[0] - 1][bomb[1] - 1] += 1
    
    # Initialize a queue to keep track of the cells to be processed
    queue = [(0, 0)]
    
    # Initialize a dictionary to keep track of the number of moves required to reach each cell
    moves = {(0, 0): 0}
    
    # Loop through the queue until it is empty
    while queue:
        # Get the current cell from the queue
        cell = queue.pop(0)
        
        # Get the number of bombs at the current cell
        num_bombs = matrix[cell[0]][cell[1]]
        
        # If the current cell has no bombs, continue to the next cell
        if num_bombs == 0:
            continue
        
        # If the current cell has a bomb, add it to the moves dictionary
        moves[cell] = moves.get(cell, 0) + 1
        
        # Add the neighbors of the current cell to the queue
        for neighbor in get_neighbors(cell, n):
            queue.append(neighbor)
    
    # Return the minimum number of moves required to defuse all the bombs
    return min(moves.values())

def get_neighbors(cell, n):
    # Get the x and y coordinates of the current cell
    x, y = cell
    
    # Get the neighbors of the current cell
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    
    # Filter out the neighbors that are out of bounds
    neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < n and 0 <= neighbor[1] < n]
    
    return neighbors

if __name__ == '__main__':
    n, b = map(int, input().split())
    bombs = []
    for _ in range(b):
        bombs.append(list(map(int, input().split())))
    print(get_min_moves(n, bombs))


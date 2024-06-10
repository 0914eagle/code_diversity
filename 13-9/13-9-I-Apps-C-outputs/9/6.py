
def get_maximum_score(grid):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through each row of the grid
    for row in grid:
        # Loop through each cell in the row
        for cell in row:
            # If the cell is not an obstacle, add its score to the maximum score
            if cell != "X":
                max_score += int(cell)
    
    # Return the maximum score
    return max_score

def set_conveyor_belts(grid, belts):
    # Loop through each row of the grid
    for row in grid:
        # Loop through each cell in the row
        for cell in row:
            # If the cell is a conveyor belt and its direction has not been set, set its direction based on the previous cell
            if cell == "?" and belts[cell] == "?":
                if row[cell - 1] == "R":
                    belts[cell] = "L"
                else:
                    belts[cell] = "R"
    
    # Return the updated conveyor belts
    return belts

def set_initial_position(grid, belts):
    # Initialize the initial position of the ball to the first column
    initial_position = (0, 0)
    
    # Loop through each row of the grid
    for row in grid:
        # Loop through each cell in the row
        for cell in row:
            # If the cell is not an obstacle and its direction has been set, set the initial position of the ball to the cell
            if cell != "X" and belts[cell] != "?":
                initial_position = (row, cell)
                break
    
    # Return the initial position of the ball
    return initial_position

def main():
    # Read the input
    R, C, K = map(int, input().split())
    grid = [input() for _ in range(R)]
    scores = list(map(int, input().split()))
    
    # Initialize the conveyor belts
    belts = {}
    for row in grid:
        for cell in row:
            if cell == "?" or cell == "R" or cell == "L":
                belts[cell] = cell
    
    # Set the conveyor belts
    belts = set_conveyor_belts(grid, belts)
    
    # Set the initial position of the ball
    initial_position = set_initial_position(grid, belts)
    
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through each cell in the grid
    for row in range(R):
        for cell in range(C):
            # If the cell is not an obstacle and its direction has been set, move the ball to the cell
            if grid[row][cell] != "X" and belts[row, cell] != "?":
                # If the ball goes through 10^20 cells or falls off the grid, end the exam
                if row * C + cell >= 10**20 or row < 0 or cell < 0:
                    break
                
                # If the ball lands on a cell with a score, add the score to the maximum score
                if grid[row][cell] != ".":
                    max_score += int(grid[row][cell])
                
                # Move the ball to the next cell based on the conveyor belt's direction
                if belts[row, cell] == "R":
                    cell += 1
                else:
                    cell -= 1
    
    # Return the maximum score
    print(max_score)

if __name__ == '__main__':
    main()


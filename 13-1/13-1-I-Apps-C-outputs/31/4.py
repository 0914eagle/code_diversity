
def get_maximum_score(grid, conveyor_belts, scores):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through each possible combination of conveyor belts
    for conveyor_belt_combination in itertools.product([0, 1], repeat=len(conveyor_belts)):
        # Set the conveyor belts for this combination
        for i, conveyor_belt in enumerate(conveyor_belt_combination):
            conveyor_belts[i] = conveyor_belt
        
        # Initialize the current score to 0
        current_score = 0
        
        # Loop through each row of the grid
        for row in grid:
            # Loop through each column of the row
            for col in range(len(row)):
                # If the current cell is a conveyor belt, move the ball in the corresponding direction
                if row[col] in [0, 1]:
                    col += conveyor_belt_combination[col]
                
                # If the current cell is a score cell, add the score to the current score
                if row[col] in scores:
                    current_score += scores[row[col]]
                    
                # If the current cell is an obstacle, end the game
                if row[col] == 'X':
                    break
                
            # If the current score is greater than the maximum score, update the maximum score
            if current_score > max_score:
                max_score = current_score
    
    # Return the maximum score
    return max_score


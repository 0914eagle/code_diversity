
def get_button_presses(floors, start, goal, up, down):
    # Calculate the difference between the start and goal floors
    diff = abs(start - goal)
    
    # Initialize a list to store the button presses
    button_presses = []
    
    # If the difference is greater than the up button can take us, we need to use the down button first
    if diff > up:
        # Calculate the number of times we need to press the down button to reach the start floor
        down_presses = (diff // down) * down
        
        # Add the down button presses to the list
        button_presses += [down_presses]
        
        # Subtract the number of down button presses from the total difference to get the new difference
        diff -= down_presses
    
    # Add the up button presses to the list
    button_presses += [diff]
    
    return button_presses


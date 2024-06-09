
def get_button_presses(floors, start, goal, up, down):
    # Calculate the difference between the start and goal floors
    diff = abs(start - goal)
    
    # Check if the difference is greater than the up or down button can reach
    if diff > up or diff > down:
        return "use the stairs"
    
    # Calculate the minimum number of button presses needed to reach the goal floor
    # by considering the up and down buttons separately and returning the minimum value
    return min(diff // up + (diff % up != 0), diff // down + (diff % down != 0))


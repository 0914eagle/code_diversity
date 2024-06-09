
def solve(n, m, pegs, dry_plan, wet_plan):
    # Initialize a list to store the safe wet plan
    safe_wet_plan = []
    
    # Iterate through the dry plan
    for i in range(len(dry_plan)):
        # If the current step is a peg placement, check if it is safe to place the peg
        if dry_plan[i] > 0:
            # Get the current point and the number of pegs required to place a peg there
            current_point = dry_plan[i]
            required_pegs = pegs[current_point - 1]
            
            # Check if the current point has enough pegs to place a peg there
            if len(safe_wet_plan) >= required_pegs:
                # Add the current point to the safe wet plan
                safe_wet_plan.append(current_point)
        
        # If the current step is a peg removal, check if it is safe to remove the peg
        else:
            # Get the current point and the number of pegs required to remove a peg there
            current_point = -dry_plan[i]
            required_pegs = pegs[current_point - 1]
            
            # Check if the current point has enough pegs to remove a peg there
            if len(safe_wet_plan) >= required_pegs:
                # Remove the current point from the safe wet plan
                safe_wet_plan.pop()
    
    # If the safe wet plan is empty, return -1
    if not safe_wet_plan:
        return -1
    
    # Return the safe wet plan
    return safe_wet_plan



def solve(n, m, pegs, plan):
    # Initialize a set to store the pegs that are safe to remove
    safe_pegs = set()
    
    # Iterate through the plan
    for i in range(len(plan)):
        # If the current step is to remove a peg, check if it is safe to remove
        if plan[i] < 0:
            # If the peg is not in the safe pegs set, return -1
            if -plan[i] not in safe_pegs:
                return -1
            # Otherwise, add the peg to the safe pegs set
            safe_pegs.add(-plan[i])
        # If the current step is to place a peg, check if it is safe to place
        else:
            # If the peg is not in the safe pegs set, return -1
            if plan[i] not in safe_pegs:
                return -1
            # Otherwise, add the peg to the safe pegs set
            safe_pegs.add(plan[i])
    
    # If we reach this point, all pegs in the plan are safe to remove, so return the plan
    return plan


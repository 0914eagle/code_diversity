
def solve(n, m, pegs, dry_plan, wet_plan):
    # Initialize a dictionary to store the pegs and their positions
    peg_dict = {}
    for i in range(n):
        peg_dict[i] = []
    
    # Add the pegs from the dry plan to the dictionary
    for i in dry_plan:
        peg_dict[i].append(i)
    
    # Remove the pegs from the wet plan that are not in the dry plan
    for i in wet_plan:
        if i not in dry_plan:
            peg_dict[i].remove(i)
    
    # Add the pegs from the wet plan that are not in the dry plan
    for i in wet_plan:
        if i not in dry_plan:
            peg_dict[i].append(i)
    
    # Check if the pegs in the wet plan are safe
    for i in wet_plan:
        if len(peg_dict[i]) == 0:
            return -1
    
    # Return the wet plan
    return wet_plan


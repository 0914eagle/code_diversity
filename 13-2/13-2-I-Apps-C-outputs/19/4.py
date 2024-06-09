
def f1(n, m, pegs, dry_plan):
    # Initialize a set to store the pegs that are safe to remove
    safe_to_remove = set()
    
    # Iterate through the dry plan
    for i in dry_plan:
        # If the current step is a removal, add the peg to the safe to remove set
        if i < 0:
            safe_to_remove.add(-i)
        # If the current step is a placement, remove the peg from the safe to remove set
        else:
            safe_to_remove.remove(i)
    
    # Initialize a set to store the pegs that are safe to place
    safe_to_place = set(range(1, n + 1))
    
    # Iterate through the dry plan in reverse
    for i in reversed(dry_plan):
        # If the current step is a placement, add the peg to the safe to place set
        if i > 0:
            safe_to_place.add(i)
        # If the current step is a removal, remove the peg from the safe to place set
        else:
            safe_to_place.remove(-i)
    
    # Initialize a list to store the wet plan
    wet_plan = []
    
    # Iterate through the safe to place set
    for i in safe_to_place:
        # If the current peg is not in the safe to remove set, add it to the wet plan
        if i not in safe_to_remove:
            wet_plan.append(i)
    
    # Return the wet plan
    return wet_plan

def f2(n, m, pegs, dry_plan):
    # Initialize a set to store the pegs that are safe to remove
    safe_to_remove = set()
    
    # Iterate through the dry plan
    for i in dry_plan:
        # If the current step is a removal, add the peg to the safe to remove set
        if i < 0:
            safe_to_remove.add(-i)
        # If the current step is a placement, remove the peg from the safe to remove set
        else:
            safe_to_remove.remove(i)
    
    # Initialize a set to store the pegs that are safe to place
    safe_to_place = set(range(1, n + 1))
    
    # Iterate through the dry plan in reverse
    for i in reversed(dry_plan):
        # If the current step is a placement, add the peg to the safe to place set
        if i > 0:
            safe_to_place.add(i)
        # If the current step is a removal, remove the peg from the safe to place set
        else:
            safe_to_place.remove(-i)
    
    # Initialize a list to store the wet plan
    wet_plan = []
    
    # Iterate through the safe to place set
    for i in safe_to_place:
        # If the current peg is not in the safe to remove set, add it to the wet plan
        if i not in safe_to_remove:
            wet_plan.append(i)
    
    # Return the wet plan
    return wet_plan

if __name__ == '__main__':
    n, m, pegs, dry_plan = map(int, input().split())
    dry_plan = [int(i) for i in input().split()]
    wet_plan = f1(n, m, pegs, dry_plan)
    print(len(wet_plan))
    for i in wet_plan:
        print(i)


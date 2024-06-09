
def f1(n, m, pegs, dry_plan, wet_plan):
    # Initialize variables
    safe_wet_plan = []
    used_pegs = set()
    removed_pegs = set()

    # Iterate through the dry plan
    for i in dry_plan:
        # If the current step is a peg placement, check if the peg is safe to place
        if i > 0:
            # Check if the peg is safe to place
            if i not in removed_pegs and i not in used_pegs:
                # Add the peg to the safe wet plan
                safe_wet_plan.append(i)
                used_pegs.add(i)
            # If the peg is not safe to place, return -1
            else:
                return -1
        # If the current step is a peg removal, remove the peg from the safe wet plan
        else:
            # Remove the peg from the safe wet plan
            safe_wet_plan.append(-i)
            removed_pegs.add(i)

    # Return the safe wet plan
    return safe_wet_plan

def f2(n, m, pegs, dry_plan, wet_plan):
    # Initialize variables
    safe_wet_plan = []
    used_pegs = set()
    removed_pegs = set()

    # Iterate through the dry plan
    for i in dry_plan:
        # If the current step is a peg placement, check if the peg is safe to place
        if i > 0:
            # Check if the peg is safe to place
            if i not in removed_pegs and i not in used_pegs:
                # Add the peg to the safe wet plan
                safe_wet_plan.append(i)
                used_pegs.add(i)
            # If the peg is not safe to place, return -1
            else:
                return -1
        # If the current step is a peg removal, remove the peg from the safe wet plan
        else:
            # Remove the peg from the safe wet plan
            safe_wet_plan.append(-i)
            removed_pegs.add(i)

    # Return the safe wet plan
    return safe_wet_plan

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    pegs = [int(x) for x in input().split()]
    dry_plan = [int(x) for x in input().split()]
    wet_plan = [int(x) for x in input().split()]
    print(f1(n, m, pegs, dry_plan, wet_plan))
    print(f2(n, m, pegs, dry_plan, wet_plan))


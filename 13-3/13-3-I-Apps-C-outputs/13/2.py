
def solve(n, strategic_points, dry_plan, wet_plan):
    # Initialize a list to store the pegs
    pegs = [0] * (n + 1)

    # Iterate through the dry plan
    for step in dry_plan:
        # If the step is to place a peg, place it
        if step > 0:
            pegs[step] = 1
        # If the step is to remove a peg, remove it
        else:
            pegs[abs(step)] = 0

    # Initialize a list to store the wet plan
    wet_plan = []

    # Iterate through the strategic points
    for i in range(1, n + 1):
        # If the point has a peg, add it to the wet plan
        if pegs[i] == 1:
            wet_plan.append(i)

    # Return the wet plan
    return wet_plan


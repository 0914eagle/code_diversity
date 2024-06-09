
def solve(n, strategic_points, dry_plan, wet_plan):
    # Initialize a list to store the pegs
    pegs = [0] * (n + 1)

    # Iterate through the dry plan
    for i in dry_plan:
        # If a peg is being placed, mark it as used
        if i > 0:
            pegs[i] = 1
        # If a peg is being removed, mark it as unused
        else:
            pegs[-i] = 0

    # Initialize a list to store the wet plan
    wet_plan = []

    # Iterate through the strategic points
    for i in range(1, n + 1):
        # If the point has a peg, add it to the wet plan
        if pegs[i] == 1:
            wet_plan.append(i)

    # Return the wet plan
    return wet_plan



def solve(n, strategic_points, dry_plan, wet_plan):
    # Initialize a set to store the pegs that are safe to remove
    safe_to_remove = set()

    # Iterate through the dry plan and mark the pegs that are safe to remove
    for i in dry_plan:
        if i not in strategic_points:
            safe_to_remove.add(i)

    # Initialize a set to store the pegs that are used in the wet plan
    used_pegs = set()

    # Iterate through the wet plan and check if the pegs are safe to remove
    for i in wet_plan:
        if i in safe_to_remove and i not in used_pegs:
            used_pegs.add(i)
        else:
            return -1

    return len(wet_plan)


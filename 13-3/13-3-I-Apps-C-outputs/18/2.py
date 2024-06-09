
def get_safe_wet_plan(n, strategic_points, dry_plan):
    # Initialize a set to store the pegs that are safe to remove
    safe_to_remove = set()

    # Iterate through the dry plan and mark the pegs that are safe to remove
    for i in dry_plan:
        if i not in strategic_points[i]:
            safe_to_remove.add(i)

    # Initialize a set to store the pegs that are currently in use
    in_use = set()

    # Iterate through the dry plan and add the pegs to the in_use set
    for i in dry_plan:
        in_use.add(i)

    # Initialize a list to store the wet plan
    wet_plan = []

    # Iterate through the dry plan and add the pegs to the wet plan
    for i in dry_plan:
        if i in safe_to_remove and len(in_use) <= 10 * len(dry_plan):
            wet_plan.append(i)
            in_use.add(i)

    # If the wet plan is empty, return -1
    if not wet_plan:
        return -1

    # Return the wet plan
    return wet_plan


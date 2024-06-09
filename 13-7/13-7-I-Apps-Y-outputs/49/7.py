
def can_deer_carry_out_plan(plan):
    # Initialize a set to store the visited points
    visited = set()
    # Add the starting point to the set
    visited.add((0, 0))
    # Iterate through the plan
    for t, x, y in plan:
        # Check if the current point is already visited
        if (x, y) in visited:
            # If it is, return False
            return False
        # Add the current point to the set
        visited.add((x, y))
        # Check if the next point is valid
        if x + 1 <= 10**5 and (x + 1, y) not in visited:
            visited.add((x + 1, y))
        if x - 1 >= 0 and (x - 1, y) not in visited:
            visited.add((x - 1, y))
        if y + 1 <= 10**5 and (x, y + 1) not in visited:
            visited.add((x, y + 1))
        if y - 1 >= 0 and (x, y - 1) not in visited:
            visited.add((x, y - 1))
    # If all points are visited and there are no duplicates, return True
    return len(visited) == len(set(visited))


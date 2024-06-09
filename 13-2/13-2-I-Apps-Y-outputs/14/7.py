
def can_atcodeer_carry_out_his_plan(plan):
    # Initialize a set to store the visited points
    visited = set()
    # Add the starting point to the set
    visited.add((0, 0))
    # Iterate through the plan
    for t, x, y in plan:
        # Get the current point
        current_point = (x, y)
        # Check if the current point has been visited before
        if current_point in visited:
            # If it has, return False
            return False
        # Add the current point to the set of visited points
        visited.add(current_point)
        # Get the four possible next points
        next_points = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        # Check if any of the next points are valid
        for next_point in next_points:
            # If any of the next points are valid, add them to the set of visited points
            if next_point[0] >= 0 and next_point[1] >= 0:
                visited.add(next_point)
    # If all points have been visited and there are no duplicates, return True
    return len(visited) == len(set(visited))



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
        # Get the next four points
        next_points = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        # Check if any of the next points have been visited before
        for next_point in next_points:
            if next_point in visited:
                # If any of them have, return False
                return False
    # If we reach here, it means that AtCoDeer can carry out his plan
    return True


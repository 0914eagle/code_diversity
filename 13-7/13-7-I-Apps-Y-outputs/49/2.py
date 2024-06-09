
def can_atcodeer_deer_carry_out_his_plan(plan):
    # Initialize a set to store the points AtCoDeer has visited
    visited_points = set()
    # Add the starting point to the set
    visited_points.add((0, 0))
    # Iterate through the plan
    for i in range(len(plan)):
        # Get the current point and time
        current_point, current_time = plan[i]
        # Get the next point and time
        next_point, next_time = plan[i+1]
        # Check if the next point is reachable from the current point and time
        if next_point in get_reachable_points(current_point, current_time, next_time):
            # Add the next point to the set of visited points
            visited_points.add(next_point)
        else:
            # If the next point is not reachable, return False
            return False
    # If all points are visited and there are no unvisited points, return True
    return len(visited_points) == len(plan) and len(visited_points) == len(set(visited_points))

def get_reachable_points(current_point, current_time, next_time):
    # Initialize a list to store the reachable points
    reachable_points = []
    # Iterate through the possible points AtCoDeer can be at the next time step
    for x in range(current_point[0], next_time):
        for y in range(current_point[1], next_time):
            # If the point is not the current point, add it to the list of reachable points
            if (x, y) != current_point:
                reachable_points.append((x, y))
    return reachable_points

# Test the function with the sample input
plan = [(3, 1, 2), (6, 1, 1)]
print(can_atcodeer_deer_carry_out_his_plan(plan))


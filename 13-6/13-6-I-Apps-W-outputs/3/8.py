
def solve(n, k, M, t):
    points = 0
    for i in range(n):
        # Sort the subtasks by time required
        sorted_t = sorted(t)
        # Initialize the time spent to 0
        time_spent = 0
        # Iterate through the subtasks and add the points
        for j in range(k):
            # Check if the time spent is less than the given time limit
            if time_spent < M:
                # Add the point and the time required for the subtask
                points += 1
                time_spent += sorted_t[j]
            else:
                # If the time limit is reached, break the loop
                break
    return points


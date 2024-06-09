
def solve(tasks):
    # Sort the tasks in non-decreasing order
    tasks.sort()
    # Initialize the minimum total cost to 0
    min_cost = 0
    # Loop through the tasks
    for i in range(len(tasks)):
        # Calculate the cost of completing the current task
        cost = abs(tasks[i] - tasks[(i - 1) % 3])
        # Add the cost to the minimum total cost
        min_cost += cost
    # Return the minimum total cost
    return min_cost


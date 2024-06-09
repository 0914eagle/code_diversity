
def solve(A):
    # Sort the tasks by their absolute difference
    sorted_tasks = sorted(A, key=lambda x: abs(x))
    # Initialize the total cost to 0
    total_cost = 0
    # Complete the first task at cost 0
    total_cost += sorted_tasks[0]
    # Complete the remaining tasks in order
    for i in range(1, len(sorted_tasks)):
        total_cost += abs(sorted_tasks[i] - sorted_tasks[i-1])
    return total_cost


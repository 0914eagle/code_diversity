
def solve(A):
    # Sort the tasks in non-decreasing order of cost
    A.sort()
    # Initialize the minimum total cost to 0
    min_cost = 0
    # Loop through the tasks and calculate the minimum total cost
    for i in range(len(A)):
        min_cost += A[i]
    return min_cost


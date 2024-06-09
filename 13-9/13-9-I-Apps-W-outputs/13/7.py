
def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with for each task
    total_power = [sum(a[i:i+k]) for i in range(n-k+1)]

    # Find the task with the minimum total power
    min_power = min(total_power)

    # Return the task number with the minimum total power
    return total_power.index(min_power) + 1


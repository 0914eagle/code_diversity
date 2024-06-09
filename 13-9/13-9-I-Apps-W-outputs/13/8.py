
def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with for each task
    total_power = [0] * (n + 1)
    for i in range(1, n):
        total_power[i] = total_power[i - 1] + a[i - 1]
    
    # Initialize the minimum total power and the corresponding first task
    min_total_power = float('inf')
    first_task = 1
    
    # Iterate through all possible first tasks
    for i in range(1, n - k + 2):
        # Calculate the total power for the current first task
        total_power_current = total_power[i + k - 1] - total_power[i - 1]
        
        # If the total power is less than the minimum, update the minimum and the first task
        if total_power_current < min_total_power:
            min_total_power = total_power_current
            first_task = i
    
    return first_task



def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with for each task
    total_power = [0] * (n + 1)
    for i in range(1, n):
        total_power[i] = total_power[i - 1] + a[i - 1]
    
    # Initialize the minimum power and the corresponding first task
    min_power = total_power[n]
    first_task = 1
    
    # Iterate through all possible first tasks
    for i in range(1, n - k + 2):
        # Calculate the power for the current first task
        power = total_power[i + k - 1] - total_power[i - 1]
        
        # Update the minimum power and the corresponding first task if necessary
        if power < min_power:
            min_power = power
            first_task = i
    
    return first_task


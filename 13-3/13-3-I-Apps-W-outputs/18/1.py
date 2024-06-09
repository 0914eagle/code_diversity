
def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with for each task
    total_power = [0] * (n + 1)
    for i in range(1, n):
        total_power[i] = total_power[i - 1] + a[i - 1]
    
    # Initialize the minimum power and the corresponding task number
    min_power = total_power[n]
    task_number = 1
    
    # Iterate through all possible starting tasks
    for i in range(1, n - k + 2):
        # Calculate the total power Inna tells Dima off with for the current task and the next k - 1 tasks
        current_power = total_power[i + k - 1] - total_power[i - 1]
        
        # If the current total power is less than the minimum power, update the minimum power and the corresponding task number
        if current_power < min_power:
            min_power = current_power
            task_number = i
    
    return task_number


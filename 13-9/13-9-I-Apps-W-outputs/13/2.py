
def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with for each task
    total_power = [0] * (n + 1)
    for i in range(1, n):
        total_power[i] = total_power[i - 1] + a[i - 1]
    
    # Initialize the minimum power and the starting task
    min_power = float('inf')
    start_task = 1
    
    # Iterate through all possible starting tasks
    for i in range(1, n - k + 2):
        # Calculate the total power Inna tells Dima off with for the current starting task
        current_power = total_power[i + k - 1] - total_power[i - 1]
        
        # If the current power is less than the minimum power, update the minimum power and the starting task
        if current_power < min_power:
            min_power = current_power
            start_task = i
    
    return start_task


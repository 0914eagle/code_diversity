
def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with for each task
    total_power = [0] * (n + 1)
    for i in range(1, n):
        total_power[i] = total_power[i - 1] + a[i - 1]
    
    # Initialize the minimum power and the first task to do
    min_power = total_power[n]
    first_task = 1
    
    # Iterate through all possible first tasks
    for i in range(1, n - k + 2):
        # Calculate the total power Inna tells Dima off with for the current first task
        current_power = total_power[i + k - 1] - total_power[i - 1]
        
        # Check if the current total power is less than the minimum power
        if current_power < min_power:
            min_power = current_power
            first_task = i
    
    return first_task


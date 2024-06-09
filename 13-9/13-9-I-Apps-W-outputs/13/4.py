
def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with for each task
    total_power = [0] * (n + 1)
    for i in range(1, n + 1):
        total_power[i] = total_power[i - 1] + a[i - 1]
    
    # Initialize the minimum power and the corresponding first task
    min_power = total_power[n]
    first_task = 1
    
    # Iterate through all possible first tasks
    for i in range(1, n + 1 - k):
        # Calculate the power Inna tells Dima off with for the last k tasks
        last_k_power = total_power[i + k - 1] - total_power[i - 1]
        # If the power is less than the minimum power, update the minimum power and the corresponding first task
        if last_k_power < min_power:
            min_power = last_k_power
            first_task = i
    
    return first_task


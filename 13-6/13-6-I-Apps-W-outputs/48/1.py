
def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with for each task
    total_power = [0] * (n + 1)
    for i in range(1, n + 1):
        total_power[i] = total_power[i - 1] + a[i - 1]
    
    # Initialize the minimum power and the first task to do
    min_power = total_power[n]
    first_task = 1
    
    # Iterate through all possible first tasks
    for i in range(1, n + 1):
        # Calculate the power Inna tells Dima off with for the first k - 1 tasks
        power = total_power[i + k - 1] - total_power[i - 1]
        # If the power is less than the minimum power, update the minimum power and the first task to do
        if power < min_power:
            min_power = power
            first_task = i
    
    return first_task


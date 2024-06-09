
def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with
    total_power = sum(a)
    
    # Initialize the minimum power and the corresponding first task
    min_power = total_power
    first_task = 1
    
    # Iterate over all possible first tasks
    for i in range(1, n + 1):
        # Calculate the power Inna tells Dima off with for the current first task
        power = sum(a[i:i+k-1])
        
        # If the current power is less than the minimum power, update the minimum power and the corresponding first task
        if power < min_power:
            min_power = power
            first_task = i
    
    return first_task


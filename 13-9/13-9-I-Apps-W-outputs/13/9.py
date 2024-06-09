
def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with for each task
    total_power = [0] * (n + 1)
    for i in range(1, n + 1):
        total_power[i] = total_power[i - 1] + a[i - 1]
    
    # Initialize the minimum power and the corresponding task number
    min_power = total_power[n]
    task_number = 1
    
    # Iterate through each possible task number
    for i in range(1, n + 1):
        # Calculate the power Dima gets told off with if he starts from this task
        power = total_power[n] - total_power[i - 1]
        
        # If the power is less than the minimum power, update the minimum power and the corresponding task number
        if power < min_power:
            min_power = power
            task_number = i
    
    return task_number


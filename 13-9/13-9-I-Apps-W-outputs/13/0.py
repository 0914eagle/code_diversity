
def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with
    total_power = sum(a)
    
    # Initialize the minimum power and the corresponding task number
    min_power = total_power
    task_number = 1
    
    # Iterate through all possible tasks Dima can start with
    for i in range(n):
        # Calculate the power Inna tells Dima off with if he starts with the current task
        current_power = 0
        for j in range(i, n, k):
            current_power += a[j % n]
            
        # If the current power is less than the minimum power, update the minimum power and the corresponding task number
        if current_power < min_power:
            min_power = current_power
            task_number = i + 1
    
    return task_number


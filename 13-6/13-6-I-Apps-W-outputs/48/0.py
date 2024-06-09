
def solve(n, k, a):
    # Initialize variables
    min_power = float('inf')
    start_task = 0
    
    # Iterate over all possible starting tasks
    for i in range(n):
        # Calculate the total power Inna tells Dima off with
        total_power = 0
        for j in range(i, n, k):
            total_power += a[j % n]
        
        # If the total power is less than the minimum, update the minimum and the starting task
        if total_power < min_power:
            min_power = total_power
            start_task = i + 1
    
    return start_task


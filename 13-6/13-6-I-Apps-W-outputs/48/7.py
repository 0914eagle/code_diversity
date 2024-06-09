
def solve(n, k, a):
    # Initialize variables
    min_power = float('inf')
    start_task = 0
    
    # Iterate through all possible starting tasks
    for i in range(n):
        # Calculate the total power for this starting task
        power = 0
        for j in range(k):
            power += a[(i+j)%n]
        
        # Check if the total power is less than the minimum power
        if power < min_power:
            min_power = power
            start_task = i+1
    
    # Return the starting task with the minimum power
    return start_task


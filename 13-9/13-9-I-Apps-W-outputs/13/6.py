
def solve(n, k, a):
    # Calculate the total power Inna tells Dima off with for each task
    total_power = [0] * (n + 1)
    for i in range(1, n):
        total_power[i] = total_power[i - 1] + a[i - 1]
    
    # Find the minimum total power by starting from each task
    min_total_power = float('inf')
    min_task = 0
    for i in range(1, n + 1):
        total_power_i = total_power[i - 1] + (n - i) * k
        if total_power_i < min_total_power:
            min_total_power = total_power_i
            min_task = i
    
    return min_task


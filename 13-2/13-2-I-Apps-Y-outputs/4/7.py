
def f1(N, p, times):
    # Initialize variables
    num_ac = 0
    penalty_time = 0
    
    # Sort the times in non-decreasing order
    sorted_times = sorted(times)
    
    # Loop through the problems in non-decreasing order of estimated time
    for i in range(N):
        # If the current problem is the first problem to solve, skip it
        if i == p:
            continue
        # If the current problem cannot be solved within the remaining time, break the loop
        if sorted_times[i] > penalty_time:
            break
        # Increment the number of accepted problems
        num_ac += 1
        # Update the penalty time
        penalty_time += sorted_times[i]
    
    # Return the number of accepted problems and penalty time
    return num_ac, penalty_time

def f2(N, p, times):
    # Initialize variables
    num_ac = 0
    penalty_time = 0
    
    # Sort the times in non-decreasing order
    sorted_times = sorted(times)
    
    # Loop through the problems in non-decreasing order of estimated time
    for i in range(N):
        # If the current problem is the first problem to solve, skip it
        if i == p:
            continue
        # If the current problem cannot be solved within the remaining time, break the loop
        if sorted_times[i] > penalty_time:
            break
        # Increment the number of accepted problems
        num_ac += 1
        # Update the penalty time
        penalty_time += sorted_times[i]
    
    # Return the number of accepted problems and penalty time
    return num_ac, penalty_time

if __name__ == '__main__':
    N = 7
    p = 0
    times = [30, 270, 995, 996, 997, 998, 999]
    print(f1(N, p, times))
    print(f2(N, p, times))


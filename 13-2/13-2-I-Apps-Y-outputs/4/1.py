
def f1(N, p, times):
    # Initialize variables
    num_ac = 0
    penalty_time = 0
    
    # Sort the times in non-decreasing order
    sorted_times = sorted(times)
    
    # Loop through the times and calculate the number of accepted problems and penalty time
    for i in range(N):
        if i == p:
            # If the current problem is the first problem, add its time to the penalty time
            penalty_time += sorted_times[i]
        else:
            # If the current problem is not the first problem, add its time to the penalty time and increment the number of accepted problems
            penalty_time += sorted_times[i]
            num_ac += 1
    
    # Return the number of accepted problems and penalty time
    return num_ac, penalty_time

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N = 7
    p = 0
    times = [30, 270, 995, 996, 997, 998, 999]
    num_ac, penalty_time = f1(N, p, times)
    print(num_ac, penalty_time)


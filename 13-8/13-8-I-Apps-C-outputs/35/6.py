
def get_points(n, T, points, times, deadlines):
    # Initialize the maximum points to be 0
    max_points = 0
    # Initialize the list of tasks to be performed
    tasks = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if deadlines[i] != -1:
            # Check if the task can be completed within the deadline
            if times[i] + deadlines[i] <= T:
                # Add the task to the list of tasks to be performed
                tasks.append(i)
                # Update the maximum points
                max_points += points[i]
    
    # Return the maximum points and the list of tasks
    return max_points, tasks

def get_travel_time(n, travel_times, start, end):
    # Initialize the travel time to be 0
    travel_time = 0
    
    # Loop through each location
    for i in range(n):
        # Check if the location is between the starting and ending locations
        if start < i < end:
            # Add the travel time between the current location and the next location
            travel_time += travel_times[start][i]
            # Update the starting location
            start = i
    
    # Return the total travel time
    return travel_time

def solve(n, T, points, times, deadlines, travel_times):
    # Initialize the maximum points to be 0
    max_points = 0
    # Initialize the list of tasks to be performed
    tasks = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if deadlines[i] != -1:
            # Check if the task can be completed within the deadline
            if times[i] + deadlines[i] <= T:
                # Add the task to the list of tasks to be performed
                tasks.append(i)
                # Update the maximum points
                max_points += points[i]
    
    # Loop through each combination of tasks
    for i in range(len(tasks)):
        # Get the total travel time for the current combination of tasks
        travel_time = get_travel_time(n, travel_times, 0, n+1)
        # Check if the total travel time is less than or equal to the maximum time
        if travel_time <= T:
            # Add the points for the current combination of tasks
            max_points += sum(points[task] for task in tasks[:i+1])
            # Break out of the loop
            break
    
    # Return the maximum points and the list of tasks
    return max_points, tasks

if __name__ == '__main__':
    n, T = map(int, input().split())
    points = list(map(int, input().split()))
    times = list(map(int, input().split()))
    deadlines = list(map(int, input().split()))
    travel_times = []
    for i in range(n+2):
        travel_times.append(list(map(int, input().split())))
    
    max_points, tasks = solve(n, T, points, times, deadlines, travel_times)
    print(max_points)
    print(' '.join(map(str, tasks)))


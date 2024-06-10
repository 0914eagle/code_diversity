
def get_max_points(n, T, points, times, deadlines, distances):
    # Initialize the maximum points to be 0
    max_points = 0
    # Initialize the list of tasks to be performed
    tasks = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if deadlines[i] != -1:
            # Calculate the time left to complete the task
            time_left = T - times[i]
            # Check if the task can be completed within the time left
            if time_left >= deadlines[i]:
                # Add the task to the list of tasks to be performed
                tasks.append(i)
                # Update the maximum points
                max_points += points[i]
    
    # Return the maximum points and the list of tasks
    return max_points, tasks

def get_travel_time(distances, location, task):
    # Return the travel time from the current location to the task location
    return distances[location][task]

def get_total_time(times, task, travel_time):
    # Return the total time to complete the task including travel time
    return times[task] + travel_time

def get_max_total_points(n, T, points, times, deadlines, distances):
    # Initialize the maximum points to be 0
    max_points = 0
    # Initialize the list of tasks to be performed
    tasks = []
    
    # Loop through each task
    for i in range(n):
        # Calculate the travel time from the starting location to the task location
        travel_time = get_travel_time(distances, 0, i)
        # Calculate the total time to complete the task including travel time
        total_time = get_total_time(times, i, travel_time)
        # Check if the task can be completed within the time limit
        if total_time <= T:
            # Add the task to the list of tasks to be performed
            tasks.append(i)
            # Update the maximum points
            max_points += points[i]
    
    # Return the maximum points and the list of tasks
    return max_points, tasks

if __name__ == '__main__':
    n, T = map(int, input().split())
    points = list(map(int, input().split()))
    times = list(map(int, input().split()))
    deadlines = list(map(int, input().split()))
    distances = []
    for i in range(n+2):
        distances.append(list(map(int, input().split())))
    max_points, tasks = get_max_total_points(n, T, points, times, deadlines, distances)
    print(max_points)
    print(" ".join(map(str, tasks)))


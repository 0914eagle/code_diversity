
def get_max_points(n, T, p, t, d, dist):
    # Initialize the maximum points and the tasks to perform
    max_points = 0
    tasks = []
    
    # Loop through each location
    for i in range(n):
        # Calculate the time it takes to complete the task at this location
        task_time = t[i]
        
        # Check if there is a deadline for this task
        if d[i] != -1:
            # Check if the task can be completed within the time limit
            if task_time > T:
                continue
            else:
                task_time = d[i]
        
        # Calculate the total time it takes to travel to this location and complete the task
        total_time = dist[i][n+1] + task_time
        
        # Check if the total time is within the time limit
        if total_time <= T:
            # Add the points for this task to the maximum points
            max_points += p[i]
            # Add the task to the list of tasks to perform
            tasks.append(i)
    
    return max_points, tasks

def main():
    n, T = map(int, input().split())
    p = list(map(int, input().split()))
    t = list(map(int, input().split()))
    d = list(map(int, input().split()))
    dist = [list(map(int, input().split())) for _ in range(n+2)]
    
    max_points, tasks = get_max_points(n, T, p, t, d, dist)
    print(max_points)
    print(" ".join(map(str, tasks)))

if __name__ == '__main__':
    main()


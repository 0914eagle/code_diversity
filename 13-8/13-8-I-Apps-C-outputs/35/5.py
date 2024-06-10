
def get_max_points(locations, tasks, time_limit):
    # Initialize the maximum points and the corresponding tasks
    max_points = 0
    max_tasks = []

    # Loop through each possible combination of tasks
    for tasks_combination in combinations(tasks, len(tasks)):
        # Calculate the total time required to complete the tasks
        total_time = 0
        for task in tasks_combination:
            total_time += task[1]

        # Check if the total time is within the time limit
        if total_time <= time_limit:
            # Calculate the total points earned from the tasks
            points = 0
            for task in tasks_combination:
                points += task[0]

            # Check if the total points are greater than the current maximum
            if points > max_points:
                max_points = points
                max_tasks = tasks_combination

    return max_points, max_tasks

def main():
    # Read the input data
    locations, tasks, time_limit = read_input()

    # Find the maximum points and the corresponding tasks
    max_points, max_tasks = get_max_points(locations, tasks, time_limit)

    # Print the maximum points and the corresponding tasks
    print(max_points)
    print(" ".join(str(task[2]) for task in max_tasks))

def read_input():
    # Read the number of locations, tasks, and time limit
    n, time_limit = map(int, input().split())

    # Read the locations and tasks
    locations = []
    tasks = []
    for i in range(n):
        locations.append(list(map(int, input().split())))
        tasks.append([int(x) for x in input().split()])

    return locations, tasks, time_limit

if __name__ == '__main__':
    main()


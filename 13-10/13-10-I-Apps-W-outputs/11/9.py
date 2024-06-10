
def get_maximum_tasks(start_times, finish_times):
    # Sort the tasks based on their finishing times
    sorted_tasks = sorted(zip(finish_times, range(len(finish_times))), key=lambda x: x[0])

    # Initialize the maximum number of tasks that can be performed
    max_tasks = 0

    # Initialize the current time
    current_time = 0

    # Iterate through the sorted tasks
    for finish_time, task_index in sorted_tasks:
        # Check if the task can be performed at the current time
        if finish_time >= current_time:
            # Increment the maximum number of tasks that can be performed
            max_tasks += 1

            # Update the current time to the finish time of the task
            current_time = finish_time

    # Return the maximum number of tasks that can be performed
    return max_tasks

def main():
    # Read the number of tasks
    num_tasks = int(input())

    # Read the start and finish times of the tasks
    start_times = [int(x) for x in input().split()]
    finish_times = [int(x) for x in input().split()]

    # Call the get_maximum_tasks function
    max_tasks = get_maximum_tasks(start_times, finish_times)

    # Print the maximum number of tasks that can be performed
    print(max_tasks)

if __name__ == '__main__':
    main()


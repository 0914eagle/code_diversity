
def get_maximum_tasks(start_times, end_times):
    # Sort the tasks based on their end times
    sorted_tasks = sorted(zip(start_times, end_times), key=lambda x: x[1])

    # Initialize the maximum number of tasks that can be performed
    max_tasks = 0

    # Initialize the current task index
    current_task = 0

    # Loop through the sorted tasks
    for task in sorted_tasks:
        # If the current task does not overlap with the previous task, include it in the maximum tasks
        if task[0] >= end_times[current_task]:
            max_tasks += 1
            current_task = task[1]

    return max_tasks

def main():
    # Read the number of tasks
    num_tasks = int(input())

    # Read the start and end times of the tasks
    start_times = [int(x) for x in input().split()]
    end_times = [int(x) for x in input().split()]

    # Call the function to get the maximum number of tasks
    max_tasks = get_maximum_tasks(start_times, end_times)

    # Print the maximum number of tasks
    print(max_tasks)

if __name__ == '__main__':
    main()



def get_maximum_tasks(start_times, finish_times):
    # Sort the tasks based on their finish times
    sorted_tasks = sorted(zip(finish_times, range(len(finish_times))), key=lambda x: x[0])

    # Initialize the maximum number of tasks that can be done
    max_tasks = 0

    # Iterate through the tasks and check if they can be done one at a time
    for finish_time, task_index in sorted_tasks:
        if finish_time >= start_times[task_index]:
            max_tasks += 1

    return max_tasks

def main():
    # Read the input
    N = int(input())
    start_times = list(map(int, input().split()))
    finish_times = list(map(int, input().split()))

    # Call the function to get the maximum number of tasks
    max_tasks = get_maximum_tasks(start_times, finish_times)

    # Print the output
    print(max_tasks)

if __name__ == '__main__':
    main()


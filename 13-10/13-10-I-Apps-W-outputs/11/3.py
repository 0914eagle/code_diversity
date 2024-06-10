
def get_tasks(start_times, end_times):
    # Sort the tasks based on their ending times
    sorted_tasks = sorted(zip(start_times, end_times), key=lambda x: x[1])

    # Initialize the number of tasks that can be performed
    num_tasks = 0

    # Iterate through the sorted tasks
    for i in range(len(sorted_tasks)):
        # Check if the task can be performed
        if sorted_tasks[i][0] >= end_times[num_tasks]:
            # Increment the number of tasks that can be performed
            num_tasks += 1

    # Return the indices of the tasks that can be performed
    return [i for i in range(num_tasks)]

def main():
    # Read the number of tasks
    num_tasks = int(input())

    # Read the start and end times of the tasks
    start_times = [int(x) for x in input().split()]
    end_times = [int(x) for x in input().split()]

    # Get the indices of the tasks that can be performed
    indices = get_tasks(start_times, end_times)

    # Print the indices
    print(" ".join(map(str, indices)))

if __name__ == '__main__':
    main()


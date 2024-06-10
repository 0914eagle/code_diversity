
def get_tasks(tasks):
    # Sort the tasks based on their finish time
    tasks.sort(key=lambda x: x[1])
    # Initialize the maximum number of tasks that can be performed
    max_tasks = 0
    # Initialize the current task index
    current_task = 0
    # Loop through the tasks
    for i in range(len(tasks)):
        # Check if the current task is finished before the next task starts
        if tasks[current_task][1] <= tasks[i][0]:
            # Increment the maximum number of tasks that can be performed
            max_tasks += 1
            # Move to the next task
            current_task = i
    return max_tasks

def main():
    # Get the number of tasks
    n = int(input())
    # Get the starting and finishing times of the tasks
    tasks = []
    for i in range(n):
        start, finish = map(int, input().split())
        tasks.append([start, finish])
    # Get the maximum number of tasks that can be performed
    max_tasks = get_tasks(tasks)
    # Print the maximum number of tasks that can be performed
    print(max_tasks)

if __name__ == '__main__':
    main()



def get_maximum_tasks(start_times, end_times):
    maximum_tasks = 0
    current_task = 0
    for i in range(len(start_times)):
        if start_times[i] >= end_times[current_task]:
            maximum_tasks += 1
            current_task = i
    return maximum_tasks

def get_tasks(start_times, end_times):
    maximum_tasks = get_maximum_tasks(start_times, end_times)
    tasks = []
    current_task = 0
    for i in range(len(start_times)):
        if start_times[i] >= end_times[current_task]:
            tasks.append(i)
            current_task = i
    return tasks

if __name__ == '__main__':
    start_times = list(map(int, input().split()))
    end_times = list(map(int, input().split()))
    tasks = get_tasks(start_times, end_times)
    print(*tasks, sep=' ')


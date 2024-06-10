
def get_max_tasks(start_times, end_times):
    max_tasks = 0
    current_task = 0
    for i in range(len(start_times)):
        if start_times[i] >= end_times[current_task]:
            max_tasks += 1
            current_task = i
    return max_tasks

def main():
    n = int(input())
    start_times = [int(x) for x in input().split()]
    end_times = [int(x) for x in input().split()]
    print(get_max_tasks(start_times, end_times))

if __name__ == '__main__':
    main()



def get_finish_time(start_time, finish_time):
    return finish_time - start_time

def get_max_tasks(start_time, finish_time):
    max_tasks = 0
    current_task = 0
    for i in range(len(start_time)):
        if start_time[i] >= current_task:
            max_tasks += 1
            current_task = finish_time[i]
    return max_tasks

def main():
    num_tasks = int(input())
    start_time = list(map(int, input().split()))
    finish_time = list(map(int, input().split()))
    max_tasks = get_max_tasks(start_time, finish_time)
    print(max_tasks)

if __name__ == '__main__':
    main()



def read_input():
    N = int(input())
    start_times = list(map(int, input().split()))
    finish_times = list(map(int, input().split()))
    return N, start_times, finish_times

def find_max_tasks(N, start_times, finish_times):
    max_tasks = 0
    selected_tasks = []
    for i in range(N):
        if start_times[i] >= finish_times[max_tasks]:
            max_tasks += 1
            selected_tasks.append(i)
    return selected_tasks

def print_output(selected_tasks):
    print(*selected_tasks, sep='\n')

if __name__ == '__main__':
    N, start_times, finish_times = read_input()
    selected_tasks = find_max_tasks(N, start_times, finish_times)
    print_output(selected_tasks)


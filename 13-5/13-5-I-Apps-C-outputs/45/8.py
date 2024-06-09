
import sys

def get_input():
    t, r = map(int, input().split())
    tasks = []
    for i in range(t):
        start_time, base_priority, a = map(int, input().split())
        instructions = []
        for j in range(a):
            instructions.append(input())
        tasks.append((start_time, base_priority, instructions))
    return tasks

def priority_ceiling_protocol(tasks):
    clock = 0
    while True:
        running_tasks = [task for task in tasks if task[0] <= clock]
        if not running_tasks:
            break
        running_tasks.sort(key=lambda x: x[1])
        blocked_tasks = []
        for task in running_tasks:
            if task[2][0][0] == 'L':
                resource = int(task[2][0][1])
                if resource in [task[2][i][1] for i in range(1, len(task[2])) if task[2][i][0] == 'L']:
                    blocked_tasks.append(task)
                elif any([task[2][i][1] for i in range(1, len(task[2])) if task[2][i][0] == 'L']):
                    blocked_tasks.append(task)
        if not blocked_tasks:
            task = running_tasks[0]
            instruction = task[2][0]
            if instruction[0] == 'C':
                clock += 1
            elif instruction[0] == 'L':
                clock += 1
            elif instruction[0] == 'U':
                clock += 1
            task[2].pop(0)
        else:
            blocked_tasks.sort(key=lambda x: x[1])
            task = blocked_tasks[-1]
            instruction = task[2][0]
            if instruction[0] == 'C':
                clock += 1
            elif instruction[0] == 'L':
                clock += 1
            elif instruction[0] == 'U':
                clock += 1
            task[2].pop(0)
    return clock

if __name__ == '__main__':
    tasks = get_input()
    print(priority_ceiling_protocol(tasks))


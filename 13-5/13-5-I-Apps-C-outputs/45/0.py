
def get_input():
    t, r = map(int, input().split())
    tasks = []
    for i in range(t):
        s, b, a = map(int, input().split())
        instructions = []
        for j in range(a):
            instructions.append(input())
        tasks.append((s, b, instructions))
    return tasks

def get_priority_ceiling(tasks, r):
    priority_ceiling = [0] * (r + 1)
    for task in tasks:
        for instruction in task[2]:
            if instruction[0] == "L":
                resource = int(instruction[1:])
                priority_ceiling[resource] = max(priority_ceiling[resource], task[1])
    return priority_ceiling

def get_blocked_tasks(tasks, priority_ceiling, current_priority):
    blocked_tasks = []
    for task in tasks:
        if task[1] < current_priority:
            continue
        for instruction in task[2]:
            if instruction[0] == "L":
                resource = int(instruction[1:])
                if priority_ceiling[resource] >= current_priority:
                    blocked_tasks.append(task)
                    break
    return blocked_tasks

def get_next_task(tasks, priority_ceiling, current_priority):
    non_blocked_tasks = []
    for task in tasks:
        if task[1] < current_priority:
            continue
        blocked = False
        for instruction in task[2]:
            if instruction[0] == "L":
                resource = int(instruction[1:])
                if priority_ceiling[resource] >= current_priority:
                    blocked = True
                    break
        if not blocked:
            non_blocked_tasks.append(task)
    if len(non_blocked_tasks) == 0:
        return None
    return sorted(non_blocked_tasks, key=lambda x: x[1], reverse=True)[0]

def execute_task(task, priority_ceiling, current_priority):
    for instruction in task[2]:
        if instruction[0] == "C":
            current_priority = max(current_priority, task[1])
        elif instruction[0] == "L":
            resource = int(instruction[1:])
            priority_ceiling[resource] = max(priority_ceiling[resource], current_priority)
        elif instruction[0] == "U":
            resource = int(instruction[1:])
            priority_ceiling[resource] = 0
    return current_priority

def main():
    tasks = get_input()
    priority_ceiling = get_priority_ceiling(tasks, len(tasks[0][2]))
    current_priority = 0
    while True:
        blocked_tasks = get_blocked_tasks(tasks, priority_ceiling, current_priority)
        if len(blocked_tasks) == 0:
            break
        current_priority = max(current_priority, max(task[1] for task in blocked_tasks))
    while True:
        task = get_next_task(tasks, priority_ceiling, current_priority)
        if task is None:
            break
        current_priority = execute_task(task, priority_ceiling, current_priority)
    for task in tasks:
        print(task[0] + current_priority)

if __name__ == '__main__':
    main()


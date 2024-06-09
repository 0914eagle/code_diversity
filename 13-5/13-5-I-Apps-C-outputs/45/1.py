
def get_input():
    t, r = map(int, input().split())
    tasks = []
    for i in range(t):
        s, b, a = map(int, input().split())
        instructions = []
        for j in range(a):
            instruction = input()
            instructions.append(instruction)
        tasks.append((s, b, instructions))
    return t, r, tasks

def priority_ceiling_protocol(tasks):
    clock = 0
    running_tasks = []
    while tasks:
        # Step 1: Identify running tasks
        running_tasks = [task for task in tasks if task[0] <= clock]
        # Step 2: Determine current priorities of running tasks and which tasks are blocked
        blocked_tasks = []
        for task in running_tasks:
            blocked = False
            for instruction in task[2]:
                if instruction[0] == "L" and instruction[1] in blocked_tasks:
                    blocked = True
                    break
            if blocked:
                blocked_tasks.append(task)
        # Step 3: Execute the next instruction of the non-blocked running task with the highest current priority
        if running_tasks:
            running_tasks.sort(key=lambda x: x[1], reverse=True)
            task = running_tasks[0]
            instruction = task[2][0]
            if instruction[0] == "C":
                clock += 1
            elif instruction[0] == "L":
                clock += 1
            elif instruction[0] == "U":
                clock += 1
            task[2].pop(0)
            if not task[2]:
                tasks.remove(task)
        else:
            clock += 1
    return clock

if __name__ == '__main__':
    t, r, tasks = get_input()
    print(priority_ceiling_protocol(tasks))


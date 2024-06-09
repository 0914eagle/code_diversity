
def get_running_tasks(tasks, clock):
    return [task for task in tasks if task["start"] <= clock and not all(instruction["type"] == "compute" for instruction in task["instructions"])]

def get_current_priorities(tasks, resources):
    priorities = {}
    for task in tasks:
        priority = task["base_priority"]
        for instruction in task["instructions"]:
            if instruction["type"] == "lock" and resources[instruction["resource"]]["owner"] is not None:
                priority = max(priority, resources[instruction["resource"]]["ceiling"])
        priorities[task] = priority
    return priorities

def get_blocked_tasks(tasks, resources):
    blocked_tasks = set()
    for task in tasks:
        for instruction in task["instructions"]:
            if instruction["type"] == "lock" and resources[instruction["resource"]]["owner"] is not None:
                blocked_tasks.add(task)
                break
    return blocked_tasks

def execute_next_instruction(tasks, resources, clock):
    non_blocked_tasks = [task for task in tasks if task not in blocked_tasks]
    if non_blocked_tasks:
        non_blocked_tasks.sort(key=lambda task: task["current_priority"], reverse=True)
        task = non_blocked_tasks[0]
        instruction = task["instructions"][0]
        if instruction["type"] == "compute":
            clock += 1
        elif instruction["type"] == "lock":
            resources[instruction["resource"]]["owner"] = task
        elif instruction["type"] == "unlock":
            resources[instruction["resource"]]["owner"] = None
        task["instructions"].pop(0)
        return clock
    else:
        return clock

def priority_ceiling_protocol(tasks, resources):
    clock = 0
    while tasks:
        running_tasks = get_running_tasks(tasks, clock)
        current_priorities = get_current_priorities(running_tasks, resources)
        blocked_tasks = get_blocked_tasks(running_tasks, resources)
        clock = execute_next_instruction(running_tasks, resources, clock)
    return clock

def main():
    tasks = []
    resources = {}
    for i in range(1, int(input()) + 1):
        start, base_priority, a = map(int, input().split())
        instructions = []
        for j in range(a):
            instruction = input()
            if instruction[0] == "C":
                instructions.append({"type": "compute", "duration": int(instruction[1:])})
            elif instruction[0] == "L":
                instructions.append({"type": "lock", "resource": int(instruction[1:])})
            elif instruction[0] == "U":
                instructions.append({"type": "unlock", "resource": int(instruction[1:])})
        tasks.append({"start": start, "base_priority": base_priority, "instructions": instructions})
    for i in range(1, int(input()) + 1):
        resources[i] = {"owner": None, "ceiling": 0}
    clock = priority_ceiling_protocol(tasks, resources)
    for task in tasks:
        print(clock - task["start"])

if __name__ == "__main__":
    main()


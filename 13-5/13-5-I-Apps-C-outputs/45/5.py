
def get_current_priority(task, blocked_tasks):
    # Calculate the current priority of the task based on its base priority and the priorities of the tasks it blocks
    current_priority = task["base_priority"]
    for blocked_task in blocked_tasks:
        current_priority = max(current_priority, blocked_task["current_priority"])
    return current_priority

def execute_instruction(task, instruction, clock):
    # Execute the given instruction and update the clock
    if instruction == "C":
        clock += 1
    elif instruction == "L":
        task["current_priority"] = get_current_priority(task, [])
    elif instruction == "U":
        task["current_priority"] = get_current_priority(task, [])
    return clock

def simulate_execution(tasks, resources):
    # Simulate the execution of the tasks according to the Priority Ceiling Protocol
    clock = 0
    completed_tasks = []
    while tasks:
        # Identify running tasks
        running_tasks = [task for task in tasks if task["start_time"] <= clock]
        # Determine the current priorities of the running tasks and which of the running tasks are blocked
        blocked_tasks = []
        for task in running_tasks:
            if task["instruction"] == "L":
                resource = task["resource"]
                if resources[resource]["owner"] is not None:
                    blocked_tasks.append(task)
                else:
                    resources[resource]["owner"] = task
                    task["current_priority"] = get_current_priority(task, blocked_tasks)
            elif task["instruction"] == "U":
                resource = task["resource"]
                if resources[resource]["owner"] == task:
                    resources[resource]["owner"] = None
                    task["current_priority"] = get_current_priority(task, blocked_tasks)
        # Execute the next instruction of the non-blocked running task (if any) with the highest current priority
        if running_tasks:
            running_tasks.sort(key=lambda x: x["current_priority"], reverse=True)
            task = running_tasks[0]
            clock = execute_instruction(task, task["instruction"], clock)
            if task["instruction"] == "C":
                task["instruction"] = task["instructions"].pop(0)
            else:
                task["instruction"] = None
                completed_tasks.append(task)
        # Increment the clock by one microsecond
        clock += 1
    return completed_tasks

def main():
    # Read the input
    num_tasks, num_resources = map(int, input().split())
    tasks = []
    for _ in range(num_tasks):
        start_time, base_priority, num_instructions = map(int, input().split())
        instructions = []
        for _ in range(num_instructions):
            instruction = input()
            if instruction[0] == "C":
                instructions.append("C")
            else:
                instructions.append(instruction)
        tasks.append({"start_time": start_time, "base_priority": base_priority, "instructions": instructions, "instruction": instructions[0], "current_priority": base_priority})
    # Simulate the execution of the tasks
    resources = {i: {"owner": None} for i in range(1, num_resources + 1)}
    completed_tasks = simulate_execution(tasks, resources)
    # Print the completion times of the tasks
    for task in completed_tasks:
        print(task["start_time"] + task["instructions"].index(task["instruction"]) + 1)

if __name__ == '__main__':
    main()


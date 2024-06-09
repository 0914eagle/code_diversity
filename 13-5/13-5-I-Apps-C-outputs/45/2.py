
import sys

class Task:
    def __init__(self, start_time, base_priority, instructions):
        self.start_time = start_time
        self.base_priority = base_priority
        self.instructions = instructions
        self.current_priority = base_priority
        self.blocked_tasks = []
        self.locked_resources = []
        self.completion_time = None

    def execute(self, clock):
        if self.start_time <= clock:
            for instruction in self.instructions:
                if instruction[0] == "C":
                    clock += 1
                elif instruction[0] == "L":
                    resource = instruction[1]
                    if resource not in self.locked_resources:
                        self.locked_resources.append(resource)
                elif instruction[0] == "U":
                    resource = instruction[1]
                    if resource in self.locked_resources:
                        self.locked_resources.remove(resource)
            self.completion_time = clock
            return True
        else:
            return False

    def get_current_priority(self, blocked_tasks):
        self.current_priority = self.base_priority
        for blocked_task in blocked_tasks:
            if blocked_task.current_priority > self.current_priority:
                self.current_priority = blocked_task.current_priority
        return self.current_priority

    def get_blocked_tasks(self, tasks):
        self.blocked_tasks = []
        for task in tasks:
            if task.current_priority > self.current_priority:
                self.blocked_tasks.append(task)
        return self.blocked_tasks

def get_running_tasks(tasks, clock):
    running_tasks = []
    for task in tasks:
        if task.start_time <= clock:
            running_tasks.append(task)
    return running_tasks

def get_current_priorities(running_tasks):
    current_priorities = []
    for task in running_tasks:
        current_priorities.append(task.get_current_priority(running_tasks))
    return current_priorities

def get_blocked_tasks(running_tasks):
    blocked_tasks = []
    for task in running_tasks:
        blocked_tasks.extend(task.get_blocked_tasks(running_tasks))
    return blocked_tasks

def get_next_task(running_tasks, blocked_tasks):
    next_task = None
    for task in running_tasks:
        if task not in blocked_tasks:
            next_task = task
            break
    return next_task

def simulate(tasks):
    clock = 0
    while tasks:
        running_tasks = get_running_tasks(tasks, clock)
        current_priorities = get_current_priorities(running_tasks)
        blocked_tasks = get_blocked_tasks(running_tasks)
        next_task = get_next_task(running_tasks, blocked_tasks)
        if next_task:
            if next_task.execute(clock):
                tasks.remove(next_task)
        clock += 1
    return tasks

if __name__ == '__main__':
    t, r = map(int, input().split())
    tasks = []
    for i in range(t):
        start_time, base_priority, a = map(int, input().split())
        instructions = []
        for j in range(a):
            instruction = input()
            instructions.append(instruction)
        tasks.append(Task(start_time, base_priority, instructions))
    simulate(tasks)
    for task in tasks:
        print(task.completion_time)


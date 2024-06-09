
import sys

class Task:
    def __init__(self, start_time, base_priority, instructions):
        self.start_time = start_time
        self.base_priority = base_priority
        self.instructions = instructions
        self.current_priority = base_priority
        self.locked_resources = set()
        self.completion_time = None

    def __str__(self):
        return f"Task(start_time={self.start_time}, base_priority={self.base_priority}, instructions={self.instructions}, current_priority={self.current_priority}, locked_resources={self.locked_resources}, completion_time={self.completion_time})"

    def lock_resource(self, resource):
        self.locked_resources.add(resource)
        self.current_priority = max(self.current_priority, self.base_priority)

    def unlock_resource(self, resource):
        self.locked_resources.remove(resource)
        self.current_priority = max(self.current_priority, self.base_priority)

    def compute(self):
        self.current_priority = max(self.current_priority, self.base_priority)

    def is_blocked(self, resources):
        for resource in self.locked_resources:
            if resource in resources:
                return True
        return False

def parse_input(input_string):
    tasks = []
    lines = input_string.split("\n")
    num_tasks, num_resources = map(int, lines[0].split())
    for i in range(1, num_tasks + 1):
        start_time, base_priority, num_instructions = map(int, lines[i].split())
        instructions = []
        for j in range(num_instructions):
            instruction = lines[i + j].split()
            instructions.append(instruction)
        tasks.append(Task(start_time, base_priority, instructions))
    return tasks

def simulate(tasks):
    resources = [False] * num_resources
    clock = 0
    while True:
        running_tasks = [task for task in tasks if task.start_time <= clock and not task.is_blocked(resources)]
        if not running_tasks:
            break
        running_tasks.sort(key=lambda task: task.current_priority, reverse=True)
        for task in running_tasks:
            instruction = task.instructions[0]
            if instruction[0] == "C":
                task.compute()
            elif instruction[0] == "L":
                resource = int(instruction[1])
                if resources[resource]:
                    task.locked_resources.add(resource)
                    task.current_priority = max(task.current_priority, task.base_priority)
                else:
                    resources[resource] = True
                    task.locked_resources.add(resource)
                    task.current_priority = max(task.current_priority, task.base_priority)
            elif instruction[0] == "U":
                resource = int(instruction[1])
                if resource in task.locked_resources:
                    task.locked_resources.remove(resource)
                    task.current_priority = max(task.current_priority, task.base_priority)
                resources[resource] = False
            task.instructions.pop(0)
        clock += 1
    for task in tasks:
        task.completion_time = clock
    return tasks

if __name__ == "__main__":
    tasks = parse_input(sys.stdin.read())
    tasks = simulate(tasks)
    for task in tasks:
        print(task.completion_time)

